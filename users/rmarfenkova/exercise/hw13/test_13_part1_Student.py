import pytest
from hw13_part1_Student import Student
from class_PickleHandler import PickleHandler

def test_load_from_file():
    student = Student("Ivan", "Ivanov", 33, "Smolnay_street", [5, 5, 5, 5, 5])
    assert student.gpa() == 5
    #сохраняю в файл
    PickleHandler.save_to_file(student, "Ivanov.pkl")
    #выгружаю из файла
    loaded_student = PickleHandler.load_from_file("Ivanov.pkl")
    #добавляю оценку
    loaded_student.add_estimates(2)
    PickleHandler.save_to_file(loaded_student, "Ivanov.pkl")
    update_loaded_student = PickleHandler.load_from_file("Ivanov.pkl")
    assert update_loaded_student.gpa() == 4.5