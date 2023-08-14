from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

import sqlite3
from datetime import datetime, timedelta

with DAG(dag_id="price_count", start_date=datetime(2023, 1, 21), schedule="0 3 * * *") as dag:

    start = BashOperator(task_id="start", bash_command="echo start_count")

    @task()
    def airflow():
        print("start count")
        
        days_before = 1
        d = datetime.today() - timedelta(days=days_before)
        
        connection = sqlite3.connect('/home/jupyter-amtsu/project/price_alert/db.sqlite3')
        cursor = connection.cursor()
        q = f"""
                SELECT 
                    count(id) 
                FROM products_history
                LIMIT 10

        """
        cursor.execute(q)
        for i in cursor.fetchall():
            print(i)

        print("end price alert")

    end = BashOperator(task_id="end", bash_command="echo end_price_alert")

    # Set dependencies between tasks
    start >> airflow() >> end