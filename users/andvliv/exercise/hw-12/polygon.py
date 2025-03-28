#Создайте класс Polygon, который представляет многоугольник. У него должен быть атрибут для хранения списка вершин. Добавьте методы для вычисления площади и периметра многоугольника.
import math
class Polygon:
    def __init__(self, points):
        self.points = points

    def polygon_area(self): #считаем площадь многоугольника по формуле Гаусса
        sum1 = 0
        sum2 = 0
        result = 0
        for i in range(len(self.points) - 1):
            sum1 += self.points[i][0] * self.points[i + 1][1]
        sum1 += self.points[len(self.points) - 1][0] * self.points[0][1]
        for i in range(len(self.points) - 1):
            sum2 += self.points[i][1] * self.points[i + 1][0]
        sum2 += self.points[len(self.points) - 1][1] * self.points[0][0]
        result = abs(sum1 - sum2) / 2
        return result

    def polygon_perimeter(self):
        sum_sides = 0
        for i in range(len(self.points) - 1):
            sum_sides += ((self.points[i][0] - self.points[i + 1][0]) ** 2 + (self.points[i][1] - self.points[i + 1][1]) ** 2) ** 0.5
        sum_sides += ((self.points[len(self.points) - 1][0] - self.points[0][0]) ** 2 + (self.points[len(self.points) - 1][1] - self.points[0][1]) ** 2) ** 0.5
        return sum_sides