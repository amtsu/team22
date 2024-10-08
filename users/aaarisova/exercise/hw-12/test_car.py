import pytest
from car import Car

@pytest.mark.parametrize('model, year, color, doors, speed, expected_result', [
    ('Toyota_RAV4', '2020', 'black', '4', '150',('Toyota_RAV4', '2020', 'black', '4', '150')),
    ('Honda_Civic', 2014, 'white', 5, 180, ('Honda_Civic', 2014, 'white', 5, 180)),  
])

def test_init_car(model, year, color, doors, speed, expected_result):
    car = Car(model, year, color, doors, speed)
    assert (car.model, car.year, car.color, car.doors, car.speed) == expected_result, 'Ошибка'


def test_init_car_negative():
    with pytest.raises(NameError): 
         car_neg = Car(Lada, '1999', 'red', '4', '90')


BMW = Car('X6', '2023', 'gold', '5', '225')

def test_get_model():
    expected = 'X6'
    assert BMW.model == expected


def test_get_year():
    expected = '2023'
    assert BMW.year == expected
    

def test_get_color():
    expected = 'gold'
    assert BMW.color == expected
 

def test_get_speed():
    expected = '225'
    assert BMW.speed == expected
 
    
def test_acceleration():
    'тест ускорение +5 км/ч'
    toyota = Car('RAV4', 2020, 'orange', 5, 150)
    assert toyota.acceleration() == 155


def test_stop():
    'тест остановка а/м'
    honda = Car('Civic', 2014, 'gold', 5, 180)
    assert honda.stop() == 0


