import pytest
from part1_Point import Point

tochka = Point(3, 5)

def test_point_length():
    expected = 5.0
    assert expected == tochka.Length(6, 9) 
