
#Создайте класс Book, который представляет книгу. У него должны быть атрибуты для хранения названия, автора, количества страниц и издательства. Добавьте методы для установки и получения этих атрибутов.
class Book:
    def __init__(self, name, author, pages, publishers):
        self.name = name
        self.author = author
        self.pages = pages
        self.publishers = publishers

    def set_name(self, name): #добавляем методы установки и получения аттрибутов
        self.name = name
    def get_name(self):
        return self.name

    def set_author(self, author):
        self.author = author
    def get_author(self):
        return self.author

    def set_pages(self, pages):
        if pages is int and pages > 0:
            self.pages = pages
        else:
            print("Wrong attribute, must be at least 1 page")
    def get_pages(self):
            return self.pages
        
    def set_publishers(self, publishers):
        self.publishers = publishers
    def get_publishers(self):
        return self.publishers

             