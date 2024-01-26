#!/usr/local/bin/python
# coding: utf-8
"""
модуль с сортировкой вставками
попробую быстренько слабать
"""
from usefulstuff import (
    ColoredStr,
    generate_random_list,
    LocalLog,
)
#-------------------------------------------------------------------------------
llog = LocalLog(False)
def insertion_sort(data:list) -> list :
    """
    сортировка вставками
    Берем по элементу из исходного списка и вставляем в результирующий список
    между большим и меньшим элементами
    """
    bold_blue_text = ColoredStr("blue, bold")
    result = []
    for item in data:
        index = len(result)
        while index >0:
            if result[index-1] < item:
                break
            index -= 1    
        result.insert(index,item)
        result_str = ""
        for rindex in range(len(result)):
            if(rindex == index):
                result_str += bold_blue_text(str(result[rindex]))+", "
            else:
                result_str += (str(result[rindex]))+", "
        llog(result_str)
    return result
#-------------------------------------------------------------------------------
def main():
    input_data = generate_random_list(15)
    print(input_data)
    print(insertion_sort(input_data))
#===============================================================================
if __name__ == '__main__':
    llog = LocalLog(True)
    main()