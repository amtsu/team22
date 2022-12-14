from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# Обратите внимание на то как формируется путь к импорту созданных вами модулей
from users.amtsu.d221204t1902.TrialSportPageProcessing import TrialSportServiceProcessing

with DAG(dag_id="trialsport_5_items", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:

    # первая задача в даге
    start = BashOperator(task_id="start", bash_command="echo start_load_data_from_trialsport")

    # вторая задача в даге
    @task()
    def airflow():
        pass
        print("start TrialSportServiceProcessing")
        tssp = TrialSportServiceProcessing()
        tssp.load_url_by_default()
        tssp.process()
        tssp.send_in_api()
        print("end TrialSportServiceProcessing")

    # третья задача в даге
    end = BashOperator(task_id="end", bash_command="echo end_load_data_from_trialsport")

    # Set dependencies between tasks
    # Последовательность выполенния задач в даге
    start >> airflow() >> end