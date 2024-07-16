import pytest 
from hw13_part1_Car import Car
from class_PickleHandler import PickleHandler

def test_load_from_file():
    car = Car("Jeep", 2000, "black", 4 , 0)
    #сохраняю в файл
    PickleHandler.save_to_file(car, "car.pkl")
    #выгружаю из файла
    loaded_car = PickleHandler.load_from_file("car.pkl")
    #меняю скорость
    loaded_car.accelerate()
    #сохраняю объект с новой скоростью в файл
    PickleHandler.save_to_file(loaded_car, "car.pkl")
    update_loaded_car = PickleHandler.load_from_file("car.pkl")
    assert update_loaded_car.get_speed() == 5