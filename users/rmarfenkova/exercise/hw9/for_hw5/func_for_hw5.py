

##################### МНОЖЕСТВА #####################################
def set_union(set1, set2):
    """
    функция объединения двух множест
    """
    return set1.union(set2)

def set_difference(set1, set2):
    """
    функция разности двух множест
    """
    return set1.difference(set2)

def is_subset(set1, set2):
    """
    функция проверяет является ли одно множество подмножеством другого
    """
    return set1.issubset(set2)

def union_sets(*sets):
    """
    объединяет несколько множеств в одно
    """
    result_set = set()
    for s in sets:
        result_set.update(s)
    return result_set

def remove_element(some_set, element):
    """
    функция для удаления конкретного элемента из множества
    """
    if element in some_set:
        some_set .remove(element)
        return True
    else:
        return False

def find_intersection(*sets):
    """
    функция для поиска пересечения нескольких множеств
    """
    if len(sets) == 0:
        return set()  
    result = sets[0]  
    for s in sets[1:]:  
        result = result.intersection(s)
    return result

def check_equality(set1, set2):
    """
    функция проверки равенства двух множеств
    """
    return set1 == set2 
    
    
def union_of_sets(set1, set2, set3):
    """
    функция для нахождения объединения трех множеств
    """
    return set1 .union(set1, set3)

def is_disJoint(set1, set2):
    """
    функция проверяет, я вляются ли множества дизъюктивными
    """
    return set1 .isdisjoint(set2)

def set_difference(set1, set2):
    """
    функция нахождения разности двух множеств
    """
    return set1 - set2
    
def symmetric_difference(set1, set2):
    """
    функция нахождения симметрической разности разности двух множеств
    """
    return set1 .symmetric_difference(set2)

def create_set(*elements):
    """
    функция создает множество с заданными элементами
    """
    return set(elements)

##################### СЛОВАРИ #####################################

def create_dictionary(**kwargs):
    """
    Функция создает словарь с заданными ключами и значениями.
    Принимает словарь в формате ключ-значение и возвращает созданный словарь.
    """
    new_dict = {}
    for key, value in kwargs .items():
        new_dict[key] = value
    return new_dict

def add_student(students_dict, student_id, student_name):
    """
    функция добавления студента в заданный словарь. 
    """
    students_dict[student_id] = student_name
    return students_dict
    
    

def remove_student(students_dict, student_id):
    """
    функция удаляет студента в заданном словаре. Если
    """
    if student_id in students_dict:
        del students_dict[student_id]
    return students_dict



#def add_fruit(fruits_quantity, fruits_prices, fruit, quantity, price):
#    """
#    Добавляет фрукт, его количество и стоимость в списки. 
#    """
#    fruits_quantity = {}
#    fruits_prices = {}
#    if fruit_name in fruits_quantity:
#        fruits_quantity[fruit_name] += quantity
#    else:
#        fruits_quantity[fruit_name] = quantity
#        fruits_prices[fruit_name] = price
    

#def remove_fruit(fruits_quantity, fruits_prices, fruit):
#    """
#    Удаляет фрукт и его количество и стоимость из списков.
#    """
#    if fruit in fruits_quantity:
#        del fruits_quantity[fruit]
#    if fruit in fruits_prices:
#        del fruits_prices[fruit]
#    return 
def merge_dicts(dict1, dict2):
    """
    функция объединеня двух словарей
    """
    return {**dict1, **dict2}

def remove_item(dictionary, key):
    """
    Функция удаляет элемент из заданого словаря по ключу
    """
    if key in dictionary:
        del dictionary[key]
    return dictionary

def reverse_dict(input_dict):
    """
    функия переворачивает значение и ключ в словаре
    """
    return {value: key for key, value in input_dict.items()}

def sort_dict_reverse(input_dict):
    """
    функция для сортировки ключей в словаре, в обратном порядке
    """
    sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[0], reverse=True))
    return sorted_dict

def max_value_in_dict(input_dict):
    """
    функция возвращает наибольшее значение словаря
    """
    if not input_dict:
        return None
    return max(input_dict.values())