# Используем базовый образ python:3.12.4-slim
FROM python:3.12.4-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /teleban

# Обновляем pip до последней версии
RUN pip install --upgrade pip

# Копируем файл requirements.txt
COPY requirements.txt .

# Устанавливаем зависимости и выводим полные логи
RUN pip install --no-cache-dir -r requirements.txt --verbose

# Копируем весь проект в контейнер
COPY . .

# Указываем команду для запуска main_bot.py и main_parser.py одновременно
CMD ["sh", "-c", "alembic upgrade head && python main_bot.py & python main_parser.py"]
