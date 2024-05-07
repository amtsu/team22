import pytest
from Car import Car

def test_get_year():
    car1 = Car("Toyota Camry", 2022, "black", 4, 180)
    expected = 2022
    assert car1.get_year() == expected

    print("Тесты для метода get_year пройдены успешно!")

def test_get_model():
    car1 = Car("Toyota Camry", 2022, "black", 4, 180)
    expected = "Toyota Camry"
    assert car1.get_model() == expected
    print("Тесты для метода get_model пройдены успешно!")
    
def test_get_color():
    car1 = Car("Toyota Camry", 2022, "black", 4, 180)
    expected = "black"
    assert car1.get_color() == expected
    print("Тесты для метода get_color пройдены успешно!")

def test_get_speed():
    car1 = Car("Toyota Camry", 2022, "black", 4, 180)
    expected = 180
    assert car1.get_speed() == expected
    print("Тесты для метода get_speed пройдены успешно!")

# Пример вызова тестов
test_get_year()
test_get_model()
test_get_color()
test_get_speed()