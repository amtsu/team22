from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

from users.amtsu.d221204t1902.FondRenovationPageProcessing import FondRenovationServiceProcessing

#with DAG(dag_id="fondrenovation_all_items", start_date=datetime(2023, 4, 7), schedule="0 0 * * *") as dag:
with DAG(dag_id="fondrenovation_all_items", start_date=datetime(2024, 12, 11), schedule="0 0 * * *") as dag:

    start = BashOperator(task_id="start", bash_command="echo start_load_data_from_fondrenovation")

    @task()
    def airflow():
        print("start FondRenovationServiceProcessing")
        tssp = FondRenovationServiceProcessing()
        #tssp.load_url_by_default()
        tssp.process()
        tssp.send_in_api()
        print("end FondRenovationServiceProcessing")

    end = BashOperator(task_id="end", bash_command="echo end_load_data_from_fondrenovation")

    # Set dependencies between tasks
    start >> airflow() >> end
