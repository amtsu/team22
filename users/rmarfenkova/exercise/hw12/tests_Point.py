import pytest
from class_Point import Point

@pytest.mark.parametrize("x1, y1, x2, y2, expected_distance", [
    (0, 0, 3, 4, 5.0),  
    (1, 1, 4, 5, 5.0),  
    (-1, -1, 2, 3, 5.0)  
])
def test_distance_between_points(x1, y1, x2, y2, expected_distance):
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    assert point1.distance(point2) == expected_distance

