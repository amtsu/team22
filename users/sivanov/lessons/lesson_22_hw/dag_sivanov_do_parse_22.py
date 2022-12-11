"""
модуль для airflow, запускает разбор сайтов и выгрузку их в бд.
"""
from datetime import datetime
import sys
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
# это впрочем тоже космический костыль
import users.sivanov.dags.parsers
from users.sivanov.dags.parsers.do_parse import parser

# вот тут идет управление зданием эйрфлоу
# про расписание смотри тут https://en.wikipedia.org/wiki/Cron
# про datetime наверное тут https://pendulum.eustace.io/
with DAG(
    dag_id="sivanov_parse_22", start_date=datetime(2022, 12, 9), schedule="0 0 * * *"
) as dag:

    start = BashOperator(task_id="start", bash_command="echo sivanov_parse_22")

    @task()
    def airflow():
        """
        парсим, выливаем в джанго
        """
        print("start sivanov_parse_22")
        # начинаем парсить сайты
        result = parser.do_parse()  # пока это всё что могу
        # отправить в джанго
        #parser.send_to_api(result)
        print("end sivanov_parse_22")

    end = BashOperator(task_id="end", bash_command="echo sivanov_parse_22")

    # Set dependencies between tasks
    start >> airflow() >> end
# =============================================================================================
# def main():
#    result = parser.do_parse()
#    parser.send_to_api(result)
# if __name__ == '__main__':
#    main()
