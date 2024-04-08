'''3.Создайте класс Book, который представляет книгу. У него должны быть атрибуты для хранения названия, автора, количества страниц и издательства. Добавьте методы для установки и получения этих атрибутов.'''


class Book():
    
    def __init__(self, title, author, pages, publisher):
        self.title = title
        self.author = author
        self.pages = pages
        self.publisher = publisher


    def set_title(self, title):
        self.title = title

    
    def set_author(self,author):
        self.author = author


    def set_pages(self,pages):
        self.pages = pages
    

    def set_publisher(self,publisher):
        self.publisher = publisher


    def get_title(self):
        return self.title

    
    def get_author(self):
        return self.author


    def get_pages(self):
        return self.pages
    

    def get_publisher(self):
        return self.publisher






