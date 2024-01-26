#!/usr/local/bin/python
# coding: utf-8
"""
модуль с сортировкой выбором
"""
from usefulstuff import (
    ColoredStr,
    generate_random_list,
    LocalLog,
)
#-------------------------------------------------------------------------------
llog = LocalLog(False)
def selection_sort(data:list) -> list :
    """
    функция простой  сортировки входного массива вставками:
    ищем в данных максимум
    меняем местами с последним элементом и забываем про него
    
    """
    bold_green_text = ColoredStr("green, bold")
    bold_red_text = ColoredStr("red, bold")
    bold_blue_text = ColoredStr("blue, bold")
    data_size = len(data)
    for index in range(data_size):
        max_index = 0
        for s_index in range(data_size - index):
            #найти максимум
            if data[s_index] > data[max_index]:
                max_index = s_index
        #свопнуть местами последний и максимальный
        tmp = data[data_size - index - 1]
        data[data_size - index - 1] = data[max_index]
        data[max_index] = tmp
        data_str = ""
        for p_index in range(data_size):
            if(p_index == data_size - index - 1):
                data_str += bold_red_text(str(data[p_index])) + ", "
            elif(p_index == max_index):
                data_str += bold_blue_text(str(data[p_index])) + ", "
            elif(p_index < data_size - index - 1):
                data_str += bold_green_text(str(data[p_index])) + ", "    
            else:
                data_str += (str(data[p_index])) + ", "
        llog(data_str)
    return data
#-------------------------------------------------------------------------------
def main():
    input_data = generate_random_list(15)
    print(input_data)
    print(selection_sort(input_data))
#===============================================================================
if __name__ == '__main__':
    llog = LocalLog(True)
    main()