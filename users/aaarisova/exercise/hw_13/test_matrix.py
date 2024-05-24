import pytest
import pickle
import numpy as np
from matrix_extended import Matrix


def test_matrix_in_file():
    matrix1 = Matrix([[1,2],[2,1]])
    file = 'matrix.pkl'
    matrix1.save_to_file('matrix.pkl')
    load_f = matrix1.load_from_file('matrix.pkl')
    assert load_f.matrix == [[1,2],[2,1]]
    