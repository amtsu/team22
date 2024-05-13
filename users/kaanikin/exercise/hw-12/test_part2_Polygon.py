import pytest
from part2_Polygon import Polygon
from part1_Point import Point
from part2_Shape import Shape



def test_perimetr1():
    kvadrat = Polygon()
    point1 = Point(0, 0)
    point2 = Point(0, 1)
    point3 = Point(1, 1)
    point4 = Point(1, 0)

    kvadrat.addVertices(point1)
    kvadrat.addVertices(point2)
    kvadrat.addVertices(point3)
    kvadrat.addVertices(point4)

    expected = 4

    assert kvadrat.Perimetr() == expected
    
    

def test_square1():
    kvadrat = Polygon()
    point1 = Point(0, 0)
    point2 = Point(0, 1)
    point3 = Point(1, 1)
    point4 = Point(1, 0)

    kvadrat.addVertices(point1)
    kvadrat.addVertices(point2)
    kvadrat.addVertices(point3)
    kvadrat.addVertices(point4)

    expected = 1

    assert kvadrat.Square() == expected

def test_square2():
    poly = Polygon()
    point1 = Point(3, 4)
    point2 = Point(5, 11)
    point3 = Point(12, 8)
    point4 = Point(9, 5)
    point5 = Point(5, 6)

    poly.addVertices(point1)
    poly.addVertices(point2)
    poly.addVertices(point3)
    poly.addVertices(point4)
    poly.addVertices(point5)

    expected = 30

    assert poly.Square() == expected
    