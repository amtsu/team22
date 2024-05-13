import pytest
from part1_Triangle import Triangle

treug1 = Triangle(3, 6, 6)

def test_treug1_perim():
    expected = 15
    assert treug1.Perimetr() == expected

def test_treug1_type():
    expected = 'равнобедренный'
    assert treug1.triangle_type() == expected


treug2 = Triangle(3, 4, 5)

def test_treug2_perim():
    expected = 12
    assert treug2.Perimetr() == expected

def test_treug2_type():
    expected = 'прямоугольный'
    assert treug2.triangle_type() == expected


treug3 = Triangle(3, 3, 3)

def test_treug3_perim():
    expected = 9
    assert treug3.Perimetr() == expected

def test_treug3_type():
    expected = 'равносторонний'
    assert treug3.triangle_type() == expected
