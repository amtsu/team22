'''
Создайте класс Triangle, который представляет треугольник. У него должны быть атрибуты длины сторон. Добавьте методы для вычисления перимера треугольника и методы вычисления типа треугольника ( равностороннйи, павнобедренный, прямоуголный или разносторонний).
'''
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Равносторонний"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "Равнобедренный"
        elif self.side1**2 == self.side2**2 + self.side3**2 or self.side2**2 == self.side1**2 + self.side3**2 or self.side3**2 == self.side1**2 + self.side2**2:
            return "Прямоугольный"
        else:
            return "Разносторонний"

# Пример использования класса
triangle1 = Triangle(3, 4, 5)
print("Периметр треугольника:", triangle1.perimeter())
print("Тип треугольника:", triangle1.triangle_type())

triangle2 = Triangle(5, 5, 5)
print("Периметр треугольника:", triangle2.perimeter())
print("Тип треугольника:", triangle2.triangle_type())

triangle3 = Triangle(4, 4, 6)
print("Периметр треугольника:", triangle3.perimeter())
print("Тип треугольника:", triangle3.triangle_type())