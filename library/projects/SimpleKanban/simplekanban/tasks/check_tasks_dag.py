# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.utils.dates import days_ago
# from django.core.mail import send_mail
# from .models import Task  # Убедитесь, что этот импорт правильный
#
#
# # Функция для проверки просроченных задач
# def check_overdue_tasks():
#     from django.utils import timezone
#     today = timezone.now().date()
#
#     # Получаем все просроченные задачи
#     overdue_tasks = Task.objects.filter(due_date__lt=today, execution_status='AC')
#
#     if overdue_tasks.exists():
#         for task in overdue_tasks:
#             subject = f'Задача просрочена: {task.title}'
#             message = f'Задача "{task.title}" была просрочена. Проверьте её статус.'
#             send_mail(subject, message, 'from@example.com', ['to@example.com'])
#
#
# # Определение DAG
# default_args = {
#     'owner': 'airflow',
#     'start_date': days_ago(1),
#     'retries': 1,
# }
#
# dag = DAG(
#     'check_overdue_tasks',
#     default_args=default_args,
#     description='Проверка просроченных задач и отправка уведомлений',
#     schedule_interval='@daily',  # Запускать ежедневно
# )
#
# check_overdue = PythonOperator(
#     task_id='check_overdue_tasks',
#     python_callable=check_overdue_tasks,
#     dag=dag,
# )
#
# check_overdue



# !!!!!  ln -s /home/jupyter-arisova/github/team22/users/aaarisova/dags /home/airflow/airflow/dags/users/aaarisova


from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from django.core.mail import send_mail
from .models import Task


def check_overdue_tasks():
    from django.utils import timezone
    today = timezone.now().date()

    # Получаем все просроченные задачи и отправляем уведомления
    for task in Task.objects.filter(due_date__lt=today, execution_status='AC'):
        send_mail(
            subject=f'Задача просрочена: {task.title}',
            message=f'Задача "{task.title}" была просрочена. Проверьте её статус.',
            from_email='from@example.com',
            recipient_list=['to@example.com'],
        )


# Определение DAG
with DAG(
        'check_overdue_tasks',
        default_args={
            'owner': 'airflow',
            'start_date': days_ago(1),
            'retries': 1,
        },
        description='Проверка просроченных задач и отправка уведомлений',
        schedule_interval='@daily',  # Запускать ежедневно
) as dag:
    check_overdue = PythonOperator(
        task_id='check_overdue_tasks',
        python_callable=check_overdue_tasks,
    )
