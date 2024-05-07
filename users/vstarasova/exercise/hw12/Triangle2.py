'''
Изменить ранее написнаны классы геометрических фигур так чтобы они были наслдниками класса Shape.
'''

from Shape import Shape

class Triangle2(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

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
triangle1 = Triangle2(3, 4, 5)
print("Периметр треугольника:", triangle1.perimeter())
print("Тип треугольника:", triangle1.triangle_type())

triangle2 = Triangle2(5, 5, 5)
print("Периметр треугольника:", triangle2.perimeter())
print("Тип треугольника:", triangle2.triangle_type())

triangle3 = Triangle2(4, 4, 6)
print("Периметр треугольника:", triangle3.perimeter())
print("Тип треугольника:", triangle3.triangle_type())