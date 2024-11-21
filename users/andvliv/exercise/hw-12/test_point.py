import pytest
from point import Point

def test_point():
    point1 = Point(2, 6)
    point2 = Point(6, 9)
    assert point1.calculate_distance(point2) == 5.0