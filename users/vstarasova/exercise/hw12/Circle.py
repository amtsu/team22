
'''
Создайте класс Circle, который представляет круг. У него должен быть атрибут для хранения радиуса и цвета. Добавьте методы для вычисления площади и периметра круга.
'''

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def square(self):
        square = 3.14*(self.radius)**2
        return square
    
    def perimeter(self):
        perimeter = 3.14*self.radius*2
        return perimeter

# Пример использования класса
circle1 = Circle(5, "blue")

# Вычисляем площадь и периметр круга
print("Площадь круга:", circle1.square())
print("Периметр круга:", circle1.perimeter())

# Изменяем радиус круга
circle1.radius = 7

# Повторно вычисляем площадь и периметр круга
print("Площадь круга (после изменения радиуса):", circle1.square())
print("Периметр круга (после изменения радиуса):", circle1.perimeter())