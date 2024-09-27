from celery import Celery

# Настройка Celery с использованием Redis в качестве брокера сообщений
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Опционально: укажите количество попыток и задержку между повторными попытками
app.conf.update(task_retries=3, task_retry_delay=10)
