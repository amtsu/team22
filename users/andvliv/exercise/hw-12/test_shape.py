import pytest
from shape import Shape, Circle_shape, Rectangle_shape, Triangle_shape

def test_circle_area():
    circle1 = Circle_shape(3)
    assert circle1.calculate_area() == 28.26

def test_circle_perimeter():
    circle1 = Circle_shape(3)
    assert circle1.calculate_perimeter() == 18.84

def test_rectangle_area():
    rectangle1 = Rectangle_shape([[1, 1], [1, 4], [3, 4], [3, 1]])
    assert rectangle1.calculate_area() == 6

def test_rectangle_perimeter():
    rectangle1 = Rectangle_shape([[1, 1], [1, 4], [3, 4], [3, 1]])
    assert rectangle1.calculate_perimeter() == 10

def test_rectangle_area():
    rectangle1 = Rectangle_shape([[1, 1], [1, 4], [3, 1]])
    assert rectangle1.calculate_area() == 3

def test_rectangle_perimeter():
    rectangle1 = Rectangle_shape([[1, 1], [1, 4], [3, 1]])
    assert rectangle1.calculate_perimeter() == 8.60555127546399
    
