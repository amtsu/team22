#Создайте класс Circle, который представляет круг.
#У него должен быть атрибут для хранения радиуса и цвета.
#Добавьте методы для вычисления площади и периметра круга.
from math import pi

class Circle:
    def __init__(
            self, radius, color
    ):
        self.radius = radius
        self.color = color

    def area(self):
        return pi * self.radius**2

    def perimeter(self):
        return 2 * pi * self.radius

c1 = Circle(3, 'red')
print(c1.area())
print(c1.perimeter())