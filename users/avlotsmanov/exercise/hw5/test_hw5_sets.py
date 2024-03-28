import pytest
from hw5_sets import *

set1 = {0, 1, 2, 3, 4, 5, 6, 8}
set2 = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
set3 = {14, 15, 16}
set4 = {1, 2, 3}
set5 = {3, 6, 9, 11, 14}
set0 = set()

s1 = 5

#тесты к функции set_union

def test_set_union_pos_1():
    assert set_union(set1, set2) == {
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    }

def test_set_union__pos_2():
    assert set_union(set1, set3) != {1,2}
    
def test_set_union_neg_1():
    try:
        set_union(s1, set3)
    except TypeError:
        assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"
        
def test_set_union_neg_2():
    try:
        set_union([2,3], set3)
    except TypeError:
        assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

#тесты к функции set_difference

def test_set_difference_pos_1():
    assert set_difference(set1, set2) == {0, 1, 2}

def test_set_difference_pos_2():
    assert set_difference(set(), set()) == set()

def test_set_difference_pos_3():
    assert set_difference(set1, set0) == {0, 1, 2, 3, 4, 5, 6, 8}

def test_set_difference_neg_1():
    try:
        set_difference({1, 2}, {12, 2})
    except TypeError:
        assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"
        
def test_set_difference_neg_2():
    try:
        set_difference({1, 2}, 3)
    except TypeError:
        assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

def test_set_difference_neg_3():
    assert set_difference(set1, set3) == {
        0, 1, 2, 3, 4, 5, 6, 8
    }

#тесты к функции is_subset
def test_is_subset_pos_1():
    assert is_subset(set4, set1) == True
    
def test_is_subset_pos_2():
    assert is_subset(set0, set1) == True

def test_is_subset_neg_1():
    assert is_subset(set2, set1) == False

def test_is_subset_neg_2():
    try:
        is_subset(5, set1)
    except TypeError:
        assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

#тесты к функции combine sets

def test_combine_sets_pos_1():
    assert combine_sets(set1, set2, set3, set4) == {
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
    }

def test_combine_sets_pos_2():
    assert combine_sets(set1, set2, set3) == {
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
    }

def test_combine_sets_pos_3():
    assert combine_sets(set1, set2) == {
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    }

def test_combine_sets_pos_4():
    assert combine_sets(set1, set2, set3) != {1,2}

def test_combine_sets_pos_5():
    assert combine_sets(set(), set(), set0) == set()

def test_combine_sets_neg_1():
    try:
        combine_sets(
            {1, 2}, 3, {2, 4, 8, 9}
        )
    except TypeError:
        assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

def test_combine_sets_neg_2():
    try:
        combine_sets(
            {1, 2},
            [2, 3, 5],
            {2, 4, 8, 9}
        )
    except TypeError:
        assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

#тесты к функции intersect_sets

def test_intersect_sets_pos_1():
    assert intersect_sets(set1, set2, set4, set5) == {3}

def test_intersect_sets_pos_2():
    assert intersect_sets(set1, set2, set3) == set()

def test_intersect_sets_pos_3():
    assert intersect_sets(set1, set2) == {
        3, 4, 5, 6, 8
    }
    
def test_intersect_sets_neg_1():
    try:
        intersect_sets(
            {1, 2}, 2, {2, 4, 8, 9}
        )
    except TypeError:
        assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

def test_intersect_sets_neg_2():
    try:
        intersect_sets(
            {1, 2}, [2, 3, 5], {2, 4, 8, 9}
        )
    except TypeError:
        assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

#тесты к функции delete_value

def test_delete_value_pos_1():
    assert delete_value(1, {1, 2, 3, 4, 5}) == {2, 3, 4, 5}

def test_delete_value_pos_2():
    assert delete_value(3, {1, 2, 3, 4, 5}) == {1, 2, 4, 5}

def test_delete_value_neg_1():
    try:
        delete_value(
            {1, 2}, {1, 2, 4, 8, 9}
        )
    except UnboundLocalError:
         assert True
    else:
        assert False, "Функция не вызвала исключение UnboundLocalError"

#тесты к функции equal_sets

def test_equal_sets_pos_1():
    assert equal_sets({1, 2, 3}, {1, 2, 3}) == True

def test_equal_sets_pos_2():
    assert equal_sets({1, 2, 3}, {4, 5, 6}) == False

def test_equal_sets_neg_1():
    try:
        equal_sets(
            {1, 2}, {1, 2}, {1, 2}
        )
    except TypeError:
         assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

def test_equal_sets_neg_2():
    try:
        equal_sets({1,2}, [1,2])
    except TypeError:
         assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

#тесты к функции combine_3sets

def test_combine_3sets_pos_1():
    assert combine_3sets({1}, {2, 3}, {4, 5, 6}) == {1, 2, 3, 4, 5, 6}

def test_combine_3sets_neg_1():
    try:
        combine_3sets({2, 3}, {4, 5, 6})
    except TypeError:
         assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

#тесты к функции diffrent_sets
def test_diffrent_sets_pos_1():
    assert diffrent_sets({1, 2, 3}, {1, 2, 3}) == False

def test_diffrent_sets_pos_2():
    assert diffrent_sets({1, 2, 3}, {4, 5, 6}) == True

def test_diffrent_sets_pos_3():
    assert diffrent_sets({1, 2, 3}, set0) == True

def test_diffrent_sets_neg_1():
    try:
        diffrent_sets({1, 2, 3}, 4)
    except TypeError:
         assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"
def test_diffrent_sets_neg_2():
    try:
        diffrent_sets({1, 2, 3})
    except TypeError:
         assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"
#тесты к функции symm_difference_sets
def test_symm_difference_sets_pos_1():
    assert symm_difference_sets(set3, set4) == {1, 2, 3, 14, 15, 16}

def test_symm_difference_sets_pos_2():
    assert symm_difference_sets(set3, set0)  == {14, 15, 16}
def test_symm_difference_sets_pos_3():
    assert symm_difference_sets(set3, set3)  == set()

def test_symm_difference_sets_neg_1():
    try:
        symm_difference_sets({1, 2, 3}, 4)
    except TypeError:
         assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"
def test_symm_difference_sets_neg_2():
    try:
        symm_difference_sets({1, 2, 3})
    except TypeError:
         assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"

#тесты к функции create_set
def test_create_set_pos_1():
    assert create_set(
        1 ,2, 3, 4, 5, 6, 7, '1234') == {1, '1234', 2, 3, 4, 5, 6, 7}

def test_create_set_pos_2():
    assert create_set() == set()

def test_create_set_neg_1():
    try:
        create_set({1, 2, 3}, {1, 3})
    except TypeError:
         assert True
    else:
        assert False, "Функция не вызвала исключение TypeError"
    