import pytest
from MAI import MAI

def test_add_student():
    mai = MAI()
    mai.add_student("Иван", "Иванов", 20, "Москва", [4, 5, 4, 3])
    assert len(mai.students) == 1
    assert mai.students[0].name == "Иван"
    assert mai.students[0].surname == "Иванов"
    assert mai.students[0].age == 20
    assert mai.students[0].address == "Москва"
    assert mai.students[0].rates == [4, 5, 4, 3]

def test_remove_student():
    mai = MAI()
    mai.add_student("Иван", "Иванов", 20, "Москва", [4, 5, 4, 3])
    mai.add_student("Петр", "Петров", 22, "Санкт-Петербург", [5, 5, 4, 5])
    mai.remove_student("Иван", "Иванов")
    assert len(mai.students) == 1
    assert mai.students[0].name == "Петр"
    assert mai.students[0].surname == "Петров"
    assert mai.students[0].age == 22
    assert mai.students[0].address == "Санкт-Петербург"
    assert mai.students[0].rates == [5, 5, 4, 5]