import pytest
from func_for_hw4 import (create_lists,
creat_list,
len_list,
fibonacci_list_check,
check_fibonacci_numbers,
laws_of_the_Programmer,
solyanka,
element_5_solaynki,
add_element,
swap_elements)


a_poem = """За стеклом лежал Питон, 
Большой и толстый, как батон.
Вверх пополз,
Затем вернулся,
Круглым бубликом свернулся."""

fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]


def test_create_lists():
    """
    туст на функцию добавления элемента в конец списка
    """
    assert create_lists() == [1, 2, 3, 4, 5, 6, 9, 789], "Элемент добавлен неудачно"

def test_creat_list():
    assert creat_list(a_poem)[0] == ['З', 'а', ' ', 'с', 'т', 'е', 'к', 'л', 'о', 'м', ' ', 'л', 'е', 'ж', 'а', 'л', ' ', 'П', 'и', 'т', 'о', 'н', ',', ' ', '\n', 'Б', 'о', 'л', 'ь', 'ш', 'о', 'й', ' ', 'и', ' ', 'т', 'о', 'л', 'с', 'т', 'ы', 'й', ',', ' ', 'к', 'а', 'к', ' ', 'б', 'а', 'т', 'о', 'н', '.', '\n', 'В', 'в', 'е', 'р', 'х', ' ', 'п', 'о', 'п', 'о', 'л', 'з', ',', '\n', 'З', 'а', 'т', 'е', 'м', ' ', 'в', 'е', 'р', 'н', 'у', 'л', 'с', 'я', ',', '\n', 'К', 'р', 'у', 'г', 'л', 'ы', 'м', ' ', 'б', 'у', 'б', 'л', 'и', 'к', 'о', 'м', ' ', 'с', 'в', 'е', 'р', 'н', 'у', 'л', 'с', 'я', '.']

def test_creat_list2():    
    assert creat_list(a_poem)[1] == ['За', 'стеклом', 'лежал', 'Питон,', '\nБольшой', 'и', 'толстый,', 'как', 'батон.\nВверх', 'пополз,\nЗатем', 'вернулся,\nКруглым', 'бубликом', 'свернулся.']
    
def test_creat_list3():    
    assert creat_list(a_poem)[2] == ['За стеклом лежал Питон, ', 'Большой и толстый, как батон.', 'Вверх пополз,', 'Затем вернулся,', 'Круглым бубликом свернулся.']
   
def test_len_list():
    assert len_list(a_poem)[0] == 112

def test_len_list2():
    assert len_list(a_poem)[1] == 13

def test_len_list3():
    assert len_list(a_poem)[2] == 5

############################# добавила тесты к ним ##############################################################

def test_solyanka():
    """
    функция считает количество элементов списка
    """
    solyanka_list = [10, 5.5,'строка', ['1, 5, 3, "abc"'], {'1: "str", 2: "bar", "la-la": 22'}, ('1, 5, 3, "abc"') , {'1, 5, 3, "abc"'}]
    expected = 7
    assert solyanka(solyanka_list) == expected

def test_element_5_solaynki():
    """
    проверяет тип пятого элемента списка
    """
    solyanka_list = [10, 5.5,'строка', ['1, 5, 3, "abc"'], {'1: "str", 2: "bar", "la-la": 22'}, ('1, 5, 3, "abc"') , {'1, 5, 3, "abc"'}]
    expected = set
    assert element_5_solaynki(solyanka_list) == expected

def test_add_element():
    """
    тест на добавление последнего элемента в список и его тип
    """
    solyanka_list = [10, 5.5,'строка', ['1, 5, 3, "abc"'], {'1: "str", 2: "bar", "la-la": 22'}, ('1, 5, 3, "abc"') , {'1, 5, 3, "abc"'}]
    element = 7
    expected = [10, 5.5, 'строка', ['1, 5, 3, "abc"'], {'1: "str", 2: "bar", "la-la": 22'}, '1, 5, 3, "abc"', {'1, 5, 3, "abc"'}, [7]]
    expected2 = list
    assert add_element(solyanka_list, element)[0] == expected
    assert add_element(solyanka_list, element)[1] == expected2

def test_swap_elements():
    """
    проверяем как функция меняет местами 3 и 5 элементы в списке
    """
    a_list = [1, 2, 5, 4, 3, 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert swap_elements(a_list) == expected

#################################################################################################################
def test_fibonacci_list_check():
    expected_length = 23
    assert fibonacci_list_check(fibonacci_list)[0] == expected_length
    
def test_fibonacci_list_check2():
    exepected_repeating_element = 2
    assert fibonacci_list_check(fibonacci_list)[1] == exepected_repeating_element
    
    
def test_check_fibonacci_numbers():
    expected_results = {21: True, 33: False, 987: True, 9999: False}
    actual_results = check_fibonacci_numbers(fibonacci_list)
    assert actual_results == expected_results

def test_laws_of_the_Programmer():
    expected_results = [' Кто битым за дедлайн был,', 'тот больше не сольется.', 'Пуд багов съевший, выше ценит чистый код.', 'Кто дошик ел, тот рейтинг ценит свой.', 'Кто крашился, тот знает, что живой.']
    
    assert expected_results == laws_of_the_Programmer()
    
    
    
    