from shape import *

class Rectangle(Shape):

    type = "Rectangle"

    def __init__(self, colour: str, a: float, b: float):
        
        super().__init__(colour)            
        
        self._a = float(a)
        self._b = float(b)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b
            
    @property
    def perimeter(self):
        return 2*(self.a + self.b)

    @property 
    def area(self):
        return round(self.a*self.b, 2)
