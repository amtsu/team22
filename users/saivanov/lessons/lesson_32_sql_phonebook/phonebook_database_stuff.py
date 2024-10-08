"""
модуль, содержащий функционал работы с базой данных записной книжки
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
                    ,name VARCHAR(100) UNIQUE
                    ,lat FLOAT
                    ,lon FLOAT
                    ,major TEXT
                    )
                """
            )
        except sqlite3.OperationalError:
            pass
        # =======================================================================
        # Цвета волос
        try:
            self.__cur.execute(
                """
                CREATE TABLE Hair_colors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT
                    ,color VARCHAR(100)
                    )
                """
            )
        except sqlite3.OperationalError:
            pass
        # =======================================================================
        # любимый спорт
        try:
            self.__cur.execute(
                """
                    CREATE TABLE Favourite_sports (
                        id INTEGER PRIMARY KEY AUTOINCREMENT
                        ,sport VARCHAR(100)
                        );
                """
            )
        except sqlite3.OperationalError:
            pass
        # =======================================================================
        # любимый фрукт, и заодно заполним её фруктами
        try:
            self.__cur.execute(
                """
                    CREATE TABLE Favourite_fruits (
                        id INTEGER PRIMARY KEY AUTOINCREMENT
                        ,fruit VARCHAR(100)
                        );
                """
            )
        except sqlite3.OperationalError:
            pass
        # =======================================================================
        # Школы
        try:
            self.__cur.execute(
                """
                    CREATE TABLE Schools (
                        id INTEGER PRIMARY KEY AUTOINCREMENT
                        ,snumber INTEGER
                        ,name VARCHAR(100)
                        ,address VARCHAR(500)
                        ,city_id INTEGER
                        ,FOREIGN KEY (city_id) REFERENCES Cities(id)
                        );
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
                        ,name VARCHAR(100)
                        ,secname VARCHAR(100)
                        ,surname VARCHAR(100)
                        ,city_id INTEGER
                        ,hair_color_id INTEGER
                        ,phone_number VARCHAR(100)
                        ,school_id INTEGER
                        ,fruit_id INTEGER
                        ,sport_id INTEGER
                        ,CONSTRAINT FK_Contacts_Schools FOREIGN KEY (school_id) REFERENCES Schools(id)
                        ,CONSTRAINT FK_Contacts_Cities FOREIGN KEY (city_id) REFERENCES Cities(id)
                        ,CONSTRAINT FK_Contacts_Hair_colors FOREIGN KEY (hair_color_id) REFERENCES Hair_colors(id)
                        ,CONSTRAINT FK_Contacts_Fruits FOREIGN KEY (fruit_id) REFERENCES Favourite_fruits(id)
                        ,CONSTRAINT FK_Contacts_Sports FOREIGN KEY (sport_id) REFERENCES Favourite_sports(id)
                        );
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
    # def __enter__(self):
    #     """
    #     начало контекста
    #     """
    #     pass

    # ==============================================================================
    # def __exit__(self, exc_type, exc_value, traceback):
    #     """
    #     конец контекста
    #     """
    #     self.__cur = None
    #     self.__conn.close()
    #     print(f"exit exception text: {exc_value}")
    #     return True


# ==============================================================================
