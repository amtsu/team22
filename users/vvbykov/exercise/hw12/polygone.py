from shape import *
from point import *

class Polygone(Shape):
    
    type = "Polygone"

    def __init__(self, colour: str, points: list[Point]):
        super().__init__(colour)
        if len(points) > 2:
            self._points = points
        else:
            raise ValueError("Points should be more than 2")        

    @property
    def perimeter(self):
        p = Calculator.distance_between_points(self._points[-1], self._points[0])
        for i in range(len(self._points) - 1):
            p += Calculator.distance_between_points(self._points[i], self._points[i + 1])
        return p

    @property
    def area(self):
        p1 = self._points[-1].x*self._points[0].y
        p2 = self._points[-1].y*self._points[0].x
        for i in range(len(self._points) - 1):
            p1 += self._points[i].x*self._points[i + 1].y
            p2 += self._points[i].y*self._points[i + 1].x
        return abs(p2 - p1)/2 


                
        