#import pytest
from Car_class import Car

def test_car_model():
    car1 = Car('mazda', 2010, 'white', 4, 100)
    assert car1.model == 'mazda'
    #assert car1.year == 2010 

#test_car_model() - вызов функции не нужен еси используем pytest

def test_car_year():
    car1 = Car('mazda', 2010, 'white', 4, 100)
    assert car1.model == 'mazda'
    #assert car1.year == 2010 
    