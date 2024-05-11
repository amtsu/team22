import pytest
from Triangle import Triangle

def test_perimeter():
    triangle1 = Triangle(3, 4, 5)
    assert triangle1.perimeter() == 12

def test_triangle_type1():
    triangle1 = Triangle(3, 4, 5) 
    assert triangle1.triangle_type() == "Прямоугольный"

def test_triangle_type2():
    triangle2 = Triangle(5, 5, 5) 
    assert triangle2.triangle_type() == "Равносторонний"
    
def test_triangle_type3():
    triangle3 = Triangle(5, 5, 6)     
    assert triangle3.triangle_type() == "Равнобедренный"
    
def test_triangle_type4():
    triangle4 = Triangle(7, 8, 10)     
    assert triangle4.triangle_type() == 'Разносторонний'