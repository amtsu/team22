from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

from users.amtsu.d221204t1902.Ka5PageProcessing import Ka5ServiceProcessing

with DAG(dag_id="ka5_all_items", start_date=datetime(2022, 12, 5), schedule="0 0 * * *") as dag:

    start = BashOperator(task_id="start", bash_command="echo start_load_data_from_ka5")

    @task()
    def airflow():
        print("start Ka5ServiceProcessing")
        tssp = Ka5ServiceProcessing()
        tssp.load_url_by_default()
        tssp.process()
        tssp.send_in_api()
        print("end Ka5ServiceProcessing")

    end = BashOperator(task_id="end", bash_command="echo end_load_data_from_ka5")

    # Set dependencies between tasks
    start >> airflow() >> end