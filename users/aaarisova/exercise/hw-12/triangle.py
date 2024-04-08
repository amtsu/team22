'''7.Создайте класс Triangle, который представляет треугольник. У него должны быть атрибуты длины сторон. Добавьте методы для вычисления перимера треугольника и методы вычисления типа треугольника ( равносторонний, равнобедренный, прямоугольный или разносторонний).'''


class Triangle:

    def __init__(self, l, a, b, c):
        self.__length = l
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)


    def triangle_perimeter(self):
        p = self.a + self.b + self.c
        return p

    def triangle_angle(self):
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            return 'Не треугольник'
        elif a**2 == b**2 + c**2:
            return 'прямоугольный'
        elif a == b or a == c or b == c:
            return 'равнобедренный'
        elif a == b == c:
            return 'равносторонний'
        else:
            return 'разносторонний'
    
    



