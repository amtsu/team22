import pytest
from func_for_hw5_1_4 import (
remove_number_in_set,
make_set,
add_in_set,
element_in_set,
make_dict,
make_dict_new,
create_person,
create_person_add,
remove_key_in_my_dict,
sum_value,
pop_key_in_dict,
add_key_value_in_dict,
add_fruit_in_dict,keys_with_value_greater_than,
keys_with_value_greater_than,
cycle_element_of_set,
cycle_number)

def test_make_set():
    """
    функция создает множество из заданых целых чисел
    """
    a = 1, 2, 3, 4, 5
    expected = {1, 2, 3, 4, 5}
    assert make_set(a) == expected
    
def test_make_set2():
    """
    на вход подаю список, получаю тоже множество
    """
    a = [1, 2, 3, 4, 5]
    expected = {1, 2, 3, 4, 5}
    assert make_set(a) == expected

def test_make_set3():
    """
    на вход подаю кортеж, получаю тоже множество
    """
    a = (1, 2, 3, 4, 5)
    expected = {1, 2, 3, 4, 5}
    assert make_set(a) == expected

def test_make_set3():
    """
    на вход подаю строку, получаю тоже множество
    """
    a = "как же тебя сломать"
    expected = {' ', 'а', 'б', 'е', 'ж', 'к', 'л', 'м', 'о', 'с', 'т', 'ь', 'я'}
    assert make_set(a) == expected

def test_make_set4():
    """
    на вход подаю словарь, получаю тоже множество
    """
    a = {"похоже": 'Regina', "не": 35, "сломать": 'Saint-Petersburg'}
    expected = {'не', 'похоже', 'сломать'}
    assert make_set(a) == expected

def test_add_in_set():
    """
    функция добавляет число в множество, на выходе новое множество
    """
    my_set = {1, 2, 3, 4, 5}
    number = 6
    expected = {1, 2, 3, 4, 5, 6}
    assert add_in_set(my_set, number) == expected

def test_add_in_set2():
    """
    на вход подаю кортеж, а не множество
    """
    my_set = (1, 2, 3, 4, 5)
    number = 6
    with pytest.raises(AttributeError):
        add_in_set(my_set, number)

def test_add_in_set3():
    """
    на входе number = нехешируемый тип - список
    """
    my_set = {1, 2, 3, 4, 5}
    number = ["6"]
    with pytest.raises(TypeError):
        add_in_set(my_set, number)

def test_add_in_set4():
    """
    на входе  не множество, а список
    """
    my_set = [1, 2, 3, 4, 5]
    number =  2
    with pytest.raises(AttributeError):
        add_in_set(my_set, number)
        
    
def test_remove_number_in_set():
    """
    позитивный тест на функцию, удаляющую число из множества
    """
    my_set = {1, 2, 3, 4, 5}
    number = 2
    expected = {1, 3, 4, 5}
    assert remove_number_in_set(my_set, number) == expected
    
def test_remove_number_in_set2():
    """
    подаю на вход не множество, а кортеж
    """
    my_set = (1, 2, 3, 4, 5)
    number = 2
    with pytest.raises(AttributeError):
        remove_number_in_set(my_set, number)

def test_remove_number_in_set3():
    """
    подаю на вход список, а не множество
    """
    my_set = [1, 2, 3, 4, 5]
    number =  2
    with pytest.raises(AttributeError):
        remove_number_in_set(my_set, number)

def test_remove_number_in_set4():
    """
    пустое множество на входе
    """
    my_set = {}
    number = 2
    expected = {}
    assert remove_number_in_set(my_set, number) == expected

def test_element_in_set():
    """
    проверяем наличие элемента во множестве, возвращает True or False
    """
    my_set = {1, 2, 3, 4, 5}
    element = 6
    expected = False
    assert element_in_set(my_set, element) == expected

def test_element_in_set2():
    """
    проверяем наличие элемента во множестве, возвращает True or False
    """
    my_set = {1, 2, 3, 4, 5}
    element = 2
    expected = True
    assert element_in_set(my_set, element) == expected
    
def test_element_in_set3():
    """
    на вход подаю кортеж вместо множества и список вместо числа
    """    
    my_set = (1, [2], "3", 4, 5)
    element = ["2"]
    expected = False
    assert element_in_set(my_set, element) == expected

################# СЛОВАРИ ################################

def test_make_dict():
    """
    тест на функцию принимающую три параметра, на выходе словарь
    """
    expected = {'name': 'Regina', 'age': 35, 'city': 'Saint-Petersburg'}
    assert make_dict('Regina', 35, 'Saint-Petersburg') == expected
    
def test_make_dict_new():
    """
    функуия принимает 4 параметра и выводит готовый словарь
    """
    expected = {'name': 'Regina', 'age': 35, 'city': 'Saint-Petersburg', 'mail': 'my_mail'}
    assert make_dict_new('Regina', 35, 'Saint-Petersburg', 'my_mail') == expected

def test_create_person():
    """
    тест на функцию, принимающую словарь и возвращающую словарь
    """
    my_dict = {"name": 'Regina', "age": 35, "city": 'Saint-Petersburg'}
    expected = {"name": 'Regina', "age": 35, "city": 'Saint-Petersburg'}
    assert create_person(my_dict) == expected

def test_create_person_add():
    """
    позитивный тест: функция принимает словарь, ключ и знаение, возвращает словарь с добавленным ключом и значением, если такого ключа не было в словаре
    """
    my_dict = {'name': 'Regina', 'age': 35, 'city': 'Saint-Petersburg'}
    expected = {'name': 'Regina', 'age': 35, 'city': 'Saint-Petersburg', 'mail': '@my_mail'}
    assert create_person_add(my_dict, "mail", "@my_mail") == expected

def test_create_person_add2():
    """
    позитивный тест: подаю уже существующий ключ в словаре
    """
    my_dict = {'name': 'Regina', 'age': 35, 'city': 'Saint-Petersburg'}
    expected = {'name': 'Regina', 'age': 35, 'city': 'Saint-Petersburg'}
    assert create_person_add(my_dict, 'name', "@my_mail") == expected

def test_remove_key_in_my_dict():
    """
    позитивный тест: на функцию, которая принимает словарь и ключ, удаляет ключ если он иммется в словаре
    """
    my_dict = {'name': 'Regina', 'age': 35, 'city': 'Saint-Petersburg'}
    expected = {'name': 'Regina', 'city': 'Saint-Petersburg'}
    assert remove_key_in_my_dict(my_dict, 'age') == expected
    
def test_remove_key_in_my_dict2():
    """
    позитивный тест на удаление ключа из словаря если его нет в словаре
    """
    my_dict = {'name': 'Regina', 'age': 35, 'city': 'Saint-Petersburg'}
    assert remove_key_in_my_dict(my_dict, 'что-то') == {'name': 'Regina', 'age': 35, 'city': 'Saint-Petersburg'}

def test_sum_value():
    """
    позитивный тест на функцию, которая  складывает все значения словаря
    """
    fruits_prices = {1: 1.5, "банан": 2, "апельсин": 1.2}
    expected = 4.7
    assert sum_value(fruits_prices) == expected
    
def test_sum_value2():
    """
    негативный тест: когда значение типа - "список"
    """
    fruits_prices = {1: 1.5, "банан": "черный", "апельсин": 1.2}
    with pytest.raises(TypeError):
        sum_value(fruits_prices)
        
def test_pop_key_in_dict():
    """
    позитивный тест:на функцию, которая удаляет ключ из словаря, если его нет - выводит сообщение о его отсутствии
    """
    my_dict = {"кукла": "колдуна", "старинный": "дом", "ели": "мясо"}
    my_key = "мужики"
    expected = 'there is no such switch'
    assert pop_key_in_dict(my_dict, my_key) == expected
    
def test_pop_key_in_dict2():
    """
    негативный тест: если удаляемы ключ типа - список
    """
    my_dict = {"кукла": "колдуна", "старинный": "дом", "ели": "мясо"}
    my_key = ["мужики"]
    with pytest.raises(TypeError):
        pop_key_in_dict(my_dict, my_key)
        
def test_add_key_value_in_dict():
    """
    позитивный тест: на функцию, которая добавляет новый ключ и значение если их нет в словаре. Принимает словари, ключ и значение.
    """
    my_dict = {"кукла": "колдуна", "проклятый": "старый дом", "ели": "мясо мужики"}
    expected = {'кукла': 'колдуна', 'проклятый': 'старый дом', 'ели': 'мясо мужики', 'дурак': 'и молния'}
    assert add_key_value_in_dict(my_dict, "дурак", "и молния") == expected
    
def test_add_key_value_in_dict2():
    """
    позитивный тест: на функцию добавляет новый ключ и значение(типа список) если их нет в словаре. Принимает словари, ключ и значение.
    """
    my_dict = {"кукла": "колдуна", "проклятый": "старый дом", "ели": "мясо мужики"}
    expected = {'кукла': 'колдуна', 'проклятый': 'старый дом', 'ели': 'мясо мужики', 'дурак': ['и молния', 'грохочет гром']}
    assert add_key_value_in_dict(my_dict, "дурак", ['и молния', 'грохочет гром']) == expected

################# УСЛОВНЫЕ ОПЕРАТОРЫ ################################

def test_add_fruit_in_dict():
    """
    позитивный тест: на функцию, которая добавляет новый ключ и значение в словарь
    """
    fruits_quantity = {"яблоко": 5, "банан": 10, "апельсин": 7}
    expected = {'яблоко': 5, 'банан': 10, 'апельсин': 7, 'груша': 3}
    assert add_fruit_in_dict(fruits_quantity, "груша", 3)
    
def test_keys_with_value_greater_than():
    """
    позитивный тест: на функцию, которая выводит все ключи, у которых значения выше заданного порога
    """
    fruits_quantity = {"яблоко": 1, "банан": 55, "апельсин": 1000}
    expected = ['банан', 'апельсин']
    assert keys_with_value_greater_than(fruits_quantity, 45)

def test_keys_with_value_greater_than2():
    """
    негативный тест: на функцию, которая выводит все ключи, у которых значения выше заданного порога.
    Когда порог выше значений словаря
    """
    fruits_quantity = {"яблоко": 1, "банан": 55, "апельсин": 1000}
    expected = []
    assert keys_with_value_greater_than(fruits_quantity, 1500) == expected
    
def test_keys_with_value_greater_than3():
    """
    негативный тест: на функцию, которая выводит все ключи, у которых значения выше заданного порога.
    Когда пришел пустой словарь.
    """
    fruits_quantity = {}
    expected = []
    assert keys_with_value_greater_than(fruits_quantity, 1500) == expected
    
def test_keys_with_value_greater_than4():
    """
    негативный тест: на функцию, которая выводит все ключи, у которых значения выше заданного порога.
    Когда порог типа строка.
    """
    fruits_quantity = {"яблоко": 1, "банан": 55, "апельсин": 1000}
    with pytest.raises(TypeError):
        keys_with_value_greater_than(fruits_quantity, "45")

def test_cycle_element_of_set():
    """
    позитивный тест: на функцию, которая выводит в список все уникальные элементы множества
    """
    set1 = {1, 2, 3, 4, 5, 99, 1001, 2, 3}
    expected = [1, 2, 3, 4, 5, 99, 1001]
    assert cycle_element_of_set(set1) == expected   #если подать на вход кортеж, то функция не выведет уникальные 
                                                    #элементы множества,
                                                    #и похорошему нужно функцию доработать

def tets_cycle_number():
    """
    позитивный тест: на функцию, которая  выводит квадрат чисел от 1 до 5 через цикл
    """
    a = 1
    b = 5
    assert cycle_number(a, b) == [1, 4, 9, 16, 25]
