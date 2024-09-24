Инструкция для запуска у себя на компьютере

1.Клонируйте репозиторий с GitHub:

```bash
    git clone git@github.com:find-y/price_bot.git
    cd price_bot
```

2.Установите библиотеки в вирутальное окружение:

```bash
    python -m venv venv
    source venv/Scripts/activate
    pip install -r requirements.txt
```

3.Создайте файл .env и скопируйте в него токен бота:

```bash
    cp env_example .env
    nano .env
```

4.Запустите бота:

```bash
    python bot.py
```