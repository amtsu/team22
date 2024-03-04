from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

from users.amtsu.d221204t1902.GkOsnovaPageProcessing import GkOsnovaServiceProcessing

with DAG(dag_id="gkosnova_all_items", start_date=datetime(2024, 3, 3), schedule="0 0 * * *") as dag:

    start = BashOperator(task_id="start", bash_command="echo start_load_data_from_gkosnova")

    @task()
    def airflow():
        print("start1 gkosnovaServiceProcessing")
        import sys
        pass
        print(sys.version)

        tssp = GkOsnovaServiceProcessing()
        #tssp.load_url_by_default()
        tssp.process()
        tssp.send_in_api()
        print("end gkosnovaServiceProcessing")

    end = BashOperator(task_id="end", bash_command="echo end_load_data_from_gkosnova")

    # Set dependencies between tasks
    start >> airflow() >> end
