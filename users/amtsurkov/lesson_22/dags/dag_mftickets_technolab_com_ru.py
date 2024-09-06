from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# Обратите внимание на то как формируется путь к импорту созданных вами модулей
from users.amtsu.d221204t1902.WildberriesPageProcessing import WildberriesServiceProcessing

#with DAG(dag_id="wildberries_items", start_date=datetime(2023, 7, 30), schedule="0 0 * * *") as dag:
#with DAG(dag_id="wildberries_items", start_date=datetime(2023, 12, 1), schedule="0 0 * * *") as dag:
with DAG(dag_id="mftickets_technolab_com_ru", start_date=datetime(2024, 9, 5), schedule="0 0 * * *") as dag:

    # первая задача в даге
    start = BashOperator(task_id="start", bash_command="echo start_load_data_from_mftickets_technolab_com_ru")

    ## вторая задача в даге
    #@task()
    #def airflow():
    #    pass
    #    print("start mftickets_technolab_com_ru")
    #    #tssp = WildberriesServiceProcessing()
    #    #tssp.load_url_by_default()
    #    #tssp.process()
    #    #tssp.send_in_api()
    #    print("end mftickets_technolab_com_ru")

    airflow = DockerOperator(
        dag=dag,
        task_id='docker_task_mftickets_technolab_com_ru',
        image='python',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        command='python extract_from_api_or_something.py'
    )


    # третья задача в даге
    end = BashOperator(task_id="end", bash_command="echo end_load_data_from_mftickets_technolab_com_ru")

    # Set dependencies between tasks
    # Последовательность выполенния задач в даге
    start >> airflow() >> end
