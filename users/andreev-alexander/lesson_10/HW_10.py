"""
- Реализовать на python базу данных по персоналу с двумя таблицами из занятия.
- Заполнить ее данными.
- Написать select который вернет таблицу содержащую:
    - названия отделов
    - среднюю зарплату в отдел
    - отсортированных по убыванию средне зп.

- Добавить в первый отдел еще одно сотрудника с ЗП 1000 и посмотреть как изменится результат.
"""

import sqlite3


conn = sqlite3.connect("company.db")
cursor = conn.cursor()

select_table = """
    SELECT department.name, avg(salary)
    FROM employees JOIN department ON employees.department_id=department.id
    GROUP BY department.name
    ORDER BY avg(salary) DESC
"""

cursor.execute(select_table)
print(cursor.fetchall())


insert_employee = """
    INSERT INTO employees (name, surname, department_id, salary)
    VALUES (?, ?, ?, ?)
"""

cursor.execute(insert_employee, ('Фет', 'Афанасий', 1, 1000))
cursor.execute(select_table)
print(cursor.fetchall())
