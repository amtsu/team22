from some_func_hw5 import is_palindrome, great_com_divide, is_leap2, is_correct_date, show_fruits_info, show_squares_while, get_value_from_user

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
# get_value_from_user ()
############################################################################################

def test_get_value_from_user_correct_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 10)
    assert get_value_from_user(7) == True

def test_get_value_from_user_incorrect_input(monkeypatch): #ересь, но ничего лучше не придумала...
    i = 10
    j = 11
    while i <= j:
        try:
            monkeypatch.setattr('builtins.input', lambda _: i)
            assert get_value_from_user(j) == True
        except RecursionError:
            i += 1

def test_get_value_from_user_non_int_threshold(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 10)
    assert get_value_from_user('7') == False

def test_get_value_from_user_non_int_input(monkeypatch): # странные тесты на странную функцию...)
    i = ''
    j = 7
    k = 0
    while i == '' or i <= j:
        try:
            monkeypatch.setattr('builtins.input', lambda _: i)
            assert get_value_from_user(j) == True
        except RecursionError:
            i = 6 + k
        k += 1
















