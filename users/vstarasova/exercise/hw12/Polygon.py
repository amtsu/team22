'''
Создайте класс Polygon, который представляет многоугольник. У него должен быть атрибут для хранения списка вершин. Добавьте методы для вычисления площади и периметра многоугольника.
'''
import math

class Polygon:
    def __init__(self, vertices):
        self.vertices = vertices

    def perimeter(self):
        perimeter = 0
        for i in range(len(self.vertices)):
# Вычисляем расстояние между текущей вершиной и следующей вершиной (зацикленно)
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % len(self.vertices)]
            perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return perimeter

    def area(self):
        area = 0
        for i in range(len(self.vertices)):
# Вычисляем площадь каждого треугольника, образованного текущей вершиной и двумя соседними
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % len(self.vertices)]
            area += (x1 * y2 - x2 * y1)
        return abs(area) / 2

# Пример использования
polygon = Polygon([(0, 0), (3, 0), (3, 4), (0, 4)])
print("Периметр многоугольника:", polygon.perimeter())
print("Площадь многоугольника:", polygon.area())
