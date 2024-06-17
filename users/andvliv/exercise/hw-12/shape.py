#Создайте класс Shape для представления различных геометрических фигур(круг, прямоугольник треугольник). Реализуйте в нем методы вчисления площали и периметра.
#Изменить ранее написнаны классы геометрических фигур так чтобы они были наслдниками класса Shape.
class Shape:
    def __init__(self, points):
        self.points = points

    def calculate_area(self): #считаем площадь многоугольника по формуле Гаусса
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

    def calculate_perimeter(self):
        sum_sides = 0
        for i in range(len(self.points) - 1):
            sum_sides += ((self.points[i][0] - self.points[i + 1][0]) ** 2 + (self.points[i][1] - self.points[i + 1][1]) ** 2) ** 0.5
        sum_sides += ((self.points[len(self.points) - 1][0] - self.points[0][0]) ** 2 + (self.points[len(self.points) - 1][1] - self.points[0][1]) ** 2) ** 0.5
        return sum_sides
        
class Circle_shape(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return (self.radius ** 2) * 3.14

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle_shape(Shape):
    pass
    
class Triangle_shape(Shape):
    pass


        