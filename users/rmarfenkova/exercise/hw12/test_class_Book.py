import pytest
from class_Book import Book

@pytest.mark.parametrize("title", ["Гарри Поттер", "1984", "Автостопом по галактике"])
def test_book_title(title):
    book = Book()
    book.title = title
    assert book.title == title

@pytest.mark.parametrize("author", ["Михаил Булгаков", "Дуглас Адамс", "Джордж Оруэлл"])
def test_author(author):
    book = Book()
    book.author = author
    assert book.author == author

@pytest.mark.parametrize("pages", [100, 200, 300])
def test_pages(pages):
    book = Book()
    book.pages = pages
    assert book.pages == pages

@pytest.mark.parametrize("publisher", ["Pan Books", "Москва", "Secker & Warburg"])
def test_publisher(publisher):
    book = Book()
    book.publisher = publisher
    assert book.publisher == publisher

# тестирование проверки значений атрибутов pages

@pytest.mark.parametrize("invalid_pages", [0, -100, "abc"])
def test_invalid_pages(invalid_pages):
    with pytest.raises(ValueError):
        book = Book()
        book.pages = invalid_pages

#тестирование статического метода create
@pytest.mark.parametrize("a_book_title, a_author, num_pages, a_publisher, expected", [
    ("Гарри Поттер", "Дж.К Ролинг", 600, "РОСМЭН", "Гарри Поттер"),
    ("1984", "Джордж Оруэлл", 336, "Secker & Warburg", "Джордж Оруэлл"),
    ("Автостопом по галактике", "Дуглас Адамс", 216, "Pan Books", 216),
    ("Мастер и Маргарита", "Михаил Булгаков", 384, "Художественная литература", "Художественная литература")
   
])
def test_create(a_book_title, a_author, num_pages, a_publisher, expected):
    new_book = Book.create(a_book_title, a_author, num_pages, a_publisher)
    assert new_book.book_title == a_book_title
    assert new_book.author == a_author
    assert new_book.pages == num_pages
    assert new_book.publisher == a_publisher


def test_create_negative():
    with pytest.raises(ValueError):
        new_book = Book.create("Автостопом по галактике", "Дуглас Адамс", -216, "Pan Books")
        
        
        
        

    
