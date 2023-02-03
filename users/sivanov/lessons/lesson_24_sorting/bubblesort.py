#!/usr/local/bin/python
# coding: utf-8
"""
модуль с сортировкой пузырьком
попробую быстренько слабать
"""
from usefulstuff import (
    ColoredStr,
    generate_random_list,
    LocalLog,
)
#-------------------------------------------------------------------------------
llog = LocalLog(False)
def bubble_sort(data:list) -> list :
    """
    функция простой  сортировки входного массива пузырьком
    """
    bold_red_text = ColoredStr("red, bold")
    bold_blue_text = ColoredStr("blue, bold")
    data_size = len(data)
    swapped = True
    #for index2 in range(0, data_size):
    while(swapped):
        swapped = False
        for index in range(0,data_size-1):
            # пока тут в цикле напечатаю а там посмотрим
            str_to_print = ""
            red_index = index + 1
            blue_index = index
            if data[index] > data[index+1]:
                red_index = index
                blue_index = index + 1
            for index_p in range(0, data_size):
                if index_p == red_index:
                    str_to_print += bold_red_text(str(data[index_p])) + " "
                elif index_p == blue_index:
                    str_to_print += bold_blue_text(str(data[index_p])) + " "
                else:    
                    str_to_print += str(data[index_p]) + " " 
            if data[index] > data[index+1] :
                #свопнуть элементы
                tmp = data[index+1]
                data[index+1] = data[index]
                data[index] = tmp
                swapped = True

            llog(str_to_print)        
    return data
#-------------------------------------------------------------------------------
def main():
    input_data = generate_random_list(15)
    print(input_data)
    print(bubble_sort(input_data))
#===============================================================================
if __name__ == '__main__':
    llog = LocalLog(True)
    main()