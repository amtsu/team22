import pytest
from Student2 import Student2

def test_add_rate():
    student1 = Student2("Иван", "Иванов", 20, "ул. Пушкина, д. 10", [4, 5, 3, 4, 5])
    assert student1.add_rate(5) == [4, 5, 3, 4, 5, 5]

def test_calculateGPA():
    student1 = Student2("Иван", "Иванов", 20, "ул. Пушкина, д. 10", [4, 5, 3, 4, 5])
    assert student1.calculateGPA() == 4.2