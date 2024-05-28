import pytest
import sys
sys.path.append("..") 
from triangle import *

def test_triangle():

    t1 = Triangle(3, 4, 5)

    assert t1.perimeter == 3 + 4 + 5
    assert t1.triangle_type == "прямоугольный"


def test_triangle_v2():

    t2 = Triangle_v2("red", 3, 4, 5)

    assert t2.type == "Triangle" 
    
    assert t2.colour == "red"
    assert t2.a == 3
    assert t2.b == 4
    assert t2.c == 5
    
    assert t2.perimeter == 12
    assert t2.area == 6

