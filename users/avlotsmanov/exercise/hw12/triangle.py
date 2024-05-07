

#Создайте класс Triangle, который представляет треугольник.
#У него должны быть атрибуты длины сторон.
#Добавьте методы для вычисления перимера треугольника
#и методы вычисления типа треугольника ( равностороннйи, павнобедренный, прямоуголный или разносторонний).

class Triangle:
    def __init__(
            self, a, b, c
                 ):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c

    def type(self) -> str:
        """
        Функция, определяющая тип треугольника по длинам его сторон
        """
        a = self.a
        b = self.b
        c = self.c
        result = "не треугольник"
        triangle_exist = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
        if triangle_exist:
            sides = [a, b, c]
            sides.sort()
            acuteTriangle = (sides[0] ** 2 + sides[1] ** 2) > sides[2] ** 2
            obtuseTriangle = (sides[0] ** 2 + sides[1] ** 2) < sides[2] ** 2
            rightTriangle = abs((sides[0] ** 2 + sides[1] ** 2) - sides[2] ** 2) <= 0.01

            if acuteTriangle:
                result = "остроугольный"
            elif obtuseTriangle:
                result = "тупоугольный"
            elif rightTriangle:
                result = "прямоугольный"
        return result


triangle1 = Triangle(3,4,5)
print(triangle1.perimetr())
print(triangle1.type())