'''7.Создайте класс Triangle, который представляет треугольник. У него должны быть атрибуты длины сторон. Добавьте методы для вычисления перимера треугольника и методы вычисления типа треугольника ( равносторонний, равнобедренный, прямоугольный или разносторонний).'''


class Triangle:

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)


    def perimeter(self):
        p = self.a + self.b + self.c
        return p

    
    def classify_triangles(self):
        a, b, c = sorted([self.a, self.b, self.c])
        
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 'Не треугольник'
           
        elif a**2 + b**2 == c**2:
            return 'прямоугольный'
                        
        elif len(set([a, b, c])) == 1:
            return 'равносторонний'
            
        elif len(set([a, b, c])) == 2:
            return 'равнобедренный'
            
        else:    
            return 'разносторонний'
    
    



