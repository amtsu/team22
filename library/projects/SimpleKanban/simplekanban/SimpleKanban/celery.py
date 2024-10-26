from __future__ import absolute_import
import os
from celery import Celery

# Установка модуля настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SimpleKanban.settings')

# Создание экземпляра Celery
app = Celery('SimpleKanban')

# Настройка Celery с параметрами из Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находит и загружает задачи из приложений
app.autodiscover_tasks()
