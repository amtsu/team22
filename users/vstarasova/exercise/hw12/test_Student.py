import pytest
from Student import Student

def test_init():
    student1 = Student("Иван", "Иванов", 20, "ул. Пушкина, д. 10", [4, 5, 3, 4, 5])
    assert student1.name == "Иван"
    assert student1.surname == "Иванов"
    assert student1.age == 20
    assert student1.address == "ул. Пушкина, д. 10"
    assert student1.rates == [4, 5, 3, 4, 5]
