from part1_Point import Point
from part2_Shape import Shape

class Polygon(Shape):
    """Создайте класс Polygon, который представляет многоугольник. У него должен быть атрибут для хранения списка вершин. Добавьте методы для вычисления площади и периметра многоугольника."""
    def __init__(self):
        self.vertices_list = []

    def addVertices(self, vert):
        self.vertices_list.append(vert) 

    
        


    def Perimetr(self):
        perimetr = 0
        for i in range(len(self.vertices_list)):
            perimetr += self.vertices_list[i].Length(self.vertices_list[i-1])
                
        return perimetr

    
    def Square(self):
        square = 0
        for i in range(len(self.vertices_list)):
            x1 = self.vertices_list[i].getX()
            y1 = self.vertices_list[i].getY()
            x2 = self.vertices_list[i-1].getX()
            y2 = self.vertices_list[i-1].getY() 
            square += (x1 * y2) - (y1 * x2)
            print(square)
        return 0.5*abs(square)
    
    
    
   