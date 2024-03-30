from some_func_hw5 import is_palindrome, great_com_divide

# is_palindrome
def test_is_palindrome():
    """
    Проверка простой строки на палиндромность
    """
    input_data = "оно"
    expected = True
    assert expected == is_palindrome(input_data)

test_is_palindrome()

def test_is_palindrome_letter_case():
    """
    Проверка строки на палиндромность с учетом регистра
    """
    input_data = "А роза упала на лапу Азора"
    expected = True
    assert expected == is_palindrome(input_data)

test_is_palindrome_letter_case()

def test_is_palindrome_with_symbols():
    """
    Проверка строки на палиндромность с учетом дополнительных символов
    """
    input_data = "А роза упала$ на лапу Азора"
    expected = True
    assert expected == is_palindrome(input_data)

test_is_palindrome_with_symbols()

def test_is_palindrome_not():
    """
    Проверка строки на палиндромность (строка - не палиндром)
    """
    input_data = "абра-кадабра"
    expected = False
    assert expected == is_palindrome(input_data)

test_is_palindrome_not()

def test_is_palindrome_not_str():
    """
    Проверка на неверный тип аргумента
    """
    input_data = 2024
    expected = None
    assert expected == is_palindrome(input_data)

test_is_palindrome_not_str()

def test_is_palindrome_empty_str():
    """
    Проверка на передачу пустой строки в качестве аргумента
    """
    input_data = ""
    expected = False
    assert expected == is_palindrome(input_data)

test_is_palindrome_empty_str()

def test_is_palindrome_single_char():
    """
    Проверка на передачу пустой строки в качестве аргумента
    """
    input_data = "Я"
    expected = True
    assert expected == is_palindrome(input_data)

test_is_palindrome_single_char()


# great_com_divide

def test_great_com_divide_normal():
    """
    Проверка работоспособности great_com_divide() при нормальных условиях
    """
    input_data = [11,33]
    expected = 11
    assert expected == great_com_divide(*input_data)

test_great_com_divide_normal()

def test_great_com_divide_zero_1():
    """
    Проверка работы great_com_divide() при нулевом значении одного из параметров
    """
    input_data = [0,33]
    expected = None
    assert expected == great_com_divide(*input_data)

test_great_com_divide_zero_1()

def test_great_com_divide_zero_2():
    """
    Проверка работы great_com_divide() при нулевых значениях обоих параметров
    """
    input_data = [0,0]
    expected = None
    assert expected == great_com_divide(*input_data)

test_great_com_divide_zero_2()

def test_great_com_divide_neg_num_1():
    """
    Проверка работы great_com_divide() при отрицательном значении одного из параметров
    """
    input_data = [-10,20]
    expected = None
    assert expected == great_com_divide(*input_data)

test_great_com_divide_neg_num_1()

def test_great_com_divide_neg_num_2():
    """
    Проверка работы great_com_divide() при отрицательных значениях обоих параметров
    """
    input_data = [-10,-20]
    expected = None
    assert expected == great_com_divide(*input_data)

test_great_com_divide_neg_num_2()

def test_great_com_divide_incorect_input_1():
    """
    Проверка работы great_com_divide() при неверном типе введенных параметров
    """
    input_data = ["lala", 20]
    expected = None
    assert expected == great_com_divide(*input_data)

test_great_com_divide_incorect_input_1()

def test_great_com_divide_incorect_input_2():
    """
    Проверка работы great_com_divide() при неверном типе введенных параметров
    """
    input_data = ["11", 22]
    expected = None
    assert expected == great_com_divide(*input_data)

test_great_com_divide_incorect_input_2()


