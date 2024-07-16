import pytest
from Point import Point

     
def test_distance_to():
    point1 = Point(3, 4)
    point2 = Point(6, 8)
    assert point1.distance_to(point2) == 5.0
