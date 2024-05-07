
'''
Изменить ранее написнаны классы геометрических фигур так чтобы они были наслдниками класса Shape.
'''
from Shape import Shape

class Circle2(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
