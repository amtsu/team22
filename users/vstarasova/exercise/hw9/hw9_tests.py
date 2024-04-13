import pytest
from hw9_functions import (set_union, set_difference, set_subset, setunion, remove_union, set_same, sets_disjoint, sets_symm_diff, dicts_union, dict_max, compare_sets_length, even_or_no, visokos_age, palindrom_li, period_time, prime_number, only_letters, whats_the_day, print_squares_while, factorial, sum_numb, all_prime_numbers, pal_li, nod, same_symbol, correct_date)
#-------------------------------------------
# тесты для функций объединения и разности множеств.
#-------------------------------------------
def test_set_union_1():
   #  тестируем объединение числовых множеств
    set1 = {1, 3, 3, 4, 5, 6}
    set2 = {4, 5, 6, 7, 8}
    expected = {1, 3, 4, 5, 6, 7, 8}
    assert set_union(set1,set2) == expected, 'Функция объединения множеств работает неправильно'
#-------------------------------------------
def test_set_union_2():
    #  тестируем объединение буквенных множеств
    set1 = {'a','b','c','d'}
    set2 = {'c','d','e','f'}
    expected = {'a','b','c','d','e','f'}
    assert set_union(set1,set2) == expected, 'Функция объединения множеств работает неправильно'
#------------------------------------------- 
def test_set_union_3():
   #  тестируем объединение пустых множеств
    set1 = {}
    set2 = {}
    expected = {}
    assert set_union(set1,set2) == expected, 'Функция объединения множеств работает неправильно'
#-------------------------------------------
def test_set_union_4(): 
#   множества равны
    set1 = {1, 2, 3}
    set2 = {1, 2, 3}
    assert set_union(set1, set2) == {1, 2, 3}
#-------------------------------------------    
def test_set_difference_1():
    #  тестируем разность множеств
    set1 = {1, 3, 3, 4, 5, 6}
    set2 = {4, 5, 6, 7, 8}
    expected = {1, 2}
    assert set_difference(set1,set2) == expected, 'Функция разности множеств работает неправильно'
#-------------------------------------------
def test_set_difference_2():
    #   тестируем разность множеств
    set1 = {}
    set2 = {}
    expected = {}
    assert set_difference(set1,set2) == expected, 'Функция разности множеств работает неправильно'
#-------------------------------------------
# тесты для функции определения подмножества 
#-------------------------------------------
def test_set_subset1():
    # множества не равны и не входят одно в другое
    set1 = {1, 2, 3, 4, 5}
    set2 = {8, 5, 6, 7, 9}
    assert set_subset(set1, set2) == False
#-------------------------------------------
def test_set_subset_2(): 
    # множества равны
    set1 = {1, 2, 3}
    set2 = {1, 2, 3}
    assert set_subset(set1, set2) == True

def test_set_subset_3(): 
    # первое множество включает в себя второе множество
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 3}
    assert set_subset(set1, set2) == True
#-------------------------------------------
def test_set_subset_4(): 
    # второе множество включает в себя первое множество
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 3, 4, 5, 6}
    assert set_subset(set1, set2) == False
#-------------------------------------------
# тесты для функции объединения нескольких множеств.
#-------------------------------------------
def test_setunion_1():
    # три рандомных множества
    b = {1, 2, 3}
    c = {4, 5, 7}
    d = {8, 5, 9}
    assert setunion(a,b,c) == {1, 2, 3, 4, 5, 7, 8, 9}
#-------------------------------------------
def test_setunion_2():
    # три рандомных множества, одно из которых пустое
    b = {1, 2, 3}
    c = {'a', 5, 7}
    d = {}
    assert setunion(a,b,c) == {1, 2, 3, 'a', 5, 7}
#-------------------------------------------
# тесты для функции удаления конкретного элемента из множества
#-------------------------------------------
def test_remove_union():
    # Тестирование удаления элемента из пустого множества
    assert remove_union(set(), 1) == set()

    # Тестирование удаления элемента, который отсутствует в множестве
    assert remove_union({1, 2, 3}, 4) == {1, 2, 3}

    # Тестирование удаления элемента из множества, где он присутствует
    assert remove_union({1, 2, 3}, 2) == {1, 3}

    # Тестирование удаления элемента из множества с одним элементом
    assert remove_union({5}, 5) == set()

    # Тестирование удаления элемента из множества с несколькими элементами
    assert remove_union({5, 6, 7, 8}, 7) == {5, 6, 8}

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции для проверки на равенство двух множеств
#-------------------------------------------
def test_set_same():
    # Тестирование равенства двух пустых множеств
    assert set_same(set(), set()) == True

    # Тестирование неравенства пустого множества и непустого множества
    assert set_same(set(), {1, 2, 3}) == False

    # Тестирование равенства непустых множеств
    assert set_same({1, 2, 3}, {1, 2, 3}) == True

    # Тестирование неравенства множеств с разными элементами
    assert set_same({1, 2, 3}, {3, 4, 5}) == False

    # Тестирование неравенства множеств с одинаковыми элементами, но в разном порядке
    assert set_same({1, 2, 3}, {3, 2, 1}) == False

    # Тестирование равенства множеств с разными типами элементов
    assert set_same({1, 'a', True}, {True, 'a', 1}) == True

    # Тестирование неравенства множеств разной длины
    assert set_same({1, 2, 3}, {1, 2, 3, 4}) == False

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции для проверки на равенство двух множеств
#-------------------------------------------
def test_set_same():
    # Тестирование равенства двух пустых множеств
    assert set_same(set(), set()) == True

    # Тестирование неравенства пустого множества и непустого множества
    assert set_same(set(), {1, 2, 3}) == False

    # Тестирование равенства непустых множеств
    assert set_same({1, 2, 3}, {1, 2, 3}) == True

    # Тестирование неравенства множеств с разными элементами
    assert set_same({1, 2, 3}, {3, 4, 5}) == False

    # Тестирование неравенства множеств с одинаковыми элементами, но в разном порядке
    assert set_same({1, 2, 3}, {3, 2, 1}) == True

    # Тестирование равенства множеств с разными типами элементов
    assert set_same({1, 'a', True}, {True, 'a', 1}) == True

    # Тестирование неравенства множеств разной длины
    assert set_same({1, 2, 3}, {1, 2, 3, 4}) == False

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции проверки, являются ли два множества дизъюнктными (не имеют общих элементов)
#-------------------------------------------
def test_sets_disjoint():
    # Тестирование непересекающихся множеств
    assert sets_disjoint({1, 2, 3}, {4, 5, 6}) == True

    # Тестирование пересекающихся множеств
    assert sets_disjoint({1, 2, 3}, {3, 4, 5}) == False

    # Тестирование пустого множества с непустым множеством
    assert sets_disjoint(set(), {1, 2, 3}) == True

    # Тестирование непустого множества с пустым множеством
    assert sets_disjoint({1, 2, 3}, set()) == True

    # Тестирование двух пустых множеств
    assert sets_disjoint(set(), set()) == True

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции для определения симметрической разности двух множеств
#-------------------------------------------
def test_sets_symm_diff():
    # Тестирование симметрической разности двух пустых множеств
    assert sets_symm_diff(set(), set()) == set()

    # Тестирование симметрической разности пустого множества и непустого множества
    assert sets_symm_diff(set(), {1, 2, 3}) == {1, 2, 3}

    # Тестирование симметрической разности непустого множества и пустого множества
    assert sets_symm_diff({1, 2, 3}, set()) == {1, 2, 3}

    # Тестирование симметрической разности непустых множеств
    assert sets_symm_diff({1, 2, 3}, {3, 4, 5}) == {1, 2, 4, 5}

    # Тестирование симметрической разности множеств с одинаковыми элементами
    assert sets_symm_diff({1, 2, 3}, {3, 2, 1}) == set()

    # Тестирование симметрической разности множеств с разными типами элементов
    assert sets_symm_diff({1, 'a', True}, {False, 'b', 2}) == {1, 2, 'a', 'b', True, False}

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции объединения двух словарей
#-------------------------------------------
def test_dicts_union():
    # Тестирование объединения двух пустых словарей
    assert dicts_union({}, {}) == {}

    # Тестирование объединения пустого словаря с непустым словарем
    assert dicts_union({}, {'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Тестирование объединения непустых словарей
    assert dicts_union({'a': 1, 'b': 2}, {'c': 3}) == {'a': 1, 'b': 2, 'c': 3}

    # Тестирование объединения словарей с одинаковыми ключами
    assert dicts_union({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 3, 'c': 4}

    # Тестирование объединения словарей с разными типами значений
    assert dicts_union({'a': 1, 'b': 2}, {'c': [1, 2, 3], 'd': {'x': 1, 'y': 2}}) == {'a': 1, 'b': 2, 'c': [1, 2, 3], 'd': {'x': 1, 'y': 2}}

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции поиска наибольшего значения в словаре
#-------------------------------------------
def test_dict_max():
    # Тестирование максимального значения в словаре со всеми положительными числами
    assert dict_max({'a': 10, 'b': 20, 'c': 30}) == 30

    # Тестирование максимального значения в словаре со всеми отрицательными числами
    assert dict_max({'a': -5, 'b': -10, 'c': -3}) == -3

    # Тестирование максимального значения в словаре со смешанными числами
    assert dict_max({'a': 100, 'b': -20, 'c': 50, 'd': -10}) == 100

    # Тестирование максимального значения в словаре с одним элементом
    assert dict_max({'a': 5}) == 5

    # Тестирование максимального значения в пустом словаре
    assert dict_max({}) == 0

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции compare_sets_length, которая сравнивает длину двух множеств и выводит информацию о  том, какое из множеств длиннее
#-------------------------------------------
def test_compare_sets_length():
    # Тестирование, когда первое множество длиннее второго
    assert compare_sets_length({1, 2, 3}, {1, 2}) == 'set1 longer'

    # Тестирование, когда второе множество длиннее первого
    assert compare_sets_length({1, 2}, {1, 2, 3}) == 'set2 longer'

    # Тестирование, когда оба множества имеют одинаковую длину
    assert compare_sets_length({1, 2, 3}, {4, 5, 6}) == 'same length'

    # Тестирование, когда оба множества пусты
    assert compare_sets_length(set(), set()) == 'same length'

    # Тестирование, когда одно из множеств пустое
    assert compare_sets_length({1, 2, 3}, set()) == 'set1 longer'
    assert compare_sets_length(set(), {1, 2, 3}) == 'set2 longer'

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции пределения четности или нечетности числа.
#-------------------------------------------
def test_even_or_no():
    # Тестирование четного числа
    assert even_or_no(4) == 'n is even'

    # Тестирование нечетного числа
    assert even_or_no(7) == 'n is no even'

    # Тестирование отрицательного четного числа
    assert even_or_no(-2) == 'n is even'

    # Тестирование отрицательного нечетного числа
    assert even_or_no(-5) == 'n is no even'

    # Тестирование нуля
    assert even_or_no(0) == 'n is even'

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции проверки, является ли строка палиндромом
#-------------------------------------------
def test_palindrom_li():
    # Тестирование палиндрома
    assert palindrom_li("A man a plan a canal Panama") == True

    # Тестирование не палиндрома
    assert palindrom_li("This is not a palindrome") == False

    # Тестирование пустой строки
    assert palindrom_li("") == True

    # Тестирование строки с одним символом
    assert palindrom_li("a") == True

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции определения времени суток по введенному времени (утро, день, вечер, ночь)
#-------------------------------------------
def test_period_time():
    # Тестирование времени в ночной период
    assert period_time('03:00') == 'night'

    # Тестирование времени в утренний период
    assert period_time('08:00') == 'morning'

    # Тестирование времени в дневной период
    assert period_time('15:00') == 'day'

    # Тестирование времени в вечерний период
    assert period_time('21:00') == 'evening'

    # Тестирование времени в начале дня (6:00)
    assert period_time('06:00') == 'morning'

    # Тестирование времени в конце дня (18:59)
    assert period_time('18:59') == 'day'

    # Тестирование времени в начале ночи (19:00)
    assert period_time('19:00') == 'evening'

    # Тестирование времени в конце ночи (5:59)
    assert period_time('05:59') == 'night'

    print("Все тесты пройдены успешно!")

#-------------------------------------------
#  тесты для функции которая определяет, является ли введенное число простым.
#-------------------------------------------
def test_prime_number():
    # Тестирование простого числа (5)
    assert prime_number(5) == 'n is prime number'

    # Тестирование составного числа (6)
    assert prime_number(6) == 'n is not prime number'

    # Тестирование простого числа (11)
    assert prime_number(11) == 'n is prime number'

    # Тестирование составного числа (15)
    assert prime_number(15) == 'n is not prime number'

    # Тестирование единицы (1)
    assert prime_number(1) == 'n is prime number'

    # Тестирование отрицательного числа (-7)
    assert prime_number(-7) == 'n is prime number'

    print("Все тесты пройдены успешно!")

#-------------------------------------------
#  тесты для функции проверки входящей строки на наличие только буквенных символов
#-------------------------------------------
def test_only_letters():
    # Тестирование строки, содержащей только буквы
    assert only_letters("abcdef") == 'string s has only letters'

    # Тестирование строки, содержащей буквы и пробелы
    assert only_letters("abc def") == 'string s has NOT only letters'

    # Тестирование строки, содержащей буквы и цифры
    assert only_letters("abc123") == 'string s has NOT only letters'

    # Тестирование пустой строки
    assert only_letters("") == 'string s has NOT only letters'

    # Тестирование строки, содержащей только пробелы
    assert only_letters("   ") == 'string s has NOT only letters'

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции которая использует цикл while для вывода квадратов чисел от 1 до 5.
#-------------------------------------------
def test_print_squares_while():
    # Тестирование для n = 1
    assert print_squares_while(1) == [1, 4, 9, 16, 25]

    # Тестирование для n = 0
    assert print_squares_while(0) == [0, 1, 4, 9, 16, 25]

    # Тестирование для n = 5
    assert print_squares_while(5) == [25]

    # Тестирование для n = 6 (выход за границы)
    assert print_squares_while(6) == []

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты функции для генерации и вывода всех простых чисел до заданного числа.
#-------------------------------------------
def test_all_prime_numbers():
    # Тестирование для n = 10
    assert all_prime_numbers(10) == [1, 2, 3, 5, 7]

    # Тестирование для n = 20
    assert all_prime_numbers(20) == [1, 2, 3, 5, 7, 11, 13, 17, 19]

    # Тестирование для n = 1
    assert all_prime_numbers(1) == []

    # Тестирование для n = 0
    assert all_prime_numbers(0) == []

    # Тестирование для n = -1 (недопустимое значение)
    assert all_prime_numbers(-1) == []

    print("Все тесты пройдены успешно!")

#-------------------------------------------
#  тесты для функции для проверки строки на палиндромность без учёта регистра и знаков препинания
#-------------------------------------------
def test_pal_li():
    # Тестирование палиндрома с буквами
    assert pal_li("A man, a plan, a canal, Panama") == True

    # Тестирование палиндрома с цифрами
    assert pal_li("12321") == True

    # Тестирование не палиндрома
    assert pal_li("This is not a palindrome") == False

    # Тестирование пустой строки
    assert pal_li("") == True

    # Тестирование строки с одним символом
    assert pal_li("a") == True

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции для поиска наибольшего общего делителя (НОД) двух чисел.
#-------------------------------------------
def test_nod():
    # Тестирование для чисел 12 и 18
    assert nod(12, 18) == 6

    # Тестирование для чисел 20 и 30
    assert nod(20, 30) == 10

    # Тестирование для чисел 8 и 12
    assert nod(8, 12) == 4

    # Тестирование для чисел 21 и 14
    assert nod(21, 14) == 7

    # Тестирование для чисел 5 и 7 (простые числа)
    assert nod(5, 7) == 1

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции которая будет проверять введенную пользователем строку на наличие повторяющихся символов.
#-------------------------------------------
def test_same_symbol():
    # Тестирование строки с одним повторяющимся символом
    assert same_symbol("hello") == {'l'}

    # Тестирование строки с несколькими повторяющимися символами
    assert same_symbol("hello world") == {'l', 'o'}

    # Тестирование строки без повторяющихся символов
    assert same_symbol("abcde") == set()

    # Тестирование пустой строки
    assert same_symbol("") == set()

    # Тестирование строки, состоящей из одного символа
    assert same_symbol("a") == set()

    print("Все тесты пройдены успешно!")
#-------------------------------------------
#  тесты для функции которая определяет, является ли введенная дата корректной
#-------------------------------------------
def test_correct_date():
    # Тестирование правильной даты (1 января)
    assert correct_date("1.1.2022") == True

    # Тестирование правильной даты (31 декабря)
    assert correct_date("31.12.2022") == True

    # Тестирование неправильной даты (31 февраля)
    assert correct_date("31.2.2022") == False

    # Тестирование неправильной даты (30 февраля)
    assert correct_date("30.2.2022") == False

    # Тестирование неправильной даты (29 февраля в невисокосном году)
    assert correct_date("29.2.2023") == False

    # Тестирование неправильной даты (31 апреля)
    assert correct_date("31.4.2022") == False

    # Тестирование неправильного формата даты (слишком короткая строка)
    assert correct_date("1.1") == False

    # Тестирование неправильного формата даты (слишком длинная строка)
    assert correct_date("1.1.2022.2023") == False

    # Тестирование неправильного формата даты (некорректные разделители)
    assert correct_date("1-1-2022") == False

    # Тестирование неправильного формата даты (дата за границами месяца)
    assert correct_date("32.1.2022") == False

    # Тестирование неправильного формата даты (месяц за границами года)
    assert correct_date("1.13.2022") == False

    print("Все тесты пройдены успешно!")







