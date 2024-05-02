import pytest
from functions_hw_3 import *

def test_count_operacions():
    '''
    Тест на вычисление результата операций
    '''
    assert count_operacions()[0] == 80, "Ошибка умножения и сложения"
    assert count_operacions()[1] == 7.0, "Ошибка вычитания и деления"
    assert count_operacions()[2] == 32, "Ошибка возведения в степень"
    assert count_operacions()[3] == 6, "Ошибка взятия целой части от деления"
    assert count_operacions()[4] == 1, "Ошибка взятия остатка от деления"
    

def test_round_remain_number_1():
    '''
    Тест округления числа до целого
    '''
    assert round_remain_number()[0] == -3, "Ошибка округления числа до целого"

def test_round_remain_number_2():
    '''
    Тест взятие остатка от числа
    '''
    assert round_remain_number()[1] == -0.14, "Ошибка взятия остатка от числа"


def test_area_of_rectangle():
    '''Тест вычисления площади прямоугольника'''
    assert area_of_rectangle() == 35, "Ошибка вычисления площади прямоуг"

def test_air_volume():
    '''Тест рассчета объема воздуха для охлождения кв кондиционером'''
    assert air_volume() == 145.7, "Ошибка рассчета объема воздуха"


def test_discriminant_equation():
    '''Тест решения квадратного уравнения, с использованием дискриминанта.'''
    assert discriminant_equation() == (1.09, -4.59), "Ошибка решения кв уравнения"


def test_string_concatenation():
    '''Тест объединения строк, 
    + первая буква в предложении заглавная'''
    assert string_concatenation() == 'Hello, world!', "Ошибка объединения строк"
    

def test_string_length():
    '''Тест подсчета кол-ва символов в "Hello, world!" '''
    assert string_length() == 13, "Ошибка кол-ва символов"


def test_string_multiple_times():
    '''Тест вывода на экран строки la 25 раз'''
    assert string_multiple_times() == 'la la la la la la la la la la la la la la la la la la la la la la la la la ', "Ошибка вывода строки 25 раз"


def test_list_modification():
    '''Тест модификации списка'''
    assert list_modification() == [1, 'hi', 3, [8, 6, 4], 5], "Ошибка вывода модифицированного списка"


def test_extract_sublist():
    '''Извлеките подсписок с 3-го по 7-й элемент включительно.'''
    assert extract_sublist() == [3, 4, 5, 6, 7], "Ошибка вывода подсписка"

