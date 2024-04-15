import pytest
from class_Triangle import Triangle

@pytest.mark.parametrize("a, b, c, expected_perimeter", [
    (3, 4, 5, 12),  # Прямоугольный треугольник
    (2, 2, 2, 6),   # Равносторонний треугольник
    (3, 3, 4, 10),  # Равнобедренный треугольник
    (3, 4, 6, 13),  # Разносторонний треугольник
    (1, 2, 3, 6) # Невозможный треугольник
])
def test_perimeter(a, b, c, expected_perimeter):
    triangle = Triangle(a, b, c)
    assert triangle.perimeter() == expected_perimeter

@pytest.mark.parametrize("a, b, c, expected_type", [
    (3, 4, 5, "прямоугольный"),  # Прямоугольный треугольник
    (2, 2, 2, "равносторонний"),  # Равносторонний треугольник
    (3, 3, 4, "равнобедренный"),  # Равнобедренный треугольник
    (3, 4, 6, "разносторонний"),  # Разносторонний треугольник
    (1, 2, 3, "не треугольник")   # Невозможный треугольник
])
def test_type(a, b, c, expected_type):
    triangle = Triangle(a, b, c)
    assert triangle.type() == expected_type