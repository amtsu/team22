#Создайте класс Point, который представляет точку в двумерном пространстве. У него должны быть атрибуты для хранения координат x и y. Добавьте методы для вычисления расстояния между двумя точками.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def calculate_distance(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

#создадим объекты данного класса
point1 = Point(2, 6)
point2 = Point(6, 9)