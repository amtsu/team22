class Triangle():
    """
    Создайте класс Triangle, который представляет треугольник.
    У него должны быть атрибуты длины сторон.
    Добавьте методы для вычисления перимера треугольника и методы вычисления типа треугольника ( равностороннйи, павнобедренный, прямоуголный или разносторонний).
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        """ метод получения периметра треугольника """
        perimeter = (self.a + self.b + self.c)
        return perimeter
        


    def type(self):
        """ метод для определения типа треугольника """
        sides = sorted([self.a, self.b, self.c])
        a, b, c = sides
    
        if a + b <= c or a + c <= b or b + c <= a:
            return "не треугольник"
        elif a == b == c:
            return "равносторонний"
        elif a == b or a == c or b == c:
            return "равнобедренный"
        elif a ** 2 + b ** 2 == c ** 2:
            return "прямоугольный"
        else:
            return "разносторонний"
    
    