import pytest
from car import Car

def test_car_model():
    car1 = Car(model='Toyota', year=2000, color='blue', doors=4, current_speed=0)
    assert car1.get_model() == 'Toyota'

def test_car_year():
    car1 = Car(model='Toyota', year=2000, color='blue', doors=4, current_speed=0)
    assert car1.get_year() == 2000

def test_car_color():
    car1 = Car(model='Toyota', year=2000, color='blue', doors=4, current_speed=0)
    assert car1.get_color() == 'blue'

def test_car_doors():
    car1 = Car(model='Toyota', year=2000, color='blue', doors=4, current_speed=0)
    assert car1.get_doors() == 4

def test_car_speed():
    car1 = Car(model='Toyota', year=2000, color='blue', doors=4, current_speed=0)
    assert car1.get_current_speed() == 0