from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

###from users.jupyter-amtsu.TrialSportPageProcessing import TrialSportServiceProcessing
#import importlib  
#TrialSportPageProcessing = importlib.import_module("sers.jupyter-amtsu.TrialSportPageProcessing")
##from TrialSportPageProcessing import TrialSportServiceProcessing
from users.amtsu.TrialSportPageProcessing import TrialSportServiceProcessing


with DAG(dag_id="trialsport_5_items", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:

    start = BashOperator(task_id="start", bash_command="echo start_load_data_from_trialsport")

    @task()
    def airflow():
        print("start TrialSportServiceProcessing")
        #tssp =  TrialSportPageProcessing.TrialSportServiceProcessing()
        tssp = TrialSportServiceProcessing()
        tssp.load_url_by_default()
        tssp.process()
        tssp.send_in_api()
        print("end TrialSportServiceProcessing")

    end = BashOperator(task_id="end", bash_command="echo end_load_data_from_trialsport")

    # Set dependencies between tasks
    start >> airflow() >> end
