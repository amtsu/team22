from HW_05 import (
    phone_numbers,
    phone_numbers_finally,
    safe_divide,
    safe_divide_final,
    calculation,
    calculation_all
)
from pytest import MonkeyPatch

def test_phone_numbers(monkeypatch):
    "Проверяем работу функции"
    monkeypatch.setattr('builtins.input', lambda _: "Misha")
    result = phone_numbers()
    assert result == 88009004552

def test_phone_numbers_noname(monkeypatch):
    "Проверяем отсутствие значения в словаре"
    monkeypatch.setattr('builtins.input', lambda _: "Mish")
    result = phone_numbers()
    assert result == "Такого имени нет"



def test_safe_divide(monkeypatch):
    inputs = iter(["6", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = safe_divide()
    assert result == 2.0

def test_safe_divide_by_0(monkeypatch):
    inputs = iter(["6", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = safe_divide()
    assert result == "На 0 делить нельзя"

def test_safe_divide_final(monkeypatch):
    inputs = iter(["6", "3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = safe_divide_final()
    assert result == 2.0

def test_safe_divide_final_by_0(monkeypatch):
    inputs = iter(["6", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = safe_divide_final()
    assert result == "На 0 делить нельзя"



def test_calculation_math(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "13 - 7")
    result = calculation()
    assert result == 6.0

# def test_calculation_math_not_type(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: "asffs7saf")
#     result = calculation()
#     assert result == "Введите данные вида 'число_+/-_число'"

# def test_calculation_math_not_type_2(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: "asf - fs7saf")
#     result = calculation()
#     assert result == "Введи числа"


def test_calculation_all_math(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "13 - 7")
    result = calculation_all()
    assert result == 6.0

def test_calculation_all_math_2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "13 / 0")
    result = calculation_all()
    assert result == "На 0 делить нельзя"

def test_calculation_all_math_3(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "13 * 0")
    result = calculation_all()
    assert result == 0.0