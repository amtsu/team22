from shape import Shape

class Circle (Shape):
    """
    Класс, который представляет круг. 
    Имеет атрибуты для хранения радиуса и цвета. 
    Имеет методы для вычисления площади и периметра круга.
    """

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color
        self._figure = "circle"

    # def count_area(self):
    #     return round(3.14 * (self.__radius ** 2),2)

    # def count_perimeter(self):
    #     return round(2 * 3.14 * self.__radius,2)