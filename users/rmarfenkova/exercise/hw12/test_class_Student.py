import pytest
from class_Student import Student

@pytest.fixture
def student():
    return Student("Ivan", "Ivanov", 33, "Smolnay_street", [5, 3, 4, 4, 5])
    
def test_student_name(student):
    assert student.name == "Ivan"

def test_student_surname(student):
    assert student.surname == "Ivanov"

def test_student_age(student):
    assert student.age == 33

def test_test_student_address(student):
    assert student.address == "Smolnay_street"

def test_test_list_estimates(student):
    assert student.list_estimates == [5, 3, 4, 4, 5]
    
def test_add_estimates(student):
    student.add_estimates(2)
    assert student.list_estimates == [5, 3, 4, 4, 5, 2]

def test_gpa(student):
    assert student.gpa() == 4.2
    
def test_gpa_negative():
    student = Student("Ivan", "Ivanov", 33, "Smolnay_street", [])
    assert student.gpa() == 'Список пуст'
        