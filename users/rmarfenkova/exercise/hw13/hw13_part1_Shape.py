import pickle
from class_PickleHandler import PickleHandler

class Shape():
    def __init__(self, shape_type: str):
        self.shape_type = shape_type
        
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius: int):
        super().__init__("круг")   # позволяет инициализировать объекты во всех уровнях наследования.
        self.radius = radius

    def area(self):
        """ метод вычисления площади круга"""
        return 3.14 * self.radius ** 2

    def perimeter(self):
        """ метод вычисления периметра круга """
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        super().__init__("прямоугольник")
        self.width = width
        self.height = height

    def area(self):
        """ метод вычисления площади прямоугольника"""
        return self.width * self.height

    def perimeter(self):
        """метод вычисления периметра прямоугольника"""
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side1: int, side2: int, side3: int):
        super().__init__("треугольник")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """ метод вычисления площади треугольника"""
        s = (self.side1 + self.side2 + self.side3) / 2
        return ((s * (s - self.side1) * (s - self.side2) * (s - self.side3))) ** 0.5

    def perimeter(self):
        """метод вычисления периметра прямоугольника"""
        return self.side1 + self.side2 + self.side3


if __name__ == "__main__":
    circle = Circle(5)
    PickleHandler.save_to_file(circle, "circle.pkl")
    
    rectangle =  Rectangle(4, 2)
    PickleHandler.save_to_file(rectangle, "rectangle.pkl")
    
    triangle = Triangle(3, 4, 5)
    PickleHandler.save_to_file(triangle, "triangle.pkl")
    
    files = ["circle.pkl", "rectangle.pkl", "triangle.pkl"]
    for file in files:
        shapes = PickleHandler.load_from_file(file)
        print(f"\nТип фигуры: {shapes.shape_type}")
        print(f"Площадь: {shapes.area()}")
        print(f"Периметр: {shapes.perimeter()}")

