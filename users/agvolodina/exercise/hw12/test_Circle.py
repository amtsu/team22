from func_Circle import Circle
Circle1 =  Circle()
#тест для проверки вычисления площади круга
def test_square ():
    assert Circle1.square(5) == 78.5
#тест для проверки вычисления периметра круга
def test_perimeter():
    assert Circle1.perimeter(5) == 31
    