from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

from users.amtsu.d221204t1902.AuchanPageProcessing import AuchanServiceProcessing

#with DAG(dag_id="auchan_all_items", start_date=datetime(2023, 12, 1), schedule="0 0 * * *") as dag:
with DAG(dag_id="auchan_all_items", start_date=datetime(2024, 12, 11), schedule="0 0 * * *") as dag:

    start = BashOperator(task_id="start", bash_command="echo start_load_data_from_auchan")

    @task()
    def airflow():
        print("start auchanServiceProcessing")
        pass
        tssp = AuchanServiceProcessing()
        tssp.load_url_by_default()
        tssp.process()
        tssp.send_in_api()
        print("end auchanServiceProcessing")

    end = BashOperator(task_id="end", bash_command="echo end_load_data_from_auchan")

    # Set dependencies between tasks
    start >> airflow() >> end
