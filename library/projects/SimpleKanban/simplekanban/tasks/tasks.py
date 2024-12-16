# from celery import shared_task
# from datetime import datetime
# from .models import Task
#
# @shared_task
# def update_overdue_tasks():
#     current_time = datetime.now()
#     overdue_tasks = Task.objects.filter(execution_status='active', due_date__lt=current_time)
#     for task in overdue_tasks:
#         task.execution_status = 'overdue'
#         task.save()

from celery import shared_task
from django.utils import timezone
from .models import Task

@shared_task
def update_task_status():
    """Обновляет статус задач, которые стали просроченными."""
    now = timezone.now().date()
    overdue_tasks = Task.objects.filter(execution_status='AC', due_date__lt=now)
    count = overdue_tasks.update(execution_status='EX')  # Обновляем статус
    return f'{count} задач(а) обновлено'
