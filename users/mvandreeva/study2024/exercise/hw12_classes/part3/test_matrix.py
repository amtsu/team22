import pytest
import numpy as np
from matrix import Matrix

def test_add():
    matrix1 = Matrix([[1,2,],[5,6,],[9,10,]])
    matrix2 = [[2,1,],[1,2,],[2,1,]]
    assert (matrix1 + matrix2 == [[ 3,  3], [ 6,  8], [11, 11]]).all()

def test_sub():
    matrix1 = Matrix([[1,2,],[5,6,],[9,10,]])
    matrix2 = [[2,1,],[1,2,],[2,1,]]
    assert (matrix1 - matrix2 == [[-1, 1],[ 4, 4],[ 7, 9]]).all()

def test_mul():
    matrix1 = Matrix([[1,2,],[5,6,]])
    matrix2 = [[2,1,],[1,2,]]
    assert (matrix1 * matrix2 == [[ 4, 5],[16, 17]]).all()

def test_transponse():
    matrix1 = Matrix([[1,2,],[5,6,],[9,10,]])
    assert (matrix1.transponse() == [[1, 5, 9],[2, 6, 10]]).all()

def test_determinant():
    matrix1 = Matrix([[1,2,],[5,6,]])
    assert (matrix1.determinant() == -4.0).all()

def test_inverce():
    matrix1 = Matrix([[1,1,],[5,6,]])
 #    assert (matrix1.inverce() == [[ 6., -1.],
 # [-5.,  1.]]).all()
    assert np.isclose(matrix1.inverce(), [[ 6., -1.],
 [-5.,  1.]]).all