import pytest
from class_Circle import Circle

@pytest.mark.parametrize("radius, color, expected_area", [
    (1, "red", 3.14),  
    (2, "blue", 12.56),  
    (3, "green", 28.26), 
])
def test_circle_area(radius, color, expected_area):
    """
    тест на метод нахождения площади круга
    """
    circle = Circle(radius, color)
    assert circle.area() == f" Площадь круга: {expected_area}"

@pytest.mark.parametrize("radius, color, expected_perimeter", [
    (1, "red", 6.28),  
    (2, "blue", 12.56),  
    (3, "green", 18.84),  
])
def test_circle_perimeter(radius, color, expected_perimeter):
    """
    тест на метод нахождения периметра круга
    """
    circle = Circle(radius, color)
    assert circle.perimeter() == f"Периметр круга: {expected_perimeter}"
