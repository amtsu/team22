class Book:
    def __init__(self, title: str, author: str, number_of_pages: int, publisher: str):
        self.__title = title
        self.__author = author
        self.__number_of_pages = number_of_pages
        self.__publisher = publisher

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def number_of_pages(self):
        return self.__number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, number_of_pages: int):
        self.__number_of_pages = number_of_pages

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher


if __name__ == "__main__":
    book = Book('Гарри Поттер', 'Джоан Роулинг', 432, 'Махаон')
    book.title = 'Занимательная ядерная физика'
    assert book.title == 'Занимательная ядерная физика'
    book.author = 'Мухин Константин Никифорович'
    assert book.author == 'Мухин Константин Никифорович'
    book.number_of_pages = 1972
    assert book.number_of_pages == 1972
    book.publisher = 'Голос'
    assert book.publisher == 'Голос'
