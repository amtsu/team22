"""
модуль, содержащий функционал работы с базой данных для бухгалтерии
"""
import sqlite3

# ==============================================================================
class AdDatabase:
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
        try:
            self.__cur.execute(
                """CREATE TABLE Departments
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE)"""
            )
        except sqlite3.OperationalError:
            pass
        try:
            self.__cur.execute(
                """CREATE TABLE Employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                secname TEXT,
                surname TEXT,
                dep_id INTEGER,
                salary INTEGER,
                FOREIGN KEY (dep_id) REFERENCES Departments(id))"""
            )
        except sqlite3.OperationalError:
            pass

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
