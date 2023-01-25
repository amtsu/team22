#!/usr/local/bin/python
# coding: utf-8
"""
модуль с сортировкой пузырьком
попробую быстренько слабать
"""
from usefulstuff import (
    ColoredStr,
    generate_random_list,
)
#-------------------------------------------------------------------------------
def bubble_sort(data:list) -> list :
    """
    функция простой  сортировки входного массива пузырьком
    """
    data_size = len(data)
    for index2 in range(0, data_size):
        for index in range(0,data_size-1):
            if data[index] > data[index+1] :
                #свопнуть элементы
                tmp = data[index+1]
                data[index+1] = data[index]
                data[index] = tmp
    return data
#-------------------------------------------------------------------------------
def main():
    input_data = generate_random_list(100)
    print(input_data)
    print(bubble_sort(input_data))
#===============================================================================
if __name__ == '__main__':
    main()