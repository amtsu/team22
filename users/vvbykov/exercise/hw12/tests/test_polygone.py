import pytest
import sys
sys.path.append("..") 
from polygone import *

def test_polygone():

    p1 = Point(1, 3)
    p2 = Point(4, 3)
    p3 = Point(4, 7)
    
    p4 = Point(5, 7)
    p5 = Point(9, 7)
    p6 = Point(10, 2)
    p7 = Point(2, 2)
    
    poly1 = Polygone("red", [p1, p2, p3])
    assert poly1.perimeter == 12
    assert poly1.area == 6

    poly2 = Polygone("red", [p4, p5, p6, p7])
    assert poly2.perimeter == 22.93
    assert poly2.area == 30

