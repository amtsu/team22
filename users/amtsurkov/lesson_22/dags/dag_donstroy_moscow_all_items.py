from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# Обратите внимание на то как формируется путь к импорту созданных вами модулей
from users.amtsu.d221204t1902.DonstroyMoscowPageProcessing import DonstroyMoscowServiceProcessing

with DAG(dag_id="donstroy_moscow_items", start_date=datetime(2024, 12, 11), schedule="0 0 * * *") as dag:

    # первая задача в даге
    start = BashOperator(task_id="start", bash_command="echo start_load_data_from_tdonstroy_moscow")

    # вторая задача в даге
    @task()
    def airflow():
        #pass
        print("start DonstroyMoscowProcessing")
        tssp = DonstroyMoscowServiceProcessing()
        tssp.load_url_by_default()
        tssp.process()
        tssp.send_in_api()
        print("end DonstroyMoscowServiceProcessing")

    # третья задача в даге
    end = BashOperator(task_id="end", bash_command="echo end_load_data_from_donstroy_moscow")

    # Set dependencies between tasks
    # Последовательность выполенния задач в даге
    start >> airflow() >> end
