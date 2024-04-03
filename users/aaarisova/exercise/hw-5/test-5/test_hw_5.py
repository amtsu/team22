import pytest
from functions_hw_5 import (create_set_1, add_element_to_set, remove_element_from_set, has_element_in_set, create_set_2, find_union_sets, difference_sets, create_sets_of_rainbows, intersection_of_sets, union_sets_in_new_set, create_dict_person, add_email_to_dict, del_key_to_dict, dict_total_of_fruits, add_stud_to_dict, adult_person, compare_sets, price_is_over_limit) 


# I.

def test_create_set_1():
    '''тест функции - создание множество set1 из целых чисел'''
    numbers = [1, 2, 3, 4, 5]
    assert create_set_1(numbers) == {1, 2, 3, 4, 5}


def test_add_element_to_set():
    '''Тест-проверка добавен ли в это множество элемент 6'''
    set1 = {1, 2, 3, 4, 5}
    elem = 6
    assert add_element_to_set(set1, elem) == {1, 2, 3, 4, 5, 6}, 'Ошибка добавления элемента'


def test_remove_element_from_set():
    '''Тест удален ли элемент 2 из множества '''
    set1 = {1, 2, 3, 4, 5, 6}
    elem = 2
    assert remove_element_from_set(set1, elem) == {1, 3, 4, 5, 6}, 'Ошибка удаления элемента'


def test_has_element_in_set():
    '''тест. проверяем, содержит ли множество элемент 3'''
    set1 = {1, 3, 4, 5, 6}
    assert has_element_in_set(set1, 3) == True, 'Ошибка в содержании элемента 3 в множестве'


def test_create_set_2():
    '''Тест на создание второго множества set2 с элементами 4, 5, 6, 7, 8'''
    elements = [4, 5, 6, 7, 8]
    assert create_set_2(elements) == {4, 5, 6, 7, 8}, 'Ошибка создания множества'

 
def test_find_union_sets_1():
    '''Тест на объединение множеств set1 и set2'''
    set1 = {1, 3, 4, 5, 6}
    set2 = {4, 5, 6, 7, 8}
    assert find_union_sets(set1, set2) == {1, 3, 4, 5, 6, 7, 8}, 'Ошибка объединения множеств'   


def test_find_union_sets_2():   #негативный. словарь, вместо множества
    '''Тест на объединение множеств set1 и set2'''
    set1 = {'a':'b', 'c':'d'}
    set2 = {4, 5, 6, 7, 8}
    with pytest.raises(TypeError):
        find_union_sets(set1, set2)


def test_difference_sets():
    '''тест нахождения разности множеств set1 и set2'''
    set1 = {1, 3, 4, 5, 6}
    set2 = {4, 5, 6, 7, 8}
    assert difference_sets(set1,set2) == {1, 3}, 'ошибка нахождения разности множеств'


def test_difference_sets_2():     #множества пустые
    '''тест нахождения разности множеств set1 и set2'''
    set1 = set()
    set2 = set()
    assert difference_sets(set1,set2) == set(), 'ошибка нахождения разности множеств'


def test_difference_sets_3():  #переменные не только числа
    '''тест нахождения разности множеств set1 и set2'''
    set1 = {1,2,'a','s'}
    set2 = {2,'a','e'}
    assert difference_sets(set1,set2) == {1,'s'}, 'ошибка нахождения разности множеств'


def test_create_sets_of_rainbows():
    ''' Тест на создание два множества, содержащие цвета радуги.'''

    set1 = {"красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"}
    set2 = {"оранжевый", "зеленый", "голубой", "синий", "Мальвиновый"}
    result = create_sets_of_rainbows(set1, set2)
    
    assert result == ({'голубой','желтый','зеленый','красный','оранжевый','синий','фиолетовый'},
 {'Мальвиновый', 'голубой', 'зеленый', 'оранжевый', 'синий'}) 

 
def test_intersection_of_sets():
    '''Тест на нахождение пересечения множеств set1 и set2'''

    set1 = {"красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"}
    set2 = {"оранжевый", "зеленый", "голубой", "синий", "Мальвиновый"}
    
    result = intersection_of_sets(set1, set2)
    assert result == {'голубой', 'зеленый', 'оранжевый', 'синий'}



def test_union_sets_in_new_set():
    '''Тест на объединение множества set1 и set2 и сохр результата в новое множество rainbow_colors'''

    set1 = {"красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"}
    set2 = {"оранжевый", "зеленый", "голубой", "синий", "Мальвиновый"}

    result = union_sets_in_new_set(set1, set2)
    assert result == {'Мальвиновый','голубой','желтый','зеленый','красный','оранжевый','синий','фиолетовый'}


# II.

def test_create_dict_person():
    '''тест создания словарь'''
    dict_person = {"name": "Ivan", "age": "26", "city": "Moscow"}
    assert create_dict_person(dict_person) == {"name": "Ivan", "age": "26", "city": "Moscow"}, 'Ошибка создания словаря'


def test_add_email_to_dict():
    '''тест на добавление в словарь нового ключа со значением электронного адреса'''
    person_dict = {'name': 'Ivan', 'age': '26', 'city': 'Moscow'}
    email = 'anna.arisova@gmail.com'
    assert add_email_to_dict(person_dict, email) == {'name': 'Ivan', 'age': '26', 'city': 'Moscow', 'email': 'anna.arisova@gmail.com'}, 'Ошибка добавления ключа "email" в словарь.'


def test_del_key_to_dict():
    '''тест функции для удаления ключа из словаря.'''
    person_dict = {'name': 'Ivan', 'age': '26', 'city': 'Moscow', 'email': 'anna.arisova@gmail.com'}
    del_key = 'city'
    assert del_key_to_dict(person_dict, del_key) == {'name': 'Ivan', 'age': '26', 'email': 'anna.arisova@gmail.com'}, 'Ошибка удаления ключа "city" из словаря.'


def test_dict_total_of_fruits():
    '''тест подсчета стоимости всех фруктов, имеющихся в наличии'''
    fruits_quantity = fruits_quantity = {"яблоко": 5, "банан": 10, "апельсин": 7}
    fruits_prices = {"яблоко": 2, "банан": 1, "апельсин": 3}
    assert dict_total_of_fruits(fruits_quantity, fruits_prices) == 41, 'Ошибка подсчета стоимости всех фруктов, имеющихся в наличии'


def test_add_stud_to_dict():
    '''тест функции добавления нового студента "Смирнова" возрастом 20 лет в словарь.'''
    dict_stud = {"Иванов": 22, "Петрова": 13, "Сидоров": 23}
    surname = 'Смирнов'
    age = 20
    assert add_stud_to_dict(dict_stud, surname, age) == {'Иванов': 22, 'Петрова': 13, 'Сидоров': 23, 'Смирнов': 20}, 'Ошибка добавления нового студента "Смирнова" в словарь.'



#III, IV.

def test_adult_person():
    '''тест функции вывода сообщения "Совершеннолетний" или "Несовершеннолетний".'''
    person = {"name": "Ivan", "age": "26", "city": "Moscow"}
    assert adult_person(person) == 'Совершеннолетний'


def test_compare_sets_1():
    '''тест функции сравнения длины двух множеств и вывода сообщения о том, какое из множеств больше.'''

    set1 = {"красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"}
    set2 = {"оранжевый", "зеленый", "голубой", "синий", "Мальвиновый"}
    assert compare_sets(set1, set2) == 'set1 > set2', 'Ошибка сравнения множеств'


def test_compare_sets_2():
    '''тест функции сравнения длины двух множеств и вывода сообщения о том, какое из множеств больше.'''

    set1 = {"красный", "оранжевый", "желтый", "зеленый", "голубой"}
    set2 = {"оранжевый", "зеленый", "голубой", "синий", "Мальвиновый"}
    assert compare_sets(set1, set2) == 'set1 = set2', 'Ошибка сравнения множеств'


def test_compare_sets_3():
    '''тест функции сравнения длины двух множеств и вывода сообщения о том, какое из множеств больше.'''

    set1 = {}
    set2 = {1}
    assert compare_sets(set1, set2) == 'set1 < set2', 'Ошибка сравнения множеств'  


def test_price_is_over_limit():
    ''' Тест для функции, которая выводит список продуктов, цена которых превышает указанное число'''
    fruits_prices = {"яблоко": 1.5, "банан": 2, "апельсин": 1.2}
    assert price_is_over_limit(fruits_prices, 1.4) == ["яблоко", "банан"], 'Ошибка в тесте'






