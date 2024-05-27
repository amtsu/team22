from Polygon import Polygon

def test_polygon_perimeter():
    polygon = Polygon([(0, 0), (3, 0), (3, 4), (0, 4)])
    assert round(polygon.perimeter(), 2) == 14.0

def test_polygon_area():
    polygon = Polygon([(0, 0), (3, 0), (3, 4), (0, 4)])
    assert polygon.area() == 12.0

if __name__ == "__main__":
    test_polygon_perimeter()
    test_polygon_area()
