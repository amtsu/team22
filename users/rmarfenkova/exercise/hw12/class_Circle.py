class Circle():
    """
    Создайте класс Circle, который представляет круг.
    У него должен быть атрибут для хранения радиуса и цвета.
    Добавьте методы для вычисления площади и периметра круга.
    """

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    def area(self):
        """ вычисляет площаль круга """
        area = 3.14 * self.radius ** 2
        return f" Площадь круга: {round(area, 2)}"

    def perimeter(self):
        """ вычисляет периметр круга """
        perimetr = 2 * 3.14 * self.radius
        return f"Периметр круга: {round(perimetr, 2)}"