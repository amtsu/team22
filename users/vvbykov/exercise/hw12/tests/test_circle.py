import pytest
import math
import sys
sys.path.append("..") 
from circle import *

def test_circle():
    
    c1 = Circle("blue", 34)
    
    assert c1.colour == "blue"
    assert c1.radius == 34
    assert c1.perimeter == round(2*math.pi*34, 2)
    assert c1.area == round(math.pi*34**2, 2)    

    with pytest.raises(ValueError):
        c2 = Circle("", 99)


def test_circle_v2():

    c2 = Circle_v2("blue", 34)
    
    assert c2.type == "Circle"
    assert c2.colour == "blue"
    assert c2.radius == 34
    assert c2.perimeter == round(2*math.pi*34, 2)
    assert c2.area == round(math.pi*34**2, 2)    

    with pytest.raises(ValueError):
        c3 = Circle_v2("", 99)
