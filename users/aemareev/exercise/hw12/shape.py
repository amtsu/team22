from math import pi, sqrt


class Shape:
    def __init__(self):
        self.c = None
        self.b = None
        self.a = None
        self.radius = None

    def get_s_circle(self):
        return pi * self.radius ** 2

    def get_p_circle(self):
        return 2 * pi * self.radius

    def get_s_rectangle(self):
        return self.a * self.b

    def get_p_rectangle(self):
        return (self.a + self.b) * 2

    def get_s_triangle(self):
        # Вычисляем полупериметр
        p = (self.a + self.b + self.c) / 2
        # Вычисляем площадь по формуле Герона
        area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area

    def get_p_triangle(self):
        return self.a + self.b + self.c
