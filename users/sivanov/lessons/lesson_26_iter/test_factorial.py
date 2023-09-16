"""
функции, тестирующие класс factorial
"""
from factorial import Factorial


def test_factorial_1():
    """
    функция тестирует корректность вычисления факториала
    """
    expected = (
        1,
        1,
        2,
        3,
        6,
        24,
        120,
        720,
        5040,
        40320,
        362880,
        3628800,
        39916800,
        479001600,  # пока хватит
    )
    result = Factorial(20)
    for element in expected:
        assert element == next(result)
