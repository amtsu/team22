import pytest
from triangle import Triangle

def test_triangle_perimeter():
    triangle1 = Triangle(3, 3, 3)
    assert triangle1.calculate_perimeter() == 9

def test_triangle_perimeter_2():
    triangle2 = Triangle(2, 2, 6)
    assert triangle2.calculate_perimeter() == 'not triangle'

def test_triangle_type():
    triangle1 = Triangle(3, 3, 3)  
    assert triangle1.triangle_type() == 'equilateral'  

def test_triangle_type_2():
    triangle2 = Triangle(3, 3, 4)
    assert triangle2.triangle_type() == 'equicrural'
    
def test_triangle_type_3():
    triangle3 = Triangle(4, 5, 3)
    assert triangle3.triangle_type() == 'right'

def test_triangle_type_4():
    triangle4 = Triangle(6, 7, 8)
    assert triangle4.triangle_type() == 'scalene'

def test_triangle_type_5():
    triangle5 = Triangle(2, 2, 6)
    assert triangle5.triangle_type() == 'not triangle'