import pytest
from class_Car import Car 

@pytest.mark.parametrize("model, year_of_issue, color, door, speed, expected", [
    ("Toyota", 2020, "red", 4, 100, "Toyota"),
    (["BMW"], 2018, "blue", 2, 120, ["BMW"]),
    ("Ford", 2015, "black", 4, 80, "Ford")
])
def test_car_attributes(model, year_of_issue, color, door, speed, expected):
    car = Car(model, year_of_issue, color, door, speed)
    assert car.get_model() == model



@pytest.mark.parametrize("model, year_of_issue, color, door, speed, expected", [
    ("Toyota", "2020", "red", 4, 100, "2020"),
    ("BMW", (2018), "blue", 2, 120, 2018),
    ("Ford", 2015, "black", 4, 80, 2015)
])
def test_car_attributes2(model, year_of_issue, color, door, speed, expected):
    car = Car(model, year_of_issue, color, door, speed)
    assert car.get_year_of_issue() == year_of_issue


    
@pytest.mark.parametrize("model, year_of_issue, color, door, speed, expected", [
    ("Toyota", 2020, "red", 4, 100, "red"),
    ("BMW", 2018, "blue", 2, 120, "blue"),
    ("Ford", 2015, "black", 4, 80, "black")
])
def test_car_attributes3(model, year_of_issue, color, door, speed, expected):
    car = Car(model, year_of_issue, color, door, speed)   
    assert car.get_color() == color



@pytest.mark.parametrize("model, year_of_issue, color, door, speed, expected", [
    ("Toyota", 2020, "red", 4, "100", "100"),
    ("BMW", 2018, "blue", 2, 120, 120),
    ("Ford", 2015, "black", 4, 80, 80)
])
def test_car_attributes4(model, year_of_issue, color, door, speed, expected):
    car = Car(model, year_of_issue, color, door, speed)
    assert car.get_speed() == speed

def test_accelerate():
    car2 = Car("Toyota", "2020", "red", 4, 100)
    car2.accelerate()
    assert car2.get_speed() == 105
    
def test_stop():
    car2 = Car("Toyota", "2020", "red", 4, 100)
    car2.stop()
    assert car2.get_speed() == 0
    
    


