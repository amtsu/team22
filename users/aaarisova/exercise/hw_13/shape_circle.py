import math
class Circle(Shape):
    
    def __init__(self, radius, color):
        self.radius = float(radius)
        self.color = color

    def area(self):
        pi = 3.14
        area_result = pi*self.radius**2
        return round(area_result, 2)

    
    def perimeter(self):
        pi = 3.14
        p_result = 2 * pi * self.radius
        return round(p_result, 2)


class Circle2(Shape):
    
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.circle = Circle(radius, color = 'black')

    def area(self):
        return self.circle.area()

    def perimeter(self):
        return self.circle.perimeter()
