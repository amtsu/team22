from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(
        dag_id="test_kaanikin_20240922_dag", start_date=datetime(2024, 9, 21), schedule="* * * * *"
) as dag:
    
    ls = BashOperator(
        task_id="test_ls", bash_command="ls"
    )
    
    @task()    
    def iplus5():
        print("start ") 
        i = 0
        i += 5
        print(i)
        print("end ")
        
    ls >> iplus5()
