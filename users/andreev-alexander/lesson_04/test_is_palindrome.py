import pytest

from HW_functions import is_palindrome


def test_str_with_space_return_value_error():
    """Проверяется, что строка не содержит пробелов,
    иначе вызывается исключение."""
    with pytest.raises(ValueError):
        is_palindrome("string with space")

def test_str_with_upper_letter_return_value_error():
    """Проверяется, что строка не содержит заглавных букв,
    иначе вызывается исключение."""
    with pytest.raises(ValueError):
        is_palindrome("stringWithCapitalLetter")

def test_return_true():
    """Проверяется, что функция возвращает True, если
    строка - палиндром."""
    assert is_palindrome("abccba")

def test_return_false():
    """Проверяется, что функция возвращает False, если
    строка - не палиндром."""
    assert is_palindrome("aabbb") == False
