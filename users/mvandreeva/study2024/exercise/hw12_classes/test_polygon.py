from polygon import Polygon

def test_count_area():
    p = Polygon([{'x': 0, 'y': 0}, {'x': 0, 'y': 3}, {'x': 3, 'y': 3}, {'x': 3, 'y': 0}])
    assert p.count_area() == 9

def test_count_area2():
    p = Polygon([{'x': 0, 'y': 0}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 1, 'y': 0}])
    assert p.count_area() == 1

def test_count_perimiter():
    p = Polygon([{'x': 0, 'y': 0}, {'x': 0, 'y': 3}, {'x': 3, 'y': 3}, {'x': 3, 'y': 0}])
    assert p.count_perimiter() == 12