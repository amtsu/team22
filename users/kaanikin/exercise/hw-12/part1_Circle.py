class Circle:
    """
    Создайте класс Circle, который представляет круг. У него должен быть атрибут для хранения радиуса и цвета. Добавьте методы для вычисления площади и периметра круга.
    """
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def Square(self):
        result = 3.14 * self.radius**2
        return round(result, 2)

    def Perimetr(self):
        result = 2 * 3.14 * self.radius
        return round(result, 2)

