from abc import ABC, abstractmethod

"""Создайте класс Shape для представления различных геометрических фигур(круг, прямоугольник треугольник). Реализуйте в нем методы вчисления площали и периметра."""

class Shape(ABC):
    
# Абстрактные методы - это методы, которые объявлены, но не реализованы в абстрактном базовом классе. 
# Они должны быть реализованы в подклассах.
# Классы-потомки Circle, Rectangle и Triangle должны реализовать эти абстрактные методы,
# иначе возникнет ошибка при попытке создания экземпляров этих классов.
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

"""Изменить ранее написнаны классы геометрических фигур так чтобы они были наслдниками класса Shape."""


class Circle(Shape):
    
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        """ метод вычисления площади круга"""
        return 3.14 * self.radius ** 2

    def perimeter(self):
        """ метод вычисления периметра круга """
        return 2 * 3.14 * self.radius

class Rectangle(Shape):

    def __init__(self, width: int, height: int):
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
        
    