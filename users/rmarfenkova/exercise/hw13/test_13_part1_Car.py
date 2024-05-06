import pytest 

from hw13_part1_Car import Car

def test_car():
    car = Car("Jeep", 2000, "black", 4 , 0)
    # Сохраняем объект автомобиля в файл
    car.save_to_file("car_data.pkl")
    # Загружаем объект автомобиля из файла
    loaded_car = Car.load_from_file("car_data.pkl")
    # Проверяем, что объект успешно загружен
    assert isinstance(loaded_car, Car)
    # изменяем скорость автомобиля
    loaded_car.accelerate()
    loaded_car.save_to_file("updated_car_data.pkl")
    #Загружаем объект автомобиля из файла после изменения
    updated_loaded_car = Car.load_from_file("updated_car_data.pkl")
    # Проверяем, что скорость была изменена
    assert updated_loaded_car.get_speed() == 5
