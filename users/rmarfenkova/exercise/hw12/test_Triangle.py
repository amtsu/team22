import pytest
from class_Triangle import Triangle

@pytest.mark.parametrize("a, b, c, expected_perimeter", [
    (3, 4, 5, 12),  
    (2, 2, 2, 6),   
    (3, 3, 4, 10), 
    (3, 4, 6, 13),  
    (1, 2, 3, 6) 
])
def test_perimeter(a, b, c, expected_perimeter):
    triangle = Triangle(a, b, c)
    assert triangle.perimeter() == expected_perimeter

@pytest.mark.parametrize("a, b, c, expected_type", [
    (3, 4, 5, "прямоугольный"),  
    (2, 2, 2, "равносторонний"),  
    (3, 3, 4, "равнобедренный"),  
    (3, 4, 6, "разносторонний"),  
    (1, 2, 3, "не треугольник")   
])
def test_type(a, b, c, expected_type):
    triangle = Triangle(a, b, c)
    assert triangle.type() == expected_type