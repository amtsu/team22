import pytest

from triangle import triangle_type

#тесты для функции triangle_type
def test_triangle_type_positive_1():
    input = [3, 4, 3]
    expected = 'остроугольный'
    assert triangle_type(*input) == expected

def test_triangle_type_positive_2():
    input = [3, 4, 5]
    expected = 'прямоугольный'
    assert triangle_type(*input) == expected

def test_triangle_type_negative():
    input = [3, 4]
    try:
        triangle_type(*input)
    except TypeError:
        assert True

@pytest.mark.parametrize(
    'a, b, c, expected',
    [
        (3, 4, 4, 'остроугольный'),
        (3, 4, 5, 'прямоугольный'),
        (1, 10, 1, 'не треугольник'),
    ]
)
def test_triangle_type_positive (a, b, c, expected):
    assert triangle_type(a, b, c) == expected

@pytest.mark.parametrize(
    'a, b, c, expected_error',
    [
        (3, 4, 'a', TypeError),
        ([1, 3, 3], 4, 5, TypeError),
        ('3', '4', 'a', TypeError),
    ]
)
def test_triangle_type_negative (a, b, c, expected_error):
    with pytest.raises(expected_error):
        triangle_type(a, b, c)