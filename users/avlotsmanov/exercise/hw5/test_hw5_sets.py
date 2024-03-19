import pytest
from hw5_sets import *

set1 = {0,1,2,3,4,5,6,8}
set2 = {3,4,5,6,7,8,9,10,11,12,13}
set3 = {14,15,16}
set4 = {1,2,3}
set0 = set()

s1 = 5

def test_set_union_pos_1():
    assert set_union(set1, set2) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

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

def test_set_difference_pos_1():
    assert set_difference(set1, set2) == {0, 1, 2}

def test_set_difference_pos_2():
    assert set_difference(set(), set()) == set()

def test_set_difference_pos_3():
    assert set_difference(set1, set0) == {0,1,2,3,4,5,6,8}

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
    assert set_difference(set1, set3) == {0,1,2,3,4,5,6,8}

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