from typing import Union, Tuple

import pytest


# Реализовать функцию, вычисляющую длину гипотенузы прямоугольного треугольника. Параметры – длины катетов.
# Указание: для вычисления квадратного корня можно возвести число в степень 0,5.
# Можно использовать функцию, написанную в предыдущей задаче.


def gipotenuza(katet_1: Union[int, float], katet_2: Union[int, float]) -> float:
    """
    Calculation of the hypotenuse of a right triangle from the lengths of two legs
    :param katet_1:
    :param katet_2:
    :return float number:
    """
    if not isinstance(katet_1, int | float) or not isinstance(katet_2, int | float):
        raise TypeError("Неподдерживаемый тип данных")
    return pow(pow(katet_1, 2) + pow(katet_2, 2), 0.5)


def test_hp_gipotenuza():
    """Happy pass test"""
    assert gipotenuza(3, 4) == 5


def test_typeerror_gipotenuza():
    """TypeError test"""
    with pytest.raises(TypeError):
        gipotenuza("ghb", "grt")
    with pytest.raises(TypeError):
        gipotenuza([2], [3])
    with pytest.raises(TypeError):
        gipotenuza({2}, {3})
    with pytest.raises(TypeError):
        gipotenuza((2, 3), (3, 4))
    with pytest.raises(TypeError):
        gipotenuza(3 + 0j, 4 + 0j)


# Написать функцию arithmetic, принимающую 3 аргумента: первые два - числа, третий - операция, которая должна быть
# произведена над ними. Если третий аргумент равен ‘+’, сложить их; ‘—’ -вычесть; ‘*’ — умножить; ‘/’ — разделить. В
# остальных случаях вернуть строку "Неизвестная операция".

def arithmetic(first_arg: Union[int, float], second_arg: Union[int, float], operation: str) -> float:
    """
    Simple calculator with operations: < + >, < - >, < * >, < / >
    :param first_arg:
    :param second_arg:
    :param operation:
    :return float number:
    """
    if not isinstance(first_arg, int | float) or not isinstance(second_arg, int | float) or not isinstance(operation,
                                                                                                           str):
        raise TypeError("Неподдерживаемый тип данных")
    if operation == "+":
        result = first_arg + second_arg
    elif operation == "-":
        result = first_arg - second_arg
    elif operation == "*":
        result = first_arg * second_arg
    elif operation == "/":
        if second_arg == 0:
            raise ZeroDivisionError
        else:
            result = first_arg / second_arg
    else:
        result = "Неизвестная операция"
    return result


def test_hp_arithmetic():
    """Happy pass test"""
    assert arithmetic(3, 4, "+") == 7
    assert arithmetic(3, 4, "-") == -1
    assert arithmetic(3, 4, "*") == 12
    assert arithmetic(3, 4, "/") == 0.75


def test_zerodivision():
    """ZeroDivisionError test"""
    with pytest.raises(ZeroDivisionError):
        arithmetic(3, 0, "/")


def test_unsupported_operation():
    """Unsupported operation test"""
    assert arithmetic(3, 4, "**") == "Неизвестная операция"


def test_typeerror_arithmetic():
    """TypeError test"""
    with pytest.raises(TypeError):
        arithmetic("ghb", "grt", "grt")
    with pytest.raises(TypeError):
        arithmetic([2], [3], [3])
    with pytest.raises(TypeError):
        arithmetic({2}, {3}, {3})
    with pytest.raises(TypeError):
        arithmetic((2, 3), (3, 4), (3, 4))
    with pytest.raises(TypeError):
        arithmetic(3 + 0j, 4 + 0j, 4 + 0j)


# Написать функцию square_parameters, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения:
# периметр квадрата, площадь квадрата и диагональ квадрата.

def square_parameters(length_of_the_square: Union[int, float]) -> Tuple[float, float, float]:
    """
    A function that calculates the perimeter, area and diagonal of a square
    :param length_of_the_square:
    :return tuple of float numbers:
    """
    if not isinstance(length_of_the_square, (int, float)):
        raise TypeError("Неподдерживаемый тип данных")
    else:
        return float(4 * length_of_the_square), float(pow(length_of_the_square, 2)), gipotenuza(length_of_the_square,
                                                                                                length_of_the_square)


def test_hp_square_parameter():
    """Happy pass test"""
    assert square_parameters(3.0) == (12.0, 9.0, 4.242640687119285)


def test_typeerror_square_parameters():
    """TypeError test"""
    with pytest.raises(TypeError):
        square_parameters("ghb")
    with pytest.raises(TypeError):
        square_parameters([2])
    with pytest.raises(TypeError):
        square_parameters({2})
    with pytest.raises(TypeError):
        square_parameters((2, 3))
    with pytest.raises(TypeError):
        square_parameters(3 + 0j)


# Написать функцию is_prime, принимающую 1 аргумент — число, и определяющее, простое оно или составное.
# Простые числа делятся без остатка только на 1 и на самого себя. Если число делится без остатка на какое-то другое
# число, то оно составное.

def is_prime(number: int) -> str:
    """
    Determines whether a number is prime or composite
    :param number:
    :return string:
    """
    if not isinstance(number, int):
        raise TypeError("Неподдерживаемый тип данных.\nПринимаются только целые числа")
    result = "prime"
    for num in range(2, abs(number)):
        if number % num == 0:
            result = "composite"
            break
    return result


def test_hp_is_prime():
    """Happy pass test"""
    assert is_prime(3) == "prime"
    assert is_prime(97) == "prime"
    assert is_prime(98) == "composite"
    assert is_prime(1) == "prime"
    assert is_prime(-1) == "prime"
    assert is_prime(-98) == "composite"


def test_typeerror_is_prime():
    """TypeError test"""
    with pytest.raises(TypeError):
        is_prime("ghb")
    with pytest.raises(TypeError):
        is_prime(-0.98)
    with pytest.raises(TypeError):
        is_prime([2])
    with pytest.raises(TypeError):
        is_prime({2})
    with pytest.raises(TypeError):
        is_prime((2, 3))
    with pytest.raises(TypeError):
        is_prime(3 + 0j)


# Написать функцию is_palindrome, принимающую 1 аргумент — строку (без пробелов, строчные буквы) и определяющую,
# является ли она палиндромом, т.е. читается одинаково слева направо и справа налево.
# Если да, вернуть True, иначе False.

def is_palindrome(string: str) -> bool:
    """
    Determines whether a word is a palindrome or not
    :param string:
    :return bool:
    """
    if not isinstance(string, str):
        raise TypeError("Неподдерживаемый тип данных.\nПринимаются только строки")
    return string == "".join(reversed(string))


def test_hp_is_palindrome():
    """Happy pass test"""
    assert is_palindrome("шалаш") == True
    assert is_palindrome("привет") == False


def test_typeerror_is_palindrome():
    """TypeError test"""
    with pytest.raises(TypeError):
        is_palindrome(1)
    with pytest.raises(TypeError):
        is_palindrome(-0.98)
    with pytest.raises(TypeError):
        is_palindrome([2])
    with pytest.raises(TypeError):
        is_palindrome({2})
    with pytest.raises(TypeError):
        is_palindrome((2, 3))
    with pytest.raises(TypeError):
        is_palindrome(3 + 0j)


# Как решить предыдущую задачу с помощью срезов?

def is_palindrome_2(string: str) -> bool:
    """
    Determines whether a word is a palindrome or not
    :param string:
    :return bool:
    """
    if not isinstance(string, str):
        raise TypeError("Неподдерживаемый тип данных.\nПринимаются только строки")
    return string == string[::-1]


def test_hp_is_palindrome_2():
    """Happy pass test"""
    assert is_palindrome_2("шалаш") == True
    assert is_palindrome_2("привет") == False


def test_typeerror_is_palindrome_2():
    """TypeError test"""
    with pytest.raises(TypeError):
        is_palindrome_2(1)
    with pytest.raises(TypeError):
        is_palindrome_2(-0.98)
    with pytest.raises(TypeError):
        is_palindrome_2([2])
    with pytest.raises(TypeError):
        is_palindrome_2({2})
    with pytest.raises(TypeError):
        is_palindrome_2((2, 3))
    with pytest.raises(TypeError):
        is_palindrome_2(3 + 0j)


# Усовершенствовать предыдущую функцию, чтобы проверяемая строка могла содержать пробелы, а также прописные и
# строчные буквы.

def is_palindrome_3(string: str) -> bool:
    """
    Determines whether a word is a palindrome or not
    :param string:
    :return bool:
    """
    if not isinstance(string, str):
        raise TypeError("Неподдерживаемый тип данных.\nПринимаются только строки")
    result = string.lower().replace(" ", "")
    return result == result[::-1]


def test_is_palindrome_3():
    """Happy pass test"""
    assert is_palindrome_3("Ш а     л А  ш") == True
    assert is_palindrome_3("Кидал в зубра арбуз Владик") == True
    assert is_palindrome_3("re vr  vf D s") == False


def test_typeerror_is_palindrome_3():
    """TypeError test"""
    with pytest.raises(TypeError):
        is_palindrome_3(1)
    with pytest.raises(TypeError):
        is_palindrome_3(-0.98)
    with pytest.raises(TypeError):
        is_palindrome_3([2])
    with pytest.raises(TypeError):
        is_palindrome_3({2})
    with pytest.raises(TypeError):
        is_palindrome_3((2, 3))
    with pytest.raises(TypeError):
        is_palindrome_3(3 + 0j)


# Написать функцию, которая возводит число в 3тью степень.
def chislo_v_tretyu_stepen(number: int) -> int:
    """
    Returns the passed number to the third power
    :param number:
    :return integer:
    """
    if not isinstance(number, int):
        raise TypeError("Неподдерживаемый тип данных.\nПринимаются только целые числа")
    return pow(number, 3)


def test_third_stepen():
    """Happy pass test"""
    assert chislo_v_tretyu_stepen(4) == 64
    assert chislo_v_tretyu_stepen(-3) == -27


def test_typeerror_chislo_v_tretyu_stepen():
    """TypeError test"""
    with pytest.raises(TypeError):
        chislo_v_tretyu_stepen("ghb")
    with pytest.raises(TypeError):
        chislo_v_tretyu_stepen(-0.98)
    with pytest.raises(TypeError):
        chislo_v_tretyu_stepen([2])
    with pytest.raises(TypeError):
        chislo_v_tretyu_stepen({2})
    with pytest.raises(TypeError):
        chislo_v_tretyu_stepen((2, 3))
    with pytest.raises(TypeError):
        chislo_v_tretyu_stepen(3 + 0j)


# Написать функцию, которая возводит в квадрат (проверить результаты для числа 3 и -3)

def square_of_number(number: int) -> int:
    """
    Returns the passed number to the second power
    :param number:
    :return integer:
    """
    if not isinstance(number, int):
        raise TypeError("Неподдерживаемый тип данных.\nПринимаются только целые числа")
    return pow(number, 2)


def test_hp_square_of_number():
    """Happy pass test"""
    assert square_of_number(3) == 9
    assert square_of_number(-3) == 9


def test_typeerror_square_of_number():
    """TypeError test"""
    with pytest.raises(TypeError):
        square_of_number("ghb")
    with pytest.raises(TypeError):
        square_of_number(-0.98)
    with pytest.raises(TypeError):
        square_of_number([2])
    with pytest.raises(TypeError):
        square_of_number({2})
    with pytest.raises(TypeError):
        square_of_number((2, 3))
    with pytest.raises(TypeError):
        square_of_number(3 + 0j)


# Написать функцию, которая принимает строку и число:
# обрезает строку до указанной длинны если длина строки меньше числа,
# удваивает строку, если длина строки равна числу.
# Если больше, то берет остаток от деления числа на строку и обрезает до этой длины

def mahinacii_s_strokoy(string: str, number: int) -> str:
    """
    returns a string converted according to the conditions: If the length of the word is greater than the second
    argument, then truncate the string to the number of characters equal to the second argument. If the length of the
    word is equal to the second argument, then returns a string twice the length. If the length of the word is less
    than the second argument, then truncates the word to the number of characters equal to the remainder of dividing
    the second argument by the length of the word
    :param string:
    :param number:
    :return string:
    """
    if not isinstance(string, str) or not isinstance(number, int):
        raise TypeError("Неподдерживаемый тип данных")
    if len(string) > number:
        result = string[0: number]
    elif len(string) == number:
        result = 2 * string
    else:
        result = string[0: number % len(string)]
    return result


def test_hp_mahinacii_s_strokoy():
    """Happy pass test"""
    assert mahinacii_s_strokoy("привет", 4) == "прив"
    assert mahinacii_s_strokoy("привет", 6) == "приветпривет"
    assert mahinacii_s_strokoy("привет", 8) == "пр"
    assert mahinacii_s_strokoy("двенадцать !", 17) == "двена"


def test_typeerror_mahinacii_s_strokoy():
    """TypeError test"""
    with pytest.raises(TypeError):
        mahinacii_s_strokoy("ghb", "grt")
    with pytest.raises(TypeError):
        mahinacii_s_strokoy([2], [3])
    with pytest.raises(TypeError):
        mahinacii_s_strokoy({2}, {3})
    with pytest.raises(TypeError):
        mahinacii_s_strokoy((2, 3), (3, 4))
    with pytest.raises(TypeError):
        mahinacii_s_strokoy(3 + 0j, 4 + 0j)
