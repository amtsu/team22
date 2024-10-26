from celery import shared_task
from django.utils import timezone
from .models import Task
from django.core.mail import send_mail


@shared_task
def check_and_notify_overdue_tasks():
    now = timezone.now()
    overdue_tasks = Task.objects.filter(date_expired__lt=now, execution_status='in_progress')

    for task in overdue_tasks:
        send_overdue_notification(task)

def send_overdue_notification(task):
    subject = f"Задача просрочена: {task.title}"
    message = f"Задача '{task.title}' просрочена. Срок выполнения: {task.date_expired}."
    recipient_email = task.author.email

    send_mail(
        subject,
        message,
        'from@example.com',
        [recipient_email],
        fail_silently=False,
    )
