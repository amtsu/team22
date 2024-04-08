'''5.Создайте класс Circle, который представляет круг. У него должен быть атрибут для хранения радиуса и цвета. Добавьте методы для вычисления площади и периметра круга.'''

class Circle:
    
    def __init__(self, radius, color):
        self.__radius = radius
        self.__color = color

    def circle_area(self):
        pi = 3.14
        s = pi*self.__radius**2
        return s

    
    def circle_perimeter(self):
        pi = 3.14
        p = 2 * pi * self.__radius
        return p
    



