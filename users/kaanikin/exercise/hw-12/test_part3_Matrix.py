import numpy as np
from part3_Matrix import Matrix


def test_matrix_addition():
    matrix_1 = Matrix([[3, 3], [3, 3], [3, 3]])
    matrix_2 = Matrix([[3, 3], [3, 3], [3, 3]])    
    assert matrix_1.add(matrix_2) == [[6, 6], [6, 6], [6, 6]]

def test_matrix_deduction():
    matrix_1 = Matrix([[3, 3], [3, 3], [3, 3]])
    matrix_2 = Matrix([[3, 3], [3, 3], [3, 3]]) 
    assert matrix_1.subtract(matrix_2) == [[0, 0], [0, 0], [0, 0]]

def test_matrix_multiply1():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    expected = [[19, 22], [43, 50]]
    assert matrix1.multiply(matrix2) == expected   

def test_matrix_multiply2():
    matrix1 = Matrix([[1, 2], [3, 4]])
    vector = Matrix([[5], [6]])
    expected = [[17, 0], [39, 0]]
    assert matrix1.multiply(vector) == expected   

def test_matrix_trans1():
    matrix_1 =  Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert matrix_1.transpose() == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

def test_matrix_trans2():
    vector = Matrix([[1], [2], [3]])
    assert vector.transpose() == [[1, 2, 3]]

def test_matrix_det():
    matrix_3 = Matrix([[11, -3], [-15, -2]])
    assert matrix_3.get_determinant() == -67

def test_matrix_inverse():
    matrix_3 = Matrix([[11, -3], [-15, -2]])
    expected = [[-2, 3], [15, 11]]
    result = matrix_3.inverse()
    assert  result == expected

