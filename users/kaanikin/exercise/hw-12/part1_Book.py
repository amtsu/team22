class Book:
    """
    Создайте класс Book, который представляет книгу. У него должны быть атрибуты для хранения названия, автора, количества страниц и издательства. Добавьте методы для установки и получения этих атрибутов.
    """
    def __init__(self, name, author, num_pages, publisher):
        self.name = name
        self.author = author
        self.num_pages = num_pages
        self.publisher = publisher

    def getName(self):
        return self.name

    def getAuthor(self):
        return self.author

    def getNum_pages(self):
        return self.num_pages

    def getPublisher(self):
        return self.publisher

    def setName(self, value):
        self.name = value

    def setAuthor(self, value):
        self.author = value

    def setNum_pages(self, value):
        set.num_pages = value

    def setPublisher(self, value):
        set.publisher = value


