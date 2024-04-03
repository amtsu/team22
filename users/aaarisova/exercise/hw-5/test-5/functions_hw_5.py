# I. Множества из hw-5-part-1 

def create_set_1(numbers):
    '''функция создает множество set1 из целых чисел'''
    set1 = set(numbers)
    return set1


def add_element_to_set(set1, elem):
    '''функция добавляет в множество элемент '''
    set1.add(elem)
    return set1


def remove_element_from_set(set1, elem):
    '''функция удаляет элемент из множества '''
    set1.remove(elem)
    return set1  


def has_element_in_set(set1, elem):
    '''функция проверяет, содержит ли множество элемент'''
    result = elem in set1
    return result


def create_set_2(elements):
    '''функция создает второе множество set2 с элементами'''
    set2 = set(elements)
    return set2


def find_union_sets(set1, set2):
    '''функция находит объединение множеств set1 и set2'''
    union_sets = set1 | set2
    return union_sets 


def difference_sets(set1, set2):
    '''функция нахождения разности множеств set1 и set2'''
    difference = set1 - set2
    return difference


def create_sets_of_rainbows(set1, set2):
    '''функция создает два множества'''
    return set1, set2


def intersection_of_sets(set1, set2):
    '''Найдите пересечение множеств set1 и set2'''
    intersection_set = set1 & set2
    return intersection_set


def union_sets_in_new_set(set1, set2):
    '''Объедините множества set1 и set2 и сохраните результат в новое множество rainbow_colors'''
    rainbow_colors = set1 | set2
    return rainbow_colors



#II. Словари из hw-5-part-2

def create_dict_person(dict_person):
    '''функция создания словарь'''
    return dict_person


def add_email_to_dict(person_dict, email):
    '''функция добавления в словарь нового ключа со значением электронного адреса'''
    person_dict["email"] = email
    return person_dict 


def del_key_to_dict(person_dict, del_key):
    '''функция удаления ключа из словаря.'''
    del person_dict[del_key]
    return person_dict


def dict_total_of_fruits(fruits_quantity, fruits_prices):
    '''функция подсчета стоимости всех фруктов, имеющихся в наличии'''
    total_cost = sum(fruits_quantity[fruit] * fruits_prices[fruit] for fruit in fruits_quantity)
    return total_cost


def add_stud_to_dict(dict_stud, surname, age):
    '''функция добавления нового студента c возрастом в словарь.'''
    dict_stud[surname] = age
    return dict_stud


#III, IV. Условные операторы, циклы

def adult_person(person):
    '''функция выводит сообщение "Совершеннолетний" или "Несовершеннолетний".'''
    age = int(person['age'])
    if age >= 18:
        return 'Совершеннолетний'
    else:
        return 'Несовершеннолетний'


def compare_sets(set1, set2):
    '''функция сравнивает длину двух множеств и выводит сообщение о том, какое из множеств больше.'''

    x = len(set1) 
    y = len(set2)
    
    if x > y:
        print("set1 > set2") 
        return "set1 > set2"
    elif x < y:
        print("set1 < set2")
        return "set1 < set2"
    else:
        print("set1 = set2")
        return "set1 = set2"


def price_is_over_limit(fruits_prices, num):
    '''Выведите сообщение "Дорогой товар" для продуктов, цена которых превышает указанное число'''
    expensive_fruits = []
    for fruit, price in fruits_prices.items(): 
        if price > num:
            expensive_fruits.append(fruit)
            print(f"Дорогой товар: {fruit}")
    return expensive_fruits

