#Создайте класс Circle, который представляет круг. У него должен быть атрибут для хранения радиуса и цвета. Добавьте методы для вычисления площади и периметра круга.
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)
        
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

#Создадим объект класса Circle
circle1 = Circle(3, 'white')
circle2 = Circle(5, 'black')