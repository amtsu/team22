import pytest

from cars import Car

def test_get_year():
    my_car = Car("ВАЗ-2101", 1972, "red", 4, 0)
    assert my_car.get_year() == 1972

def test_get_model():
    my_car = Car("LADA", 1991, "white", 4, 0)
    assert my_car.get_model() == "LADA"

def test_get_color():
    my_car = Car("Toyota", 2020, "silver", 4, 0)
    assert my_car.get_color() == "silver"

def test_get_current_speed():
    my_car = Car("KIA", 2024, "black", 4, 10)
    assert my_car.get_current_speed() == 10