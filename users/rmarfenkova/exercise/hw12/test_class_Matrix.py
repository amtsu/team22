import pytest

from class_Matrix import Matrix 

def test_addition():
    matrix_A = Matrix([[1, 2], [3, 4]])
    matrix_B = Matrix([[5, 6], [7, 8]])
    result = matrix_A + matrix_B
    assert result.rows == [[6, 8], [10, 12]]

def test_subtraction():
    matrix_A = Matrix([[1, 2], [3, 4]])
    matrix_B = Matrix([[5, 6], [7, 8]])
    result = matrix_B - matrix_A
    assert result.rows == [[4, 4], [4, 4]]

def test_multiplication():
    matrix_A = Matrix([[1, 2], [3, 4]])
    matrix_B = Matrix([[5, 6], [7, 8]])
    result = matrix_A * matrix_B
    assert result.rows == [[19, 22], [43, 50]]

def test_transpose():
    matrix_A = Matrix([[1, 2], [3, 4], [5, 6]])
    result = matrix_A.transpose()
    assert result.rows == [[1, 3, 5], [2, 4, 6]]

def test_determinant():
    matrix_A = Matrix([[1, 2], [3, 4]])
    assert matrix_A.determinant() == -2

def test_inverse():
    matrix_A = Matrix([[1, 2], [3, 4]])
    inverse_A = matrix_A.inverse()
    product = matrix_A * inverse_A
    
    # Округляем элементы матрицы до 6 знаков после запятой
    rounded_product = [[round(element, 6) for element in row] for row in product.rows]
    
    # Ожидаем, что получится единичная матрица
    assert rounded_product == [[1.0, 0.0], [0.0, 1.0]]