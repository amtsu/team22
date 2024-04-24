from shape import Shape


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    # def get_triangle_perimeter(self):
    #     return self.a + self.b + self.c

    def get_triangle_type(self):
        lst = [self.a, self.b, self.c]
        lst.sort()
        if lst[0] + lst[1] <= lst[2]:
            result = "не треугольник"
        elif self.a == self.b == self.c:
            result = "равносторонний"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            result = "равнобедренный"
        elif lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
            result = "прямоугольный"
        else:
            result = "разносторонний"
        return result


if __name__ == "__main__":
    triangle_1 = Triangle(3, 3, 9)
    triangle_2 = Triangle(4, 3, 6)
    triangle_3 = Triangle(5, 4, 3)
    triangle_4 = Triangle(3, 3, 3)
    triangle_5 = Triangle(5, 2, 5)
    print(f'{triangle_1.get_triangle_type()}, периметр: {triangle_1.get_p_triangle()}')
    print(f'{triangle_2.get_triangle_type()}, периметр: {triangle_2.get_p_triangle()}')
    print(f'{triangle_3.get_triangle_type()}, периметр: {triangle_3.get_p_triangle()}')
    print(f'{triangle_4.get_triangle_type()}, периметр: {triangle_4.get_p_triangle()}')
    print(f'{triangle_5.get_triangle_type()}, периметр: {triangle_5.get_p_triangle()}')
    assert triangle_2.get_p_triangle() == 13
    assert triangle_4.get_p_triangle() == 9
