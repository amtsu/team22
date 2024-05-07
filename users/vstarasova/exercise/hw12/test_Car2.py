import pytest
from Car2 import Car2

def test_increase_speed():
    car2 = Car2("Toyota Camry", 2022, "black", 4, 180)
    expected = 185
    assert car2.increase_speed() == expected

    print("Тесты для метода increase_speed пройдены успешно!")

def test_stop():
    car2 = Car2("Toyota Camry", 2022, "black", 4, 180)
    expected = 0
    assert car2.stop() == expected

    print("Тесты для метода stop пройдены успешно!")