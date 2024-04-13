class Point:
    """
    Создайте класс Point, который представляет точку в двумерном пространстве. У него должны быть атрибуты для хранения координат x и y. Добавьте методы для вычисления расстояния между двумя точками.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Length(self, other_point):
        length = ((other_point.x-self.x)**2 + (other_point.y - self.y)**2)**0.5
        return length

