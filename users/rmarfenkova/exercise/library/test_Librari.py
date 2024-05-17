import pytest
from class_Library import Book, User, Library

def tets_add_books_for_user():
    """добавление книг для пользователя больше 5"""
    user = User("Regina")
    books = [Book("Преступление и наказание", "Фёдор Достоевский", "роман", 400),
             Book("Властелин колец", "avtor2", "фентези", 300),
             Book("Анна Каренина", "avtor2", "роман", 300),
             Book("Гарри Поттер и философский камен", "Дж. К. Роулинг", "фентези", 300),
             Book("title5", "avtor5", "ужасы", 300),
             Book("title6", "avtor6", "триллер", 500)]
    with pytest.raises(ValueError):
        for book in books:
            user.add_books_for_user(book)


def test_take_book():
    """забираю книгу у пользователя и возвращаю в библиотеку"""
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", "роман", 400)
    book = Book("Властелин колец", "avtor2", "фентези", 300)
    library = Library()
    library.add_book(book2)
    library.add_book(book)
    user = User("Regina")
    #библиотека выдает книгу и списывает ее из библиотеки
    library.give_book(book, user)
    # библиотека забирает книгу у пользователя и добавляет книгу обратно
    library.take_book(user, book)
    assert library.count_book_in_library() == 2
    assert user.count_books_for_user() == None
   

def test_give_book():
    """выдача книги пользователю из библиотеки"""
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", "роман", 400)
    book = Book("Властелин колец", "avtor2", "фентези", 300)
    library = Library()
    library.add_book(book)
    library.add_book(book2)
    user = User("Regina")
    library.give_book(book, user)
    assert library.count_book_in_library() == 1
    assert user.count_books_for_user() == 1


def tets_return_book_in_library():
    """пользователь возвращает книгу"""
    user = User("Regina")
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", "роман", 400)
    book = Book("Властелин колец", "avtor2", "фентези", 300)
    book3 = Book("Анна Каренина", "avtor2", "роман", 300)
    user.return_book_in_library(book2)
    assert user.count_books_for_user() == 2
    
    
def tets_add_books_for_user():
    """добавление книг для чтения пользователю"""
    user = User("Regina")
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", "роман", 400)
    book = Book("Властелин колец", "avtor2", "фентези", 300)
    book3 = Book("Анна Каренина", "avtor2", "роман", 300)
    user.add_books_for_user(book2)
    user.add_books_for_user(book)
    user.add_books_for_user(book3)    
    assert user.count_books_for_user() == 3 


def test_add_book():
    """тест на добавление книг в библиотеку"""
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", "роман", 400)
    book = Book("Властелин колец", "avtor2", "фентези", 300)
    book3 = Book("Анна Каренина", "avtor2", "роман", 300)
    book4 = Book("Гарри Поттер и философский камен", "Дж. К. Роулинг", "фентези", 300)
    
    library = Library()
    library.add_book(book)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    assert library.count_book_in_library() == 4
    


def test_find_book():
    """тест на поиск книг в библиотеке по жанру, автору и названию"""
    book2 = Book("Преступление и наказание", "Фёдор Достоевский", "роман", 400)
    book = Book("Властелин колец", "avtor2", "фентези", 300)
    book3 = Book("Анна Каренина", "avtor2", "роман", 300)
    book4 = Book("Гарри Поттер и философский камен", "Дж. К. Роулинг", "фентези", 300)
    
    library = Library()
    library.add_book(book)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    rezult = library.find_book("Преступление и наказание", "avtor2", "роман")
    assert len(rezult) == 3

    
def test_total_pages_in_library():
    """ тест на подсчет общего количества страниц в библиотеке"""
    book2 = Book("title2", "avtor1", "fantasy", 400)
    book = Book("title1", "avtor2", "roman", 300)
    
    library = Library()
    library.add_book(book)
    library.add_book(book2)
    assert library.total_pages_in_library() == 700
    


def test_avg_pages_in_library():
    """тест на среднее количество страниц"""
    book2 = Book("title2", "avtor1", "fantasy", 400)
    book = Book("title1", "avtor2", "roman", 300)
    
    library = Library()
    library.add_book(book)
    library.add_book(book2)
    assert library.avg_pages_in_library() == 350
    

def test_count_book_in_library():
    """метод считает количество книг в библиотеке"""
    book2 = Book("title2", "avtor1", "fantasy", 400)
    book = Book("title1", "avtor2", "roman", 300)
    library = Library()
    library = Library()
    library.add_book(book)
    library.add_book(book2)
    assert library.count_book_in_library() == 2
    
