import pytest
from part1_Book import Book

LoR = Book('Властелин колец', 'Толкин', 1500, 'Эксмо')

def test_book_getAuthor():
    expected = 'Толкин'
    assert expected == LoR.getAuthor()

def test_book_setgetAuthor():
    expected = 'Толкиен'
    LoR.setAuthor('Толкиен')
    assert expected == LoR.getAuthor()

def test_book_getName():
    expected = 'Властелин колец'
    assert expected == LoR.getName()
