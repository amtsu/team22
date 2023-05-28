from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

from users.mvandreeva.d221217_2227.hals_parsing import HALSParser

with DAG(dag_id="hals", start_date=datetime(2023, 5, 11), schedule="0 0 * * *") as dag:

    start = BashOperator(task_id="start", bash_command="echo start_load_data_from_hals")

    @task()
    def airflow():
        """
        Получение данных с сайта и загрузка на сервер
        """
        print("start HALSParser")
        url = "https://hals-development.ru/realty/residential"
        hals = HALSParser(url)
        hals.get_dict_list()
        hals.send_to_api()
        print("end HALSParser")

    end = BashOperator(task_id="end", bash_command="echo end_load_data_from_hals")

    # Set dependencies between tasks
    start >> airflow() >> end # pylint: Expression "start >> airflow() >> end" is assigned to nothing (expression-not-assigned)
