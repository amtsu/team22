from hw_5 import (set_union,set_difference,set_union_many,delete_value,set_intersection_many,equality_sets,disjunctive,create_set,merge_dict,)

# Создайте функции set_union и set_difference для операций объединения и разности множеств

def test_set_union_1():
    input1 = {1, 3, 3, 4, 5, 6}
    input2 = {4, 5, 6, 7, 8}
    expected = {1, 3, 4, 5, 6, 7, 8}
    assert set_union(input1,input2) == expected, 'неправильно объединили множества'

def test_set_union_2():
    input1 = {1, 2, 3}
    input2 = {3, 3, 3, 3, 4}
    expected = {1, 2, 3, 4}
    assert set_union(input1,input2) == expected, 'неправильно объединили множества'

def test_set_union_3():
    input1 = {}
    input2 = {}
    expected = {}
    assert set_union(input1,input2) == expected, 'неправильно объединили множества'

def test_set_difference_1():
    input1 = {2,5,6,7,9}
    input2 = {4,5,7,8,9}
    expected = {2,6}
    assert set_difference(input1,input2) == expected, 'неправильно нашли разность множеств'

def test_set_difference_2():
    input1 = {2,5,6,7,9}
    input2 = {1,3,4,8}
    expected = {2,5,6,7,9}
    assert set_difference(input1,input2) == expected, 'неправильно нашли разность множеств'

def test_set_difference_3():
    input1 = {4}
    input2 = {4,5,7}
    expected = set()
    assert set_difference(input1,input2) == expected, 'неправильно нашли разность множеств'

# Создайте функцию для объединения нескольких множеств

def test_set_union_many_1 ():
    input1 = {1,2,3}
    input2 = {1,4,4,5}
    input3 = {2,4,6,5}
    input4 = {8,7,4,1}
    expected = {1, 2, 3, 4, 5, 6, 7, 8}
    assert set_union_many(input1,input2,input3,input4) == expected, 'неправильно объединили несколько множеств'

def test_set_union_many_2 ():
    input1 = {1}
    input2 = {}
    input3 = {6,5}
    input4 = {8,7}
    expected = {1, 5, 6, 7, 8}
    assert set_union_many(input1,input2,input3,input4) == expected, 'неправильно объединили несколько множеств'

def test_set_union_many_3 ():
    input1 = {}
    input2 = {}
    input3 = {}
    expected = set()
    assert set_union_many(input1,input2,input3) == expected, 'неправильно объединили несколько множеств'

# Создайте функцию для удаления конкретного элемента из множества

def test_delete_value_1 ():
    input1 = {1,2,4,88,6}
    input2 = 5
    expected = {1, 2, 4, 6, 88}
    assert delete_value(input1,input2) == expected, 'неправильно удален конкретный элемент из множества'

def test_delete_value_2 ():
    input1 = {1,2,3}
    input2 = 2
    expected = {1, 3}
    assert delete_value(input1,input2) == expected, 'неправильно удален конкретный элемент из множества'

def test_delete_value_3 ():
    input1 = {}
    input2 = 5
    expected = {}
    assert delete_value(input1,input2) == expected, 'неправильно удален конкретный элемент из множества'

# Создайте функцию для поиска пересечения нескольких множеств

def test_set_intersection_many_1 ():
    input1 = {1,2,3,10}
    input2 = {1,4,2,5,3}
    input3 = {2,4,3,5}
    input4 = {8,3,4,1}
    expected = {3}
    assert set_intersection_many(input1,input2,input3,input4) == expected, 'неправильно нашли пересечения нескольких множеств'

def test_set_intersection_many_2 ():
    input1 = {1,2,3,10}
    input2 = {1,4,2,5,3}
    input3 = {1,2,4,3,5}
    input4 = {8,3,4,1}
    expected = {1, 3}
    assert set_intersection_many(input1,input2,input3,input4) == expected, 'неправильно нашли пересечения нескольких множеств'

def test_set_intersection_many_3 ():
    input1 = {1,2,10}
    input2 = {1,4,2}
    input3 = {3,5}
    expected = set()
    assert set_intersection_many(input1,input2,input3) == expected, 'неправильно нашли пересечения нескольких множеств'

# Создайте функцию для проверки на равенство двух множеств.

def test_equality_sets_1():
    input1 = {1, 3, 3, 4, 5, 6}
    input2 = {1, 3, 4, 5, 6}
    expected = True
    assert equality_sets(input1,input2) == expected, 'неправильно проверили на равенство двух множеств'

def test_equality_sets_2():
    input1 = {1, 3, 3, 4, 5, 6}
    input2 = {1, 3, 4, 5, 6 , 7}
    expected = False
    assert equality_sets(input1,input2) == expected, 'неправильно проверили на равенство двух множеств'

def test_equality_sets_3():
    input1 = {}
    input2 = {}
    expected = True
    assert equality_sets(input1,input2) == expected, 'неправильно проверили на равенство двух множеств'

# Создайте функцию для проверки, являются ли два множества дизъюнктными (не имеют общих элементов).

def test_disjunctive_1():
    input1 = {1, 3, 3, 4, 5, 6}
    input2 = {1, 3, 4, 5, 6}
    expected = False
    assert disjunctive(input1,input2) == expected, 'неправильно проверили два множества на дизъюнкцию'

def test_disjunctive_2():
    input1 = {1, 3}
    input2 = {4, 5, 6}
    expected = True
    assert disjunctive(input1,input2) == expected, 'неправильно проверили два множества на дизъюнкцию'

def test_disjunctive_3():
    input1 = set()
    input2 = set()
    expected = False
    assert disjunctive(input1,input2) == expected, 'неправильно проверили два множества на дизъюнкцию'

# Функция должна принимать переменное количество аргументов и возвращать новое множество.

def test_create_set_1 ():
    input1 = 2
    input2 = "привет"
    input3 = 1.5
    input4 = ("mir",555)
    expected = {1.5, 2, 'привет', ('mir', 555)}
    assert create_set(input1,input2,input3,input4) == expected, 'неправильно нашли новое множество'

def test_create_set_2 ():
    input1 = 2
    input2 = 7777
    expected = {2, 7777}
    assert create_set(input1,input2) == expected, 'неправильно нашли новое множество'

def test_create_set_3 ():
    input1 = 2
    input2 = "привет"
    input3 = 1.7
    input4 = "привет"
    expected = {'привет', 2, 1.7}
    assert create_set(input1,input2,input3,input4) == expected, 'неправильно нашли новое множество'

# Создайте функцию для объединения двух словарей.

def test_merge_dict_1():
    input1 = {"Irina": 25, "Ivan" : 24, "Anton" : 33}
    input2 = {"Ivan": 11, "Dima" : 56, "Oleg" : 63}
    expected = {'Irina': 25, 'Ivan': 11, 'Anton': 33, 'Dima': 56, 'Oleg': 63}
    assert merge_dict(input1,input2) == expected, 'неправильно объединили два словаря'

def test_merge_dict_2():
    input1 = {"Ivan" : 33, "Anton" : 1}
    input2 = {"Dima" : 3}
    expected = {'Ivan': 33, 'Anton': 1, 'Dima': 3}
    assert merge_dict(input1,input2) == expected, 'неправильно объединили два словаря'

def test_merge_dict_3():
    input1 = {}
    input2 = {}
    expected = {}
    assert merge_dict(input1,input2) == expected, 'неправильно объединили два словаря'
