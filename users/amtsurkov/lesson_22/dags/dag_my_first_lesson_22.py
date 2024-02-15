from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

#from users.amtsu.d221204t1902.TrialSportPageProcessing import TrialSportServiceProcessing

#with DAG(dag_id="dag_my_first_lesson_22_id", start_date=datetime(2022, 12, 3), schedule="0 0 * * *") as dag:
with DAG(dag_id="dag_my_first_lesson_22_id", start_date=datetime(2023, 12, 1), schedule="0 0 * * *") as dag:

    task_1 = BashOperator(task_id="task_1", bash_command="echo start_load_data_from_trialsport")

    @task()
    def task_2_python():
        print("start TrialSportServiceProcessing")

    task_3 = BashOperator(task_id="task_3", bash_command="echo end_load_data_from_trialsport")
    
    task_4 = BashOperator(task_id="task_4", bash_command="echo task")

    # Set dependencies between tasks
    task_1 >> task_2_python() >> task_4 >> task_3
