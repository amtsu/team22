import pytest
from part2_College import College
from part1_Student import Student

MAI = College()

Petya = Student('Petr', 'Petrov', 57, 'Petrovka 38', [5, 2, 5, 2, 3])
Vasya = Student('Vasiliy', 'Petrov', 37, 'Petrovka 20', [2, 2, 5, 2, 2])
Olya = Student('Olga', 'Petrova', 27, 'Petrovka 11', [5, 5, 5, 5, 5])


def test_get_list():
    MAI.add(Petya)
    MAI.add(Vasya)
    MAI.add(Olya)
    expected = ['Petr Petrov', 'Vasiliy Petrov', 'Olga Petrova']
    assert expected == MAI.get_list()
    

def test_remove_student():
    MAI.remove(Vasya)
    expected = ['Petr Petrov', 'Olga Petrova']
    assert expected == MAI.get_list()



