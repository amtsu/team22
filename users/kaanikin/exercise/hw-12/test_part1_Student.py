import pytest
from part1_Student import Student

Petya = Student('Petr', 'Petrov', 77, 'Petrovka 38', [5, 2, 5, 2, 3])

def test_petya_marks():
    expected = [5, 2, 5, 2, 3]
    assert expected == Petya.marks_list

def test_petya_address():
    expected = 'Petrovka 38'
    assert expected == Petya.address

def test_petya_age():
    expected = 77
    assert expected == Petya.age
