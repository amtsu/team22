from part2_Shape import Shape

class Triangle(Shape):
    """
    Создайте класс Triangle, который представляет треугольник. У него должны быть атрибуты длины сторон. Добавьте методы для вычисления периметра треугольника и методы вычисления типа треугольника (равносторонний, равнобедренный, прямоуголный или разносторонний).
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Perimetr(self):
        perimetr = self.a + self.b + self.c
        return perimetr

    def Square(self):
        semi_perimetr = (self.a + self.b + self.c)/2
        square = (semi_perimetr*(semi_perimetr-self.a)*(semi_perimetr-self.b)*(semi_perimetr-self.c)) ** 0.5
        return round(square, 2)

    
    def triangle_type(self):
        """
        Функция, определяющая тип треугольника по длинам его сторон
        """
        result = "не треугольник"
        l = [self.a, self.b, self.c]
        l.sort()
        a, b, c = l[0], l[1], l[2]
        
        triangle_exist = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
       
        if triangle_exist:
                    
            if (a == b) and (b == c) and (c == a):
                result = 'равносторонний'
            elif a == b or b == c or a == c:
                result = 'равнобедренный'
            elif (a**2 + b**2) == c**2:
                result = 'прямоугольный'
            else:
                result = 'разносторонний'
                        
        return result

    
        

treug1 = Triangle(3, 6, 6)
print(treug1.Perimetr())
print(treug1.triangle_type())

treug2 = Triangle(3, 4, 5)
print(treug2.Perimetr())
print(treug2.triangle_type())

treug3 = Triangle(3, 3, 3)
print(treug3.Perimetr())
print(treug3.triangle_type())
            