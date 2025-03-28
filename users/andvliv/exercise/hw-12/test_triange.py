import pytest
from triangle import Triangle

def test_triangle_perimeter():
    triangle1 = Triangle(3, 3, 3)
    triangle2 = Triangle(2, 2, 6)
    assert triangle1.calculate_perimeter() == 9
    assert triangle2.calculate_perimeter() == 'not triangle'

def test_triangle_type():
    triangle1 = Triangle(3, 3, 3)
    triangle2 = Triangle(3, 3, 4)
    triangle3 = Triangle(4, 5, 3)
    triangle4 = Triangle(6, 7, 8)
    triangle5 = Triangle(2, 2, 6)
    assert triangle1.triangle_type() == 'equilateral'
    assert triangle2.triangle_type() == 'equicrural'
    assert triangle3.triangle_type() == 'right'
    assert triangle4.triangle_type() == 'scalene'
    assert triangle5.triangle_type() == 'not triangle'