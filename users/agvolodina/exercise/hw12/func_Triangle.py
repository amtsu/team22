#Создайте класс Triangle, который представляет треугольник. У него должны быть атрибуты длины сторон. Добавьте методы для вычисления перимера треугольника и методы вычисления типа треугольника ( равностороннйи, павнобедренный, прямоуголный или разносторонний).

class Triangle():
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    #метод вычисления периметра
    def perimeter(self,a,b,c):
        return a+b+c
    #метод вычисления типа треугольника
    def triangle_type(self, a: float, b: float, c: float) -> str:
        result = "не треугольник"
        triangle_exist = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
        if triangle_exist:
            sides = [self.a, self.b, self.c]
            sides.sort()
            acuteTriangle = (sides[0]**2 + sides[1]**2) > sides[2]**2
            obtuseTriangle = (sides[0]**2 + sides[1]**2) < sides[2]**2
            rightTriangle = abs((sides[0]**2 + sides[1]**2) - sides[2]**2) <= 0.01

            if acuteTriangle:
                result = "остроугольный"
            elif obtuseTriangle:
                result = "тупоугольный"
            elif rightTriangle:
                result  = "прямоугольный"
        return result