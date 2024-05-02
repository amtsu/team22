import pytest

from func_for_hw3 import (calculate_result,
fractional_calculation,
calculat_air_volume_for_conditioner,
quadratic_equation_solution,
string_concatenation_function,
string_multiplication_function,
list_modification)


def test_calculate_result1():
    """
    тест на вычисление операции "+", "*" над числовыми знаениями  
    """
    assert calculate_result()[0] == 80, "Ошибка вычислений"

def test_calculate_result2():
    """
    тест на вычисление операции "-", "/" над числовыми знаениями 
    """
    assert calculate_result()[1] == 7.0, "Ошибка вычислений" 

def test_calculate_result3():
    """
    тест на возведение в степень 
    """
    assert calculate_result()[2] == 32, "Ошибка вычислений возведения в степень"

def test_calculate_result4():
    """
    тест на целочисленное деление
    """
    assert calculate_result()[3] == 6, "Ошибка вычислений целочисленного деления"

def test_calculate_result5():
    """
    тест вычисления остатка от деления
    """
    assert calculate_result()[4] == 1, "Ошибка вычисления остатка от деления"
################################################################################################

def test_fractional_calculation1():
    """
    тест на округление дробного отрицательного числа
    """
    assert fractional_calculation()[0] == -3, "Ошибка вычисления"

def test_fractional_calculation2():
    """
    тест на остаток от деления
    """
    assert fractional_calculation()[1] == - 0.14, "Ошибка вычисления"

#################################################################################################

def test_calculat_air_volume_for_conditioner():
    """
    тест на функцию вычисления объема воздуха для кондиционера
    """
    assert calculat_air_volume_for_conditioner() == 145.70000000000002

###################################################################################################

def test_quadratic_equation_solution():
    """
    тест на функцию решения квадратного уровнения через дискриминант
    """
    assert quadratic_equation_solution() == (-2.0, -2.5), "Ошибка вычисления корней уровнения"

#####################################################################################################

def test_string_concatenation_function():
    """
    туст на функция объединения строк, где первая буква заглавная
    """
    assert string_concatenation_function() == "Hello, world!", "Неверный вывод"

#######################################################################################################

def test_string_multiplication_function():
    """
     тест на функция умножения строк
    """
    assert string_multiplication_function() == "la la la la la la la la la la la la la la la la la la la la la la la la la "

########################################################################################################

def test_list_modification():
    """
    тест на функцию модификации списка
    """
    assert list_modification() == [1, 'hi', 3, [8, 6, 4], 5]
    