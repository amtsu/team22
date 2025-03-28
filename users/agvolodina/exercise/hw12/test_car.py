from func_car import Car

car1 = Car (year=2024, model='lada', color='red', door=4, speed=60)
#тест на проверку года выпуска автомобиля
def test_Getyear():
    assert car1.Getyear() == 2024
#тест на проверку марки
def test_Getmodel():
    assert car1.Getmodel() == 'lada'
def test_Getcolor():
    assert car1.Getcolor() == 'red'
#тест на проверку скорости автомобиля
def test_Getspeed():
    assert car1.Getspeed() == 60
