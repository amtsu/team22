'''5.Создайте класс Circle, который представляет круг. У него должен быть атрибут для хранения радиуса и цвета. Добавьте методы для вычисления площади и периметра круга.'''

class Circle:
    
    def __init__(self, radius, color):
        self.radius = float(radius)
        self.color = color

    def area(self):
        pi = 3.14
        area_result = pi*self.radius**2
        return round(area_result, 2)

    
    def perimeter(self):
        pi = 3.14
        p_result = 2 * pi * self.radius
        return round(p_result,2)
    



