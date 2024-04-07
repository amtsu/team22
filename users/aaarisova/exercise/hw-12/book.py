'''3.Создайте класс Book, который представляет книгу. У него должны быть атрибуты для хранения названия, автора, количества страниц и издательства. Добавьте методы для установки и получения этих атрибутов.'''


class Book():
    
    def __init__(self, title, author, pages, publisher):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__publisher = publisher


    def my_book(self):
        return self.__title, self.__author, self.__pages, self.__publisher


