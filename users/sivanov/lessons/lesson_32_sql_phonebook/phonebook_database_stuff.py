"""
модуль, содержащий функционал работы с базой данных для бухгалтерии
"""
import sqlite3

# ==============================================================================
class PhDatabase:
    """
    класс-обертка над БД
    """

    # ==============================================================================
    def __init__(self, path: str):
        """
        конструктор класса
        """
        self.__conn = sqlite3.connect(path)
        self.__cur = self.__conn.cursor()
        # создадим структуру таблиц БД
        # =======================================================================
        # Города
        try:
            self.__cur.execute(
                """
                CREATE TABLE Cities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    ,name TEXT UNIQUE
                    ,lat FLOAT
                    ,lon FLOAT
                    ,major TEXT
                    )
                """
            )
            #create table City(city varchar(10), city_lantitude int, city_longitude int, mayor VARCHAR(20))
        except sqlite3.OperationalError:
            pass
        # =======================================================================
        # Цвета волос
        try:
            self.__cur.execute(
                """
                CREATE TABLE Hair_colors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    ,color TEXT
                    )
                """
            )
        except sqlite3.OperationalError:
            pass
        # =======================================================================
        #Школы
        try:
            self.__cur.execute(
                """
                CREATE TABLE Schools (
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    ,snumber INTEGER
                    ,name TEXT
                    ,address TEXT
                    ,city_id INTEGER
                    ,FOREIGN KEY (citi_id) REFERENCES Cities(id)
                    )
                """
            )
        except sqlite3.OperationalError:
            pass
        # =======================================================================
        # сами записи
        try:
            self.__cur.execute(
                """
                CREATE TABLE Contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    ,name TEXT
                    ,secname TEXT
                    ,surname TEXT
                    ,city_id INTEGER
                    ,hair_color_id INTEGER
                    ,phone_number TEXT
                    ,FOREIGN KEY (citi_id) REFERENCES Cities(id)
                    ,FOREIGN KEY (hair_color_id) REFERENCES Hair_colors(id)
                    )
                """
            )
        except sqlite3.OperationalError:
            pass
        # =======================================================================
    # ==============================================================================
    def execute(self, template_request, data=tuple()):
        """
        Интерфейс для cursor.execute
        """
        # print(template_request)
        self.__cur.execute(template_request, data)
        return self.__cur.fetchall()

    # ==============================================================================
    def executemany(self, template_request, data):
        """
        Интерфейс для sqlite3.cursor.executemany
        """
        return self.__cur.executemany(template_request, data)

    # ==============================================================================
    def commit(self):
        """
        Интерфейс для sqlite3.connection.commit
        """
        self.__conn.commit()

    # ==============================================================================
    def create_function(self, *args, **kwargs):
        """
        Интерфейс для sqlite3.connection.create_function
        """
        self.__conn.create_function(args, kwargs)
    # ==============================================================================    
    def __enter__(self):
        """
        начало контекста
        """
        pass
    # ==============================================================================  
    def __exit__(self, exc_type, exc_value, traceback):
        """
        конец контекста
        """
        self.__cur = None
        self.__conn.close()
        print('exit exception text: %s' % exc_value)
        return True
# ==============================================================================
