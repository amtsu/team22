import pytest
import math
import sys
sys.path.append("..") 
from rectangle import *

def test_rectangle():
    
    r1 = Rectangle("blue", 3, 9)
    
    assert r1.colour == "blue"
    assert r1.a == 3
    assert r1.b == 9
    assert r1.perimeter == 2*(3 + 9)
    assert r1.area == 27    



