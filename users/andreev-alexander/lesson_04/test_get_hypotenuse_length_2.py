import pytest

from HW_functions import get_hypotenuse_length_2


test_cases_math = [
    (2, 3, 3.605551275463989),
    (12, 33, 35.11409973215888)
]

@pytest.mark.parametrize("cathet_one, cathet_two, expected", test_cases_math)
def test_math(cathet_one, cathet_two, expected):
    """Проверяется, что математика считается верно."""
    result = get_hypotenuse_length_2(cathet_one, cathet_two)
    assert result == expected


test_cases_value_error = [
    (0, 2),
    (-1, 3)
]

@pytest.mark.parametrize("cathet_one, cathet_two", test_cases_value_error)
def test_cathet_is_great_or_equal_one(cathet_one, cathet_two):
    """Проверяется, что, если сторона треугольника <= 0,
    то вызывается исключение ValueError."""
    with pytest.raises(ValueError):
        get_hypotenuse_length_2(cathet_one, cathet_two)


def test_cathet_is_string_return_typeerror():
    """Проверяется, что, если аргумент функции не число, 
    то вызывается исключение TypeError из пакета math."""
    with pytest.raises(TypeError):
        get_hypotenuse_length_2("12321", 2)
