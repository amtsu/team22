import abc
class Shape(abc.ABC):
    pass

    """
    Создайте класс Shape для представления различных геометрических фигур(круг, прямоугольник треугольник). Реализуйте в нем методы вчисления площали и периметра.
    """
    
    @abc.abstractmethod
    def Square(self):
        pass
    
    @abc.abstractmethod
    def Perimetr(self):
        pass

