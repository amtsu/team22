'''6. Создайте класс Point, который представляет точку в двумерном пространстве. У него должны быть атрибуты для хранения координат x и y. Добавьте методы для вычисления расстояния между двумя точками.'''

from math import sqrt

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, new_point):
        distance = sqrt((self.x - new_point.x)**2 + (self.y - new_point.y)**2)            
        return round(distance, 2)




