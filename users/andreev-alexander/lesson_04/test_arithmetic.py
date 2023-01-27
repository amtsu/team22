import pytest

from HW_functions import arithmetic


test_cases_math = [
    (2, 3, "+", 5),
    (0, 0, "+", 0),
    (0.1, 0.001, "+", 0.101),
    (2, 3, "-", -1),
    (2, 3, "*", 6),
    (6, 3, "/", 2),     
    (6, 3.5, "+", 9.5)   
]

@pytest.mark.parametrize("num_one, num_two, operator, expected", test_cases_math)
def test_math(num_one, num_two, operator, expected):
    """Проверяется, что математика считается верно."""
    assert arithmetic(num_one, num_two, operator) == expected

def test_operator_not_math():
    """Проверяется, operator является одним из валидных
    арифметических операторов. Если нет, то вызывается исключение ValueError."""
    with pytest.raises(ValueError):
        arithmetic(2, 2, "not_math_operator")

def test_params_not_digits():
    """Проверяется, что параметры функции числа. Если нет, то вызывается
    исключение TypeError."""
    with pytest.raises(TypeError):
        arithmetic("25", 5, "/")

def test_zero_division():
    """Проверяется, что при делении на 0 вызывается
    исключение ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        arithmetic(25, 0, "/")
