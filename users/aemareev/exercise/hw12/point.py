from math import sqrt, pow


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, point):
        if not isinstance(point, Point):
            raise TypeError(f'{point} не является объектом класса Point.')
        dif_x = point.x - self.x
        dif_y = point.y - self.y
        return sqrt(pow(dif_x, 2) + pow(dif_y, 2))


if __name__ == "__main__":
    point_1 = Point(3, 3)
    point_2 = Point(5, 5)
    assert point_1.get_distance(point_2).__round__(2) == 2.83
