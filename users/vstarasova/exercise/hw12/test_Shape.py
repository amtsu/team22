import math
from Shape import Shape

def test_circle_area():
    circle = Shape("circle", 5)
    assert round(circle.area(), 2) == round(25 * math.pi, 2)

def test_circle_perimeter():
    circle = Shape("circle", 5)
    assert round(circle.perimeter(), 2) == round(10 * math.pi, 2)

def test_rectangle_area():
    rectangle = Shape("rectangle", 3, 4)
    assert rectangle.area() == 12

def test_rectangle_perimeter():
    rectangle = Shape("rectangle", 3, 4)
    assert rectangle.perimeter() == 14

def test_triangle_area():
    triangle = Shape("triangle", 3, 4, 5)
    assert triangle.area() == 6

def test_triangle_perimeter():
    triangle = Shape("triangle", 3, 4, 5)
    assert triangle.perimeter() == 12

if __name__ == "__main__":
    test_circle_area()
    test_circle_perimeter()
    test_rectangle_area()
    test_rectangle_perimeter()
    test_triangle_area()
    test_triangle_perimeter()
    print("All tests passed!")