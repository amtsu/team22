import pytest
from student import Student

def test_mean_marks():
    student1 = Student('Andrey', 'Ivanchenko', 35, 'Vladimirskaya, 11-1', [4, 3, 4, 3])
    assert student1.mean_marks() == 3.5
