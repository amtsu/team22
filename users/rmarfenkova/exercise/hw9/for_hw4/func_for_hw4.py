import pytest

def create_lists():
    """
    функция добавляет в конец списка элемент
    """
    list_one = [1, 2, 3, 4, 5, 6, 9]
    list_one.append(789)
    return list_one
    
def creat_list(abc): 
    """
    функия делает каждый элемент списка отдельным элементом
    каждое слово отдельным элементом
    каждую строку отдельным элементом
    """
    creat1 = list(abc)
    creat2 = (abc).split(" ")
    creat3 = (abc).split("\n")
    return creat1, creat2, creat3
    
def len_list(abc):
    """
    функция выводит длинну списков
    """
    len_creat1 = len(abc)
    len_creat2 = len((abc).split(" "))
    len_creat3 = len((abc).split("\n"))
    return len_creat1, len_creat2, len_creat3

################### добавила еще функций ################################
def solyanka(my_list):
    """
    функция считает количество элементов списка
    """
    len_list = len(my_list)
    return len_list
    
def element_5_solaynki(my_list):
    """
    Выведите на экран тип пятого от начала списка элемента
    """
    for index, item in enumerate(my_list):
        if index == 4:
            return type(item)
            
def add_element(my_list, element):
    """
    функция добавляет элемент в конец списка и определяет тип последнего элемента
    """
    my_list.append([element])
    return my_list, type(my_list[-1])

def swap_elements(my_list):
    """
    функция меняет местами стретий и пятый элементы
    """
    if len(my_list) >= 5:
        my_list[2], my_list[4] = my_list[4], my_list[2]
    return my_list
    
##########################################################################
def fibonacci_list_check(my_list):
    len_sequence = len(my_list)
    repeating_element = my_list.count(1)
    return len_sequence, repeating_element

def check_fibonacci_numbers(my_list):
    numbers_to_check = [21, 33, 987, 9999]
    results = {}
    for number in numbers_to_check:
        if number in my_list:
           results[number] = True
        else:
            results[number] = False
    return results

def laws_of_the_Programmer():
    true_story_list = ['Пуд багов съевший, выше ценит чистый код.']
    true_story_list .append('Кто дошик ел, тот рейтинг ценит свой.')
    true_story_slice = ['Кто дошик ел, тот рейтинг ценит свой.Кто крашился, тот знает, что живой.']
    true_story_list .append(true_story_slice)
    true_story_slice .clear()
    true_story_list .insert(0,' Кто битым за дедлайн был,')
    del true_story_list [-1]
    true_story_list .insert(1,'тот больше не сольется.' )
    true_story_tail = ['Кто крашился, тот знает, что живой.'] * 2
    true_story_list .extend(true_story_tail)
    del true_story_list[4]
    
    return true_story_list


    