#!/usr/local/bin/python
# coding: utf-8
"""
модуль тестирования для сортировки пузырьком
попробую быстренько слабать
"""
from insertionsort import(
    insertion_sort,
)
def test_insertion_sort_1():
    """
    один из тестов баблсорта
    """
    assert insertion_sort([1,0])==[0,1]
    
def test_insertion_sort_2():
    """
    один из тестов баблсорта
    """
    assert insertion_sort([3,2,1]) == [1,2,3]
    
def test_insertion_sort_3():
    """
    один из тестов баблсорта
    """
    assert insertion_sort([5]) == [5]

def test_insertion_sort_4():
    """
    один из тестов баблсорта
    """
    assert insertion_sort([5,5,3,4,2,2,1,5]) == [1,2,2,3,4,5,5,5]

def test_insertion_sort_5():
    """
    один из тестов баблсорта
    """
    given   =  [14, 8, 14, 15, 8, 5, 2, 2, 10, 10, 7, 9, 15, 10, 11]
    expected = [2, 2, 5, 7, 8, 8, 9, 10, 10, 10, 11, 14, 14, 15, 15]
    assert insertion_sort(given) == expected 