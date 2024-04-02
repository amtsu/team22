import pytest

from hw7 import print_matrix, ten_times

#тесты для print_matrix
@pytest.mark.parametrize('input_matrix, expected_result', [
    (
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ),
    (
        [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ),
    (
        [[1, 3, 5, 7], [2, 4, 6, 8]],
        [1, 2, 3, 4, 5, 6, 7, 8]
    ),
    (
        [[1, 4], [2, 5], [3, 6]],
        [1, 2, 3, 4, 5, 6]
        
    ),
    (
        [[1, 2, 3]],
        [1, 2, 3]
    ),
    (
        [],
        []
    )
])
def test_print_matrix_positive(input_matrix, expected_result):
    assert print_matrix(input_matrix) == expected_result

#тесты для ten_times
@pytest.mark.parametrize('expected_result', [
    ('Запустили 10 раз'),
])
def test_ten_times_positive(expected_result):
    assert ten_times() == expected_result