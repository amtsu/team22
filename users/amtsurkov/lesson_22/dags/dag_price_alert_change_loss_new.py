from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

import sqlite3
from datetime import datetime, timedelta

with DAG(dag_id="price_alert_change", start_date=datetime(2022, 12, 5), schedule="0 3 * * *") as dag:

    start = BashOperator(task_id="start", bash_command="echo start_prcie_alert_change")


    @task()
    def check_object():
        print("start price alert change")
        
        #days_before = 2
        days_before_1 = 1
        #d2 = datetime.today() - timedelta(days=days_before)
        d1 = datetime.today() - timedelta(days=days_before_1)
        
        connection = sqlite3.connect('/home/jupyter-amtsu/project/price_alert/db.sqlite3')
        cursor = connection.cursor()
        q = f"""
            WITH sales_numbered AS (
                SELECT 
                    count(1) as c
                FROM products_history
                where datetime_create >= "{d1.date()}"
                group by url, title
                --ORDER BY id desc
                LIMIT 1000000
            )
            SELECT 
                c,
                count(1) count
            FROM sales_numbered
            group by c

        """
        print(q)
        cursor.execute(q)
        for i in cursor.fetchall():
            print(i)

        print("end price alert change")
    
    
    @task()
    def loss_object():
        print("start price alert change")
        
        days_before = 2
        days_before_1 = 1
        d2 = datetime.today() - timedelta(days=days_before)
        d1 = datetime.today() - timedelta(days=days_before_1)
        d0 = datetime.today()
        
        connection = sqlite3.connect('/home/jupyter-amtsu/project/price_alert/db.sqlite3')
        cursor = connection.cursor()
        q = f"""
            WITH sales_numbered AS (
                SELECT 
                    id, 
                    title,
                    price_sale,  
                    url,
                    datetime_create,
                    count(1) as c
                FROM products_history
--                where datetime_create >= "{d2.date()}"
                where datetime_create >= "{d1.date()}"
                group by url, title
                having c = 1
                --ORDER BY id desc
                LIMIT 1000000
            )
            SELECT 
                id, 
                title,
                price_sale,  
                url
            FROM sales_numbered
--            where datetime_create <= "{d1.date()}"
            where datetime_create <= "{d0.date()}"
        """
        cursor.execute(q)
        print(q)
        count = 0
        for i in cursor.fetchall():
            print(i)
            count += 1
        print('count loss object =', count)

        print("end price alert change")
        

    @task()
    def new_object():
        print("start price alert change")
        
        days_before = 2
        days_before_1 = 1
        d2 = datetime.today() - timedelta(days=days_before)
        d1 = datetime.today() - timedelta(days=days_before_1)
        d0 = datetime.today()
        
        connection = sqlite3.connect('/home/jupyter-amtsu/project/price_alert/db.sqlite3')
        cursor = connection.cursor()
        q = f"""
            WITH sales_numbered AS (
                SELECT 
                    id, 
                    title,
                    price_sale,  
                    url,
                    datetime_create,
                    count(1) as c
                FROM products_history
--                where datetime_create >= "{d2.date()}"
                where datetime_create >= "{d1.date()}"
                group by url, title
                having c = 1
                --ORDER BY id desc
                LIMIT 1000000
            )
            SELECT 
                id, 
                title,
                price_sale,  
                url
            FROM sales_numbered
--            where datetime_create >= "{d1.date()}"
            where datetime_create >= "{d0.date()}"
        """
        cursor.execute(q)
        count = 0
        print(q)
        for i in cursor.fetchall():
            print(i)
            count += 1
        print('count new object =', count)

        print("end price alert change")


    end = BashOperator(task_id="end", bash_command="echo end_price_alert")

    # Set dependencies between tasks
    start >> check_object() >> loss_object() >> new_object() >> end