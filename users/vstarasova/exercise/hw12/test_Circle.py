import pytest
from Circle import Circle

def test_square():
    circle1 = Circle(2, "blue")
    assert circle1.square() == 12.56

    print("Тест для метода square пройден успешно!")

def test_perimeter():
    circle1 = Circle(2, "blue")
    assert circle1.perimeter() == 12.56

    print("Тест для метода perimeter пройден успешно!")
    
