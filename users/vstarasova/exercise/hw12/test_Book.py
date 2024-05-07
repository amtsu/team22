import pytest
from Book import Book

def test_set_title():
    book1 = Book("1984", "George Orwell", 328, "Penguin Books")
    book1.set_title("Cindirella")
    assert book1.get_title() == "Cindirella"

    print("Тесты для метода set_title пройдены успешно!")

def test_get_title():
    book1 = Book("1984", "George Orwell", 328, "Penguin Books")
    assert book1.get_title() == "1984"

    print("Тесты для метода get_title пройдены успешно!")

def test_set_author():
    book1 = Book("1984", "George Orwell", 328, "Penguin Books")
    book1.set_author("James Brown")
    assert book1.get_author() == "James Brown"

    print("Тесты для метода set_author пройдены успешно!")

def test_get_author():
    book1 = Book("1984", "George Orwell", 328, "Penguin Books")
    assert book1.get_author() == "George Orwell"

    print("Тесты для метода get_author пройдены успешно!")

def test_set_pages():
    book1 = Book("1984", "George Orwell", 328, "Penguin Books")
    book1.set_pages(100)
    assert book1.get_pages() == 100

    print("Тесты для метода set_pages пройдены успешно!")

def test_get_pages():
    book1 = Book("1984", "George Orwell", 328, "Penguin Books")
    assert book1.get_pages() == 328

    print("Тесты для метода set_pages пройдены успешно!")

def test_set_publisher():
    book1 = Book("1984", "George Orwell", 328, "Penguin Books")
    book1.set_publisher("Alpina Book")
    assert book1.get_publisher() == "Alpina Book"

    print("Тесты для метода set_publisher пройдены успешно!")

def test_get_publisher():
    book1 = Book("1984", "George Orwell", 328, "Penguin Books")
    assert book1.get_publisher() == "Penguin Books"

    print("Тесты для метода set_publishere пройдены успешно!")