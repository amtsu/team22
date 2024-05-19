import pytest
from hw13_part1_Student import Student
from hw13_part1_University import University
from class_PickleHandler import PickleHandler

def test_load_from_file():
    student1 = Student("Ivan", "Petrov", 33, "Smolnay_street", [])
    student2 = Student("Stas", "Ivanov", 25, "Smolnay_street", [])
    student3 = Student("Anna", "Kim", 28, "Smolnay_street", [])
    
    university = University()
    university.add_student(student1)
    university.add_student(student2)
    university.add_student(student3)
    
    #сохраняю в файл студентов в университете
    PickleHandler.save_to_file(university, "list_student.pkl")
    load_university = PickleHandler.load_from_file("list_student.pkl")
    
    #удаляю студента
    load_university.remove_student("Petrov")
    PickleHandler.save_to_file(load_university, "list_student.pkl")
    updated_university = PickleHandler.load_from_file("list_student.pkl")
    assert updated_university.count_students() == 2