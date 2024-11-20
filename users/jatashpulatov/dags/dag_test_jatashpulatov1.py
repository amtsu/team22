from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="test_uptime_dag", start_date=datetime(2024, 9, 21), schedule="* * * * *"
) as dag:
    
    start = BashOperator(
        task_id="test_uptime", bash_command="uptime"
    )

    @task()    
    def raising_i():
        print("start ") 
        i = 0
        i += 5
        print(i)
        print("end ")

    # Set dependencies between tasks
    start >> raising_i()
