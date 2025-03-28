from func_book import Book

#Создайте класс Book, который представляет книгу. У него должны быть атрибуты для хранения названия, автора, количества страниц и издательства. Добавьте методы для установки и получения этих атрибутов.
books_1 = Book ('Идиот', 'Достоевский', 640, 'Эксмо')

#тест для проверки названия книги
def test_Getname():
    assert books_1.Getname() == 'Идиот'
#тест для проверки автора
def test_Getauthor():
    assert books_1.Getauthor() == 'Достоевский'
#тест для проверки автора
def test_Getnumber_pages():
    assert books_1.Getnumber_pages() == 640
#тест для проверки издательства
def test_Getpublishing():
    assert books_1.Getpublishing() == 'Эксмо'