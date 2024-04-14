import pytest
from some_func_hw5 import (
is_palindrome, 
great_com_divide, 
is_leap2, 
is_correct_date, 
show_fruits_info, 
show_squares_while, 
get_value_from_user, 
check_age,
has_repeats,
print_students,
is_prime,
generate_prime,
sum_cummulat,
count_factorial,
deff_week_day,
)

@pytest.fixture
def func():
    x = 5
    return x

def test1(func):
    assert 5 == func
    
def test2(func):
    assert 6 != func
    
############################################################################################
# deff_week_day (8)
############################################################################################

@pytest.mark.parametrize("num, expected", [
    (1, "Понедельник"),
    (7, "Воскресение"),
    (10, None),
    (-5, None),
    (0, None)
])

def test_deff_week_day_correct_input(num, expected):
    assert deff_week_day(num) == expected

@pytest.mark.parametrize("num, expected", [
    (3.5, KeyError),
    ("5", TypeError),
    (None, TypeError)
])

def test_deff_week_day_incorrect_input(num, expected):
    with pytest.raises(expected):
        deff_week_day(num) == expected
    # assert deff_week_day(num) == pytest.raises(expected)
    # assert deff_week_day(num) == raise expected
    # pytest.raises(expected, deff_week_day, *num)

# def test_deff_week_day_incorrect_input():
#     input = 3.5
#     try:
#         deff_week_day(input) 
#     except Exception as exception:
#        assert exception.__class__.__qualname__ == 'KeyError'

    

############################################################################################
# count_factorial (9)
############################################################################################

@pytest.mark.parametrize("num, expected", [
    (0, 1),
    (1, 1),
    (3, 6),
    (10, 3628800),
    (-5, None),
    (3.5, 13.125),
])

def test_count_factorial_correct_input(num, expected):
    assert count_factorial(num) == expected

@pytest.mark.parametrize("num, expected", [
    ("5", TypeError),
    (None, TypeError),
    ({1,5}, TypeError)
])

def test_count_factorial_incorrect_input(num, expected):
    with pytest.raises(expected):
        count_factorial(num) == expected
        
############################################################################################
# sum_cummulat (10)
############################################################################################

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 5, 15),
    (2, 30, 464),
    (0, 0, 0),
    (5, 0, 0),
    (-5, -1, -15),
    (-5, -7, 0),
])

def test_sum_cummulat_correct_input(num1, num2, expected):
    assert sum_cummulat(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    ("5", 10, TypeError),
    (None, 0, TypeError),
    (5.5, 10, TypeError),
    ({1,5}, 8, TypeError)
])

def test_sum_cummulat_incorrect_input(num1, num2, expected):
    with pytest.raises(expected):
        sum_cummulat(num1, num2) == expected

############################################################################################
# is_prime (11)
############################################################################################

@pytest.mark.parametrize("num, expected", [
    (11, True),
    (2, True),
    # (2147483647, True),
    (131, True),
    (1991, False),
    (0, False),
    (1, False),
    (-5, False)    
])

def test_is_prime_correct_input(num, expected):
    assert is_prime(num) == expected

@pytest.mark.parametrize("num, expected", [
    ("5", TypeError),
    (None, TypeError),
    (5.5, TypeError),
    ({1,5}, TypeError)
])

def test_is_prime_incorrect_input(num, expected):
    with pytest.raises(expected):
        is_prime(num) == expected

############################################################################################
# generate_prime (6)
############################################################################################

@pytest.mark.parametrize("num, expected", [
    (0, []),
    (22, [2, 3, 5, 7, 11, 13, 17, 19]),
    (-5, [])
])

def test_generate_prime_correct(num, expected):
    assert generate_prime(num) == expected

@pytest.mark.parametrize("num, expected", [
    ("5", TypeError),
    (None, TypeError),
    (5.5, TypeError)
])

def test_generate_prime_incorrect(num, expected):
    with pytest.raises(expected):
        generate_prime(num) == expected
        
############################################################################################
# print_students (7)
############################################################################################

@pytest.mark.parametrize("student_dict, expected", [
    ({"Иванов": 22, "Петрова": 13, "Сидоров": 23}, ['Студент: Иванов, возраст: 22 годик(ов)', 'Студент: Петрова, возраст: 13 годик(ов)', 'Студент: Сидоров, возраст: 23 годик(ов)']),
    ({}, []),
    ({"": 30}, ['Студент: , возраст: 30 годик(ов)']),
    ({30: None}, ['Студент: 30, возраст: None годик(ов)']),
    ({0: 0}, ['Студент: 0, возраст: 0 годик(ов)'])
])

def test_print_students_correct_data_type(student_dict, expected):
    assert print_students(student_dict) == expected

@pytest.mark.parametrize("student_dict, expected", [
    (["Алексей", 20], AttributeError),
    (None, AttributeError)
])

def test_print_students_incorrect_input(student_dict, expected):
    with pytest.raises(expected):
        print_students(student_dict) == expected

############################################################################################
# has_repeats (3)
############################################################################################

def test_has_repeats_correct(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "Hakuna matata")
    assert has_repeats() == {'a': 5, 't': 2}

def test_has_repeats_empty_str(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "")
    assert has_repeats() == {}

def test_has_repeats_no_repeats(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "qwerty")
    assert has_repeats() == {}

############################################################################################
# check_age (5)
############################################################################################

def test_check_age_less18(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 10)
    assert check_age() == "Несовершеннолетний"

def test_check_age_between18_65(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 50)
    assert check_age() == "Совершеннолетний"

def test_check_age_exceed65(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 70)
    assert check_age() == "Пенсионер"

def test_check_age_zero(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 0)
    assert check_age() == ""

def test_check_age_not_int(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'str')
    assert check_age() == ""

############################################################################################
# is_palindrome (7)
############################################################################################

def test_is_palindrome():
    """
    Проверка простой строки на палиндромность
    """
    input_data = "оно"
    expected = True
    assert expected == is_palindrome(input_data)

# test_is_palindrome()

def test_is_palindrome_letter_case():
    """
    Проверка строки на палиндромность с учетом регистра
    """
    input_data = "А роза упала на лапу Азора"
    expected = True
    assert expected == is_palindrome(input_data)

# test_is_palindrome_letter_case()

def test_is_palindrome_with_symbols():
    """
    Проверка строки на палиндромность с учетом дополнительных символов
    """
    input_data = "А роза упала$ на лапу Азора"
    expected = True
    assert expected == is_palindrome(input_data)

# test_is_palindrome_with_symbols()

def test_is_palindrome_not():
    """
    Проверка строки на палиндромность (строка - не палиндром)
    """
    input_data = "абра-кадабра"
    expected = False
    assert expected == is_palindrome(input_data)

# test_is_palindrome_not()

def test_is_palindrome_not_str():
    """
    Проверка на неверный тип аргумента
    """
    input_data = 2024
    expected = None
    assert expected == is_palindrome(input_data)

# test_is_palindrome_not_str()

def test_is_palindrome_empty_str():
    """
    Проверка на передачу пустой строки в качестве аргумента
    """
    input_data = ""
    expected = False
    assert expected == is_palindrome(input_data)

# test_is_palindrome_empty_str()

def test_is_palindrome_single_char():
    """
    Проверка на передачу пустой строки в качестве аргумента
    """
    input_data = "Я"
    expected = True
    assert expected == is_palindrome(input_data)

# test_is_palindrome_single_char()

############################################################################################
# great_com_divide (7)
############################################################################################

def test_great_com_divide_normal():
    """
    Проверка работоспособности great_com_divide() при нормальных условиях
    """
    input_data = [11,33]
    expected = 11
    assert expected == great_com_divide(*input_data)

# test_great_com_divide_normal()

def test_great_com_divide_zero_1():
    """
    Проверка работы great_com_divide() при нулевом значении одного из параметров
    """
    input_data = [0,33]
    expected = None
    assert expected == great_com_divide(*input_data)

# test_great_com_divide_zero_1()

def test_great_com_divide_zero_2():
    """
    Проверка работы great_com_divide() при нулевых значениях обоих параметров
    """
    input_data = [0,0]
    expected = None
    assert expected == great_com_divide(*input_data)

# test_great_com_divide_zero_2()

def test_great_com_divide_neg_num_1():
    """
    Проверка работы great_com_divide() при отрицательном значении одного из параметров
    """
    input_data = [-10,20]
    expected = None
    assert expected == great_com_divide(*input_data)

# test_great_com_divide_neg_num_1()

def test_great_com_divide_neg_num_2():
    """
    Проверка работы great_com_divide() при отрицательных значениях обоих параметров
    """
    input_data = [-10,-20]
    expected = None
    assert expected == great_com_divide(*input_data)

# test_great_com_divide_neg_num_2()

def test_great_com_divide_incorect_input_1():
    """
    Проверка работы great_com_divide() при неверном типе введенных параметров
    """
    input_data = ["lala", 20]
    expected = None
    assert expected == great_com_divide(*input_data)

# test_great_com_divide_incorect_input_1()

def test_great_com_divide_incorect_input_2():
    """
    Проверка работы great_com_divide() при неверном типе введенных параметров
    """
    input_data = ["11", 22]
    expected = None
    assert expected == great_com_divide(*input_data)

# test_great_com_divide_incorect_input_2()

############################################################################################
# is_leap2 (5)
############################################################################################

def test_is_leap_true():
    """
    Проверка работы функции is_leap2() при вводе високосного года
    """
    input_data = 1600
    expected = True
    assert expected == is_leap2(input_data)

def test_is_leap_true2():
    """
    Проверка работы функции is_leap2() при вводе високосного года
    """
    input_data = 2024
    expected = True
    assert expected == is_leap2(input_data)

def test_is_leap_false():
    """
    Проверка работы функции is_leap2() при вводе невисокосного года
    """
    input_data = 1900
    expected = False
    assert expected == is_leap2(input_data)

def test_is_leap_false2():
    """
    Проверка работы функции is_leap2() при вводе невисокосного года
    """
    input_data = 1991
    expected = False
    assert expected == is_leap2(input_data)

def test_is_leap_None():
    """
    Проверка работы функции is_leap2() при вводе невисокосного года
    """
    input_data = '1991'
    expected = None
    assert expected == is_leap2(input_data)

############################################################################################
# is_correct_date (5)
############################################################################################

def test_is_correct_date_true():
    """
    Проверка работы функции is_correct_date() при вводе корректной даты
    """
    input_data = [25,7, 1991]
    expected = True
    assert expected == is_correct_date(*input_data)

def test_is_correct_date_true2():
    """
    Проверка работы функции is_correct_date() при вводе корректной даты високосного года
    """
    input_data = [29,2,2024]
    expected = True
    assert expected == is_correct_date(*input_data)

def test_is_correct_date_false():
    """
    Проверка работы функции is_correct_date() при вводе некорректной даты корректного типа данных
    """
    input_data = [201, 5, 222]
    expected = False
    assert expected == is_correct_date(*input_data)

def test_is_correct_date_false2():
    """
    Проверка работы функции is_correct_date() при вводе некорректной даты некорректного типа данных
    """
    input_data = ['5',8, 2006]
    expected = False
    assert expected == is_correct_date(*input_data)

def test_is_correct_date_false3():
    """
    Проверка работы функции is_correct_date() при вводе некорректной даты некорректного типа данных (всех трёх значений)
    """
    input_data = ['5','8', '2006']
    expected = False
    assert expected == is_correct_date(*input_data)

############################################################################################
# show_fruits_info (4)
############################################################################################

def test_show_fruits_info_corr_data():
    """
    Проверка работы функции show_fruits_info() при вводе корректных данных
    """
    fruits_quantity = {"яблоко": 5, "банан": 10, "апельсин": 7}
    fruits_prices = {"яблоко": 1.5, "банан": 2, "апельсин": 1.2}
    expected = ['яблоко, количество: 5, цена: 1.5', 'банан, количество: 10, цена: 2', 'апельсин, количество: 7, цена: 1.2']
    assert expected == show_fruits_info(fruits_quantity, fruits_prices)

def test_show_fruits_info_empty_dict1():
    """
    Проверка работы функции show_fruits_info(), если первый параметр - пустой словарь
    """
    fruits_quantity = {}
    fruits_prices = {"яблоко": 1.5, "банан": 2, "апельсин": 1.2}
    expected = []
    assert expected == show_fruits_info(fruits_quantity, fruits_prices)

def test_show_fruits_info_empty_dict2():
    """
    Проверка работы функции show_fruits_info(), если второй параметр - пустой словарь
    """
    fruits_quantity = {"яблоко": 5, "банан": 10, "апельсин": 7}
    fruits_prices = {}
    expected = []
    assert expected == show_fruits_info(fruits_quantity, fruits_prices)

def test_show_fruits_info_not_dict():
    """
    Проверка работы функции show_fruits_info() при вводе данных некорректного типа
    """
    fruits_quantity = {"яблоко": 5, "банан": 10, "апельсин": 7}
    fruits_prices = ""
    expected = []
    assert expected == show_fruits_info(fruits_quantity, fruits_prices)

############################################################################################
# show_squares_while (1)
############################################################################################

def test_show_squares_while():
    """
    Проверка работы функции show_squares_while() при вводе корректных данных
    """
    expected = [1, 4, 9, 16]
    assert expected == show_squares_while()

############################################################################################
# get_value_from_user (4)
############################################################################################

def test_get_value_from_user_correct_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 10)
    assert get_value_from_user(7) == True

def test_get_value_from_user_incorrect_input(monkeypatch): #ересь, но ничего лучше не придумала...
    i = 10
    j = 11
    while i <= j:
        try:
            monkeypatch.setattr('builtins.input', lambda x: i)
            assert get_value_from_user(j) == True
        except RecursionError:
            i += 1

def test_get_value_from_user_non_int_threshold(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 10)
    assert get_value_from_user('7') == False

def test_get_value_from_user_non_int_input(monkeypatch): # странные тесты на странную функцию...)
    i = ''
    j = 7
    k = 0
    while i == '' or i <= j:
        try:
            monkeypatch.setattr('builtins.input', lambda x: i)
            assert get_value_from_user(j) == True
        except RecursionError:
            i = 6 + k
        k += 1
















