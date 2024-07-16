import pytest
import sys
sys.path.append("..") 
from point import *

def test_point():

    p1 = Point(-1, 3)
    p2 = Point(6, 2)
    
    assert Calculator.distance_between_points(p1, p2) == 7.07

    with pytest.raises(TypeError):
        Calculator.distance_between_points(1, p2)