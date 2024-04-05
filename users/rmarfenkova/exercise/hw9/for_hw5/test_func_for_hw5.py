import pytest
from func_for_hw5 import (
set_union,
set_difference,
is_subset,
union_sets,
remove_element,
find_intersection,
check_equality,
union_of_sets,
is_disJoint,
set_difference,
symmetric_difference,
create_set,
create_dictionary,
add_student,
remove_student,
merge_dicts,
remove_item,
reverse_dict,
sort_dict_reverse,
max_value_in_dict,
check_age,
compare_sets_length,
check_even_odd,
is_leap_year,
is_palindrome,
is_prime,
check_date)

##################### МНОЖЕСТВА #####################################
def test_set_union():
    """
    тест на объединения двух множеств
    """
    input_a = {1, 2, 3, 4, 5}
    input_b = {4, 5, 6, 7, 8}
    expected = {1, 2, 3, 4, 5, 6, 7, 8}
    assert expected == set_union(input_a, input_b), "Ошибка, объединение множеств найдено неверно"
    
def test_set_difference():
    """
    тест на разности двух множест
    """
    input_a = {1, 2, 3, 4, 5}
    input_b = {4, 5, 6, 7, 8}
    expected = {1, 2, 3}
    assert expected == set_difference(input_a, input_b), "Ошибка, разность множеств найдена неверно"

def test_is_subset_false():
    """
    тест проверяет, что одно множество не являестя подмножеством другого
    """
    input_a = {1, 2, 3, 4, 5}
    input_b = {4, 5, 6, 7, 8}
    expected = False
    assert expected == is_subset(input_a, input_b), "Ошибка, множество является помножеством другого"
    
def test_is_subset_true():
    """
    тест проверяет, что одно множество  являестя подмножеством другого
    """
    input_a = {1, 2, 3, 4, 5}
    input_b = {1, 2, 3, 4, 5}
    expected = True
    assert expected == is_subset(input_a, input_b), "Ошибка, множество не является подмножеством другого"
    
def test_union_sets():
    """
    тест на объединение нескольких множеств в одно 
    """
    sets = (
            {1, 2, 3, 4, 5, 6},
            {3, 4, 5, 6, 7, 8},
            {5, 6, 7, 8, 9, 10}
    )
    expected = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    assert expected == union_sets(*sets), "Ошибка, множества были объединены неверно"

def test_remove_element():
    """
    тест удаление конкретного элемента из множества
    """
    some_set = {1, 2, 3, 4, 5, 6}
    element = 3
    expected = True
    assert expected == remove_element(some_set, element), "Ошибка, такого элетента нет в множестве"
    
def test_remove_element_not_in_set():
    """
    тест на отсутствие удаляемого элемента во множестве
    """
    some_set = {1, 2, 3, 4, 5, 6}
    element = 7
    expected = False
    assert expected == remove_element(some_set, element), "Ошибка, элмент есть во множестве"
    
def test_find_intersection():
    """
    тест поиска пересечения нескольких множеств
    """
    sets = (
        {2, 3, 4, 5},
        {3, 4, 5, 6},
        {4, 5, 6, 7}
    )
    expected = {4, 5}
    assert expected == find_intersection(*sets), "Ошибка, объединение нескольких множеств неверно"
    
def test_find_intersection2():
    """
    тест на проверку пустое множества на входе
    """
    
    expected = set()      
    assert expected == find_intersection(set()) # тут не уверена, что так записала, но тест прошел 

def test_check_equality():
    """
    тест проверки равенства двух множеств
    """
    input_a = {1, 2, 3}
    input_b = {1, 2, 3}
    expected = True
    assert expected == check_equality(input_a, input_b), "Ошибка, множества не равны"

def test_check_equality2():
    """
    тест проверки что множества не равны
    """
    input_a = {1, 2, 3}
    input_b = {3, 4, 5}
    expected = False
    assert expected == check_equality(input_a, input_b), "Ошибка, множества равны"
    
def test_union_of_sets():
    """
    тест на нахождение объединения трех множеств
    """
    input_a = {1, 2, 3, 4, 5, 6}
    input_b = {3, 4, 5, 6, 7, 8}
    input_c = {5, 6, 7, 8, 9, 10}
    expected = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    assert expected == union_of_sets(input_a, input_b, input_c), "Ошибка, объединения трех множеств найдено неверно"

def test_is_disJoint():
    """
    тест  провеяет являются ли два множества дизъюктивными
    """
    input_a = {1, 2, 3}
    input_b = {4, 5, 6}
    expected = True
    assert expected == is_disJoint(input_a, input_b), "Ошибка, множества не дизъюктивны"

def test_is_disJoint2():
    """
    тест  провеяет, что  два множества не дизъюктивны
    """
    input_a = {1, 2, 3}
    input_b = {3, 5, 6}
    expected = False
    assert expected == is_disJoint(input_a, input_b), "Ошибка, множества дизъюктивны"
    
def test_set_difference():
    """
    тест нахождения разности двух множеств
    """
    input_a = {1, 2, 3}
    input_b = {3, 4, 5}
    expected = {1, 2}
    assert expected == set_difference(input_a, input_b), "Ошибка, разность найдена неверно"

def test_symmetric_difference():
    """
    тест нахождения симметрической  разности двух множеств
    """
    input_a = {1, 2, 3, 4, 5} 
    input_b = {3, 4, 5, 6, 7}
    expected = {1, 2, 6, 7}
    assert expected == symmetric_difference(input_a, input_b), "Ошибка симметрическая разность не найдена"

def test_symmetric_difference2():
    """
    тест на нахождения симметрической  разности двух множеств, если множества на входе равны
    """
    input_a = {1, 2, 3, 4, 5}   
    input_b = {1, 2, 3, 4, 5}   
    expected = set()
    assert expected == symmetric_difference(input_a, input_b), "Ошибка, симметрическая разность множеств существует"

def test_create_set():
    """
    тест на создание множества с заданными элементами
    """
    elements = (1, 2, 3, 4, 5)
    expected = {1, 2, 3, 4, 5}
    assert expected == create_set(*elements), "Ошибка, множество не создано" 
    
def test_create_set2():
    """
    тест на создание множества с пустым вводом 
    """
    elements = create_set()
    expected = set()
    assert expected == create_set(*elements), "Ошибка, множество не пустое"
    
def test_create_set3():
    """
    тест проверяет удаляются ли дубликаты из множества
    """
    elements = create_set(1, 2, 2, 3, 3, 3)
    expected = {1, 2, 3}
    assert expected == create_set(*elements), "Ошибка, во множестве есть повторяющиеся элементы"
    
##################### СЛОВАРИ #####################################
    
def test_create_dictionary():
    """
    Тест на функцию, которая создает словарь с заданными ключами и значениями.
    Принимает словарь в формате ключ-значение и возвращает созданный словарь.
    """
    expected = {'appeles': 5, 'bananas': 10, 'oranges': 7}
    assert expected == create_dictionary(appeles=5, bananas=10, oranges=7), "Ошибка, словарь создан неправильно"

def test_create_dictionary2():
    """
    тест на создание пустого словаря
    """
    assert create_dictionary() == {}

          
def test_add_student():
    """
    тест на добавление студента в заданый словарь
    """
    students = {1: 'Иванов', 2: 'Петров', 3: 'Сидоров'}
    student_id = 4
    student_name = 'Смирнов'
    expected = {1: 'Иванов', 2: 'Петров', 3: 'Сидоров', 4: 'Смирнов'} 
    assert add_student(students, student_id, student_name) == expected

def test_remove_student():
    """
    тест на функцию удаляющую студента в заданном словаре.
    """
    students = {1: 'Иванов', 2: 'Петров', 3: 'Сидоров', 4: 'Смирнов'}
    student_id = 4
    expected = {1: 'Иванов', 2: 'Петров', 3: 'Сидоров'}
    assert remove_student(students, student_id) == {1: 'Иванов', 2: 'Петров', 3: 'Сидоров'}

def test_remove_student2():
    """
    тест на функцию удаляющую студента в заданном словаре, если такого student_id нет в словаре
    """
    students = {1: 'Иванов', 2: 'Петров', 3: 'Сидоров', 4: 'Смирнов'}
    student_id = 7
    expected = {1: 'Иванов', 2: 'Петров', 3: 'Сидоров', 4: 'Смирнов'}
    assert remove_student(students, student_id) == {1: 'Иванов', 2: 'Петров', 3: 'Сидоров', 4: 'Смирнов'}
    
############ тесты на добавление удаление фруктов не получились потом еще попробую ###################  

def test_merge_dicts():
    """
    тест на функцию объединеня двух словарей
    """
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert merge_dicts(dict1, dict2) == expected
    
def test_merge_dicts2():
    """
    тест проверяет функцию когда один из словарей пришел пустой
    """
    dict1 = {}
    dict2 = {'c': 3, 'd': 4}
    expected = {'c': 3, 'd': 4}
    assert merge_dicts(dict1, dict2) == expected

def test_remove_item():
    """
    тест на функцию которая удаляет элемент из заданого словаря по ключу
    """
    my_dict = {'apple': 2, 'banana': 3, 'orange': 1}
    my_key = 'banana'
    expected = {'apple': 2, 'orange': 1}
    assert remove_item(my_dict, my_key) == expected


def test_remove_item2():
    """
    тест на функцию которая удаляет элемент из заданого словаря по ключу, которого нет в словаре
    """
    my_dict = {'apple': 2, 'banana': 3, 'orange': 1}
    my_key = 'что - то'
    expected = {'apple': 2, 'banana': 3, 'orange': 1}
    assert remove_item(my_dict, my_key) == expected

def test_remove_item3():
    """
    тест проверяет как функция удвляет ключ, если он является кортежем, принимает словарь и ключ
    """
    my_dict = {("ну", "да"):1, ("ну", "нет"):2, "а": 3, "вот": 4, "и": 5, "да": 6 }
    my_key = ("ну", "да")
    expected = {('ну', 'нет'): 2, 'а': 3, 'вот': 4, 'и': 5, 'да': 6}
    assert remove_item(my_dict, my_key)
    
def test_reverse_dict():
    """
    тест проверяет как функция переворачивает значение и ключ в словаре
    """
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    expected = {1: 'a', 2: 'b', 3: 'c'}
    assert reverse_dict(my_dict) == expected
    
def test_sort_dict_reverse():
    """
    тест на функцию сортировки ключей в словаре, в обратном порядке
    """
    my_dict = {3: 'apple', 1: 'banana', 2: 'orange'}
    expected = {3: 'apple', 2: 'orange', 1: 'banana'}
    assert sort_dict_reverse(my_dict) == expected
    
def test_sort_dict_reverse2():
    """
    тест на функцию сортировки ключей в словаре, в обратном порядке, когда ключи - строки
    """
    my_dict = {'a': 'apple', 'f': 'banana', 'b': 'orange'}
    expected = {'f': 'banana', 'b': 'orange', 'a': 'apple'}
    assert sort_dict_reverse(my_dict) == expected

def test_max_value_in_dict():
    """
    тест на функцию, которая возвращает наибольшее значение словаря
    """
    input_dict = {'a': 1, 'b': 2, 'c': 3}
    expected = 3
    assert max_value_in_dict(input_dict) == expected
    
def test_max_value_in_dict2():
    """
    тест на функцию, которая возвращает наибольшее значение словаря, если значение типа str
    """
    my_dict = {1 : "распакоука", 2 : "словаря", 3 : "чек" }
    expected = "чек"
    assert max_value_in_dict(my_dict) == expected

def test_max_value_in_dict3():
    """
    тест на поиск наибольшего значения словаря, если словарь не поступил
    """
    my_dict = {}
    expected = None
    assert max_value_in_dict(my_dict) == expected
############################################################################    

@pytest.mark.parametrize("student_name, expected", [
    ("Алексей", "Алексей совершеннолетний"), 
    ("Мария", "Мария несовершеннолетний"), 
    ("Екатерина", "Студент не найден в базе данных")
])

def test_check_age(student_name, expected):
    """
    позитивный тест на проверку совершенный ли студент в заданном словаре
    """
    students = {"Алексей": 20, "Мария": 17, "Иван": 22}
    assert check_age(students, student_name) == expected
    
    
@pytest.mark.parametrize("my_dict, student_name, expected", [
    ({"Алексей": "20"}, "Алексей", TypeError),
    ({"Алексей": (20, 10)}, "Алексей", TypeError)
])
                                      
def test_check_age_negative(my_dict, student_name, expected):
    with pytest.raises(expected):
        check_age(my_dict, student_name) == expected

@pytest.mark.parametrize("set1, set2, expected", [
    ({1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, "{1, 2, 3, 4, 5} равно {1, 2, 3, 4, 5}"),
    ({1, 2, 3}, {1, 2, 3, 4, 5}, "{1, 2, 3, 4, 5} длиннее {1, 2, 3}"),
    ({1, 2, 3, 4, 5}, {1, 2, 3}, "{1, 2, 3, 4, 5} длиннее {1, 2, 3}"),
    ({}, {1, 2, 3}, "{1, 2, 3} длиннее {}"),
    ({}, {}, "{} или {} не множество"),
    ((1, 2, 3), {1: 3, 2: 4, 3: 5}, "(1, 2, 3) или {1: 3, 2: 4, 3: 5} не множество")
])
        
def test_compare_sets_length(set1, set2, expected):
    """
    позитивный тест на функцию, которая сравнивает длинну множества
    """
    assert compare_sets_length(set1, set2) == expected
    

@pytest.mark.parametrize("number, expected", [
    (2, "Число 2 является четным"),
    (7, "Число 7 является нечетным"),
    (-4, "Число -4 является четным"),
    (-11, "Число -11 является нечетным"),
    ("what", "'what' может быть только типа int"),
    (0, "Число 0 является четным")
])

def test_check_even_odd(number, expected):
    """
    позитивныке тесты на функцию, проверяющую четность числа
    """
    assert check_even_odd(number) == expected

@pytest.mark.parametrize("year, expected", [
    (1764, "1764 - високосный"),
    (1904, "1904 - високосный"),
    (2000, "2000 - високосный"),
    (2001, "2001 - не високосный"),
    ("F", "Введены неверные данные"),
    (-1, "Введены неверные данные")
])
    
def test_is_leap_year(year, expected):
    """
    позитивные тесты на функцию проверяющую високостность года
    """
    assert is_leap_year(year) == expected


@pytest.mark.parametrize("s, expected", [
    ("asa", "asa Строка является палиндромом"),
    ("!asa!", "!asa! Строка является палиндромом"),
    ("3!asa!3", "3!asa!3 Строка является палиндромом"),
    ("123gshd", "123gshd Строка не является палиндромом"),
    ({1, 2, 3}, "{1, 2, 3} не строка")
])
def test_is_palindrome(s, expected):
    """
    функция проверяет, является ли строка полиандропом
    """
    assert is_palindrome(s) == expected


@pytest.mark.parametrize("number, expected", [
    (0, False),
    (1, False),
    (2, True),
    (-3, False),
    ("a", False),
    (None, False)
])
def test_is_prime(number, expected):
    """
    тесты на функцию вычисления простого числа
    """
    assert is_prime(number) == expected


@pytest.mark.parametrize("day, month, year, expected", [
    (32, 7, 2003, False),
    (15, 13, 2000, False),
    (3, 9, 2300, False),
    (30, 2, 2024, False),
    ("1", 12, 2000, "Вы можете ввести только числа"),
    (5, 4, 2024, True)
])
def test_check_date(day, month, year, expected):
    """
    позитивные тесты на проверку корректности даты
    """
    assert check_date(day, month, year) == expected
