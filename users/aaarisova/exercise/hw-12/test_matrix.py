import pytest
import numpy as np
from matrix import Matrix


def test_matrix_add():
    matrix1 = Matrix([[1,2],[3,4],[5,6]]) 
    matrix2 = Matrix([[2,1],[2,1],[2,1]])   
    result = matrix1 + matrix2
    assert result.matrix == [[3, 3], [5, 5], [7, 7]]

def test_subtract():
    matrix1 = Matrix([[1,2],[3,4],[5,6]]) 
    matrix2 = Matrix([[2,1],[2,1],[2,1]])   
    result = matrix1 - matrix2
    assert result.matrix == [[-1, 1], [1, 3], [3, 5]]

def test_multiply():
    matrix1 = Matrix([[1, 2], [0, 1]])
    matrix2 = Matrix([[2, 0], [1, 3]])
    result = matrix1 * matrix2
    assert result.matrix == [[4, 6], [1, 3]]

def test_transpose():
    matrix1 = Matrix([[1,2],[3,4],[5,6]]) 
    result = matrix1.transpose()
    assert result.matrix == [[1, 3, 5],[2, 4, 6]]

def test_determinant():
    matrix = Matrix([[1, 2], [3, 4]])
    assert round(matrix.determinant(),2) == -2    #1 * 4 - 2 * 3 = 4 - 6 = -2

def test_inverse():
    matrix = Matrix([[1, 2], [3, 4]])
    matrix_inv = matrix.inverse() 
    rounded_matrix_inv = [[round(elem, 2) for elem in row] for row in matrix_inv] 
    assert rounded_matrix_inv == [[-2.0, 1.0], [1.5, -0.5]]




