"""
модуль для airflow, запускает разбор сайтов и выгрузку их в бд.
"""
from datetime import datetime
import sys
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# вот тут идет управление зданием эйрфлоу
# про расписание смотри тут https://en.wikipedia.org/wiki/Cron
# про datetime наверное тут https://pendulum.eustace.io/
with DAG(
    dag_id="sivanov_test_1", start_date=datetime(2022, 12, 2), schedule="0 0 * * *"
) as dag:

    start = BashOperator(task_id="start", bash_command="echo sivanov_test_1")

    @task()
    def airflow():
        """
        просто пытаюсь запустить даг
        """
        print("running sivanov_test_1")
    end = BashOperator(task_id="end", bash_command="echo sivanov_test_1")

    # Set dependencies between tasks
    start >> airflow() >> end

