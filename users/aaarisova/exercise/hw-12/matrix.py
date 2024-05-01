'''Создайте класс для работы с матрицами. Который будет предоставлять матрицы и поддреживать основные операции сложение, вычитание умножение транспонирование. Затем добавьте методы для вычисления определителя матрицы и вычисления обраной матрицы.'''

import numpy as np


class Matrix():

    def __init__(self, matrix):
        self.matrix = matrix       
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __str__(self):
        matrix_string = ''
        for row in self.matrix:
            matrix_string += ' '.join(map(str, row)) + '\n'
        return matrix_string.strip()   

    def matrix_add(self, other):
        matrix_add = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        if self.rows != other.rows or self.columns != other.columns:
            return 'Матрицы должны быть одинакового размера.'
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    matrix_add[i][j] += self.matrix[i][j] + other.matrix[i][j]
            return matrix_add 

    
    def subtract(self, other): 
        matrix_subtract = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        if self.rows != other.rows or self.columns != other.columns:
            return 'Матрицы должны быть одинакового размера.'
        else:
            for i in range(self.rows):
                for j in range(other.columns):
                    matrix_subtract[i][j]  += self.matrix[i][j] - other.matrix[i][j]
            return matrix_subtract 
                
    def multiply(self, other):
        new_matrix = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        if self.columns != other.rows:
            return "Матрицы должны быть одинакового размера."
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return new_matrix
    
    def transpose(self):    #строки становятся столбцами и наоборот
        new_matrix = [[0 for j in range(self.rows)] for i in range(self.columns)]
        for i in range(self.rows):
            for j in range(self.columns):
                new_matrix[j][i] = self.matrix[i][j]
        return new_matrix

    def determinant(self): #разобрать
        if self.rows != self.columns:
            return "Матрица должна быть квадратной для вычисления определителя"
        return np.linalg.det(self.matrix)  # Используем библиотеку NumPy для вычисления определителя

    def inverse(self):  #разобрать
        if self.rows != self.columns:
            return "Матрица должна быть квадратной для нахождения обратной матрицы"
        try:
            inv_matrix = np.linalg.inv(self.matrix)  # Используем библиотеку NumPy для вычисления обратной матрицы
            return inv_matrix.tolist()
        except np.linalg.LinAlgError:
            return "Обратная матрица не существует"

