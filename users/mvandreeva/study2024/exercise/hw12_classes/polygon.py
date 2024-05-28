class Polygon:
    """
    класс представляет многоугольник. 
    Имеет атрибут для хранения списка вершин. 
    Имеет методы для вычисления площади и периметра многоугольника.
    """
    def __init__(self, vertex_list):
       self.__vertex_list = vertex_list

    def count_area(self):
        """"
        Метод вычисления площади многоугольника
        area = abs((x1*y2 + x2*y3 + ... + xn*y1) - (y1*x2 + y2*x3 + ... + yn*x1)) / 2
        """
        minuend = 0
        subtrahend = 0
        for i in range(0, len(self.__vertex_list) - 1):
            minuend += self.__vertex_list[i]['x'] * self.__vertex_list[i + 1]['y']
            print(minuend)
            subtrahend += self.__vertex_list[i]['y'] * self.__vertex_list[i + 1]['x']
            print(subtrahend)
        minuend += self.__vertex_list[len(self.__vertex_list) - 1]['x'] * self.__vertex_list[0]['y']
        subtrahend += self.__vertex_list[len(self.__vertex_list) - 1]['y'] * self.__vertex_list[0]['x']
        area = abs(minuend - subtrahend) / 2
        return area

    def count_perimiter(self):
        """
        Метод вычисления периметра многоугольника
        """
        perimeter = 0
        for i in range(1, len(self.__vertex_list)):
            side = (((self.__vertex_list[i]['x'] - self.__vertex_list[i -1]['x'])**2) + ((self.__vertex_list[i]['y'] - self.__vertex_list[i - 1]['y'])**2)) ** 0.5
            print(i)
            perimeter += side
        perimeter += (((self.__vertex_list[0]['x'] - self.__vertex_list[len(self.__vertex_list) - 1]['x'])**2) + ((self.__vertex_list[0]['y'] - self.__vertex_list[len(self.__vertex_list) - 1]['y'])**2)) ** 0.5
        return perimeter
    
        