"""
основной файл работы с базой данных бухгалтерии (accounts department)
"""
from ad_database_stuff import AdDatabase

# ==============================================================================
def go_away(*args, **kwargs):
    """
    попытка аккуратно закончить с циклом выполнения программы
    """
    print("exiting...")
    return False  # d-_-b


# ==============================================================================
def show_all_employees_data(*args, **kwargs):
    """
    выводит на экран список всех работников в базе данных
    """
    result = kwargs["db"].execute(
        """
        SELECT e.id, e.name, e.secname, e.surname, e.salary, d.name
        FROM Employees e
        JOIN  Departments d WHERE e.dep_id = d.id
        """
    )
    width = 1 + 4 + 1 + 5 * 21 + 1
    print("=" * width)
    t_caption = (
        "#",
        "Фамилия",
        "Имя",
        "Отчество",
        "Зарплата",
        "Название отдела",
    )
    print(
        f"|{t_caption[0]:4}|{t_caption[1]:20}|{t_caption[2]:20}|"
        f"{t_caption[3]:20}|{t_caption[4]:^10}|{t_caption[5]:^30}|"
    )
    print("=" * width)
    for record in result:
        print(
            f"|{record[0]:4}|{record[3]:20}|{record[1]:20}|{record[2]:20}|"
            f"{record[4]:^10}|{record[5]:^30}|"
        )
    print("=" * width)


# ==============================================================================
def show_all_departments_data(*args, **kwargs):
    """
    выводит на экран список всех работников в базе данных
    """
    result = kwargs["db"].execute("SELECT * FROM Departments")
    width = 1 + 30 + 1 + 4 + 1
    t_caption = (
        "#",
        "Название",
    )
    print("=" * width)
    print(f"|{t_caption[0]:4}|{t_caption[1]:30}|")
    print("=" * width)
    for record in result:
        print(f"|{record[0]:4}|{record[1]:30}|")
    print("=" * width)


# ==============================================================================
def swich_to_test_db(*args, **kwargs):
    """
    Переключение на тестовую базу данных
    """
    kwargs["db"] = AdDatabase(":memory:")


# ==============================================================================
def enter_department_id_interactive(*args, **kwargs):
    """
    Ввод номера отдела с контролем корректности и интерактивом
    """
    departments = kwargs["db"].execute("SELECT id FROM Departments")
    department_id = None
    trash_input = False
    while not isinstance(department_id, int):
        department_id = input("Номер отдела (hint для вывода списка отделов): ")
        department_id = department_id.strip().lower()
        if department_id == "hint":
            show_all_departments_data(db=kwargs["db"])
            continue
        try:
            department_id = int(department_id)
        except ValueError:
            trash_input = True
        # print(departments)
        if (trash_input) or ((department_id,) not in departments):
            print("Введите корректный номер отдела!")
            department_id = None
            trash_input = False
    return department_id


# ==============================================================================
def add_employee(*args, **kwargs):
    """
    добавляет сотрудника в базу сотрудников
    """
    surname = input("Фамилия: ")
    name = input("Имя: ")
    secname = input("Отчество: ")
    dep_id = enter_department_id_interactive(db=kwargs["db"])
    salary = input("Зарплата: ")
    kwargs["db"].execute(
        """
        INSERT INTO Employees (name, secname, surname, dep_id, salary)
        values(?,?,?,?,?)
        """,
        (
            name,
            secname,
            surname,
            int(dep_id),
            int(salary),
        ),
    )


# ==============================================================================
def save_database(*args, **kwargs):
    """
    Сохраняет изменения в БД
    """
    kwargs["db"].commit()
    print("Изменения сохранены!")


# ==============================================================================
def add_department(*args, **kwargs):
    """
    добавить новый отдел в БД
    """
    name = input("Название отдела: ")
    kwargs["db"].execute(
        """
        INSERT INTO Departments (name)
        values(?)
        """,
        (name,),
    )


# ==============================================================================
def show_average_salary_by_deps(*args, **kwargs):
    """
    Посчитать и вывести на экран среднюю зарплату по отделам
    """
    average_data = kwargs["db"].execute(
        """
        SELECT d.name, avg(e.salary) avg_sal
        FROM Employees e
        JOIN  Departments d WHERE e.dep_id = d.id
        GROUP BY d.name
        ORDER BY avg_sal DESC
        """
    )
    width = 1 + 30 + 1 + 20 + 1
    t_caption = (
        "Название отдела",
        "Средняя зарплата",
    )
    print("=" * width)
    print(f"|{t_caption[0]:30}|{t_caption[1]:^20}|")
    print("=" * width)
    for record in average_data:
        print(f"|{record[0]:30}|{record[1]:^20}|")
    print("=" * width)


# ==============================================================================
def export_data_to_excel_csv(*args, **kwargs):
    """
    Выгрузка данных в csv для excel - с разделителями ;
    """
    result = kwargs["db"].execute(
        """
        SELECT e.name, e.secname, e.surname, e.salary, d.name  FROM Employees e
        JOIN  Departments d WHERE e.dep_id = d.id
        """
    )
    with open("export.csv", "w",encoding="utf-8") as fout:
        for record in result:
            out_str = ""
            for element in record:
                out_str += f"{element};"
            print(
                out_str,
                file=fout,
            )
    print("Экспорт завершен!")
    print("=" * 20)


# ==============================================================================
def import_data_from_excel_csv(*args, **kwargs):
    """
    импорт данных из экселевского csv - с разделителями - ";"
    """
    filename = input("Введите имя файла с данными: ")
    employees = []
    departments = []
    try:
        with open(filename, "r",encoding="utf-8") as fin:
            for line in fin:
                raw_data = line.strip().split(";")
                employees.append(
                    (
                    raw_data[0],
                    raw_data[1],
                    raw_data[2],
                    raw_data[4],
                    raw_data[3],
                    )
                )
                if (raw_data[4],) not in departments:
                    departments.append((raw_data[4],))
    except FileNotFoundError:
        print("="*30)
        print("Файл не найден, импорт не выполнен!")
        print("="*30)
        return
    # заполнить таблицу отделов
    dep_sql_template = "INSERT INTO Departments (name) values(?)"
    kwargs["db"].executemany(dep_sql_template, departments)
    # тут узкое место, я знаю как сделать это средствами питона,
    # но интересно как сделать это средствами sql
    emp_sql_template = "INSERT INTO Employees (name, secname, surname, dep_id, salary) \
                        values(?,?,?,(SELECT id FROM Departments WHERE name like ?),?)"
    kwargs["db"].executemany(emp_sql_template, employees)
    print("Импорт завершен!")
    print("=" * 20)


# ==============================================================================
def show_interface():
    """
    пользовательский крутой консольный интерфейс к базе.
    пока будет как одна функция, может быть имеет смысл его разбить
    """
    indexer = (str(i) for i in range(1, 100))
    interface_contents = [
        {
            "key": next(indexer),
            "name": "Вывести список всех работников",
            "foo": show_all_employees_data,
        },
        {
            "key": next(indexer),
            "name": "Вывести список всех отделов",
            "foo": show_all_departments_data,
        },
        {"key": next(indexer), "name": "Добавить сотрудника", "foo": add_employee},
        {"key": next(indexer), "name": "Добавить отдел", "foo": add_department},
        {
            "key": next(indexer),
            "name": "Вывести среднюю ЗП по отделам",
            "foo": show_average_salary_by_deps,
        },
        {
            "key": next(indexer),
            "name": "Экспорт данных в csv",
            "foo": export_data_to_excel_csv,
        },
        {
            "key": next(indexer),
            "name": "Импорт данных из csv",
            "foo": import_data_from_excel_csv,
        },
        {"key": next(indexer), "name": "Сохранить изменения", "foo": save_database},
        {"key": "0", "name": "Закончить работу", "foo": go_away},
        #        {#TODO это не работатет
        #            "key": "test",
        #            "name": "Переключиться на тестовую БД",
        #            "foo": swich_to_test_db,
        #        },
    ]
    is_working = True
    database = AdDatabase("Accounts.db")
    #with AdDatabase("Accounts.db") as database: #TODO E1129
    # и вообще надо подумать над этим
    while is_working:
        for task in interface_contents:
            print(f"{task['key']}:{task['name']}")
        user_responce = input("Введите номер желаемого действия:")
        user_responce = user_responce.strip()
        for task in interface_contents:
            if task["key"] == user_responce:
                # print("=============================")
                if task["foo"](db=database) is False:
                       is_working = False


# ==============================================================================
def main():
    """
    главная функция модуля
    """
    show_interface()


# ==============================================================================
if __name__ == "__main__":
    main()
