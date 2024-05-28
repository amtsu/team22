'''
Создайте класс Point, который представляет точку в двумерном пространстве. У него должны быть атрибуты для хранения координат x и y. Добавьте методы для вычисления расстояния между двумя точками.
'''
import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance

# Пример использования класса
point1 = Point(3, 4)
point2 = Point(6, 8)

distance = point1.distance_to(point2)
print("Расстояние между точками:", distance)