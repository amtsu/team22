"""
Взял тут:
https://github.com/amtsu/team22/blob/e5d9868f4aaa96c4dac26f8ab10ba9129f2d5806/users/andreev-aleksey/lesson_sql/create_table_and_insert_data.py
"""

import sqlite3


# создаем соединение с БД
conn = sqlite3.connect("company.db")

# открываем курсор
cur = conn.cursor()

# создаем таблицу отделов
cur.execute("""
            CREATE TABLE department (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        "name" varchar(255)
                        );
""")

# создаем таблицу сотрудников
cur.execute("""
            CREATE TABLE employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            "name" varchar(255) NOT NULL,
            surname varchar(255) NOT NULL,
            department_id int4 NOT NULL,
            salary int NOT NULL,
            CONSTRAINT department_fk FOREIGN KEY (department_id) REFERENCES department(id)
            );
""")

# наполняем таблицу отделов
cur.execute("""
                INSERT INTO department (name)
                VALUES 
                ('Маркетинг'),
                ('Продажи'),
                ('Бухгалтерия'),
                ('')
                ;
            """)

# наполняем таблицу сотрудников
cur.execute("""
                INSERT INTO employees (name, surname, department_id, salary)
                VALUES 
                ('Иван', 'Иванов', 1, 5000),
                ('Света', 'Сидорова', 1, 4500),
                ('Илья', 'Макаров', 2, 4500),
                ('Марина', 'Федорова', 2, 6000),
                ('Вадим', 'Ильин', 3, 7000),
                ('Илья', 'Филатов', 2, 5500),
                ('Марина', 'Сидорова', 2, 9000),
                ('Вадим', 'Ильин', 3, 7000)
                ;
""")
            
# сохраняем внесенные изменения
conn.commit()
