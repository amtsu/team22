import pytest
from hw5_part1 import (add_element, remove_element, element_in_set, 
union_sets, difference_sets, intersection_of_sets)


def test_set_union1():
   
    input_a = {1, 2, 3, 4, 5}
    input_b = {4, 5, 6, 7, 8}
    expected = {1, 2, 3, 4, 5, 6, 7, 8}
    assert expected == union_sets(input_a, input_b) , "Неверно посчитано объединение"
    
def test_set_union2():
   
    input_a = {"красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"}
    input_b = {"оранжевый", "зеленый", "голубой", "синий", "Мальвиновый"}
    expected = {'Мальвиновый', 'голубой', 'желтый', 'зеленый', 'красный', 'оранжевый', 'синий', 'фиолетовый'}
    assert expected == union_sets(input_a, input_b) , "Неверно посчитано объединение"

def test_intersection_of_sets():
    input_a = {"красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"}
    input_b = {"оранжевый", "зеленый", "голубой", "синий", "Мальвиновый"}
    expected = {'голубой', 'зеленый', 'оранжевый', 'синий'}
    assert expected == intersection_of_sets(input_a, input_b)  , "Неверно посчитано пересечение"

def test_set_difference():
    
    input_a = {1, 2, 3, 4, 5}
    input_b = {4, 5, 6, 7, 8}
    expected = {1, 2, 3}
    assert expected == difference_sets(input_a, input_b), "Неверно посчитана разность"


    

def test_remove_element():
   
    some_set = {1, 2, 3, 4, 5, 6}
    element = 3
    expected = {1, 2, 4, 5, 6}
    assert expected == remove_element(some_set, element), "Ошибка, такого элетента нет в множестве"
    

    
