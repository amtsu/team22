import pytest
from point import Point


def test_point_initialization():
    point_1 = Point(2,5)
    assert point_1.x == 2
    assert point_1.y == 5


def test_calculate_distance():
    point_1 = Point(2,5)
    point_2 = Point(1,-6)
    assert point_1.calculate_distance(point_2) == 11.05           
      

def test_calculate_distance():
    point_2 = Point(0,0)
    point_3 = Point(-3,-5)
    assert point_2.calculate_distance(point_3) == 5.83           
          

