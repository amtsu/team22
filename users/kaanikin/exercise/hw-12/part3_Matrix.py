import numpy as np
class Matrix:

    def __init__(self,matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def __str__(self):
        matrix_string = ''
        for row in self.matrix:
            matrix_string += ' '.join(map(str, row)) + '\n'
        return matrix_string.strip()     

    def add(self, other):
        new_matrix = [[0 for _ in range(self.columns)] for _ in range(other.rows)]
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Размеры матриц не совпадают")
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    new_matrix[i][j] += self.matrix[i][j] + other.matrix[i][j]
            return new_matrix

    def subtract(self, other):
        new_matrix = [[0 for _ in range(self.columns)] for _ in range(other.rows)]
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Размеры матриц не совпадают")
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    new_matrix[i][j] += self.matrix[i][j] - other.matrix[i][j]
            return new_matrix

    def multiply(self, other):
        new_matrix = [[0 for _ in range(self.columns)] for _ in range(other.rows)]
        if self.columns != other.rows:
            raise ValueError("Размеры матриц не совпадают")
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return new_matrix


    def transpose(self):
        new_matrix = [[0 for _ in range(self.rows)] for _ in range(self.columns)]
        for i in range(self.rows):
            for j in range(self.columns):
                new_matrix[j][i] = self.matrix[i][j]
        return new_matrix

    def get_determinant(self):
        if self.columns != self.rows:
            print('Определителя для не квадратной матрицы не существует')
            return
        else:
            return round(np.linalg.det(self.matrix))
        
        """
        if self.rows != self.columns:
            raise ValueError("Матрица должна быть квадратной")
        elif self.rows == 1:
            return self.matrix[0][0]
        else:
            def determinant(matrix):
                n = len(matrix)
                if n == 1:
                    return matrix[0][0]
    
                det = 0
                for j in range(n):
                    minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
                    det += (-1) ** j * matrix[0][j] * determinant(minor)
    
                return det

            return determinant(self.matrix) """

    def inverse(self):
        determinant = self.get_determinant()
        if determinant == 0:
            raise ValueError("Матрица не имеет обратной")
        elif self.get_determinant() == 0:
            print('Определитель равен нулю, обратной матрицы не существует')
        else:
            adjoint_matrix = np.linalg.inv(self.matrix) * determinant
            inverse_matrix = [list(map(int, row)) for row in adjoint_matrix]
            return inverse_matrix
        
        """
        result = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                result[i][j] = self.matrix[j][i] / determinant
        return result
        
        
       

   
    def multiply(self, other):
        new_matrix = [[0 for _ in range(self.columns)] for _ in range(other.rows)]
        if self.columns != other.rows:
            raise ValueError("Размеры матриц не совпадают")
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(other.rows, self.columns).set_matrix(new_matrix)


    def transpose(self):
        new_matrix = [[0 for _ in range(self.rows)] for _ in range(self.columns)]
        for i in range(self.rows):
            for j in range(self.columns):
                new_matrix[j][i] = self.matrix[i][j]
        return Matrix(self.columns, self.rows).set_matrix(new_matrix)

    def get_determinant(self):
        if self.rows != self.columns:
            raise ValueError("Матрица должна быть квадратной")
        elif self.rows == 1:
            return self.matrix[0][0]
        else:
            determinant = 0
            sign = 1
            for i in range(self.rows):
                minor = self.minor_matrix(i)
                determinant += sign * self.matrix[i][0] * self.get_determinant(minor)
                sign *= -1
            return determinant

    def minor_matrix(self, row):
        result = []
        for i in range(self.rows):
            if i != row:
                result.append([self.matrix[i][j] for j in range(self.columns)])
        return Matrix(self.rows - 1, self.columns - 1).matrix

    def inverse(self):
        determinant = self.get_determinant()
        if determinant == 0:
            raise ValueError("Матрица не имеет обратной")
        else:
            inverse_matrix = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
            for i in range(self.rows):
                for j in range(self.columns):
                    inverse_matrix[i][j] = self.matrix_element_inverse(i, j, determinant)
            return Matrix(self.rows, self.columns).matrix

"""    

        

    