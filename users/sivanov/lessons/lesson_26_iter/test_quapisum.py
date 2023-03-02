"""
функции, тестирующие класс quapirow
"""
from quapisum import QuaPiSum


def test_quapirow_1():
    """
    функция тестирует примерную правильность вычисления суммы ряда
    на каждой итерации.
    """
    expected = (
        1,
        2.0 / 3.0,
        13.0 / 15.0,
        76.0 / 105.0,
        263.0 / 315.0,
        2578 / 3465,
        36979 / 45045,
        33976 / 45045,
    )
    result = QuaPiSum(20)
    for element in expected:
        assert abs(element - next(result)) < 0.00001


# мамкин инженер, определил для себя точность вычисления
