from func_for_list import *

def test_check_1():
    list_name =  ['Vasya', 'Misha', 'Petya']
    znach_1 = 'Petya'
    index_1 = index_search(znach_1, list_name)
    assert index_1 == 2

def test_check2():
    list_name =  ['Vasya', 'Misha', 'Petya']
    znach_2 = 'Vasya'
    index_2 = index_search(znach_2, list_name)
    assert index_2 == 0

def test_check3():
    list_name =  ['Moscow', 'SPB', 'Kazan']
    znach_1 = 'SPB'
    index_1 = index_search(znach_1, list_name)
    assert index_1 == 1

def test_check4():
    list_name =  ['Moscow', 'SPB', 'Kazan']
    znach_1 = 'Kiev'
    index_1 = index_search(znach_1, list_name)
    assert index_1 == None