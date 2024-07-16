from shape import *

class Triangle:

    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    @property
    def perimeter(self):
        return self._a + self._b + self._c

    @property
    def triangle_type(self) -> str:
        a = self._a
        b = self._b
        c = self._c
        result = "не треугольник"        
        triangle_exist = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
        
        if triangle_exist:
            sides = [a, b, c]
            sides.sort()
            acuteTriangle = (sides[0]**2 + sides[1]**2) > sides[2]**2
            obtuseTriangle = (sides[0]**2 + sides[1]**2) < sides[2]**2
            rightTriangle = abs(sides[2] - (sides[0]**2 + sides[1]**2)**0.5) <= 0.1
    
            if rightTriangle:
                result  = "прямоугольный"
            elif acuteTriangle:
                result = "остроугольный"
            elif obtuseTriangle:
                result = "тупоугольный"
        return result


class Triangle_v2(Shape):

    type = "Triangle"
    
    def __init__(self, colour: str, a: float, b: float, c: float):
        
        super().__init__(colour)            
        
        self._a = float(a)
        self._b = float(b)
        self._c = float(c)

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b
        
    @property
    def c(self):
        return self._c
    
    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property 
    def area(self):
        p = self.perimeter/2
        return round((p*(p - self.a)*(p - self.b)*(p - self.c))**0.5, 2)


    