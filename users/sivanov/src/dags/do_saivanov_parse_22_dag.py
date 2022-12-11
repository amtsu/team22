"""
модуль для airflow, запускает разбор сайтов и выгрузку их в бд.
"""
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
# прописать путь к коду с уроками
import sys
if "/home/jupyter-isergy/github/team22/users/sivanov/lessons/lesson_22_hw/parsers/" not in sys.path:
    sys.path.append("/home/jupyter-isergy/github/team22/users/sivanov/lessons/lesson_22_hw/parsers/")
from do_parse import parser

# вот тут идет управление зданием эйрфлоу
# про расписание смотри тут https://en.wikipedia.org/wiki/Cron
# про datetime наверное тут https://pendulum.eustace.io/
with DAG(dag_id="saivanov_parse_22", start_date=datetime(2022, 12, 11), schedule="0 0 * * *") as dag:

    start = BashOperator(task_id="start", bash_command="echo sivanov_parse_22")

    @task()
    def airflow():
        print("start sivanov_parse_22")
        #начинаем парсить сайты
        result = parser.do_parse() # пока это всё что могу
        #отправить в джанго
        parser.send_to_api(result)
        print("end sivanov_parse_22")

    end = BashOperator(task_id="end", bash_command="echo sivanov_parse_22")

    # Set dependencies between tasks
    start >> airflow() >> end
#====================================================================================================
#def main():
#    result = parser.do_parse()
#    parser.send_to_api(result)
#if __name__ == '__main__':
#    main()
    