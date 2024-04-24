import pytest
from class_Student import Student
from class_University import University

@pytest.fixture
def students():
    university = University()
    student1 = Student("Ivan", "Ivanov", 20, "street1", [])
    student2 = Student("Maria", "Petrova", 22, "street2", [])
    student3 = Student("John", "Smith", 21, "street3", [])
    university.add_student(student1)
    university.add_student(student2)
    university.add_student(student3)
    return university

def test_add_student(students):
    assert len(students.students_list) == 3

def test_remove_student(students):
    students.remove_student("Ivanov")
    assert len(students.students_list) == 2

def test_remove_student(students):
    result = students.remove_student("Кто-то")
    assert result == "Студент Кто-то не найден"
    assert len(students.students_list) == 3

def test_display_students(students):
    expected = ["Ivan Ivanov", "Maria Petrova", "John Smith"]
    assert students.display_students() == expected