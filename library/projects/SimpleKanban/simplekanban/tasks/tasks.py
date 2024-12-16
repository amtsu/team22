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
