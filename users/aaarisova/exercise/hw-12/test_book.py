import pytest
from book import Book


book1 = Book('Ведьмак', 'А.Сапкоовский', 320, 'ACT')
book2 = Book('Лабиринт отражений', 'С.Лукьяненко', -470, 'Азбука')

def test_atributes():
    assert book2.title == 'Лабиринт отражений'
    assert book2.author == 'С.Лукьяненко'
    assert book2.pages == -470
    assert book2.publisher == 'Азбука'


def test_get_book1_title():
    assert book1.get_title() == 'Ведьмак'

    
def test_get_book1_author():
    assert book1.get_author() == 'А.Сапкоовский'


def test_get_book1_title():
    assert book1.get_pages() == 320


def test_get_book1_publisher():
    assert book1.get_publisher() == 'ACT'   


def test_set_book1_title():
    excepted_result = 'The Witcher'
    book1.set_title(excepted_result)
    assert excepted_result == book1.get_title()

    
def test_set_book1_author():
    excepted_result = 'Sapkowski Andrzej'
    book1.set_author(excepted_result)
    assert excepted_result == book1.get_author()


def test_set_book1_pages():
    excepted_result = 280
    book1.set_pages(excepted_result)
    assert excepted_result == book1.get_pages()
    

def test_set_book1_publisher():
    excepted_result = 'Orion'
    book1.set_publisher(excepted_result)
    assert excepted_result == book1.get_publisher()




