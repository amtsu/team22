from point import Point


class Polygon:
    def __init__(self, list_of_vertices: list[Point] | tuple[Point]):
        self.list_of_vertices = list_of_vertices

    def get_p_polygon(self):
        p = 0
        for i in range(len(self.list_of_vertices)):
            p += self.list_of_vertices[i].get_distance(self.list_of_vertices[i - 1])
        return round(p, 2)

    def get_s_polygon(self):
        s = 0
        n = len(self.list_of_vertices)
        for i in range(n):
            xi, yi = self.list_of_vertices[i].x, self.list_of_vertices[i].y
            xj, yj = self.list_of_vertices[(i + 1) % n].x, self.list_of_vertices[(i + 1) % n].y
            s += xi * yj - xj * yi
        return round(0.5 * abs(s), 2)


if __name__ == "__main__":
    point_1 = Point(0, 0)
    point_2 = Point(3, 0)
    point_3 = Point(3, 4)
    point_4 = Point(1, 2)
    polygon = Polygon([point_1, point_2, point_3, point_4])
    assert polygon.get_p_polygon() == 12.06
    assert polygon.get_s_polygon() == 7.0
