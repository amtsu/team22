#!/usr/local/bin/python
# coding: utf-8
"""
модуль тестирования для сортировки выбором
попробую быстренько слабать
"""
from quicksort import(
    quick_sort,
    swap
)
def test_swap_1():
    """
    один из тестов swap
    """
    data = [1,0]
    swap(data,0,1)
    assert data == [0,1]
def test_swap_2():
    """
    один из тестов swap
    """
    data = [1,0,2]
    swap(data,0,1)
    assert data == [0,1,2]    
def test_swap_3():
    """
    один из тестов swap
    """
    data = [2,1,0]
    swap(data,1,2)
    assert data == [2,0,1]
def test_swap_4():
    """
    один из тестов swap
    """
    data = [2]
    swap(data,0,0)
    assert data==[2]   
def test_swap_5():
    """
    один из тестов swap
    """
    data = [2,2,3,4,5,6,7,8,9]
    swap(data,4,4)
    assert data == [2,2,3,4,5,6,7,8,9]    
def test_quick_sort_1():
    """
    один из тестов сортировки
    """
    assert quick_sort([1,0])==[0,1]
    
def test_quick_sort_2():
    """
    один из тестов сортировки
    """
    assert quick_sort([3,2,1]) == [1,2,3]
    
def test_quick_sort_3():
    """
    один из тестов сортировки
    """
    assert quick_sort([5]) == [5]

def test_quick_sort_4():
    """
    один из тестов сортировки
    """
    assert quick_sort([5,5,3,4,2,2,1,5]) == [1,2,2,3,4,5,5,5]

def test_quick_sort_5():
    """
    один из тестов сортировки
    """
    given   =  [14, 8, 14, 15, 8, 5, 2, 2, 10, 10, 7, 9, 15, 10, 11]
    expected = [2, 2, 5, 7, 8, 8, 9, 10, 10, 10, 11, 14, 14, 15, 15]
    assert quick_sort(given) == expected 