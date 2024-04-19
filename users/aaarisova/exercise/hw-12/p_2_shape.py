#Создайте класс Shape для представления различных геометрических фигур(круг, прямоугольник треугольник). Реализуйте в нем методы вчисления площали и периметра.

from circle import Circle
import math 

class Shape():

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle2(Shape):
    
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.circle = Circle(radius, color = 'black')

    def area(self):
        return self.circle.area()

    def perimeter(self):
        return self.circle.perimeter()


class Rectangle(Shape):

    def __init__(self, width, height):
       #? super().__init__()  # Вызываем конструктор базового класса Shape
        if width <= 0 or height <= 0:
            raise ValueError('Ширина и высота должны быть > 0')
            #return None, 'Ширина и высота должны быть > 0')
        self.width = float(width)
        self.height = float(height)
  
    def area(self):
        return self.width * self.height  
        
    
    def perimeter(self):
        return 2 * (self.width + self.height) 


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

      
    
        