def make_set(number):
    """
    функция создает множество из заданых целых чисел
    """
    my_set = set(number)
    return my_set

def add_in_set(my_set, number):
    """
    функция добавляет число в множество, на выходе новое множество
    """
    my_set.add(number)
    return my_set

def remove_number_in_set(my_set, number):
    """
    функция удаляет заданное число из множества
    """
    if number in my_set:
        my_set.discard(number)
    return my_set

def element_in_set(my_set, element):
    """
    функция проверяет наличие элемента во множестве
    """
    if element in my_set:
        return True
    else:
        return False

################# СЛОВАРИ ################################

def make_dict(name, age, city):    ## не понравилось не получится с ними дальше что то сделать
    """
    функуия принимает три параметра и выводит готовый словарь
    """
    my_dict = {
        "name": name,
        "age": age,
        "city": city
    }
    return my_dict

def make_dict_new(name, age, city, mail):   ## не понравилось не получится с ними дальше что то сделать
    """
    функуия принимает 4 параметра и выводит готовый словарь
    """
    my_dict = {
        "name": name,
        "age": age,
        "city": city,
        "mail": mail
    }
    return my_dict

# переделала
def create_person(my_dict):
    """
    принимает словарь, возвращает словарь
    """
    return my_dict

def create_person_add(my_dict, key, value):
    """
    функция принимает словарь, ключ и знаение, возвращает словарь с добавленным ключом и значением, если такого ключа не было
    """
    if key not in my_dict:
        my_dict[key] = value
    return my_dict

def remove_key_in_my_dict(my_dict, key):
    """
    функция принимает словарь и ключ, удаляет ключ если он иммется в словаре
    """
    if key in my_dict:
       del my_dict[key]
    return my_dict

def sum_value(my_dict):
    """
    функция складывает все значения словаря
    """
    total_sum = 0
    for key, value in my_dict.items():
        total_sum += value
    return total_sum

def pop_key_in_dict(my_dict, key):
    """
    функция удаляет ключ из словаря, если его нет - выводит сообщение о его отсутствии
    """
    return my_dict.pop(key, "there is no such switch")

def add_key_value_in_dict(my_dict, key, value):
    """
    функция добавляет новый ключ и значение если их нет в словаре
    """
    if key not in my_dict:
        my_dict[key] = value
    return my_dict
        
################# УСЛОВНЫЕ ОПЕРАТОРЫ ################################    
    

def add_fruit_in_dict(my_dict, my_key, my_value):
    """
    функция добавляет новый ключ и значение в словарь
    """
    if my_key not in my_dict:
        my_dict[my_key] = my_value
    return my_dict
    
def keys_with_value_greater_than(my_dict, threshold):
    """
    функция выводит все ключи, у которых значения выше заданного порога
    """
    items = []
    for key, value in my_dict.items(): 
        if value > threshold:
            items.append(key)
            
    return items

def cycle_element_of_set(my_set):
    """
    функция выводит в список все уникальные элементы множества
    """
    all_element = []
    for element in my_set:
        all_element.append(element)
    return all_element

def cycle_number(a, b):
    """
    функция возвращает список квадратов чисел от a до b
    """
    squares = []
    while a <= b:
        squares.append(a ** 2)
        a += 1
    return squares
