# Импорт нужных библиотек
import torch
from transformers import BertTokenizer, BertModel, BertConfig
import logging
import os
import psycopg2

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
query = "SELECT rating, description FROM anime WHERE description IS NOT NULL AND rating>0 AND set=0 AND rating>8 ORDER BY RANDOM() LIMIT 100"
logging.info("Выполнение SQL-запроса для извлечения данных из таблицы")
cursor.execute(query)
rows = cursor.fetchall()
logging.info(f"Извлечено {len(rows)} строк из таблицы")

new_reviews = []
real_ratings = []

for row in rows:
    real_ratings.append(row[0])
    new_reviews.append(row[1])

# Загрузка токенизатора BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


# Загрузка сохраненной модели
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


# Настройка модели BERT для регрессии
config = BertConfig.from_pretrained('bert-base-uncased', num_labels=1)

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

# Инициализация модели
model = BertForRegression(bert_model)

# Загрузка весов модели
model.load_state_dict(torch.load('bert_rating_model.pth'))

# Перевод модели в режим оценки (инференса)
model.eval()

# Токенизация нескольких отзывов
inputs = tokenizer(new_reviews, return_tensors='pt', padding=True, truncation=True, max_length=512)

# Прогнозирование рейтингов
with torch.no_grad():
    outputs = model(input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'])
    predicted_ratings = outputs.squeeze().tolist()  # Конвертируем предсказания в список

num = 0
total_error = 0
for review, rating, real in zip(new_reviews, predicted_ratings, real_ratings):
    error = abs(rating * 10 - float(real))
    total_error += error
    num += 1
    print(f'{error:.2f} pred: {rating * 10:.2f} real: {real:.2f} {review[0:50].replace("\n", " ")}')

if total_error > 0:
    print("Avg error: " + str(total_error / num))
