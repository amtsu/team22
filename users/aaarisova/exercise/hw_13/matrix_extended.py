'''Расширте класс для работы с матрицами, загрузкой и сохранением. Придумаейте тесты.'''

import pickle 
import numpy as np


class Matrix():

    def __init__(self, matrix):
        self.matrix = matrix       
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __str__(self):
        '''метод строкового представления объекта'''
        matrix_string = ''
        for row in self.matrix:
            matrix_string += ' '.join(map(str, row)) + '\n'
        return matrix_string.strip()   

    def __add__(self, other):  
        '''метод сложения двух матриц'''
        result_matrix = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError('Матрицы должны быть одинакового размера.')
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    result_matrix[i][j] += self.matrix[i][j] + other.matrix[i][j]
            return Matrix(result_matrix) #Создаем новый объект типа Matrix на основе полученной матрицы

    
    def __sub__(self, other): 
        '''метод вычитания матриц'''
        matrix_subtract = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError('Матрицы должны быть одинакового размера.')
        else:
            for i in range(self.rows):
                for j in range(other.columns):
                    matrix_subtract[i][j]  += self.matrix[i][j] - other.matrix[i][j]
            return Matrix(matrix_subtract) 
                
    def __mul__(self, other):
        '''метод умножения матриц'''
        new_matrix = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        if self.columns != other.rows:
            raise ValueError("Матрицы должны быть одинакового размера.")
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(new_matrix)
    
    def transpose(self):    #строки становятся столбцами и наоборот
        '''метод транспонирования матриц'''
        new_matrix = [[0 for j in range(self.rows)] for i in range(self.columns)]
        for i in range(self.rows):
            for j in range(self.columns):
                new_matrix[j][i] = self.matrix[i][j]
        return Matrix(new_matrix)

    def determinant(self):
        '''методы для вычисления определителя матрицы'''
        if self.rows != self.columns:
            raise ValueError("Матрица должна быть квадратной для вычисления определителя.")
        return np.linalg.det(self.matrix)  

    
    def inverse(self):
        '''метод вычисления обраной матрицы.'''
        if self.rows != self.columns:
            raise ValueError("Матрица должна быть квадратной для нахождения обратной матрицы.")
        try:
            inv_matrix = np.linalg.inv(self.matrix)  
            return inv_matrix.tolist()
        except np.linalg.LinAlgError:
            return "Обратная матрица не существует"

    
    def save_to_file(self,file_name):
        '''методы сохранения и загрузки обекта из памяти в файл'''
        with open(file_name, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_file(file_name):
        '''метод загрузки объекта из файла в память с помощью десериализации.'''
        with open(file_name, 'rb') as f:
            return pickle.load(f)

 

