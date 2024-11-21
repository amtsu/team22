import pytest
from matrix import Matrix

def test_trans_matrix():
    matrix1 = Matrix([[2, 1], [1, 3], [4, 3]])
    assert matrix1.trans_matrix() == [[2, 1, 4], [1, 3, 3]]

def test_plus_matrix():
    matrix1 = Matrix([[2, 1], [1, 3], [4, 3]])
    matrix2 = Matrix([[1, 1], [2, 2], [3, 3]])
    assert matrix1.plus_matrix(matrix2) == [[3, 2], [3, 5], [7, 6]]

def test_minus_matrix():
    matrix1 = Matrix([[2, 1], [1, 3], [4, 3]])
    matrix2 = Matrix([[1, 1], [2, 2], [3, 3]])
    assert matrix1.minus_matrix(matrix2) == [[1, 0], [-1, 1], [1, 0]]