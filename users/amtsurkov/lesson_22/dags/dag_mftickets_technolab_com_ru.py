from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.operators.docker_operator import DockerOperator

from docker.types import Mount

# Обратите внимание на то как формируется путь к импорту созданных вами модулей
from users.amtsu.d221204t1902.WildberriesPageProcessing import WildberriesServiceProcessing

#with DAG(dag_id="wildberries_items", start_date=datetime(2023, 7, 30), schedule="0 0 * * *") as dag:
#with DAG(dag_id="wildberries_items", start_date=datetime(2023, 12, 1), schedule="0 0 * * *") as dag:
with DAG(dag_id="mftickets_technolab_com_ru", start_date=datetime(2024, 9, 6, 14, 10), schedule="* * * * *") as dag:

    # первая задача в даге
#    start = BashOperator(task_id="start", bash_command="echo start_load_data_from_mftickets_technolab_com_ru")

#    info = BashOperator(task_id="info", bash_command="curl --unix-socket /var/run/docker.sock http://localhost/version")
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
        image='mftickets_technolab_com_ru',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        #docker_url='unix://run/docker.sock',
        #docker_url='/run/docker.sock',
        #volumes={"/home/airflow/artem_volume": "/data"},
        mounts=[Mount(source="/home/airflow/artem_volume", target="/data", type='bind')],
        command='python /code/mftickets_technolab_com_ru.py'
    )



    pass
    pass
    # третья задача в даге
#    end = BashOperator(task_id="end", bash_command="echo end_load_data_from_mftickets_technolab_com_ru")

    # Set dependencies between tasks
    # Последовательность выполенния задач в даге
    #start >> info >> airflow >> end
    #start >> airflow >> end
    airflow
