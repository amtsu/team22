import pytest
from book import Book

def test_book_name():
    book1 = Book('Old man adn the sea', 'Hemingway', 120, 'XX century books')
    assert book1.get_name() == 'Old man adn the sea'

def test_book_author():
    book1 = Book('Old man adn the sea', 'Hemingway', 120, 'XX century books')
    assert book1.get_author() == 'Hemingway'

def test_book_pages():
    book1 = Book('Old man adn the sea', 'Hemingway', 120, 'XX century books')
    assert book1.get_pages() == 120

def test_book_publishers():
    book1 = Book('Old man adn the sea', 'Hemingway', 120, 'XX century books')
    assert book1.get_publishers() == 'XX century books'