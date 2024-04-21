"""
Создайте класс Polygon, который представляет многоугольник.
У него должен быть атрибут для хранения списка вершин.
Добавьте методы для вычисления площади и периметра многоугольника.
"""
class Polygon:
    def __init__(self, points):
        self.points = points

    def perimeter(self):
        """ вычисляет периметр многоугольника """
        perimeter = 0
        for i in range(len(self.points)):
            current_point = self.points[i]
            next_point = self.points[(i + 1) % len(self.points)]  # следующая точка, с учетом замыкающейся формы многоугольника
            perimeter += current_point.distance(next_point)
        return round(perimeter, 2)

    def area(self):
        """ вычисляет площадь многоугольника """
        area = 0
        for i in range(len(self.points)):
            current_point = self.points[i]
            next_point = self.points[(i + 1) % len(self.points)]  # следующая точка, с учетом замыкающейся формы многоугольника
            area += current_point.x * next_point.y - current_point.y * next_point.x
        return round(abs(area) * 0.5, 2)