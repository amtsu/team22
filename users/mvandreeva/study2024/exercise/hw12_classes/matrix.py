import numpy as np

class Matrix:
    """
    Класс для работы с матрицами. 
    Имеет операции сложение, вычитание, умножение, транспонирование. 
    Имеет методы для вычисления определителя матрицы и вычисления обраной матрицы.
    """
    def __init__(self, matrix):
        self.__matrix = matrix

    def __add__(self, another_matrix):
        result = np.array(self.__matrix) + np.array(another_matrix)
        return result 

    def __sub__(self, another_matrix):
        result = np.array(self.__matrix) - np.array(another_matrix)
        return result 

    def __mul__(self, another_matrix):
        result = np.dot(self.__matrix, another_matrix) 
        return result 

    def transponse(self):
        arr_matrix = np.array(self.__matrix)
        transp_matrix = arr_matrix.transpose()
        return transp_matrix

    def determinant(self):
        resullt = numpy.linalg.det(self.__matrix)
        return result

    def inverce(self):
        inverse_array = np.linalg.inv(self.__matrix)
        return inverse_array




        