class Book:
    """
    Класс представляет книгу. 
    Имеет атрибуты для хранения названия, автора, количества страниц и издательства. 
    Имеет методы для установки и получения этих атрибутов.
    """
    def __init__(self):
        self.__title = ""
        self.__author = ""
        self.__pages_num = 0
        self.__publisher = ""

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author 

    def set_pages_num(self, pages_num):
        self.__pages_num = pages_num

    def set_publisher(self, publisher):
        self.__publisher = publisher 

    def get_title(self, title):
        return self.__title

    def get_author(self, author):
        return self.__author 

    def get_pages_num(self, pages_num):
        return self.__pages_num

    def get_publisher(self, publisher):
        return self.__publisher