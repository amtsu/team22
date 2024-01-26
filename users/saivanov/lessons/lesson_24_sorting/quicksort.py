#!/usr/local/bin/python
# coding: utf-8
"""
модуль с быстрой сортировкой
"""
from usefulstuff import (
    ColoredStr,
    generate_random_list,
    LocalLog,
)
#-------------------------------------------------------------------------------
llog = LocalLog(False)
def swap(data:list, first: int, second : int) -> None :
    """
    меняет местами элементы data с индексами first и second
    портит data (сохраняет изменения в него же)
    """
    tmp = data[first]
    data[first] = data[second]
    data[second] = tmp
#-------------------------------------------------------------------------------
def split(data: list, left:int, right:int) -> int : 
    """
    распределяет исходный массив на два относительно самого правого элемента
    возвращает индекс этого элемента в результирующем массиве
    слева от него не большие значения
    справа - большие
    портит data    
    """
    special_x = data[right];
    less = left;
    for index in range(left,right):
        if data[index] <= special_x :
            swap(data, index, less)
            less+=1
    swap(data, less, right);
    return less
#-------------------------------------------------------------------------------
def quick_sort_do_stuff(data: list, left:int, right:int) -> list:
    """
    главный воркер быстрой сортировки
    распределяет элементы
    рекурсивно вызывает сама себя для половинок
    """
    if left < right :
        selected_x = split(data, left, right)
    #----------------------
        bold_green_text = ColoredStr("green, bold")
        bold_red_text = ColoredStr("red, bold")
        data_str = ""
        for index in range(len(data)):
            if (index >= left) and (index <= selected_x - 1):
                data_str += bold_green_text(str(data[index])) + ", "
            elif (index >= selected_x + 1) and (index <= right):
                data_str += bold_red_text(str(data[index])) + ", "
            else:
                data_str += (str(data[index])) + ", "
        llog(data_str)
     #----------------------
        quick_sort_do_stuff(data, left, selected_x - 1)
        quick_sort_do_stuff(data, selected_x + 1, right)
    
#-------------------------------------------------------------------------------
def quick_sort(data:list) -> list :
    """
    функция быстрой сортировки входного массива:
    выбираем опорный элемент, и перемещаем элементы, превосходящие его правее,
    а непревосходящие левее. к каждой из частей массива применяем рекурсивно 
    этот же алгоритм    
    """
    data_size = len(data)
    quick_sort_do_stuff(data, 0, data_size-1);
    return data
#-------------------------------------------------------------------------------
def main():
    input_data = generate_random_list(30)
    print(input_data)
    print(quick_sort(input_data))
#===============================================================================
if __name__ == '__main__':
    llog = LocalLog(True)
    main()