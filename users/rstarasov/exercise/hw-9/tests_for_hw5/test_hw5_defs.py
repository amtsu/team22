# Материалы для использования в функциях:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {10, 11, 12}
set4 = {11, 12, 13}
fruits_quantity = {'яблоко': 5, 'банан': 10, 'апельсин': 7}
fruits_prices = {"яблоко": 1.5, "банан": 2, "апельсин": 1.2}

##################################################################################
# Функция объеденения множеств:
##################################################################################

from hw5_defs import set_union

def test_set_union():
    input_set3 = {10, 11, 12}
    input_set4 = {11, 12, 13}
    expected = {10, 11, 12, 13}
    assert expected == set_union(input_set3, input_set4)

def test_set_union_2():
    input_set1 = {1, 2, 3, 4, 5}
    input_set2 = {4, 5, 6, 7, 8}
    expected = {1, 2, 3, 4, 5, 6, 7, 8}
    assert expected == set_union(input_set1, input_set2)

##################################################################################
# Является ли одно множество подмножеством другого:
##################################################################################

from hw5_defs import is_subset

def test_is_subset():
    input_set1 = {1, 2, 3, 4, 5}
    input_set2 = {4, 5, 6, 7, 8}
    expected = False
    assert expected == is_subset(input_set1, input_set2)

def test_is_subset_2():
    input_set1 = {1, 2, 3, 4, 5}
    input_set5 = {1, 2, 3}
    expected = True
    assert expected == is_subset(input_set5, input_set1)

##################################################################################
# Создайте функцию для объединения нескольких множеств:
##################################################################################

from hw5_defs import many_unions

def test_many_unions():
    input_set1 = {1, 2, 3, 4, 5}
    input_set2 = {4, 5, 6, 7, 8}
    input_set3 = {10, 11, 12}
    expected = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12}
    assert expected == many_unions(input_set1, input_set3, input_set2)

def test_many_unions_2():
    input_set2 = {4, 5, 6, 7, 8}
    input_set3 = {10, 11, 12}
    input_set4 = {11, 12, 13}
    expected = {4, 5, 6, 7, 8, 10, 11, 12, 13}

##################################################################################
# Создайте функцию для удаления конкретного элемента из множества:
##################################################################################

from hw5_defs import del_set_element

def test_del_set_element():
    input_set1 = {1, 2, 3, 4, 5}
    input_element = 3
    expected = {1, 2, 4, 5}
    assert expected == del_set_element(input_set1, input_element)

def test_del_set_element_2():
    input_set2 = {4, 5, 6, 7, 8}
    input_element = 8
    expected = {4, 5, 6, 7}
    assert expected == del_set_element(input_set2, input_element)

##################################################################################
# Создайте функцию для проверки на равенство двух множеств:
##################################################################################

from hw5_defs import equality

def test_equality():
    input_set1 = {1, 2, 3, 4, 5}
    input_set2 = {4, 5, 6, 7, 8}
    expected = False
    assert expected == equality(input_set1, input_set2)

def test_equality_2():
    input_set3 = {10, 11, 12}
    input_set6 = {10, 11, 12}
    expected = True
    assert expected == equality(input_set3, input_set6)

##################################################################################
# Создайте функцию create_set для создания множества с заданными элементами:
##################################################################################

from hw5_defs import create_set

def test_create_set():
    expected = {3, 5, 23, 25, 92}
    assert expected == create_set(3, 5, 23, 25, 92)

##################################################################################
# Coздайте функцию create_dictionary для создания словаря с заданными ключами и значениями:
##################################################################################
    
from hw5_defs import create_dictionary

def test_create_dictionary():
    input_key = 'Ivan'
    input_value = 25
    expected = {'Ivan': 25}
    assert expected == create_dictionary(input_key, input_value)

##################################################################################
# Напишите функции add_student и remove_student для добавления и удаления студентов из словаря:
##################################################################################

from hw5_defs import add_student, remove_student

def test_add_student():
    input_dict = {'Mila': 23}
    input_student = 'Lexa'
    input_age = 19
    expected = {'Mila': 23, 'Lexa': 19}
    assert expected == add_student(input_dict, input_student, input_age)

def test_remove_student():
    input_dict = {'Mila': 23, 'Lexa': 19}
    input_student = 'Lexa'
    expected = {'Mila': 23}
    assert expected == remove_student(input_dict, input_student)

##################################################################################
# Напишите функции add_fruit и remove_fruit для добавления и удаления фруктов, их количества и стоимости в списки fruits_quantity и fruits_prices:
##################################################################################

from hw5_defs import add_fruit, remove_fruit

# Добавление фруктов:

def test_add_fruit():
    input_quantity_dict = {}
    input_price_dict = {}
    input_fruit = 'Apple'
    input_quantity = 5
    input_price = 1.1
    expected_quantity_dict = {'Apple': 5}
    expected_price_dict = {'Apple': 1.1}
    add_fruit(input_quantity_dict, input_price_dict, input_fruit, input_quantity, input_price)
    assert expected_quantity_dict == input_quantity_dict

def test_add_fruit_2():
    input_quantity_dict = {}
    input_price_dict = {}
    input_fruit = 'Apple'
    input_quantity = 5
    input_price = 1.1
    expected_quantity_dict = {'Apple': 5}
    expected_price_dict = {'Apple': 1.1}
    add_fruit(input_quantity_dict, input_price_dict, input_fruit, input_quantity, input_price)
    assert expected_price_dict == input_price_dict

def test_add_fruit_3():
    input_quantity_dict = {}
    input_price_dict = {}
    input_fruit = 'Apple'
    input_quantity = 5
    input_price = 1.1
    expected_quantity_dict = {'Apple': 5}
    expected_price_dict = {'Apple': 1.1}
    expected_all = ({'Apple': 5}, {'Apple': 1.1})
    assert expected_all == add_fruit(input_quantity_dict, input_price_dict, input_fruit, input_quantity, input_price)

# Удаление фруктов:

def test_remove_fruit():
    input_quantity_dict = {'Apple': 5, 'Banana': 12}
    input_price_dict = {'Apple': 1.1, 'Banana': 2.3}
    input_fruit = 'Apple'
    expected_quantity_dict = {'Banana': 12}
    expected_price_dict = {'Banana': 2.3}
    remove_fruit(input_quantity_dict, input_price_dict, input_fruit)
    assert expected_quantity_dict == input_quantity_dict

def test_remove_fruit_2():
    input_quantity_dict = {'Apple': 5, 'Banana': 12}
    input_price_dict = {'Apple': 1.1, 'Banana': 2.3}
    input_fruit = 'Apple'
    expected_quantity_dict = {'Banana': 12}
    expected_price_dict = {'Banana': 2.3}
    remove_fruit(input_quantity_dict, input_price_dict, input_fruit)
    assert expected_price_dict == input_price_dict

def test_remove_fruit_3():
    input_quantity_dict = {'Apple': 5, 'Banana': 12}
    input_price_dict = {'Apple': 1.1, 'Banana': 2.3}
    input_fruit = 'Apple'
    expected_quantity_dict = {'Banana': 12}
    expected_price_dict = {'Banana': 2.3}
    expected_all = ({'Banana': 12}, {'Banana': 2.3})
    assert expected_all == remove_fruit(input_quantity_dict, input_price_dict, input_fruit)

##################################################################################
# Создайте функцию для объединения двух словарей:
##################################################################################

from hw5_defs import dict_union

def test_dict_union():
    input_dict1 = {'Ivan': 25}
    input_dict2 = {'Anton': 30}
    expected = {'Ivan': 25, 'Anton': 30}
    assert expected == dict_union(input_dict1, input_dict2)

##################################################################################
# Создайте функцию для удаления элемента из словаря по заданному ключу:
##################################################################################

from hw5_defs import element_del

def test_element_del():
    input_dict = {'Ivan': 25, 'Anton': 30}
    input_del = 'Anton'
    expected = {'Ivan': 25}
    assert expected == element_del(input_dict, input_del)

##################################################################################
# Создайте функцию для переворачивания значений и ключей в словаре:
##################################################################################

from hw5_defs import change_key_to_value

def test_change_key_to_value():
    input_dict = {'Ivan': 25, 'Anton': 30}
    expected = {25: 'Ivan', 30: 'Anton'}
    assert expected == change_key_to_value (input_dict)

##################################################################################
# Создайте функцию для сортировки словаря по ключам в обратном порядке:
##################################################################################

from hw5_defs import sort_reversed

def test_sort_reversed():
    input_dict = {5: 'яблоко', 10: 'банан', 7: 'апельсин', 13: 'дыня'}
    expected = {13: 'дыня', 10: 'банан', 7: 'апельсин', 5: 'яблоко'}
    assert expected == sort_reversed (input_dict)

##################################################################################
# Создайте функцию возвращающую наибольшее значение элемента словаря:
##################################################################################

from hw5_defs import biggest

def test_biggest():
    input_dict = {'яблоко': 1.5, 'банан': 2, 'апельсин': 1.2, 'дыня': 1.1}
    expected = [2, 'банан']
    assert expected == biggest (input_dict)

##################################################################################
# Создайте функцию check_fruit_price для проверки стоимости фрукта и вывода соответствующего сообщения:
##################################################################################

from hw5_defs import check_fruit_price

def test_check_fruit_price():
    input_dict = {'яблоко': 1.5, 'банан': 2, 'апельсин': 1.2, 'дыня': 1.1}
    input_fruit = 'банан'
    expected = 'дорогой товар'
    assert expected == check_fruit_price(input_dict, input_fruit)

##################################################################################
# Создайте функцию check_age для проверки возраста студента и вывода соответствующего сообщения:
##################################################################################

from hw5_defs import check_age

def test_check_age():
    input_dict = {'Victor': 21, 'Nikolay': 26, 'Nina': 18, 'Tasya': 20, 'Ivan': 17}
    input_name = 'Ivan'
    expected = 'Несовершеннолетний'
    assert expected == check_age(input_dict, input_name)

def test_check_age_2():
    input_dict = {'Victor': 21, 'Nikolay': 26, 'Nina': 18, 'Tasya': 20, 'Ivan': 17}
    input_name = 'Victor'
    expected = 'Совершеннолетний'
    assert expected == check_age(input_dict, input_name)

##################################################################################
# Создайте функцию compare_sets_length, которая сравнивает длину двух множеств и выводит информацию о том, какое из множеств длиннее:
##################################################################################

from hw5_defs import compare_sets_length

def test_compare_sets_length():
    input_set1 = {1, 2, 3, 4, 5}
    input_set2 = {4, 5, 7, 8}
    expected = 'Первое множество больше второго'
    assert expected == compare_sets_length(input_set1, input_set2)

def test_compare_sets_length_2():
    input_set1 = {4, 5, 7, 8}
    input_set2 = {1, 2, 3, 4, 5}
    expected = 'Первое множество меньше второго'
    assert expected == compare_sets_length(input_set1, input_set2)

##################################################################################
# Создайте функцию для определения четности или нечетности числа:
##################################################################################

from hw5_defs import even_odd_number

def test_even_odd_number():
    input = 10
    expected = 'Четное'
    assert expected == even_odd_number(input)

##################################################################################
# Создайте функцию для определения високосного года. Функция должна принимать на вход год в виде числа и возвращать строку "високосный" или "обычный":
##################################################################################

from hw5_defs import leap_year

def test_leap_year():
    input_year = 2024
    expected = True
    assert expected == leap_year(input_year)

def test_leap_year_2():
    input_year = 2023
    expected = False
    assert expected == leap_year(input_year)

##################################################################################
# Создайте функцию для проверки, является ли строка палиндромом:
##################################################################################

from hw5_defs import palindrom

def test_palindrom():
    input_word = 'anna'
    expected = 'Это палиндром'
    assert expected == palindrom(input_word)

def test_palindrom_2():
    input_word = 'Nana'
    expected = 'Это не палиндром'
    assert expected == palindrom(input_word)

##################################################################################
# Создайте функцию для определения времени суток по введенному времени:
##################################################################################

from hw5_defs import time_of_day

def test_time_of_day():
    input_hours = 20
    input_minuts = 45
    expected = 'вечер'
    assert expected == time_of_day(input_hours, input_minuts)

##################################################################################
# Создайте функцию, которая определяет, является ли введенное число простым:
##################################################################################

from hw5_defs import prime_number

def test_prime_number():
    input_number = 13
    expected = 'prime'
    assert expected == prime_number(input_number)

def test_prime_number_2():
    input_number = 10
    expected = 'not prime'
    assert expected == prime_number(input_number)

##################################################################################
# Создайте функцию для проверки входящей строки на наличие только буквенных символов:
##################################################################################

from hw5_defs import isalfa_string

def test_isalfa_string():
    input_string = 'wsdefrg'
    expected = 'Только буквы'
    assert expected == isalfa_string(input_string)

def test_isalfa_string_2():
    input_string = 'wsdefrg1234'
    expected = 'Не только буквы'
    assert expected == isalfa_string(input_string) 

##################################################################################
# Создайте функцию, которая определяет, является ли введенная дата корректной:
##################################################################################

from hw5_defs import check_date

def test_check_date():
    input_day = 13
    input_month = 12
    input_year = 2023
    expected = True
    assert expected == check_date(input_day, input_month, input_year)

##################################################################################
# Создайте функцию, которая определяет, является ли введенное число палиндромом:
##################################################################################

from hw5_defs import palindrom_number

def test_palindrom_number():
    input_number = 123321
    expected = 'Палиндром'
    assert expected == palindrom_number(input_number)

def test_palindrom_number_2():
    input_number = 2225543
    expected = 'Неа'
    assert expected == palindrom_number(input_number)

##################################################################################
# Создайте функцию для определения дня недели по введенному номеру дня:
##################################################################################

from hw5_defs import day_counter

def test_day_counter():
    input_day = 2
    expected = 'вторник'
    assert expected == day_counter(input_day)

def test_day_counter_2():
    input_day = 9
    expected = 'вторник'
    assert expected == day_counter(input_day)

##################################################################################
# Создайте функцию для вывода факториала заданного числа:
##################################################################################

from hw5_defs import factorial

def test_factorial():
    input_number = 6 
    expected = 720
    assert expected == factorial(input_number)

def test_factorial_2():
    input_number = 4
    expected = 24
    assert expected == factorial(input_number)

##################################################################################
# Создайте функцию для поиска суммы чисел в заданном диапазоне:
##################################################################################

from hw5_defs import sum_between

def test_sum_between():
    input_first_number = 5
    input_second_number = 10
    expected = 45
    assert expected == sum_between (input_first_number, input_second_number)

def test_sum_between_2():
    input_first_number = 6
    input_second_number = 5
    expected = 'Первое число должно быть меньше второго'
    assert expected == sum_between (input_first_number, input_second_number)

##################################################################################
# Создайте функцию для генерации и вывода всех простых чисел до заданного числа:
##################################################################################

from hw5_defs import every_prime_inrange

def test_every_prime_inrange():
    input_first = 14
    input_second = 150
    expected = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
    assert expected == every_prime_inrange (input_first, input_second)

##################################################################################
# Создайте функцию для проверки строки на палиндромность без учёта регистра и знаков препинания:
##################################################################################

from hw5_defs import ultra_palindrom

def test_ultra_palindrom():
    input_palindrom = 'Он — верба, но / Она — бревно'
    expected = 'Палиндром'
    assert expected == ultra_palindrom (input_palindrom)

def test_ultra_palindrom():
    input_palindrom = 'Он — верб, но / Она — ревно'
    expected = 'Не палиндром'
    assert expected == ultra_palindrom (input_palindrom)

##################################################################################
# Создайте функцию для поиска наибольшего общего делителя (НОД) двух чисел:
##################################################################################

from hw5_defs import nod

def test_nod():
    input_a = 6
    input_b = 4
    expected = 2
    assert expected == nod (input_a, input_b)
    
def test_nod_2():
    input_a = 4
    input_b = 7
    expected = 1
    assert expected == nod (input_a, input_b)
    
##################################################################################
# Создайте функцию print_students для вывода информации о студентах из словаря:
##################################################################################

from hw5_defs import students_age

def test_students_age():
    input_dict =  {'Victor': 21, 'Olga': 25, 'Nikolay': 26, 'Nina': 18, 'Tasya': 20, 'Ivan': 17}
    expected = [('Victor', 21), ('Olga', 25), ('Nikolay', 26), ('Nina', 18), ('Tasya', 20), ('Ivan', 17)]
    assert expected == students_age (input_dict)

##################################################################################
# Создайте функцию print_students для вывода информации о студентах из словаря:
##################################################################################

from hw5_defs import get_value_from_user

def test_get_value_from_user():
    input_floor = 5
    input_number = 6
    expected = True
    assert expected == get_value_from_user (input_floor, input_number)

def test_get_value_from_user_2():
    input_floor = 10
    input_number = 4
    expected = 'Число должно быть больше порога', 10
    assert expected == get_value_from_user (input_floor, input_number)

##################################################################################
# Создайте функцию, которая будет запрашивать у пользователя его возраст:
##################################################################################

from hw5_defs import show_me_your_age

def test_show_me_your_age():
    input_age = 102
    expected = 'Ультрапенсионер'
    assert expected == show_me_your_age(input_age)

##################################################################################
# Создайте функцию, которая будет проверять введенную пользователем строку на наличие повторяющихся символов:
##################################################################################

from hw5_defs import repeat_simbols

def test_repeat_simbols():
    input_string = 'string of nothing gggg'
    expected = {'t': 2, 'i': 2, 'n': 3, 'g': 6, ' ': 3, 'o': 2}
    assert expected == repeat_simbols(input_string)







































