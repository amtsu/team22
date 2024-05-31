from func_Point import Point

def test_distance():
    point1 = Point(1, 2)
    point2 = Point(4, 6)
    assert point1.distance(point2) == 5