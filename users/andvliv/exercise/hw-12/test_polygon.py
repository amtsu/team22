import pytest
from polygon import Polygon

def test_polygon_area():
    polygon1 = Polygon([[1, 1], [1, 3], [3, 3], [3, 1]])
    assert polygon1.polygon_area() == 4

def test_polygon_area_2():
    polygon2 = Polygon([[1, 1], [1, 4], [4, 6], [8, 3], [4, 1]])
    assert polygon2.polygon_area() == 22

def test_poligon_perimeter():
    polygon1 = Polygon([[1, 1], [1, 3], [3, 3], [3, 1]])
    assert polygon1.polygon_perimeter() == 8
                     
def test_poligon_perimeter_2():
    polygon2 = Polygon([[1, 1], [1, 5], [3, 5], [3, 1]])
    assert polygon2.polygon_perimeter() == 12