from hw_exclusion import calc_all

def test_calc_plus_int(monkeypatch):
    """Проверяется, что отдается правильный ответ."""
    monkeypatch.setattr("builtins.input", lambda _: "10 + 2")
    result = calc_all()
    assert result == 12.0

def test_calc_plus_float(monkeypatch):
    """Проверяется, что отдается правильный ответ."""
    monkeypatch.setattr("builtins.input", lambda _: "10.1 + 2.2")
    result = calc_all()
    assert result == 12.3

def test_calc_devide_float(monkeypatch):
    """Проверяется, что отдается правильный ответ."""
    monkeypatch.setattr("builtins.input", lambda _: "10.2 / 2.0")
    result = calc_all()
    assert result == 5.1

def test_calc_devide_int(monkeypatch):
    """Проверяется, что отдается правильный ответ."""
    monkeypatch.setattr("builtins.input", lambda _: "10 / 2")
    result = calc_all()
    assert result == 5.0

def test_calc_multiply_float(monkeypatch):
    """Проверяется, что отдается правильный ответ."""
    monkeypatch.setattr("builtins.input", lambda _: "10.2 * 2.0")
    result = calc_all()
    assert result == 20.4

def test_calc_multiply_int(monkeypatch):
    """Проверяется, что отдается правильный ответ."""
    monkeypatch.setattr("builtins.input", lambda _: "10 * 2")
    result = calc_all()
    assert result == 20.0

def test_calc_minus_int(monkeypatch):
    """Проверяется, что отдается правильный ответ."""
    monkeypatch.setattr("builtins.input", lambda _: "10 - 2")
    result = calc_all()
    assert result == 8.0

def test_calc_minus_float(monkeypatch):
    """Проверяется, что отдается правильный ответ."""
    monkeypatch.setattr("builtins.input", lambda _: "10.7 - 2.1")
    result = calc_all()
    assert result == 8.6

def test_bad_input_four_args(monkeypatch):
    """Проверяется, что отдается сообщение, если аргументов больше трех."""
    monkeypatch.setattr("builtins.input", lambda _: "10.7 1 2.1 2")
    result = calc_all()
    assert result == "Введите 'число, знак операции, число' через пробел!"

def test_bad_input_two_args(monkeypatch):
    """Проверяется, что отдается сообщение, если аргументов меньше трех."""
    monkeypatch.setattr("builtins.input", lambda _: "2.1 2")
    result = calc_all()
    assert result == "Введите 'число, знак операции, число' через пробел!"

def test_arguments_is_not_float(monkeypatch):
    """Проверяется, что сообщение 'Введите числа, а не слова.',
    если аргумент не число."""
    monkeypatch.setattr("builtins.input", lambda _: "12 + two")
    result = calc_all()
    assert result == "Введите числа, а не слова."

def test_operator_not_correct(monkeypatch):
    """Проверяется, что выдается сообщение, если оператор не +, -, /, *."""
    monkeypatch.setattr("builtins.input", lambda _: "12 a 12")
    result = calc_all()
    assert result == "Значение оператора должо быть: +, -, *, /."

def test_zero_devide(monkeypatch):
    """Проверяется, что выдается сообщение, при делении на ноль."""
    monkeypatch.setattr("builtins.input", lambda _: "12 / 0")
    result = calc_all()
    assert result == "На ноль делить нельзя."
