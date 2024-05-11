import math

class Shape:
    def __init__(self, shape_type, *args):
        self.shape_type = shape_type
        self.args = args

    def area(self):
        if self.shape_type == "circle":
            return self.args[0] ** 2 * math.pi
        elif self.shape_type == "rectangle":
            return self.args[0] * self.args[1]
        elif self.shape_type == "triangle":
            # Используем формулу Герона для вычисления площади треугольника
            s = sum(self.args) / 2
            return math.sqrt(s * (s - self.args[0]) * (s - self.args[1]) * (s - self.args[2]))
        else:
            return "Unknown shape"

    def perimeter(self):
        if self.shape_type == "circle":
            return 2 * self.args[0] * math.pi
        elif self.shape_type == "rectangle":
            return 2 * (self.args[0] + self.args[1])
        elif self.shape_type == "triangle":
            return sum(self.args)
        else:
            return "Unknown shape"

# Пример использования
circle = Shape("circle", 5)
print("Площадь круга:", circle.area())
print("Периметр круга:", circle.perimeter())

rectangle = Shape("rectangle", 3, 4)
print("Площадь прямоугольника:", rectangle.area())
print("Периметр прямоугольника:", rectangle.perimeter())

triangle = Shape("triangle", 3, 4, 5)
print("Площадь треугольника:", triangle.area())
print("Периметр треугольника:", triangle.perimeter())
