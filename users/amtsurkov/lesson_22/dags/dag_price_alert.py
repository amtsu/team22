from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

import sqlite3
from datetime import datetime, timedelta

with DAG(dag_id="price_alert", start_date=datetime(2022, 12, 5), schedule="0 3 * * *") as dag:

    start = BashOperator(task_id="start", bash_command="echo start_prcie_alert")

    @task()
    def airflow():
        """
        Находим поциции цена по кототорым зменилась по сравнению с ценой за вчера.
        """
        print("start price alert")
        
        days_before = 2
        d = datetime.today() - timedelta(days=days_before)
        
        connection = sqlite3.connect('/home/jupyter-amtsu/project/price_alert/db.sqlite3')
        cursor = connection.cursor()
        q = f"""
            WITH sales_numbered AS (
                SELECT 
                    id, 
                    title,
                    price_sale,  
                    LEAD(price_sale,1,0) OVER (PARTITION BY title, url ORDER BY  title, id desc ) AS prev_price_sale,  
                    price_sale - LEAD(price_sale,1,0) OVER (PARTITION BY title, url  ORDER BY title, id desc ) AS diff,
                    ROW_NUMBER() OVER(PARTITION BY title, url ORDER BY id desc) AS row_number
                FROM products_history
                where datetime_create >= "{d.date()}"
                ORDER BY id desc
                LIMIT 1000000
            )
            SELECT 
                id, 
                title,
                price_sale,  
                prev_price_sale,
                diff,
                ROUND(diff / price_sale * 100) as per,
                row_number
            FROM sales_numbered
            WHERE row_number = 1 and diff !=0 and diff != price_sale and (diff + prev_price_sale) != 0
            Order by per;

        """
        cursor.execute(q)
        count = 0
        for i in cursor.fetchall():
            print(i)
            count += 1
        print('count all diff =', count)

        print("end price alert")

    end = BashOperator(task_id="end", bash_command="echo end_price_alert")

    # Set dependencies between tasks
    start >> airflow() >> end