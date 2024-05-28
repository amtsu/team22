"""
Создайте класс Book, который представляет книгу. У него должны быть атрибуты для хранения названия, автора, количества страниц и издательства. Добавьте методы для установки и получения этих атрибутов.
"""
class Book:

    def __init__(self, title, author, pages, publisher):
        self.title = title
        self.author = author
        self.pages = pages
        self.publisher = publisher

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_pages(self, pages):
        self.pages = pages

    def get_pages(self):
        return self.pages

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self):
        return self.publisher

# Пример использования класса
book1 = Book("1984", "George Orwell", 328, "Penguin Books")

# Получаем информацию о книге
print("Название книги:", book1.get_title())
print("Автор книги:", book1.get_author())
print("Количество страниц:", book1.get_pages())
print("Издательство:", book1.get_publisher())

# Изменяем издательство книги
book1.set_publisher("Random House")

# Повторно получаем информацию о книге
print("\nИзмененное издательство:", book1.get_publisher())