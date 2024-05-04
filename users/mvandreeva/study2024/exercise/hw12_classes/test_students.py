import pytest

from student import Student

def test_student_attr():
    new_student = Student("Fedor", "Semenov", 18, "Moscow, lubyanka 1", {'math': 5, 'rus': 4})
    assert new_student.name == "Fedor"
    assert new_student.surname == "Semenov"
    assert new_student.age == 18
    assert new_student.address == "Moscow, lubyanka 1"
    assert new_student.record_book == {'math': 5, 'rus': 4}

def test_get_mark():
    new_student = Student("Maria", "Semenova", 20, "Moscow, Petrovka 21", {'math': 4, 'rus': 5})
    new_student.get_mark('eng', 5)
    assert new_student.record_book == {'math': 4, 'rus': 5, 'eng': 5}

def test_count_avg_score():
    new_student = Student("Maria", "Semenova", 20, "Moscow, Petrovka 21", {'math': 4, 'rus': 5})
    assert new_student.count_avg_score() == 4.5

def test_gcount_avg_score2():
    new_student = Student("Maria", "Semenova", 20, "Moscow, Petrovka 21", {'math': 5, 'rus': 5, 'eng': 5})
    assert new_student.count_avg_score() == 5