import pytest
import pickle
from car_extended import Car


@pytest.fixture
def car():
    return Car("Toyota", 2024, "silver", 4, 40)


def test_load_car_1(car):        
    file_name = 'file_car.pickle'
    car.save_to_file('file_car.pickle')
    loaded_car = Car.load_from_file(file_name)    
    assert loaded_car.get_model() == "Toyota"  #Проверка,что загруж-ые данные соотв-ют ожидаемым знач
    assert loaded_car.get_year() == 2024
    assert loaded_car.get_color() == "silver"
    assert loaded_car.doors == 4
    assert loaded_car.speed == 40 


'''1.3. Создайте тест который, загружает автомобиль с файла меняет скорость автомобиля и сохраняет автомобиль с новой соростью в файл'''
 
def test_change_speed_car_1(car):
    file_name = 'file_car.pickle'
    car.speed  = 60  
    car.save_to_file(file_name)
    loaded_car = Car.load_from_file(file_name) 
    assert loaded_car.speed == 60
    