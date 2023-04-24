from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# from users.mvandreeva.d221217t2227.tricolor_parsing import TricolorParser
#from users.mvandreeva.dags.tricolor_parsing import TricolorParser

from users.mvandreeva.d221217_2227.tricolor_parsing import TricolorParser
from users.mvandreeva.d221217_2227.page_parsing import PagePerser
#import users.mvandreeva.d221217_2227.tricolor_parsing


# from users.amtsu.d221204t1902.TrialSportPageProcessing import TrialSportServiceProcessing

with DAG(
    dag_id="tricolor", start_date=datetime(2023, 3, 14), schedule="0 0 * * *"
) as dag:

    start = BashOperator(
        task_id="start", bash_command="echo start_load_data_from_tricolor"
    )

    @task()
    def airflow():
        print("start TricolorParser")
        url = "https://cg-tricolor.ru/catalog/flats"
        tp = TricolorParser(url)
        tp.get_dict_list()
        tp.send_to_api()
        # dict_list = tp.get_dict_list()
        # send_to_api = dict_list.send_to_api()
        print("end TricolorParser")

    end = BashOperator(task_id="end", bash_command="echo end_load_data_from_tricolor")

    # Set dependencies between tasks
    start >> airflow() >> end
