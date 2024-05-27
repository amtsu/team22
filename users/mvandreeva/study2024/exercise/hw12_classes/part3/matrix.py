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
        # print(result)
        return result 

    def __sub__(self, another_matrix):
        result = np.array(self.__matrix) - np.array(another_matrix)
        # print(result)
        return result 

    def __mul__(self, another_matrix):
        result = np.dot(self.__matrix, another_matrix) 
        # print(result)
        return result 

    def transponse(self):
        """Метод транспонирования матриц"""
        arr_matrix = np.array(self.__matrix)
        transp_matrix = arr_matrix.transpose()
        # print(transp_matrix)
        return transp_matrix

    def determinant(self):
        """Метод вычисления определителя матрицы"""
        result = round(np.linalg.det(self.__matrix),2)
        # print(result)
        return result

    def inverce(self):
        """Метод вычисления обраной матрицы"""
        inverse_array = np.linalg.inv(self.__matrix)
        # print(inverse_array)
        return inverse_array




        