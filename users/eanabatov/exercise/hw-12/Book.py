"""
Создайте класс Book, который представляет книгу.
У него должны быть атрибуты для хранения названия,
автора, количества страниц и издательства.
Добавьте методы для установки и получения этих атрибутов.
"""


class Book:
    def __init__(self, name: str, author: str, number_of_pages: int, publisher: str):
        self.__validation(self, name, author, number_of_pages, publisher)
        self.__name: str = name.strip()
        self.__author: str = author.strip()
        self.__number_of_pages: int = number_of_pages
        self.__publisher: str = publisher.strip()

    @staticmethod
    def __validation(name: str, author: str, number_of_pages: int, publisher: str):
        is_valid_name: bool = isinstance(name, str)
        is_valid_author: bool = isinstance(author, str)
        is_valid_number_of_pages: bool = isinstance(number_of_pages, int) and (number_of_pages > 0)
        is_valid_publisher: bool = isinstance(publisher, str)

        is_not_valid: bool = not (
            is_valid_name
            and is_valid_author
            and is_valid_number_of_pages
            and is_valid_publisher
        )
        if is_not_valid:
            raise TypeError("Ошибка инициализации. Некорректные данные")

