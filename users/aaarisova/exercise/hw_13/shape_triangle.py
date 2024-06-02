import math
from shape_extended import Shape

class Triangle(Shape):
    
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError('Стороны должны быть > 0')
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.side3 = float(side3)

    def area(self):
        '''площадь треуг по формуле Герона: S = √(sp(sp-a)(sp-b)(sp-c)), где sp — полупериметр: sp=(a+b+c)/2''' 
        sp = (self.side1 + self.side2 + self.side3) / 2      #ищем полупериметр(sp-semiperimeter)
        area = math.sqrt(sp * (sp - self.side1) * (sp - self.side2) * (sp - self.side3))
        return round(area,2)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

      