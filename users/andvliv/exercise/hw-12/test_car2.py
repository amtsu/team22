import pytest
from car2 import Car2

def test_car_accelerate():
    car1 = Car2(model='Toyota', year=2000, color='blue', doors=4, current_speed=0)
    expected = 5
    assert car1.car_accelerate() == 5

def test_car_stop():
    car1 = Car2(model='Toyota', year=2000, color='blue', doors=4, current_speed=5)
    expected = 0
    assert car1.car_stop() == 0