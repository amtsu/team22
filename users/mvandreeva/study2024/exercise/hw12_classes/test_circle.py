import pytest

from circle import Circle

def test_count_area():
    new_circle = Circle(4, 'red')
    assert new_circle.count_area() == 50.24

def test_count_perimeter():
    new_circle = Circle(5, 'blue')
    assert new_circle.count_perimeter() == 31.4
