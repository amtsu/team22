#Создайте класс Point, который представляет точку в двумерном пространстве.
#У него должны быть атрибуты для хранения координат x и y.
#Добавьте методы для вычисления расстояния между двумя точками.
from math import sqrt
class Point:
    def __init__(
            self, x, y
    ):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

point1 = Point(3,4)
point2 = Point(0,0)
print(point1.distance(point2))