import pytest
from part1_Car import Car

mercedes = Car('s600', 1995, 'black', 4, 250)

def test_car1():
    
    expected = 's600'
    assert mercedes.getModel() == expected 

def test_car2():
    
    expected = 1995
    assert mercedes.getYear() == expected 

def test_car3():
    expected = 'black'
    assert mercedes.getColor() == 'black'