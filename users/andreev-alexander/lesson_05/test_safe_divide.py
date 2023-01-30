from hw_exclusion import safe_divide

def test_safe_divide_math_int(monkeypatch):
    """Проверяется, что отдается правильный ответ."""
    monkeypatch.setattr("builtins.input", lambda _: "10 2")
    result = safe_divide()
    assert result == 5.0

def test_safe_divide_math_float(monkeypatch):
    """Проверяется, что отдается правильный ответ."""
    monkeypatch.setattr("builtins.input", lambda _: "36.0 18.0")
    result = safe_divide()
    assert result == 2.0

def test_bad_input_three_args(monkeypatch):
    """Проверяется, что ответ 'Введите два числа через пробел!',
    если введено три значения."""
    monkeypatch.setattr("builtins.input", lambda _: "10 3 2")
    result = safe_divide()
    assert result == "Введите два числа через пробел!"

def test_bad_input_one_args(monkeypatch):
    """Проверяется, что ответ 'Введите два числа через пробел!',
    если введено одно значение."""
    monkeypatch.setattr("builtins.input", lambda _: "10")
    result = safe_divide()
    assert result == "Введите два числа через пробел!"

def test_arguments_is_not_float(monkeypatch):
    """Проверяется, что сообщение 'Введите числа, а не слова.',
    если аргумент не число."""
    monkeypatch.setattr("builtins.input", lambda _: "12 two")
    result = safe_divide()
    assert result == "Введите числа, а не слова."

def test_zero_division(monkeypatch):
    """Проверяется, что сообщение 'На ноль делить нельзя.',
    если второй аргумент равен 0."""
    monkeypatch.setattr("builtins.input", lambda _: "12 0")
    result = safe_divide()
    assert result == "На ноль делить нельзя."
