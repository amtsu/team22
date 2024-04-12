import pytest
from class_Student import Student

@pytest.mark.parametrize("name, surname, age, address, estimates, expected", [
    ("Ivan", "Ivanov", 33, "Voskova_street", [5, 5, 5, 4, 5], 'Ivan'),
    (("Jony"), "Depp", 40, "Smolnay_street", [5, 3, 5, 5, 5], 'Jony')
])

def test_student_info(name, surname, age, address, estimates, expected):
    """
    получаем имя студента
    """
    student_info = Student(name, surname, age, address, estimates)
    assert student_info.name == expected

@pytest.mark.parametrize("name, surname, age, address, estimates, expected", [
    ("Ivan", "Ivanov", 33, "Smolnay_street", [5, 5, 5, 3, 5], "Ivanov"),
    ("Ivan", ["Petrov"], 33, "Smolnay_street", [5, 4, 5, 5, 5], ["Petrov"])
])

def test_student_info2(name, surname, age, address, estimates, expected):
    """
    получаем фамилию студента
    """
    student_info = Student(name, surname, age, address, estimates)
    assert student_info.surname == expected

@pytest.mark.parametrize("name, surname, age, address, estimates, expected", [
    ("Ivan", "Ivanov", 33, "Smolnay_street", [5, 5, 5, 3, 5], 33),
    ("Ivan", ["Petrov"], 25, "Smolnay_street", [5, 4, 5, 5, 5], 25)
])

def test_student_info3(name, surname, age, address, estimates, expected):
    """
    получаем возраст студента
    """
    student_info = Student(name, surname, age, address, estimates)
    assert student_info.age == expected

@pytest.mark.parametrize("name, surname, age, address, estimates, expected", [
    ("Ivan", "Ivanov", 33, "Косой преулок", [5, 5, 5, 3, 5], 'Косой преулок'),
    ("Ivan", ["Petrov"], 25, "Улица разбитых фонарей", [5, 4, 5, 5, 5], 'Улица разбитых фонарей')
])

def test_student_info3(name, surname, age, address, estimates, expected):
    """
    получаем адрес студента
    """
    student_info = Student(name, surname, age, address, estimates)
    assert student_info.address == expected

@pytest.mark.parametrize("name, surname, age, address, estimates, expected", [
    ("Ivan", "Ivanov", 33, "Косой преулок", [5, 5, 5, 3, 5], [5, 5, 5, 3, 5]),
    ("Ivan", ["Petrov"], 25, "Улица разбитых фонарей", (5, 4, 5, 5, 5), (5, 4, 5, 5, 5))
])

def test_student_info4(name, surname, age, address, estimates, expected):
    """
    получаем адрес студента
    """
    student_info = Student(name, surname, age, address, estimates)
    assert student_info.estimates == expected

