import math
from shape_extended import Shape

class Circle(Shape):
    
    def __init__(self, radius, color):
        
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = float(radius)
        self.color = color

    def area(self):
        area_result = math.pi*self.radius**2
        return round(area_result, 2)

    
    def perimeter(self):
        p_result = 2 * math.pi * self.radius
        return round(p_result, 2)
