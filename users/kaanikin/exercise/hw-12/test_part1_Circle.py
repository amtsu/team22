import pytest
from part1_Circle import Circle

krug = Circle(5,'синий')

def test_circle_color():
    expected = 'синий'
    assert expected == krug.color

def test_circle_radius():
    expected = 5
    assert expected == krug.radius

def test_circle_perimetr():
    expected = 31.4
    assert expected == krug.Perimetr()

def test_circle_square():
    expected = 78.5
    assert expected == krug.Square()
