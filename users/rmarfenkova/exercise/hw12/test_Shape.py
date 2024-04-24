import pytest
from Shape import Circle, Rectangle, Triangle

def test_area_circle():
    c = Circle(5)
    assert c.area() == 78.5
    
def test_circle_perimeter():
    c = Circle(5)
    assert c.perimeter() == 31.400000000000002
    
def test_rectangle_area():
    r = Rectangle(5, 7)
    assert r.area() == 35
    
def test_rectangle_perimeter():
    r = Rectangle(5, 7)
    assert r.perimeter() == 24
    
def test_triangle_area():
    t = Triangle(5, 5, 5)
    assert t.area() == 10.825317547305483
        
def test_triangle_perimeter():
    t = Triangle(5, 5, 5)
    assert t.perimeter() == 15
