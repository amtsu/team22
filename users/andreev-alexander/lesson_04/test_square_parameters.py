import pytest

from HW_functions import square_parameters


test_cases_math = [
    (2, 8, 4, 2.8284271247461903),
    (1.2, 4.8, 1.44, 1.697056274847714)     
]

@pytest.mark.parametrize("side_length, perimeter, square_are, diagonal", test_cases_math)
def test_math(side_length, perimeter, square_are, diagonal):
    """Проверяется, что математика считается верно."""
    assert square_parameters(side_length) == [perimeter, square_are, diagonal]

def test_cathet_is_great_or_equal_one():
    """Проверяется, что, если сторона квадрата <= 0,
    то вызывается исключение ValueError."""
    with pytest.raises(ValueError):
        square_parameters(0)

def test_side_length_is_string_return_typeerror():
    """Проверяется, что, если аргумент функции не число, 
    то вызывается исключение TypeError из пакета math."""
    with pytest.raises(TypeError):
        square_parameters("12321")
