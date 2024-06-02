import pytest
import sys
sys.path.append("..") 
from mydate import *

def test_mydate():

    d1 = MyDate(2024, 5, 4)
    d2 = MyDate(2024, 5, 4)
    d3 = MyDate(2024, 5, 1)
    
    assert d1.year == 2024
    assert d1.month == 5
    assert d1.day == 4

    assert d1 == d2
    assert d1 != d3

    assert d1 - d3 == 3
    
