import sqlite3

"""
Реализовать на python базу данных по персоналу с двумя таблицами из занятия.  Заполнить ее данными.
Написать select который вернет таблицу содержащую названия отделов, среднюю зарплату в отдел, отсортированных по убыванию средне зп.

Добавить в первый отдел еще одно сотрудника с ЗП 1000 и посмотреть как изменится результат.
"""
# создаем соединение с БД
conn = sqlite3.connect("company.db")

# открываем курсор
cur = conn.cursor()

# выполянем запрос и выводим его результат
cur.execute("""
                SELECT d.name AS department_name, avg(salary) AS avg_salary
                FROM employees e 
                JOIN department d ON e.department_id = d.id
                GROUP BY d.name
                ORDER BY avg_salary DESC;
            """)
print(cur.fetchall())


# добавляем еще одного сотрудника в отдел Маркетинга с ЗП 1000
cur.execute("""
                INSERT INTO employees (name, surname, department_id, salary)
                VALUES 
                ('Алексей', 'Андреев', 1, 1000)
                ;
""")
# сохраняем внесенные изменения
conn.commit()


# смотрим, тем же запросом, как изменились данные по средней ЗП
cur.execute("""
                SELECT d.name AS department_name, avg(salary) AS avg_salary
                FROM employees e 
                JOIN department d ON e.department_id = d.id
                GROUP BY d.name
                ORDER BY avg_salary DESC;
            """)
print(cur.fetchall())


# добавляем еще одного сотрудника в отдел Маркетинга с ЗП 1000
cur.execute("""
                INSERT INTO employees (name, surname, department_id, salary)
                VALUES 
                ('Андрей', 'Алексеев', 3, 1000)
                ;
""")
# сохраняем внесенные изменения
conn.commit()


# смотрим, тем же запросом, как изменились данные по средней ЗП
cur.execute("""
                SELECT d.name AS department_name, avg(salary) AS avg_salary
                FROM employees e 
                JOIN department d ON e.department_id = d.id
                GROUP BY d.name
                ORDER BY avg_salary DESC;
            """)
print(cur.fetchall())
