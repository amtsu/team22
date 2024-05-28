import numpy as np

class Matrix:
    def __init__(self, rows):
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0]) if rows else 0

    def __add__(self, other):
        """сложение матриц"""
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Матрицы должны быть одного размера")
        result = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(self.rows[i][j] + other.rows[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        """вычитание матриц"""
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Матрицы должны быть одного размера")
        result = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(self.rows[i][j] - other.rows[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):   # Cji = Aik * Bkj
        """произведение матриц"""
        if self.num_cols != other.num_rows:
            raise ValueError("Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице.")
        result = []
        for i in range(self.num_rows):
            row = []
            for j in range(other.num_cols):
                element = 0
                for k in range(self.num_cols):
                    element += self.rows[i][k] * other.rows[k][j]
                row.append(element)
            result.append(row)
        return Matrix(result)

    def transpose(self):
        """транспонирование матрицы: - первая строка матрицы А становится первым столбцом матрицы В"""
        transposed = [[self.rows[j][i] for j in range(self.num_rows)] for i in range(self.num_cols)]
        return Matrix(transposed)

    def determinant(self):
        """определитель матрицы, способ рекурсивного поиска"""
        if self.num_rows != self.num_cols:
            raise ValueError("Определитель можно вычислить только для квадратных матриц.")
        if self.num_rows == 1:
            return self.rows[0][0]
        if self.num_rows == 2:
            return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]
        det = 0
        for j in range(self.num_cols):
            minor = [row[:j] + row[j + 1:] for row in self.rows[1:]]
            det += ((-1) ** j) * self.rows[0][j] * Matrix(minor).determinant()
        return det

    def inverse(self):
        """Вычисление обратной матрицы с помощью NumPy"""
        if self.num_rows != self.num_cols:
            raise ValueError("Можно вычислить только для квадратных матриц")

        # Преобразуем список списков в массив NumPy
        matrix_np = np.array(self.rows)

        # Проверяем, является ли матрица сингулярной
        if np.linalg.det(matrix_np) == 0:
            raise ValueError("Матрица сингулярна, ее нельзя вычислить обратно")

        # Вычисляем обратную матрицу с помощью NumPy
        inverse_matrix_np = np.linalg.inv(matrix_np)

        # Преобразуем обратную матрицу из массива NumPy обратно в список списков
        inverse_matrix = inverse_matrix_np.tolist()
        return Matrix(inverse_matrix)
            