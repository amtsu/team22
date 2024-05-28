import pytest
import sys
sys.path.append("..") 
from car import *


@pytest.fixture
def first_car():
    return Car("geely", "white", 2015, 4)


@pytest.mark.parametrize("model, colour, year, doors", 
                         [("geely", "none", 2015, 4),
                          ("geely", "blue", 1900, 4),
                          ("geely", "blue", 2015, 1),
                          ("geely", "blue", 2015, 6),
                          ("geely", "blu", 2015, 3),
                          ("geely", "blue", 2026, 3),
                          ("", "blue", 2024, 3)
                         ])
def test_car_init(model, colour, year, doors):
   with pytest.raises(ValueError):
       car = Car(model, colour, year, doors)

def test_car_stop(first_car):
    assert first_car.speed == 0

def test_car_go(first_car):
    first_car.go()
    assert first_car.speed == 40


def test_car_stop_after_go(first_car):
    first_car.go()
    first_car.stop()
    assert first_car.speed == 0


def test_car_extended():
    car = Car("Ford Ka", "blue", 1998, 3)
    assert car.speed == 0
    car.go()
    assert car.speed == 40
    car.speed_up()
    assert car.speed == 45
    car.speed_up()
    car.speed_up()
    car.speed_up()    
    assert car.speed == 60
    car.speed_down()
    assert car.speed == 55
    car.speed_down()
    car.speed_down()
    car.speed_down()    
    assert car.speed == 40
    car.stop()
    car.speed_up()
    assert car.speed == 5
    car.speed_down()
    car.speed_down()    
    assert car.speed == 0
    
    
    
    
    
     
