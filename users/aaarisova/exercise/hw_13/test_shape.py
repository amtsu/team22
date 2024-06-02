'''Напишите тест который проходится по несколькьким фалйам, загружает из них фигуры и выводит их периметр и площадь'''

import pytest
import pickle
from shape_circle import Circle
from shape_rectangle import Rectangle
from shape_triangle import Triangle


def test_shapes():
    triangle = Triangle(6, 6, 6)
    rectangle = Rectangle(4, 6)
    circle = Circle(3, 'red')
    triangle.save_to_file('triangle.pkl')
    rectangle.save_to_file('rectangle.pkl')
    circle.save_to_file('circle.pkl')
    triangle.load_from_file('triangle.pkl')
    rectangle.load_from_file('rectangle.pkl')
    circle.load_from_file('circle.pkl')
    assert (triangle.side1, triangle.side2, triangle.side3) == (6, 6, 6)
    assert (rectangle.width, rectangle.height) == (4, 6)
    assert (circle.radius, circle.color) == (3, 'red')

    assert (triangle.area(), triangle.perimeter()) == (15.59, 18)
    assert (rectangle.area(), rectangle.perimeter()) == (24, 20)
    assert (circle.area(), circle.perimeter()) == (28.27, 18.85)


