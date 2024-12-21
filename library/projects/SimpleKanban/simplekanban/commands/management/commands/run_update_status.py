from django.core.management.base import BaseCommand
from tasks.tasks import update_task_status


class Command(BaseCommand):
    help = 'Запускает обновление статусов задач'

    def handle(self, *args, **kwargs):
        update_task_status.delay()
        self.stdout.write('Задача обновления статусов успешно добавлена в очередь.')

#после запуска ввожу первые 2 команды (в пвзных терминалах), третья для ручного обновления
# celery -A simplekanban beat --loglevel=info #Celery Beat запускает планировщик задач
# celery -A simplekanban worker --loglevel=info #Celery Worker выполняет сами задачи, добавленные в очередь Beat или вручную
# python manage.py run_update_status
