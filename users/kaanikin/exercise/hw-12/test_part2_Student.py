import pytest
from part1_Student import Student

Pooh = Student('Winnie', 'Pooh', 3, 'Pooh tree', [4, 2, 4, 2, 3])

def test_student_marks():
    expected = [4, 2, 4, 2, 3]
    assert expected == Pooh.marks_list

def test_student_address():
    expected = 'Pooh tree'
    assert expected == Pooh.address

def test_student_age():
    expected = 3
    assert expected == Pooh.age

def test_student_averageMark():
    expected = 3
    assert expected == Pooh.averageMark()

def test_student_addMark():
    expected = [4, 2, 4, 2, 3, 5]
    Pooh.addMark(5)
    assert expected == Pooh.marks_list
    
