import pytest
from shape import Shape, Rectangle, Circle2, Triangle
from circle import Circle



def test_circle_area_1():
    circle =  Circle2(5)
    assert circle.area() == 78.5 #?????? у меня округление до 2х цифр после запятой, но он ожидает 1 - ????


def test_circle_area_2():
    with pytest.raises(ValueError):
        circle =  Circle2(-5)
        circle.area() 


def test_circle_perimeter():
    circle =  Circle2(5)
    assert circle.perimeter() == 31.4 #??????? у меня округление до 2х цифр после запятой, но он ожидает 1 - ????


####################################################

def test_rectangle_init_1():
    rectangle = Rectangle(2,5)
    assert rectangle.width == 2.0
    assert rectangle.height == 5.0


def test_rectangle_init_2():
    with pytest.raises(ValueError):
        rectangle = Rectangle(-2,5)


def test_rectangle_area():
    rectangle = Rectangle(3,5)
    assert rectangle.area() == 15


def test_rectangle_perimeter():
    rectangle = Rectangle(3,5)
    assert rectangle.perimeter() == 16


def test_rectangle_init_1():
    rectangle = Rectangle(2,5)
    assert rectangle.width == 2.0
    assert rectangle.height == 5.0


def test_rectangle_init_2():
    with pytest.raises(ValueError):
        rectangle = Rectangle(-2,5)


def test_rectangle_area():
    rectangle = Rectangle(3,5)
    assert rectangle.area() == 15


def test_rectangle_perimeter():
    rectangle = Rectangle(3,5)
    assert rectangle.perimeter() == 16


####################################################

def test_triangle_init_1():
    triangle = Triangle(7,7,7)
    assert triangle.side1 == 7.0
    assert triangle.side2 == 7.0
    assert triangle.side3 == 7.0


def test_triangle_init_2():
    with pytest.raises(ValueError):
        rectangle = Triangle(-7,-7,-7)


def test_triangle_area():
    triangle = Triangle(7,7,7)
    assert triangle.area() == 21.22


def test_triangle_perimeter():
    triangle = Triangle(7,7,7)
    assert triangle.perimeter() == 21.0







    
