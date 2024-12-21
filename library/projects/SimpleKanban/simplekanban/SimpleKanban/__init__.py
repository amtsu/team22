from __future__ import absolute_import, unicode_literals

# Загружаем Celery при старте проекта
from .celery import app as celery_app

__all__ = ('celery_app',)
