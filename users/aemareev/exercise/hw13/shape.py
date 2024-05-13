import os
from math import pi, sqrt
from file_methods import FileMethods


class Shape(FileMethods):
    def __init__(self, a=None, b=None, c=None, radius=None):
        super().__init__()
        self.c = c
        self.b = b
        self.a = a
        self.radius = radius
        if self.radius:
            self.file_name = 'shape_circle.pickle'
        elif self.a and self.b and self.c:
            self.file_name = 'shape_triangle.pickle'
        elif self.a and self.b:
            self.file_name = 'shape_rectangle.pickle'
        else:
            self.file_name = 'shape_no_name.pickle'

    def get_area(self):
        if self.radius:
            return pi * self.radius ** 2
        elif self.a and self.b and self.c:
            # Вычисляем полупериметр
            p = (self.a + self.b + self.c) / 2
            # Вычисляем площадь по формуле Герона
            area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
            return area
        elif self.a and self.b:
            return self.a * self.b
        else:
            raise ValueError

    def get_perimeter(self):
        if self.radius:
            return 2 * pi * self.radius
        elif self.a and self.b and self.c:
            return self.a + self.b + self.c
        elif self.a and self.b:
            return (self.a + self.b) * 2
        else:
            raise ValueError


if __name__ == '__main__':
    circle = Shape(radius=5)
    circle.dump_obj()
    rectangle = Shape(4, 8)
    rectangle.dump_obj()
    triangle = Shape(6, 6, 6)
    triangle.dump_obj()

    for file in os.listdir('.'):
        if file.endswith('.pickle') and file.title()[:5] == 'Shape':
            obj: Shape = Shape.load_obj(file.title())
            name = file.title()[6:-7]
            area = obj.get_area().__round__(2)
            perimeter = obj.get_perimeter().__round__(2)
            print(f'{name}: периметр {perimeter}, площадь {area}')
