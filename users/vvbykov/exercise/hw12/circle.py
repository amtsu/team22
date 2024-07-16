import math 
from shape import * 

class Circle:

    colours = ("red", "blue", "black", "white")
    
    def __init__(self, colour: str, radius: float):
        
        if colour in Circle.colours:
            self._colour = colour
        else:
            raise ValueError("Invalid colour value")

        self._radius = float(radius)


    @property
    def radius(self):
        return self._radius
    
    @property
    def colour(self):
        return self._colour
    
    @property
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    @property
    def area(self):
        return round(math.pi * self.radius ** 2, 2)


class Circle_v2(Shape):
    type = "Circle"
    
    def __init__(self, colour: str, radius: float):
        super().__init__(colour)            
        self._radius = float(radius)

    @property
    def radius(self):
        return self._radius    
    
    @property
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    @property
    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    
    