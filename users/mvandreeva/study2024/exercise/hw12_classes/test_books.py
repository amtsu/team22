import pytest

from books import Book

def test_books_title():
    new_book = Book()
    new_book.set_title("Война и мир")
    assert new_book.get_title() == "Война и мир"

def test_books_author():
    new_book = Book()
    new_book.set_author("Л.Н.Толстой")
    assert new_book.get_author() == "Л.Н.Толстой"

def test_books_pages_num():
    new_book = Book()
    new_book.set_pages_num(3000)
    assert new_book.get_pages_num() == 3000

def test_books_publisher():
    new_book = Book()
    new_book.set_publisher("ЭКСМО")
    assert new_book.get_publisher() == "ЭКСМО"