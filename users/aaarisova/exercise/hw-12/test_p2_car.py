import pytest
from p2_car import Car2


def test_acceleration():
    toyota = Car2('RAV4', 2020, 'orange', 5, 150)
    assert toyota.acceleration() == 155


def test_stop():
    honda = Car2('Civic', 2014, 'gold', 5, 180)
    assert honda.stop() == 0


