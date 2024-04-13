import pytest
from part1_Car import Car

ferrari = Car('testarossa', 1995, 'rosso corsa', 2, 330)

def test_car1():
    
    expected = 'testarossa'
    assert ferrari.getModel() == expected 

def test_car2():
    
    expected = 1995
    assert ferrari.getYear() == expected 

def test_car3():
    expected = 'rosso corsa'
    assert ferrari.getColor() == expected 

def test_car_acc():
    expected = 335
    ferrari.acc()
    assert ferrari.getSpeed() == expected 

def test_car_brake():
    expected = 0
    ferrari.brake()
    assert ferrari.getSpeed() == expected 