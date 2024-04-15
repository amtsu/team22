#тесты на новые методы - 1)ускорениe на 5 км/час, 2)остановки автомобиля. Остальные проверены в "test_car.py"

import pytest
from p2_car import Car


def test_acceleration():
    toyota = Car('RAV4', 2020, 'orange', 5, 150)
    assert toyota.acceleration() == 155


def test_stop():
    honda = Car('Civic', 2014, 'gold', 5, 180)
    assert honda.stop() == 0
    

