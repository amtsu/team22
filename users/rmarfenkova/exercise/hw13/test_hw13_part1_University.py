import pytest
from hw13_part1_University import Student, University

def test_load_from_file():
    student1 = Student("Ivan", "Petrov", 33, "Smolnay_street", [])
    student2 = Student("Stas", "Ivanov", 25, "Smolnay_street", [])
    student3 = Student("Anna", "Kim", 28, "Smolnay_street", [])
    university = University()
    university.add_student(student1)
    university.add_student(student2)
    university.add_student(student3)
    university.save_to_file("list_student.pkl")
    load_university = university.load_from_file("list_student.pkl")
    assert isinstance(load_university, University)
    #удаляю студента
    load_university.remove_student("Petrov")
    load_university.save_to_file("update_student.pkl")
    updated_university = university.load_from_file("update_student.pkl")
    assert updated_university.count_students() == 2