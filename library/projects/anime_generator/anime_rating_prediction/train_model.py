import psycopg2
import pandas as pd
from transformers import BertTokenizer, BertModel, BertConfig
import torch
from torch.utils.data import DataLoader, Dataset
import torch.nn.functional as F
from transformers import AdamW
import logging
import os
from transformers import logging as transformers_logging
import time
from torch.cuda.amp import GradScaler, autocast
import torch.cuda
import pickle
import numpy as np

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
transformers_logging.set_verbosity_info()

def main():
    # Подключение к базе данных PostgreSQL
    DB_HOST = "192.168.1.156"
    DB_PORT = "5432"
    DB_NAME = "myanimelist_db"
    DB_USER = "myanimelist_db"
    DB_PASSWORD = "myanimelist_dbmyanimelist_db"

    logging.info("Подключение к базе данных PostgreSQL")
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )
    cursor = conn.cursor()

    # Извлечение данных из таблицы
    query = "SELECT rating, description FROM anime WHERE description IS NOT NULL AND rating>0 AND set=0"
    logging.info("Выполнение SQL-запроса для извлечения данных из таблицы")
    cursor.execute(query)
    rows = cursor.fetchall()
    logging.info(f"Извлечено {len(rows)} строк из таблицы")

    # Преобразование данных в DataFrame
    data = pd.DataFrame(rows, columns=['rating', 'description'])
    logging.info("Преобразование данных в DataFrame завершено")

    # Закрытие подключения
    cursor.close()
    conn.close()
    logging.info("Подключение к базе данных закрыто")

    # 1. Нормализация отзывов по длине

    # Установка минимальной длины отзыва (например, 10 слов) и максимальной длины токенов (512 токенов)
    min_length = 10
    max_tokens = 512

    # Фильтрация коротких отзывов
    logging.info("Фильтрация отзывов, которые короче минимально допустимой длины")
    data['word_count'] = data['description'].apply(lambda x: len(x.split()))
    data = data[data['word_count'] >= min_length]
    logging.info(f"После фильтрации осталось {len(data)} отзывов")

    # Функция для усечения длинных отзывов до max_tokens
    def truncate_review(review, max_tokens):
        tokens = review.split()  # Разбиваем текст на слова
        if len(tokens) > max_tokens:
            tokens = tokens[:max_tokens]  # Оставляем только первые max_tokens слов
        return " ".join(tokens)

    # Применение усечения для длинных отзывов
    logging.info("Применение усечения для длинных отзывов")
    data['description'] = data['description'].apply(lambda x: truncate_review(x, max_tokens))

    # 2. Токенизация отзывов

    # Загрузка токенизатора BERT
    logging.info("Загрузка токенизатора BERT")
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Проверка наличия закешированных токенов
    token_cache_path = 'tokenized_inputs.pkl'
    if os.path.exists(token_cache_path):
        logging.info("Загрузка закешированных токенов из файла")
        with open(token_cache_path, 'rb') as f:
            inputs = pickle.load(f)
    else:
        # Токенизация отзывов
        logging.info("Токенизация отзывов и сохранение в кэш")
        inputs = tokenizer(list(data['description']), padding=True, truncation=True, return_tensors='pt')
        with open(token_cache_path, 'wb') as f:
            pickle.dump(inputs, f)

    # Преобразование рейтингов в float и нормализация
    logging.info("Преобразование рейтингов в float и нормализация")
    data['rating'] = data['rating'].astype(float)
    data = data[data['rating'].notna() & ~data['rating'].isin([np.inf, -np.inf])]
    data['rating'] = data['rating'] / data['rating'].max()  # Нормализация рейтингов в диапазон [0, 1]
    logging.info(f"После фильтрации непустых и допустимых рейтингов осталось {len(data)} строк")  # Нормализация рейтингов в диапазон [0, 1]

    # 3. Подготовка модели BERT для регрессии

    class BertForRegression(torch.nn.Module):
        def __init__(self, bert):
            super(BertForRegression, self).__init__()
            self.bert = bert
            self.regressor = torch.nn.Linear(bert.config.hidden_size, 1)

        def forward(self, input_ids, attention_mask):
            outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
            cls_output = outputs.pooler_output
            rating = self.regressor(cls_output)
            return rating

    # Проверка наличия предобученной модели на диске
    model_path = 'bert_model'
    if os.path.exists(model_path):
        logging.info("Загрузка предобученной BERT-модели из локального файла")
        bert_model = BertModel.from_pretrained(model_path)
    else:
        logging.info("Загрузка предобученной BERT-модели с сервера и сохранение на диск с выводом прогресса")
        config = BertConfig.from_pretrained('bert-base-uncased', num_labels=1)
        bert_model = BertModel.from_pretrained('bert-base-uncased', config=config)
        bert_model.save_pretrained(model_path)

    # Инициализация модели для регрессии
    logging.info("Инициализация модели для регрессии")
    model = BertForRegression(bert_model)

    # Определение устройства (CPU или GPU)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    logging.info(f"Используемое устройство: {device}")
    model.to(device)

    # 4. Подготовка данных для обучения

    class ReviewDataset(Dataset):
        def __init__(self, encodings, labels):
            self.encodings = encodings
            self.labels = labels

        def __getitem__(self, idx):
            item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
            item['labels'] = torch.tensor(self.labels[idx], dtype=torch.float32)
            return item

        def __len__(self):
            return len(self.labels)

    # Создание датасета
    logging.info("Создание датасета")
    dataset = ReviewDataset(inputs, data['rating'].values)

    # Разделение данных на батчи
    logging.info("Разделение данных на батчи")
    dataloader = DataLoader(dataset, batch_size=96, shuffle=True, num_workers=0)

    # 5. Настройка оптимизатора и функции потерь

    # Оптимизатор AdamW
    logging.info("Настройка оптимизатора AdamW")
    optimizer = AdamW(model.parameters(), lr=5e-6, weight_decay=0.01)  # Уменьшение скорости обучения

    # Функция потерь (среднеквадратичная ошибка)
    logging.info("Настройка функции потерь (MSE)")
    criterion = torch.nn.MSELoss(reduction='mean')

    # 6. Обучение модели с использованием смешанной точности

    # Перевод модели в режим обучения
    logging.info("Перевод модели в режим обучения")
    model.train()

    # Инициализация GradScaler для mixed precision
    scaler = GradScaler()

    # Обучение на 10 эпохах (можно увеличить количество эпох для лучшего результата)
    logging.info("Начало обучения модели")
    for epoch in range(10):
        epoch_loss = 0
        total_batches = len(dataloader)
        start_time = time.time()
        for batch_idx, batch in enumerate(dataloader):
            optimizer.zero_grad()
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            # Прямой проход через модель с использованием mixed precision
            with autocast():
                outputs = model(input_ids=input_ids, attention_mask=attention_mask)
                loss = criterion(outputs, labels.unsqueeze(1))  # Rating prediction vs. True labels

            # Проверка на NaN в функции потерь
            if torch.isnan(loss) or torch.isinf(loss):
                logging.warning(f"NaN найден в функции потерь на эпохе {epoch + 1}, батче {batch_idx + 1}. Пропуск батча.")
                continue

            # Обратное распространение ошибки и обновление весов с использованием scaler
            scaler.scale(loss).backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)
            scaler.update()

            epoch_loss += loss.item()

            elapsed_time = time.time() - start_time
            estimated_total_time = (elapsed_time / (batch_idx + 1)) * total_batches
            remaining_time = estimated_total_time - elapsed_time
            memory_allocated = torch.cuda.memory_allocated(device) / (1024 ** 3) if torch.cuda.is_available() else 0
            memory_reserved = torch.cuda.memory_reserved(device) / (1024 ** 3) if torch.cuda.is_available() else 0
            if batch_idx % 10 == 0:
                logging.info(f'Epoch {epoch + 1}, Batch {batch_idx + 1}/{total_batches}, Loss: {loss.item()}, Estimated time left: {remaining_time:.2f} seconds, Memory Allocated: {memory_allocated:.2f} GB, Memory Reserved: {memory_reserved:.2f} GB')

        logging.info(f'Epoch {epoch + 1} completed, Average Loss: {epoch_loss / total_batches}')

    # 7. Сохранение модели
    logging.info("Сохранение обученной модели")
    torch.save(model.state_dict(), 'bert_rating_model_new.pth')
    logging.info("Модель успешно сохранена в 'bert_rating_model_new.pth'")

if __name__ == '__main__':
    main()