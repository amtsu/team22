import pytest

from hw13_part1_Student import Student

def test_update_loaded_student():
    student = Student("Ivan", "Ivanov", 33, "Smolnay_street", [5, 5, 5, 5, 5])
    student.save_to_file("Ivanov.pkl")
    loaded_student = Student.load_from_file("Ivanov.pkl")
    assert isinstance(loaded_student, Student)
    student.add_estimates(2)
    student.save_to_file("Ivanov.pkl")
    update_loaded_student = Student.load_from_file("Ivanov.pkl")
    assert update_loaded_student.gpa() == 4.5