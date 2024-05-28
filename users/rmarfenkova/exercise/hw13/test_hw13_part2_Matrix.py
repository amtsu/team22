import pytest
from hw13_part2_Matrix import Matrix
from class_PickleHandler import PickleHandler

def test_save_load():
    original_matrix = Matrix([[1, 2], [3, 4]])
    PickleHandler.save_to_file(original_matrix, "matrix1.pkl")
    loaded_matrix = PickleHandler.load_from_file("matrix1.pkl")
    assert loaded_matrix.rows == original_matrix.rows

def test_save_load_with_empty_matrix():
    original_matrix = Matrix([])
    PickleHandler.save_to_file(original_matrix, "matrix2.pkl")
    loaded_matrix = PickleHandler.load_from_file("matrix2.pkl")
    assert loaded_matrix.rows == original_matrix.rows