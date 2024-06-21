import pytest
from func import (set_union, set_subset, set_remove, set_same, sets_disjoint, sets_symm_diff, dicts_union, dict_max, compare_sets_length, even_or_no, visokos_age, palindrom_li, period_time, prime_number, only_letters, whats_the_day, print_squares_while, factorial, sum_numb, all_prime_numbers, pal_li, nod, same_symbol, correct_date)

#тесты для функции объединения двух множеств
def test_set_union_1():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    assert set_union(set1, set2) == {1, 2, 3, 4, 5, 6, 7, 8}

def test_set_union_2(): #запишем другие множества
    set1 = {1, 2, 3}
    set2 = {6, 7, 8}
    assert set_union(set1, set2) == {1, 2, 3, 6, 7, 8}

def test_set_union_3(): #множества тождественны друг другу
    set1 = {1, 2, 3}
    set2 = {1, 2, 3}
    assert set_union(set1, set2) == {1, 2, 3}


#====================================================

#Тестируем функцию для проверки, является ли одно множество подмножеством другого.
def test_set_subset_1(): #сначала протестируем разные множества, одно не входит в другое
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    assert set_subset(set1, set2) == False

def test_set_subset_2(): #теперь проверим тождественные множества
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 3, 4, 5}
    assert set_subset(set1, set2) == True

def test_set_subset_3(): #первое множество включает в себя второе множество
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 3}
    assert set_subset(set1, set2) == True

def test_set_subset_4(): #второе множество включает в себя первое множество
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 3, 4, 5, 6}
    assert set_subset(set1, set2) == False

#====================================================

#Тестируем функцию для удаления конкретного элемента из множества.
def test_set_remove_1(): #удаляем один из элементов
    set1 = {1, 2, 3, 4, 5}
    assert set_remove(set1, 2) == {1, 3, 4, 5}

def test_set_remove_2(): #пробуем удалить элемент, которого нет во множжестве, метод discard() позволяет
    set1 = {1, 2, 3, 4, 5}
    assert set_remove(set1, 8) == {1, 2, 3, 4, 5}

def test_set_remove_3(): #пробуем удалить элемент из множества, где все элементы другого типа
    set1 = {'a', 'b', 4.5, 1.1}
    assert set_remove(set1, 8) == {'a', 'b', 4.5, 1.1}

#====================================================

#Тестируем функцию на проверку равенства двух множеств

def test_set_same_1(): #одно множество будет подмножеством другого
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 3, 4, 5, 6}
    assert set_same(set1, set2) == False

def test_set_same_2(): #возьмём два одинаковых множества
    set1 = {1, 2, 3, 4, 5}
    set2 = {1, 2, 3, 4, 5}
    assert set_same(set1, set2) == True
    
def test_set_same_3(): #одно множество пустое
    set1 = {1, 2, 3, 4, 5}
    set2 = set()
    assert set_same(set1, set2) == False

def test_set_same_4(): #возьмём два одинаковых множества с разными типами данных
    set1 = {1, 2, 3.1, 4.2, 'a', 'b'}
    set2 = {1, 2, 3.1, 4.2, 'a', 'b'}
    assert set_same(set1, set2) == True

#====================================================

#Тестируем функцию для проверки, являются ли два множества дизъюнктными (не имеют общих элементов).
def test_sets_disjoint_1(): #возьмём два множества, не имеющих общих элементов
    set1 = {1, 2, 3, 4, 5}
    set2 = {6, 7, 8, 9, 10}
    assert sets_disjoint(set1, set2) == True

def test_sets_disjoint_2(): #возьмём два множества, имеющих один общий элемент
    set1 = {1, 2, 3, 4, 5}
    set2 = {5, 6, 7, 8, 9}
    assert sets_disjoint(set1, set2) == False

def test_sets_disjoint_3(): #возьмём два одинаковых множества с разным типом данных
    set1 = {1, 2, 3.1, 4.2, 'a', 'b'}
    set2 = {1, 2, 3.1, 4.2, 'a', 'b'}
    assert sets_disjoint(set1, set2) == False

def test_sets_disjoint_4(): #возьмём два пустых множества
    set1 = set()
    set2 = set()
    assert sets_disjoint(set1, set2) == True

#====================================================

#Тестируем функцию для определения симметрической разности двух множеств.
def test_sets_symm_diff_1(): #возьмём два персекающихся множества
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    assert sets_symm_diff(set1, set2) == {1, 2, 6, 7}

def test_sets_symm_diff_2(): #возьмём два не пересекающихся множества с разными типами данных
    set1 = {1, 2, 3.3, 4.4, 'a'}
    set2 = {6, 7, 3.4, 4.5, 'b'}
    assert sets_symm_diff(set1, set2) == {1, 2, 3.3, 4.4, 'a', 6, 7, 3.4, 4.5, 'b'}

def test_sets_symm_diff_3(): #возьмём два одинаковых множества
    set1 = {1, 2, 3.3, 4.4, 'a'}
    set2 = {1, 2, 3.3, 4.4, 'a'}
    assert sets_symm_diff(set1, set2) == set()

#====================================================

#СЛОВАРИ
#Тестируем функцию для объединения двух словарей.
def test_dicts_union_1(): #возьмём два словаря с разными ключами и значениями
    dict1 = {'Petrov': 'fat', 'Ivanov': 'hungry'}
    dict2 = {'Sidorov': 'angry', 'Jukov': 'happy'}
    assert dicts_union(dict1, dict2) == {'Petrov': 'fat', 'Ivanov': 'hungry', 'Sidorov': 'angry', 'Jukov': 'happy'}

def test_dicts_union_2(): #возьмём одинаковые ключи в обоих словарях
    dict1 = {'Petrov': 'fat', 'Ivanov': 'hungry'}
    dict2 = {'Petrov': 'angry', 'Ivanov': 'happy'}
    assert dicts_union(dict1, dict2) == {'Petrov': 'angry', 'Ivanov': 'happy'}

def test_dicts_union_2(): #возьмём разные ключи, но одинаковые значения
    dict1 = {'Petrov': 'fat', 'Ivanov': 'hungry'}
    dict2 = {'Sidorov': 'fat', 'Jukov': 'hungry'}
    assert dicts_union(dict1, dict2) == {'Sidorov': 'fat', 'Jukov': 'hungry', 'Petrov': 'fat', 'Ivanov': 'hungry'}

#====================================================

#Тестируем функцию для поиска наибольшего значения в словаре.
def test_dict_max_1(): #берём словарь из предыдущей функции
    dict_sample = {'Petrov': 20, 'Ivanov': 10, 'Apolon': 500, 'Zeus': 1000}
    assert dict_max(dict_sample) == 1000

def test_dict_max_2(): #добавляем в словарь ключ с таким же значением, как у максимального
    dict_sample = {'Petrov': 20, 'Ivanov': 10, 'Apolon': 500, 'Zeus': 1000, 'Odin': 1000}
    assert dict_max(dict_sample) == 1000

def test_dict_max_3(): #проверяем отрицательные значения
    dict_sample = {'Petrov': 20, 'Ivanov': 10, 'Apolon': -500, 'Zeus': -1000, 'Odin': -1000}
    assert dict_max(dict_sample) == 20

#====================================================

#Тестируем функцию compare_sets_length, которая сравнивает длину двух множеств и выводит информацию о  том, какое из множеств длиннее.
def test_compare_sets_length_1(): #возьмём два множества одной длины
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    assert compare_sets_length(set1, set2) == 'same length'

def test_compare_sets_length_2(): #первое множество длиннее второго
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}
    assert compare_sets_length(set1, set2) == 'set1 longer'

def test_compare_sets_length_3(): #второе множество длиннее первого
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8, 9}
    assert compare_sets_length(set1, set2) == 'set2 longer'

def test_compare_sets_length_4(): #оба множества пустые
    set1 = set()
    set2 = set()
    assert compare_sets_length(set1, set2) == 'same length'

#====================================================

#Тестируем функцию для определения четности или нечетности числа.
def test_even_or_no_1(): #берём значение n равное 10
    n = 10
    assert even_or_no(n) == 'n is even'

def test_even_or_no_2(): #берём нечётное число
    n = 11
    assert even_or_no(n) == 'n is no even'

def test_even_or_no_3(): #берём отрицательное нечётное число
    n = -11
    assert even_or_no(n) == 'n is no even'

#====================================================

#Тестируем функцию для определения високосного года.
def test_visokos_age_1(): # возьмём чётное число, которое даёт остаток при делении на 4
    age = 1998
    assert visokos_age(age) == False

def test_visokos_age_2(): # возьмём нечётное число
    age = 2001
    assert visokos_age(age) == False

def test_visokos_age_3(): # возьмём чётное число, которое делится на 4 без остатка
    age = 2004
    assert visokos_age(age) == True

#====================================================

#Тестируем функцию для проверки, является ли строка палиндромом.
def test_palindrom_li_1(): #введём слово, являющееся палиндромом
    sentence = 'Казак'
    assert palindrom_li(sentence) == True

def test_palindrom_li_2(): #введём предложение, являющееся палиндромом
    sentence = 'А роза упала на лапу Азора'
    assert palindrom_li(sentence) == True

def test_palindrom_li_3(): #введём набор цифр и символов, являющееся палиндромом
    sentence = '123 __.. ..__ 321'
    assert palindrom_li(sentence) == True

def test_palindrom_li_4(): #введём предложение, не являющееся палиндромом
    sentence = 'Рука ногу моет'
    assert palindrom_li(sentence) == False

#====================================================

# Тестируем функцию для определения времени суток по введенному времени (утро, день, вечер, ночь).
def test_period_time_1(): #введём дневное время
    time = '16:30'
    assert period_time(time) == 'day'

def test_period_time_2(): #введём утреннее время
    time = '9:30'
    assert period_time(time) == 'morning'

def test_period_time_3(): #введём ночное время
    time = '0:30'
    assert period_time(time) == 'night'

def test_period_time_4(): #введём вечернее время
    time = '21:00'
    assert period_time(time) == 'evening'

#====================================================

#Тестируем функцию, которая определяет, является ли введенное число простым.
def test_prime_number_1(): #введём простое число
    n = 7
    assert prime_number(n) == 'n is prime number'

def test_prime_number_2(): #введём чётное число
    n = 18
    assert prime_number(n) == 'n is not prime number'

def test_prime_number_3(): #введём единицу
    n = 1
    assert prime_number(n) == 'n is prime number'

#====================================================

#Тестируем функцию для проверки входящей строки на наличие только буквенных символов.
def test_only_letters_1(): #тестируем предложение без знаков препинания и цифр
    s = 'Gremlin from Kremlin'
    assert only_letters(s) == 'string s has NOT only letters'

def test_only_letters_2(): #тестируем предложение со знаками препинания
    s = 'Veni, vedi, vici'
    assert only_letters(s) == 'string s has NOT only letters'

def test_only_letters_3(): #тестируем предложение с цифрами
    s = '100 gramm shot of whiskey'
    assert only_letters(s) == 'string s has NOT only letters'

def test_only_letters_4(): #тестируем слово без пробелов
    s = 'Abrakadabra'
    assert only_letters(s) == 'string s has only letters'

#====================================================

#Тестируем функцию для определения дня недели по введенному номеру дня (1 - Понедельник, 2 - Вторник и т.д.)
def test_whats_the_day_1(): #Понедельник - день тяжёлый)
    n = 1
    day_of_the_week = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}
    assert whats_the_day(day_of_the_week, n) == 'Понедельник'

def test_whats_the_day_2(): #Проверим субботу
    n = 6
    day_of_the_week = {1: 'Понедельник', 2: 'Вторник', 3: 'Среда', 4: 'Четверг', 5: 'Пятница', 6: 'Суббота', 7: 'Воскресенье'}
    assert whats_the_day(day_of_the_week, n) == 'Суббота'

#====================================================

#Тестируем функцию print_squares_while, которая использует цикл while для вывода квадратов чисел от 1 до 5.
def test_print_squares_while():
    n = 1
    assert print_squares_while(n) == [1, 4, 9, 16, 25]

#====================================================

#Тестируем функцию для вывода факториала заданного числа.
def test_factorial_1(): #считаем факториал от 5
    n = 5
    fact = 1
    assert factorial(n, fact) == 120

def test_factorial_2(): #считаем факториал от 10
    n = 10
    fact = 1
    assert factorial(n, fact) == 3628800

#====================================================

#Тестируем функцию для поиска суммы чисел в заданном диапазоне.
def test_sum_numb_1(): #возьмём значение x больше, чем значение y
    x = 10
    y = 5
    sum = 0
    assert sum_numb(x, y, sum) == 45

def test_sum_numb_2(): #возьмём значение x отрицательное и меньше, чем значение y
    x = -5
    y = 5
    sum = 0
    assert sum_numb(x, y, sum) == 0

def test_sum_numb_3(): #возьмём равные значения x и y
    x = -5
    y = -5
    sum = 0
    assert sum_numb(x, y, sum) == -5

#====================================================

#Тестируем функцию для генерации и вывода всех простых чисел до заданного числа.
def test_all_prime_numbers_1(): #возьмём n равное 10
    n = 10
    assert all_prime_numbers(n) == [1, 2, 3, 5, 7]

def test_all_prime_numbers_2(): #возьмём n равное 20
    n = 20
    assert all_prime_numbers(n) == [1, 2, 3, 5, 7, 11, 13, 17, 19]

#====================================================

#Тестируем функцию для проверки строки на палиндромность без учёта регистра и знаков препинания.
def test_pal_li_1(): #добавим знаки препинания в палиндром
    s = 'А - роза - упала - на - лапу - Азора'
    assert pal_li(s) == True

def test_pal_li_2(): #добавим знаки препинания и числа в палиндром
    s = 'А - роза 12 - упала - на - лапу - 21 Азора'
    assert pal_li(s) == True

def test_pal_li_3(): #проверим не палиндромное предложение
    s = 'Fat bastard gonna eat your food'
    assert pal_li(s) == False

def test_pal_li_4(): #проверим строку только из знаков препинания
    s = '.-. --===-- .-.'
    assert pal_li(s) == True

#====================================================

#Тестируем функцию для поиска наибольшего общего делителя (НОД) двух чисел.
def test_nod_1(): #введём два числа, имеющих общий делитель
    n = 10
    m = 15
    assert nod(n, m) == 5

def test_nod_2(): #введём два числа, не имеющих общий делитель больший 1
    n = 7
    m = 9
    assert nod(n, m) == 1

def test_nod_3(): #введём единицу и число больше 1
    n = 1
    m = 9
    assert nod(n, m) == 1

#====================================================

#Тестируем функцию, которая будет проверять введенную пользователем строку на наличие повторяющихся символов.
def test_same_symbol_1(): #введём слово с повторяющимися символами
    s = 'Abracadabra'
    assert same_symbol(s) == {'a', 'b', 'r'}

def test_same_symbol_2(): #введём предложение с повторяющимися символами
    s = 'Abracadabra 100 == 200 == 300'
    assert same_symbol(s) == {'a', 'b', 'r', ' ', '0', '='}

def test_same_symbol_3(): #введём слово без повторяющихся символов
    s = "What's up"
    assert same_symbol(s) == set()

#====================================================

#Тестируем функцию, которая определяет, является ли введенная дата корректной.
def test_correct_date_1(): #введём любую корректную дату
    date = '1.1.2021'
    assert correct_date(date) == True

def test_correct_date_2(): #введём некорректную дату
    date = '31.2.2021'
    assert correct_date(date) == False

def test_correct_date_3(): #введём дату неправильным образом
    date = '31 января 2021'
    assert correct_date(date) == False

#====================================================


