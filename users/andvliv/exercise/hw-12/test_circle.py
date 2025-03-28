import pytest
from circle import Circle

def test_circle_area():
    circle1 = Circle(3, 'white')
    assert circle1.calculate_area() == 28.26


def test_circle_perimeter():
    circle1 = Circle(3, 'white')
    assert circle1.calculate_perimeter() == 18.84