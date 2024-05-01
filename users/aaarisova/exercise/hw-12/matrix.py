'''Создайте класс для работы с матрицами. Который будет предоставлять матрицы и поддреживать основные операции сложение, вычитание умножение транспонирование. Затем добавьте методы для вычисления определителя матрицы и вычисления обраной матрицы.'''

from numpy import np


class Matrix():

    def __init__(self, matrix):
        self.mairix = matrix       
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    #def __str__ для вывода и возможности сравнений в тестах ожидаемого резулльтята и вывода в иде строки

    def matrix_add(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return 'Матрицы должны быть одинакового размера.'
        else:
            for i in range(len(self.rows)):
                for j in range(len(self.columns[0])):
                    result_add = self.matrix[i][j] + other.matrix[i][j]
            return result_add 

    
    def subtract(self, other):  
        if self.rows != other.rows or self.colums != other.colums:
            return 'Матрицы должны быть одинакового размера.'
        else:
            for i in range(len(self.rows)):
                for j in range(len(other.columns[0])):
                    for k in range(len(self.columns[0])):
                result_sub = self.matrix[i][j] - other.matrix[i][j]
            return result_sub 
                
    def multiply(self, other):
        new_matrix = [[0 for _ in range(self.columns)] for _ in range(other.rows)]
        if self.columns != other.rows:
            return "Матрицы должны быть одинакового размера."
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return new_matrix
    
    def transpose(self):    #строки становятся столбцами и наоборот
        new_matrix = [[0 for j in range(self.columns)] for i in range(self.rows)]
        for i in range(len(self.rows)):
            for j in range(len(self.columns[0])):
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

