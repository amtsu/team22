from part2_Shape import Shape

class Rectangle(Shape):
    """
    Создайте класс Rectangle, который представляет прямоугольник. У него должны быть атрибуты длины сторон. Добавьте методы для вычисления периметра и площади.
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
        

    def Perimetr(self):
        perimetr = (self.a + self.b) * 2
        return perimetr

    def Square(self):
        square = self.a * self.b
        return round(square, 2)

    
    
            