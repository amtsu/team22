import pytest

def create_lists():
    """
    функция добавляет в конец списка элемент
    """
    list_one = [1, 2, 3, 4, 5, 6, 9]
    list_one.append(789)
    return list_one
    
def creat_list(abc): 
    creat1 = list(abc)
    creat2 = (abc).split(" ")
    creat3 = (abc).split("\n")#
    return creat1, creat2, creat3
    
def len_list(abc):  
   len_creat1 = len(abc)
   len_creat2 = len((abc).split(" "))
   len_creat3 = len((abc).split("\n"))
   return len_creat1, len_creat2, len_creat3

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


    