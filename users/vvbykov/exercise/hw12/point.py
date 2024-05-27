
class Point:

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value
    

class Calculator:
    
    @staticmethod
    def distance_between_points(p1: Point, p2: Point):
        if (type(p1) is Point) and (type(p2) is Point):
            return round(((p1.x - p2.x)**2 + (p1.y - p2.y)**2) ** 0.5, 2)
        else:
            raise TypeError("The input parametr should be the instance of the Point class")
        
