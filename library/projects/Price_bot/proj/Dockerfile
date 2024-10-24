# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей (если есть, например requirements.txt) в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
# COPY . .
COPY bot .

# Открываем порт (если требуется)
EXPOSE 80

# Команда запуска контейнера
# Убедитесь, что bot.py - это основной файл для запуска вашего Telegram-бота
CMD ["python", "bot.py"]  
