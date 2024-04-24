import pytest
from func_for_hw7 import(
print_matrix,
print_haiku1,
print_haiku2
)

@pytest.mark.parametrize("matrix, expected", [
    ([[1,4,7,],[2,5,8,],[3,6,9,]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([[1,4,7,10],[2,5,8,11],[3,6,9,12]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    ([[1,3,5,7],[2,4,6,8],], [1, 2, 3, 4, 5, 6, 7, 8]),
    ([], [])
])

def test_print_matrix(matrix, expected):
    assert print_matrix(matrix) == expected

@pytest.mark.parametrize("haiku, expected", [
    (['Всё глазел на них', 'Сакуры цветы, пока', 'Шею не свело'],
     ['ВСЁ ГЛАЗЕЛ НА НИХ', 'САКУРЫ ЦВЕТЫ, ПОКА', 'ШЕЮ НЕ СВЕЛО'])
])
def test_print_haiku(haiku, expected):
    assert print_haiku1(haiku) == expected

@pytest.mark.parametrize("haiku, expected", [
     (['Всё глазел на них', 'Сакуры цветы, пока', 'Шею не свело'],
     ['В алаи', 'Су е,о', 'Ш  е'])
])
def test_print_haiku2(haiku, expected):
    assert print_haiku2(haiku) == expected