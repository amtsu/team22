import pytest
from triangle import Triangle


def test_triangle_init():
    triangle = Triangle(4, 3, 3)
    assert triangle.a == 4
    assert triangle.b == 3
    assert triangle.c == 3
    
    
def test_perimeter():
    triangle = Triangle(5,2,3)
    triangle.a = 5
    triangle.b = 2
    triangle.c = 3       
    assert triangle.perimeter() == 10


    
@pytest.mark.parametrize('a, b, c, expected_rezult', [
    (4, 4, 4, 'равносторонний'),
    (0, 0, 0, 'Не треугольник'),
    (9.02, 5, 5, 'равнобедренный'),
    (3, 4, 5, 'прямоугольный'),
    (2, 5, 4, 'разносторонний'),
])


def test_classify_triangles(a, b, c, expected_rezult):
    triangle = Triangle(a, b, c)
    assert triangle.classify_triangles() == expected_rezult

    





