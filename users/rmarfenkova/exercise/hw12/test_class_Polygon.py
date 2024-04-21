import pytest
from class_Point import Point
from class_Polygon import Polygon

def test_polygon1():
    """периметр"""
    point1 = Point(0, 0)
    point2 = Point(0, 4)
    point3 = Point(6, 4)
    point4 = Point(6, 0)
    polygon = Polygon([point1, point2, point3, point4])
    assert polygon.perimeter() == 20

def test_polygon2():
    """периметр"""
    point1 = Point(1, 1)
    point2 = Point(3, 3)
    point3 = Point(5, 1)
    polygon = Polygon([point1, point2, point3])
    assert polygon.perimeter() == 9.66

def test_area1():
    """площадь"""
    point1 = Point(0, 0)
    point2 = Point(0, 4)
    point3 = Point(6, 4)
    point4 = Point(6, 0)
    polygon = Polygon([point1, point2, point3, point4])
    assert polygon.area() == 24

def test_area2():
    """площадь"""
    point1 = Point(1, 1)
    point2 = Point(3, 3)
    point3 = Point(5, 1)
    polygon = Polygon([point1, point2, point3])
    assert polygon.area() == 4.0