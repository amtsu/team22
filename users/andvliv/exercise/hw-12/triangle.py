#Создайте класс Triangle, который представляет треугольник. У него должны быть атрибуты длины сторон. Добавьте методы для вычисления перимера треугольника и методы вычисления типа треугольника ( равностороннйи, павнобедренный, прямоуголный или разносторонний).

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def calculate_perimeter(self):
        if (self.a + self.b) > self.c and (self.a + self.c) > self.b and (self.b + self.c) > self.a:
            return self.a + self.b + self.c
        else:
            return 'not triangle'
        
    def triangle_type(self):
        sides = [self.a, self.b, self.c]
        sides = sorted(sides)
        if (sides[0] == sides[1]) and (sides[1] == sides[2]) and (sides[0] == sides[2]) and ((sides[0] + sides[1] > sides[2])):
            return 'equilateral'
        elif (sides[0] == sides[1] or sides[0] == sides[2] or sides[2] == sides[1]) and ((sides[0] + sides[1] > sides[2])):
            return 'equicrural'
        elif ((sides[0] ** 2 + sides[1] ** 2) == sides[2] ** 2) and ((sides[0] + sides[1] > sides[2])):
            return 'right'
        elif (sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[2] != sides[1]) and ((sides[0] + sides[1] > sides[2])):
            return 'scalene'
        else:
            return 'not triangle'

#Сооздадим несколько объектов данного класса
triangle1 = Triangle(3, 3, 3)
triangle2 = Triangle(3, 3, 4)
triangle3 = Triangle(4, 5, 3)
triangle4 = Triangle(6, 7, 8)