class Point:
    """
    Класс Point, представляет точку в двумерном пространстве,
    имеет атрибуты для хранения координат x и y
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def count_two_dots_distance(self, x2, y2):
        """
        Метод для вычисления расстояний между точками
        """
        distance = round((((self.x - x2)**2 + (self.y - y2)**2 )**0.5),2)
        return distance