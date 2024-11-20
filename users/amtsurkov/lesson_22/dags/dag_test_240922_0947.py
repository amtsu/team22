from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="test_uptime_dag", start_date=datetime(2024, 9, 21), schedule="0 0 * * *"
    #dag_id="tricolor", schedule="* * * * *"

) as dag:
    
    start = BashOperator(
        task_id="test_uptime", bash_command="uptime"
    )

    start

