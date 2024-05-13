#Создайте класс Polygon, который представляет многоугольник. У него должен быть атрибут для хранения списка вершин. Добавьте методы для вычисления площади и периметра многоугольника.

import math 

class Polygon():

    def __init__(self):
        self.vertices = []

    
    def add_vertex(self, x, y):
        self.vertices.append((x, y))
        return self.vertices


    def perimeter(self):
        perimeter = 0
        n = len(self.vertices) #количество вершин многоугольника
        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]
            '''оператор % используется для замыкания многоугольника при переборе его вершин.
            ператор % возвращает остаток от деления (i + 1) на количество вершин многоугольника n. 
            Таким образом, если (i + 1) превышает n - 1 (последний индекс), 
            остаток от деления позволит вернуться к первой вершине многоугольника.
            Это обеспечивает циклический перебор вершин многоугольника, 
            начиная с первой вершины после последней.'''
            perimeter += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) 
        return perimeter

    def polygon_area(self):
        area = 0
        n = len(self.vertices)
        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]
            area += x1 * y2 - x2 * y1
            result = 0.5 * abs(area)
        return result

