#Создайте класс Book, который представляет книгу.
#У него должны быть атрибуты для хранения названия, автора,
#количества страниц и издательства.
#Добавьте методы для установки и получения этих атрибутов.

class Book:
    def __init__(
            self,
            name = None,
            author = None,
            pages = None,
            publishing = None
    ):
        self.name = name
        self.author = author
        self.pages = pages
        self.publishing = publishing

    def get_name(self, name):
        self.name = name

    def get_author(self, author):
        self.author = author

    def get_pages(self, pages):
        self.pages = pages

    def get_publishing(self, publishing):
        self.publishing = publishing

    def ret_name(self):
        return self.name

    def ret_author(self):
        return self.author

    def ret_pages(self):
        return self.pages

    def ret_publishing(self):
        return self.publishing

book1 = Book()

print(book1.ret_name())
book1.get_name('World and Mir')
print(book1.ret_name())


