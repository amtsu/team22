import pytest
import numpy as np
from matrix import Matrix

@pytest.fixture
def matrix1():
    return Matrix([[1,2],[3,4],[5,6]])   

@pytest.fixture
def matrix2():
    return Matrix([[2,1],[2,1],[2,1]])

def test_matrix_add(matrix1, matrix2):
    assert matrix1.matrix_add(matrix2) == ([[3, 3], [5, 5], [7, 7]])

def test_subtract(matrix1, matrix2):
    assert matrix1.subtract(matrix2) == ([[-1, 1], [1, 3], [3, 5]])

def test_multiply():
    matrix1 = Matrix([[1, 2], [0, 1]])
    matrix2 = Matrix([[2, 0], [1, 3]])
    assert matrix1.multiply(matrix2) == ([[4, 6], [1, 3]])

def test_transpose(matrix1):
    assert matrix1.transpose() == ([[1, 3, 5],[2, 4, 6]]) 

def test_determinant():
    matrix = Matrix([[1, 2], [3, 4]])
    assert round(matrix.determinant(),2) == -2    #1 * 4 - 2 * 3 = 4 - 6 = -2

def test_inverse():
    matrix = Matrix([[1, 2], [3, 4]])
    matrix_inv = matrix.inverse() 
    rounded_matrix_inv = [[round(elem, 2) for elem in row] for row in matrix_inv] 
    assert rounded_matrix_inv == [[-2.0, 1.0], [1.5, -0.5]]




