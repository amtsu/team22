# from math import pi
from shape import Shape


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__()
        self.radius = radius
        self.color = color

    # def get_square(self):
    #     return pi * self.radius ** 2
    #
    # def get_perimeter(self):
    #     return 2 * pi * self.radius


if __name__ == "__main__":
    circle = Circle(3, 'red')
    assert circle.radius == 3
    assert circle.color == 'red'
    # assert circle.get_perimeter().__round__(2) == 18.85
    # assert circle.get_square().__round__(2) == 28.27
    assert circle.get_p_circle().__round__(2) == 18.85
    assert circle.get_s_circle().__round__(2) == 28.27
