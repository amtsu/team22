import pytest
from func_for_hw5 import (set_union,
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
create_set,)


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
    expected == set_difference(input_a, input_b), "Ошибка, разность множеств найдена неверно"

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
    sets = set()
    expected = set()      
    assert expected == find_intersection(*sets) # тут не уверена, что так записала, но тест прошел 

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
    elements = create_set(1, 2, 3, 4, 5)
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
    

    
    