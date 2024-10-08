"""
основной файл работы с базой данных записной телефонной книги
"""
from phonebook_database_stuff import (
    PhDatabase,
)
from usefulstuff import (
    ColoredStr,
)

# ==============================================================================
def go_away(**kwargs):
    """
    попытка аккуратно закончить с циклом выполнения программы
    """
    print("exiting...")
    return False  # d-_-b


# ==============================================================================
def show_all_contacts_data(**kwargs):
    """
    выводит на экран список всех записей в базе данных
    """
    result = kwargs["db"].execute(
        """
            SELECT con.id
                ,con.phone_number
                ,con.surname
                ,con.name
                ,s.name
                ,hc.color
                ,cit.name
            FROM Contacts con
            LEFT JOIN Cities cit ON con.city_id = cit.id
            LEFT JOIN Hair_colors hc ON con.hair_color_id = hc.id
            LEFT JOIN Schools s ON con.school_id = s.id;
        """
    )
    width = 1 + 4 + 1 + 5 * 21 + 31 + 1 - 20
    print("=" * width)
    t_caption = (
        "#",
        "Номер телефона",
        "Фамилия",
        "Имя",
        "Школа",
        "Цвет волос",
        "Город",
    )
    print(
        f"|{t_caption[0]:^4}|{t_caption[1]:^20}|{t_caption[2]:^15}|"
        f"{t_caption[3]:^15}|{t_caption[4]:^25}|{t_caption[5]:^15}|"
        f"{t_caption[6]:^20}|"
    )
    print("=" * width)
    for record in result:
        print(
            f"|{record[0]:4}|{record[1]:20}|{record[2]:15}|{record[3]:15}|"
            f"{record[4]:25}|{record[5]:15}|{record[6]:20}|"
        )
    print("=" * width)


# ==============================================================================
def show_all_contacts_data_additional_info(**kwargs):
    """
    выводит на экран список всех записей в базе данных
    с дополнительной информацией о любимых фруктах и спорте
    """
    result = kwargs["db"].execute(
        """
            SELECT con.id
                ,con.phone_number
                ,con.surname
                ,con.name
                ,con.secname
                ,ff.fruit
                ,fs.sport
            FROM Contacts con
            LEFT JOIN Favourite_fruits ff ON con.fruit_id = ff.id
            LEFT JOIN Favourite_sports fs ON con.sport_id = fs.id;
        """
    )
    width = 1 + 4 + 1 + 3* 16 + 3 * 21 + 1
    print("=" * width)
    t_caption = (
        "#",
        "Номер телефона",
        "Фамилия",
        "Имя",
        "Отчество",
        "Любимый фрукт",
        "Любимый спорт",
    )
    print(
        f"|{t_caption[0]:^4}|{t_caption[1]:^20}|{t_caption[2]:^15}|"
        f"{t_caption[3]:^15}|{t_caption[4]:^20}|{t_caption[5]:^15}|"
        f"{t_caption[6]:^20}|"
    )
    print("=" * width)
    for record in result:
        print(
            f"|{record[0]:4}|{record[1]:20}|{record[2]:15}|{record[3]:15}|"
            f"{record[4]:20}|{record[5]:15}|{record[6]:20}|"
        )
    print("=" * width)


# ==============================================================================
def show_all_cities_data(**kwargs):
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
    print(f"|{t_caption[0]:^4}|{t_caption[1]:^30}|{t_caption[2]:^10}|"
            f"{t_caption[3]:^10}|{t_caption[4]:^40}|")
    print("=" * width)
    for record in result:
        print(f"|{record[0]:4}|{record[1]:30}|{record[2]:10}|{record[3]:10}|{record[4]:40}|")
    print("=" * width)

# ==============================================================================
def show_all_schools_data(**kwargs):
    """
    выводит на экран список всех школ в базе данных
    """
    result = kwargs["db"].execute(
        """
            SELECT s.id
                ,s.snumber
                ,s.name
                ,s.address
                ,c.name
            FROM Schools s
            JOIN Cities c ON s.city_id = c.id

        """
    )
    width = 1 + 4 + 1 + 8 + 1 + 30 + 1 + 30 + 1 + 30 + 1
    t_caption = (
        "#",
        "Номер",
        "Название",
        "Адрес",
        "Город",
    )
    print("=" * width)
    print(f"|{t_caption[0]:^4}|{t_caption[1]:^8}|{t_caption[2]:^30}|"
            f"{t_caption[3]:^30}|{t_caption[4]:^30}|")
    print("=" * width)
    for record in result:
        print(f"|{record[0]:4}|{record[1]:8}|{record[2]:30}|{record[3]:30}|{record[4]:30}|")
    print("=" * width)


# ==============================================================================
def show_all_hair_color_data(**kwargs):
    """
    выводит на экран список всех цветов волос в базе данных
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
def show_all_fruits_data(**kwargs):
    """
    выводит на экран список всех фруктов в базе данных
    """
    result = kwargs["db"].execute("SELECT id, fruit FROM Favourite_fruits;")
    width = 1 + 4 + 1 + 15 + 1
    t_caption = (
        "#",
        "Любимый фрукт",
    )
    print("=" * width)
    print(f"|{t_caption[0]:^4}|{t_caption[1]:^15}|")
    print("=" * width)
    for record in result:
        print(f"|{record[0]:4}|{record[1]:15}|")
    print("=" * width)


# ==============================================================================
def show_all_sports_data(**kwargs):
    """
    выводит на экран список всех видов спорта в базе данных
    """
    result = kwargs["db"].execute("SELECT id, sport FROM Favourite_sports;")
    width = 1 + 4 + 1 + 20 + 1
    t_caption = (
        "#",
        "Вид спорта",
    )
    print("=" * width)
    print(f"|{t_caption[0]:^4}|{t_caption[1]:^20}|")
    print("=" * width)
    for record in result:
        print(f"|{record[0]:4}|{record[1]:20}|")
    print("=" * width)


# ==============================================================================
def enter_citi_id_interactive(**kwargs):
    """
    Ввод id города с контролем корректности и интерактивом
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
def enter_hair_color_id_interactive(**kwargs):
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
def enter_school_id_interactive(**kwargs):
    """
    Ввод индекса школы с контролем корректности и интерактивом
    """
    schools = kwargs["db"].execute("SELECT id FROM Schools")
    school_id = None
    trash_input = False
    while not isinstance(school_id, int):
        school_id = input("id школы (hint для вывода списка школ): ")
        school_id = school_id.strip().lower()
        if school_id == "hint":
            show_all_schools_data(db=kwargs["db"])
            continue
        try:
            school_id = int(school_id)
        except ValueError:
            trash_input = True
        # print(departments)
        if (trash_input) or ((school_id,) not in schools):
            print("Введите корректный id цвета волос!")
            school_id = None
            trash_input = False
    return school_id


# ==============================================================================
def enter_sport_id_interactive(**kwargs):
    """
    Ввод индекса любимого спорта с контролем корректности и интерактивом
    """
    sports = kwargs["db"].execute("SELECT id FROM Favourite_sports")
    sport_id = None
    trash_input = False
    while not isinstance(sport_id, int):
        sport_id = input("id вида спорта (hint для вывода списка видов спорта): ")
        sport_id = sport_id.strip().lower()
        if sport_id == "hint":
            show_all_sports_data(db=kwargs["db"])
            continue
        try:
            sport_id = int(sport_id)
        except ValueError:
            trash_input = True
        # print(departments)
        if (trash_input) or ((sport_id,) not in sports):
            print("Введите корректный id вида спорта!")
            sport_id = None
            trash_input = False
    return sport_id

# ==============================================================================
def enter_fruit_id_interactive(**kwargs):
    """
    Ввод индекса любимого фрукта с контролем корректности и интерактивом
    """
    fruits = kwargs["db"].execute("SELECT id FROM Favourite_fruits")
    fruit_id = None
    trash_input = False
    while not isinstance(fruit_id, int):
        fruit_id = input("id любимого фрукта (hint для вывода списка фруктов): ")
        fruit_id = fruit_id.strip().lower()
        if fruit_id == "hint":
            show_all_fruits_data(db=kwargs["db"])
            continue
        try:
            fruit_id = int(fruit_id)
        except ValueError:
            trash_input = True
        # print(departments)
        if (trash_input) or ((fruit_id,) not in fruits):
            print("Введите корректный id любимого фрукта!")
            fruit_id = None
            trash_input = False
    return fruit_id

# ==============================================================================
def add_record(**kwargs):
    """
    добавляет запись в  базу телефонной книги
    """
    phone_number = input("Номер телефона: ")
    surname = input("Фамилия: ")
    name = input("Имя: ")
    secname = input("Отчество: ")
    citi_id = enter_citi_id_interactive(db=kwargs["db"])
    hair_color_id = enter_hair_color_id_interactive(db=kwargs["db"])
    school_id = enter_school_id_interactive(db=kwargs["db"])
    sport_id = enter_sport_id_interactive(db=kwargs["db"])
    fruit_id = enter_fruit_id_interactive(db=kwargs["db"])
    kwargs["db"].execute(
        """
            INSERT INTO Contacts (
                name
                ,secname
                ,surname
                ,city_id
                ,hair_color_id
                ,phone_number
                ,school_id
                ,sport_id
                ,fruit_id
                )
            VALUES (
                ?
                ,?
                ,?
                ,?
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
            phone_number,
            school_id,
            sport_id,
            fruit_id
        ),
    )


# ==============================================================================
def save_database(**kwargs):
    """
    Сохраняет изменения в БД
    """
    kwargs["db"].commit()
    print("Изменения сохранены!")


# ==============================================================================
def add_city(**kwargs):
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
def add_school(**kwargs):
    """
    добавить новую школу в БД
    """
    print("Добавляем новую школу:")
    snumber = input("Номер: ")
    name = input("Название: ")
    address = input("Адрес: ")
    city_id = enter_citi_id_interactive(db=kwargs["db"])
    kwargs["db"].execute(
        """
            INSERT INTO Schools (
                snumber
                ,name
                ,address
                ,city_id
                )
            VALUES (
                ?
                ,?
                ,?
                ,?
                );
        """,
        (snumber, name, address, city_id),
    )


# ==============================================================================
def add_hair_color(**kwargs):
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
def add_fruit(**kwargs):
    """
    добавить новый фрукт в БД
    """
    print("Добавляем новый фрукт:")
    fruit = input("Название фрукта: ")
    kwargs["db"].execute(
        """
            INSERT INTO Favourite_fruits
            (fruit)
            VALUES (?);
        """,
        (fruit,),
    )

# ==============================================================================
def add_sport(**kwargs):
    """
    добавить новый вид спорта в БД
    """
    print("Добавляем новый вид спорта:")
    sport = input("Название вида спорта: ")
    kwargs["db"].execute(
        """
            INSERT INTO Favourite_sports
            (sport)
            VALUES (?);
        """,
        (sport,),
    )

# ==============================================================================
def show_all_majors(**kwargs):
    """
    Вывести количество записей в таблице, сгруппированное по мэру
    """
    average_data = kwargs["db"].execute(
        """
            SELECT major
                ,count(Contacts.name) AS count_of_contacts
            FROM Cities
            LEFT JOIN Contacts ON Cities.id = Contacts.city_id
            GROUP BY major
            ORDER BY count_of_contacts DESC
        """
    )
    width = 1 + 30 + 1 + 20 + 1
    t_caption = (
        "Мэр",
        "Число контактов",
    )
    print("=" * width)
    print(f"|{t_caption[0]:30}|{t_caption[1]:^20}|")
    print("=" * width)
    for record in average_data:
        print(f"|{record[0]:30}|{record[1]:^20}|")
    print("=" * width)

# ==============================================================================
def fill_tables_with_test_data(**kwargs):
    """
       Заполним таблицы какими-то данными
       """
    # cities
    data = kwargs["db"].execute(
        """
            INSERT INTO Cities
            (id, name, lat, lon, major)
            VALUES(2, 'Москва', 55.75222, 37.61556, 'Собянин С.С.')
            ,(3, 'Санкт-Петербург', 59.93863, 30.31413, 'Беглов А.Д.')
            ,(4, 'Пермь', 58.0105, 56.2502, 'Дёмкин А.Н.')
            ,(5, 'Самара', 53.2001, 50.15, 'Лапушкина Е.В.');
        """
    )
    # sports
    data = kwargs["db"].execute(
        """
            INSERT INTO Favourite_sports
            (id, sport)
            VALUES(1, 'Большой теннис')
            ,(2, 'Футбол')
            ,(3, 'Хоккей')
            ,(4, 'Горные лыжи')
            ,(5, 'Водное поло');
        """
    )
    # hairs
    data = kwargs["db"].execute(
        """
            INSERT INTO Hair_colors
            (id, color)
            VALUES(2, 'Блонд')
            ,(3, 'Русый')
            ,(4, 'Фиолетовый')
            ,(5, 'Каштановый')
            ,(6, 'Морской волны');
        """
    )
    # fruits
    data = kwargs["db"].execute(
        """
            INSERT INTO Favourite_fruits
            (id, fruit)
            VALUES(1, 'Абрикос')
            ,(2, 'Айва')
            ,(3, 'Апельсин')
            ,(4, 'Арбуз')
            ,(5, 'Банан')
            ,(6, 'Виноград')
            ,(7, 'Гранат')
            ,(8, 'Грейпфрут')
            ,(9, 'Груша')
            ,(10, 'Гуава')
            ,(11, 'Дыня')
            ,(12, 'Инжир')
            ,(13, 'Канталупа')
            ,(14, 'Карамбола')
            ,(15, 'Киви')
            ,(16, 'Красный банан')
            ,(17, 'Лимон')
            ,(18, 'Манго')
            ,(19, 'Марания')
            ,(20, 'Мушмула')
            ,(21, 'Пепино')
            ,(22, 'Персик')
            ,(23, 'Питайя')
            ,(24, 'Помело')
            ,(25, 'Сахарное яблоко')
            ,(26, 'Физалис')
            ,(27, 'Финик')
            ,(28, 'Хурма');
        """
    )
    # schools
    data = kwargs["db"].execute(
        """
            INSERT INTO Schools
            (id, snumber, name, address, city_id)
            VALUES(1, 1, 'Школа имени Гагарина', 'ул. Гагарина, 50', 5)
            ,(2, 4, 'Спортшкола', 'ул. Новаторов, 15/1', 4)
            ,(3, 6, 'Английская школа', 'ул. Школьная, д.1', 2);
        """
    )
    # contacts
    data = kwargs["db"].execute(
        """
            INSERT INTO Contacts
            (id, name, secname, surname, city_id, hair_color_id, phone_number, school_id, fruit_id, sport_id)
            VALUES(3, 'Иван', 'Иванович', 'Иванов', 2, 2, '+7 916 234 43 87', 1, 1, 1)
            ,(4, 'Василий', 'Павлович', 'Петров', 5, 4, '+7 903 645 73 49', 2, 2, 3)
            ,(5, 'Роман', 'Герасимович', 'Вакуленко', 3, 5, '+7 926 764 56 98', 3, 3, 1)
            ,(6, 'Петр', 'Анатольевич', 'Васильков', 2, 5, '+7 901 113 43 95', 2, 2, 2)
            ,(7, 'Анастасия', 'Артёмовна', 'Волжская', 3, 5, '+7 915 066 55 98', 2, 4, 2)
            ,(8, 'Алевтина', 'Петровна', 'Вакуленко', 5, 6, '+7 901 647 84 02', 3, 10, 5);
        """
    )
# ==============================================================================
def show_interface():
    """
    пользовательский крутой консольный интерфейс к базе.
    пока будет как одна функция, может быть имеет смысл его разбить
    """
    green_text = ColoredStr("green, bold")
    yellow_text = ColoredStr("yellow, bold")
    indexer = (str(i) for i in range(1, 100))
    interface_contents = (
        {
            "key": next(indexer),
            "name": yellow_text("Вывести все записи"),
            "foo": show_all_contacts_data,
        },
        {
            "key": next(indexer),
            "name": ("Вывести дополнительную информацию для записей (фрукты, спорт)"),
            "foo": show_all_contacts_data_additional_info,
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
        {
            "key": next(indexer),
            "name": "Вывести список всех школ",
            "foo": show_all_schools_data,
        },
        {
            "key": next(indexer),
            "name": "Вывести список всех любимых фруктов",
            "foo": show_all_fruits_data,
        },
        {
            "key": next(indexer),
            "name": "Вывести список всех любимых видов спорта",
            "foo": show_all_sports_data,
        },
        {"key": next(indexer), "name": yellow_text("Добавить запись"), "foo": add_record},
        {"key": next(indexer), "name": "Добавить город", "foo": add_city},
        {"key": next(indexer), "name": "Добавиь школу", "foo": add_school},
        {"key": next(indexer), "name": "Добавить цвет волос", "foo": add_hair_color},
        {"key": next(indexer), "name": "Добавить фрукт", "foo": add_fruit},
        {"key": next(indexer), "name": "Добавить вид спорта", "foo": add_sport},
        {"key": next(indexer), "name": "Вывести всех мэров", "foo": show_all_majors},
        {"key": next(indexer), "name": "Добавить тестовые данные", "foo": fill_tables_with_test_data},
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
        {"key": "save", "name": green_text("Сохранить изменения"), "foo": save_database},
        {"key": "exit", "name": green_text("Закончить работу"), "foo": go_away},
    )
    is_working = True
    database = PhDatabase("phonebook.sqlite3")
    red_text = ColoredStr("red, bold")
    if database is None:
        print("Не удалось инициировать работу с телефонной книгой")
        return 1
    print(f"\n{red_text('Телефонная книга v.2')}")
    print("Добро пожаловать!")

    while is_working:
        print("\nЧто делаем?")
        for task in interface_contents:
            print(f"{task['key']}:{task['name']}")
        user_responce = input("Введите номер или команду для выполнения действия:")
        user_responce = user_responce.strip()
        job_is_done = False
        for task in interface_contents:
            if task["key"] == user_responce:
                if task["foo"](db=database) is False:
                    is_working = False
                job_is_done = True
        if(is_working and job_is_done):
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
