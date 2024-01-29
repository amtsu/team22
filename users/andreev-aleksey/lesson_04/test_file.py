
from functions import (
    hypotenuse_length,
    hypotenuse_length_05,
    arithmetic,
    square_parameters,
    is_palindrome,
    is_palindrome_one_string,
    is_palindrome_all_type_string
    )


def test_math():
    """Проверяем счет"""
    result = hypotenuse_length(2, 3)
    assert result == 3.605551275463989, 'Error!'   
    
def test_args():
    """Проверяем, что сторона больше 0"""
    result = hypotenuse_length(2, -1)
    assert result == False, 'Error!'



def test_math_05():
    """Проверяем счет"""
    result = hypotenuse_length_05(2, 3)
    assert result == 3.605551275463989, 'Error!'

def test_args_05():
    """Проверяем, что сторона больше 0"""
    result = hypotenuse_length_05(2, -1)
    assert result == False, 'Error!'



def test_arithmetic_divide_by_zero():
    """Проверяем деление на 0"""
    result = arithmetic(6, 0, "/")
    assert result == False, "Error"

def test_arithmetic_not_operator():
    """Проверяем корректность оператора"""
    result = arithmetic(6, 2, "foo")
    assert result == False, "Error"

def test_arithmetic_math():
    """Проверяем корректность математики"""
    result = arithmetic(6, 2, "*")
    assert result == 12, "Error"



def test_square_parameters_less_zero():
    """Проверяем значение строны меньше 0"""
    result = square_parameters(-1)
    assert result == False, "Error"

def test_square_parameters_math():
    """Проверяем корректность математики"""
    result = square_parameters(8)
    assert result == (32, 64, 11.313708498984761), "Error"

def test_square_parameters_type():
    """Проверяем корректность типа"""
    result = square_parameters("33")
    assert result == False, "Error"



def test_is_palindrome_type():
    """Проверяем корректность типа"""
    result = is_palindrome(212)
    assert result == -1

def test_is_palindrome_space():
    """Проверяем пробелы в строке"""
    result = is_palindrome("aa s as")
    assert result == -1



def test_is_palindrome_one_string_type():
    """Проверяем корректность типа"""
    result = is_palindrome(212)
    assert result == -1

def test_is_palindrome_one_string_space():
    """Проверяем пробелы в строке"""
    result = is_palindrome("aa s as")
    assert result == -1



def test_is_palindrome_all_type_string_type():
    """Проверяем корректность типа"""
    result = is_palindrome(212)
    assert result == -1