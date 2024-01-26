#!/usr/local/bin/python
# coding: utf-8
"""
модуль тестирования для сортировки выбором
попробую быстренько слабать
"""
from selectionsort import(
    selection_sort,
)
def test_selection_sort_1():
    """
    один из тестов сортировки
    """
    assert selection_sort([1,0])==[0,1]
    
def test_selection_sort_2():
    """
    один из тестов сортировки
    """
    assert selection_sort([3,2,1]) == [1,2,3]
    
def test_selection_sort_3():
    """
    один из тестов сортировки
    """
    assert selection_sort([5]) == [5]

def test_selection_sort_4():
    """
    один из тестов сортировки
    """
    assert selection_sort([5,5,3,4,2,2,1,5]) == [1,2,2,3,4,5,5,5]

def test_selection_sort_5():
    """
    один из тестов сортировки
    """
    given   =  [14, 8, 14, 15, 8, 5, 2, 2, 10, 10, 7, 9, 15, 10, 11]
    expected = [2, 2, 5, 7, 8, 8, 9, 10, 10, 10, 11, 14, 14, 15, 15]
    assert selection_sort(given) == expected 