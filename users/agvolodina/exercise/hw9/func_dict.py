#Создайте функцию create_dictionary для создания словаря с заданными ключами и значениями.
def create_dictionary (key, value):
    new_dictionary = {key:value}
    return new_dictionary
    
#Напишите функции add_student и remove_student для добавления и удаления студентов из словаря.
def add_student (dict_student, key, value):
    dict_student[key] = value
    return dict_student

def remove_student (dict_student, key):
    del dict_student[key]
    return dict_student
#Напишите функции add_fruit и remove_fruit для добавления и удаления фруктов, их количества и стоимости в списки fruits_quantity и fruits_prices.
#функция добавляет фрукт и его количество в словарь
def add_fruit (dict_fruit, fruit, quantity):
    dict_fruit[fruit] = quantity
    return dict_fruit

#функция добавляет опреденное количество к имеющимся фруктам
def add_fruit_2 (dict_fruit, fruit, quantity):
    dict_fruit[fruit] = dict_fruit[fruit] + quantity
    return dict_fruit

#функция удаляет фрукт и его количество из словаря
def remove_fruit (dict_fruit, fruit):
    dict_fruit.pop(fruit)
    return dict_fruit

#функция удаляет определенное количество фруктов из словаря
def remove_fruit_2(dict_quantity, fruit, quantity):
    dict_quantity[fruit] = dict_quantity[fruit] - quantity
    return dict_quantity

#Создайте функцию для объединения двух словарей.
def dict_update (dict1, dict2):
    return dict1|dict2

#Создайте функцию для удаления элемента из словаря по заданному ключу.
def dict_pop (dict1, key):
    dict1.pop(key)
    return dict1

#Создайте функцию для переворачивания значений и ключей в словаре (принимает на вход словарь, возвращает другой словарь, ключами которого являются значения входного словаря, а значениями - ключи.
def dict_shift (dict1):
    new_dict = {}
    for k,v in dict1.items():
        new_dict[v] = k
    return new_dict

#Создайте функцию для сортировки словаря по ключам в обратном порядке.
def dict_sorting(dict1):
    return dict(sorted(dict1.items(), reverse=True))

#Создайте функцию возвращающую наибольшее значение элемента словаря.
def dict_max_elements(dict1):
    return max(dict1.items())

#Создайте функцию для поиска наибольшего значения в словаре.
def dict_max(dict1):
    return max(dict1.values())