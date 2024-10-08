
class Book():
    """
    Создайте класс Book, который представляет книгу. У него должны быть атрибуты для хранения названия, автора,
    количества страниц и издательства. Добавьте методы для установки и получения этих атрибутов.
    """

    def __init__(self):
        self.__book_title = ""
        self.__author = ""
        self.__pages = 0
        self.__publishing_house = ""
        
    @property    
    def title(self):      # метод получения атрибутов
        return self.__book_title

    @title.setter   
    def title(self, title):    # метод для установки фтрибутов
        self.__book_title = title
        
    @property    
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author
        
    @property    
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        if type(pages) is int and pages > 0:
            self.__pages = pages
        else:
            raise ValueError
    
    @property   
    def publisher(self):
        return self.__publisher
        
    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = publisher

    @staticmethod
    def create(a_book_title, a_author, num_pages, a_publisher):
        """
        статический метод класса(вызываемый не зависимо от создания экземпляра)
        который возвращает экземпляр класса
        """
        new_book = Book()
        new_book.book_title = a_book_title
        new_book.author = a_author
        new_book.pages = num_pages
        new_book.publisher = a_publisher
        return new_book