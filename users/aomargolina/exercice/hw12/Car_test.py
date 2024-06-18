def test_car():
    car1 = Car('mazda', 2010, 'white', 4, 100)
    assert car1.model == 'mazda'
    assert car1.year == 2010

test_car()
    