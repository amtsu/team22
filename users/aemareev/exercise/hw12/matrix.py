import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        n = len(self.matrix)
        m = len(self.matrix[0])
        if len(other.matrix) != n or len(other.matrix[0]) != m:
            raise ValueError('Складывать можно только матрицы одного размера!')
        return [[self.matrix[i][j] + other.matrix[i][j] for j in range(m)] for i in range(n)]

    def __sub__(self, other):
        n = len(self.matrix)
        m = len(self.matrix[0])
        if len(other.matrix) != n or len(other.matrix[0]) != m:
            raise ValueError('Вычитать можно только матрицы одного размера!')
        return [[self.matrix[i][j] - other.matrix[i][j] for j in range(m)] for i in range(n)]

    def __mul__(self, other):
        n = len(self.matrix)
        m = len(self.matrix[0])
        if len(other.matrix) != n or len(other.matrix[0]) != m:
            raise ValueError('Умножать можно только матрицы одного размера!')
        return [[self.matrix[i][j] * other.matrix[i][j] for j in range(m)] for i in range(n)]

    def get_trans_matrix(self):
        return Matrix([list(item) for item in zip(*self.matrix)])

    def calc_determinant(self):
        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError('Определитель можно вычислить только для квадратной матрицы!')

        def determinant(matrix):
            n = len(matrix)
            if n == 1:
                return matrix[0][0]

            det = 0
            for j in range(n):
                minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
                det += (-1) ** j * matrix[0][j] * determinant(minor)

            return det

        return determinant(self.matrix)

    def inverse_matrix(self):
        det = self.calc_determinant()
        if det == 0:
            raise ValueError('Определитель равен нулю, матрица сингулярна и не обратима!')

        adjoint_matrix = np.linalg.inv(self.matrix) * det
        inverse_matrix = [list(map(int, row)) for row in adjoint_matrix]
        return inverse_matrix


if __name__ == "__main__":
    matrix_1 = Matrix([[3, 3], [3, 3], [3, 3]])
    matrix_2 = Matrix([[3, 3], [3, 3], [3, 3]])
    matrix_3 = Matrix([[11, -3], [-15, -2]])
    assert matrix_1 + matrix_2 == [[6, 6], [6, 6], [6, 6]]
    assert matrix_1 - matrix_2 == [[0, 0], [0, 0], [0, 0]]
    assert matrix_1 * matrix_2 == [[9, 9], [9, 9], [9, 9]]
    assert matrix_1.get_trans_matrix().matrix == [[3, 3, 3], [3, 3, 3]]
    assert matrix_3.calc_determinant() == -67
    assert matrix_3.inverse_matrix() == [[-2, 3], [15, 11]]
