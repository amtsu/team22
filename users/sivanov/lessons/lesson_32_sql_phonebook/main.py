"""
основной файл работы с базой данных бухгалтерии (accounts department)
"""
from phonebook_database_stuff import (
    PhDatabase,
)
from usefulstuff import (
    ColoredStr,
)

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
            SELECT con.id
                ,con.phone_number
                ,con.surname
                ,con.name
                ,con.secname
                ,hc.color
                ,cit.name
            FROM Contacts con
            LEFT JOIN Cities cit ON con.city_id = cit.id
            LEFT JOIN Hair_colors hc ON con.hair_color_id = hc.id;
        """
    )
    width = 1 + 4 + 1 + 5 * 21 + 31 + 1
    print("=" * width)
    t_caption = (
        "#",
        "Номер телефона",
        "Фамилия",
        "Имя",
        "Отчество",
        "Цвет волос",
        "Город",
    )
    print(
        f"|{t_caption[0]:^4}|{t_caption[1]:^20}|{t_caption[2]:^20}|"
        f"{t_caption[3]:^20}|{t_caption[4]:^20}|{t_caption[5]:^20}|"
        f"{t_caption[6]:^30}|"
    )
    print("=" * width)
    for record in result:
        print(
            f"|{record[0]:4}|{record[1]:20}|{record[2]:20}|{record[3]:20}|"
            f"{record[4]:20}|{record[5]:20}|{record[6]:30}|"
        )
    print("=" * width)


# ==============================================================================
def show_all_cities_data(*args, **kwargs):
    """
    выводит на экран список всех городов в базе данных
    """
    result = kwargs["db"].execute("SELECT * FROM Cities")
    width = 1 + 4 + 1 + 30 + 1+ 10 + 1 + 10 + 1 + 40 + 1
    t_caption = (
        "#",
        "Название",
        "Широта",
        "Долгота",
        "Мэр",
    )
    print("=" * width)
    print(f"|{t_caption[0]:^4}|{t_caption[1]:^30}|{t_caption[2]:^10}|{t_caption[3]:^10}|{t_caption[4]:^40}|")
    print("=" * width)
    for record in result:
        print(f"|{record[0]:4}|{record[1]:30}|{record[2]:10}|{record[3]:10}|{record[4]:40}|")
    print("=" * width)


# ==============================================================================
def show_all_hair_color_data(*args, **kwargs):
    """
    выводит на экран список всех городов в базе данных
    """
    result = kwargs["db"].execute("SELECT * FROM Hair_colors")
    width = 1 + 4 + 1 + 30 + 1
    t_caption = (
        "#",
        "Цвет",
    )
    print("=" * width)
    print(f"|{t_caption[0]:^4}|{t_caption[1]:^30}|")
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
def enter_citi_id_interactive(*args, **kwargs):
    """
    Ввод номера отдела с контролем корректности и интерактивом
    """
    cities = kwargs["db"].execute("SELECT id FROM cities")
    citi_id = None
    trash_input = False
    while not isinstance(citi_id, int):
        citi_id = input("id города (hint для вывода списка городов): ")
        citi_id = citi_id.strip().lower()
        if citi_id == "hint":
            show_all_cities_data(db=kwargs["db"])
            continue
        try:
            citi_id = int(citi_id)
        except ValueError:
            trash_input = True
        # print(departments)
        if (trash_input) or ((citi_id,) not in cities):
            print("Введите корректный id города!")
            citi_id = None
            trash_input = False
    return citi_id
# ==============================================================================
def enter_hair_color_id_interactive(*args, **kwargs):
    """
    Ввод индекса цвета волос с контролем корректности и интерактивом
    """
    hair_colors = kwargs["db"].execute("SELECT id FROM Hair_colors")
    hair_color_id = None
    trash_input = False
    while not isinstance(hair_color_id, int):
        hair_color_id = input("id цвета волос (hint для вывода списка цветов волос): ")
        hair_color_id = hair_color_id.strip().lower()
        if hair_color_id == "hint":
            show_all_hair_color_data(db=kwargs["db"])
            continue
        try:
            hair_color_id = int(hair_color_id)
        except ValueError:
            trash_input = True
        # print(departments)
        if (trash_input) or ((hair_color_id,) not in hair_colors):
            print("Введите корректный id цвета волос!")
            hair_color_id = None
            trash_input = False
    return hair_color_id


# ==============================================================================
def add_record(*args, **kwargs):
    """
    добавляет запись в  базу телефонной книги
    """
    secname = input("Номер телефона: ")
    surname = input("Фамилия: ")
    name = input("Имя: ")
    secname = input("Отчество: ")
    citi_id = enter_citi_id_interactive(db=kwargs["db"])
    hair_color_id = enter_hair_color_id_interactive(db=kwargs["db"])
    kwargs["db"].execute(
        """
            INSERT INTO Contacts (
                name
                ,secname
                ,surname
                ,city_id
                ,hair_color_id
                ,phone_number
                )
            VALUES (
                ?
                ,?
                ,?
                ,?
                ,?
                ,?
                );
        """,
        (
            name,
            secname,
            surname,
            int(citi_id),
            int(hair_color_id),
            phone_number
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
def add_city(*args, **kwargs):
    """
    добавить новый город в БД
    """
    print("Добавляем новый город:")
    name = input("Название: ")
    lat = input("Широта: ")
    lon = input("Долгота: ")
    major = input("Мэр: ")
    kwargs["db"].execute(
        """
            INSERT INTO Cities (
                name
                ,lat
                ,lon
                ,major
                )
            VALUES (
                ?
                ,?
                ,?
                ,?
                );
        """,
        (name,lat, lon, major),
    )


# ==============================================================================
def add_hair_color(*args, **kwargs):
    """
    добавить новый цвет волос в БД
    """
    print("Добавляем новый цвет волос:")
    color = input("Цвет: ")
    kwargs["db"].execute(
        """
            INSERT INTO Hair_colors (color)
            VALUES (?);
        """,
        (color,),
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
            "name": "Вывести все записи",
            "foo": show_all_employees_data,
        },
        {
            "key": next(indexer),
            "name": "Вывести список всех городов",
            "foo": show_all_cities_data,
        },
        {
            "key": next(indexer),
            "name": "Вывести список всех цветов волос",
            "foo": show_all_hair_color_data,
        },
        {"key": next(indexer), "name": "Добавить запись", "foo": add_record},
        {"key": next(indexer), "name": "Добавить город", "foo": add_city},
        {"key": next(indexer), "name": "Добавить цвет волос", "foo": add_hair_color},
        # {
        #     "key": next(indexer),
        #     "name": "Вывести среднюю ЗП по отделам",
        #     "foo": show_average_salary_by_deps,
        # },
        # {
        #     "key": next(indexer),
        #     "name": "Экспорт данных в csv",
        #     "foo": export_data_to_excel_csv,
        # },
        # {
        #     "key": next(indexer),
        #     "name": "Импорт данных из csv",
        #     "foo": import_data_from_excel_csv,
        # },
        {"key": next(indexer), "name": "Сохранить изменения", "foo": save_database},
        {"key": "0", "name": "Закончить работу", "foo": go_away},
        #        {#TODO это не работает
        #            "key": "test",
        #            "name": "Переключиться на тестовую БД",
        #            "foo": swich_to_test_db,
        #        },
    ]
    is_working = True
    database = PhDatabase("phonebook.sqlite3")
    red_text = ColoredStr("red, bold")
    if database is None:
        print("Не удалось инициировать работу с телефонной книгой")
        return 1
    else:
        print(f"\n{red_text('Телефонная книга v.2')}")
        print("Добро пожаловать!")

    while is_working:
        print("\nЧто делаем?")
        for task in interface_contents:
            print(f"{task['key']}:{task['name']}")
        user_responce = input("Введите номер желаемого действия:")
        user_responce = user_responce.strip()
        for task in interface_contents:
            if task["key"] == user_responce:
                # print("=============================")
                if task["foo"](db=database) is False:
                       is_working = False
        if(is_working):
            dummy = input("Нажмите Enter чтобы продолжить работу...")
    return 0


# ==============================================================================
def main():
    """
    главная функция модуля
    """
    show_interface()


# ==============================================================================
if __name__ == "__main__":
    main()
