def create_dictionary(
    tuple_keys, 
    tuple_values
):
    ''' Создает словарь из переданных элементов
    :param tuple_keys: кортеж с ключами
    :param tuple_values: кортеж с значениями
    '''
    if type(tuple_keys) is not tuple or type(tuple_values) is not tuple:
        raise TypeError
    new_dict = dict()
    if len(tuple_keys) != len(tuple_values):
        raise ValueError ('Кортежи должны быть одинаковых размеров')
    else:
        for i in range(len(tuple_keys)):
            new_dict[tuple_keys[i]] = tuple_values[i]
    return new_dict

def add_students(
    students_dict,
    tuple_keys,
    tuple_values
):
    '''Добавления студентов и их возрастов в словарь
    :param students_dict: словарь студентов в формате {фамилия:возраст}
    :param tuple_keys: кортеж с фамилиями
    :param tuple_values: кортеж с возрастом
    '''
    if len(tuple_keys) != len(tuple_values):
        raise ValueError ('Кортежи должны быть одинаковых размеров')
    else:
        for i in range(len(tuple_keys)):
            students_dict[tuple_keys[i]] = tuple_values[i]
    return students_dict

def remove_students(
    students_dict,
    tuple_keys
):
    ''' Удаление студентов из словаря
    :param students_dict: словарь студентов в формате {фамилия:возраст}
    :param tuple_keys: кортеж с фамилиями
    '''
    for i in range(len(tuple_keys)):
            del students_dict[tuple_keys[i]]
    return students_dict

def merge_dict(
    dict1,
    dict2
):
    '''Объединяет два словаря
    :param dict1: первый словарь    
    :param dict2: второй словарь
    :return: объединенный словарь
    '''
    dict12 = dict()
    for key in dict1.keys():
        dict12[key] = dict1[key]
    for key in dict2.keys():
        dict12[key] = dict2[key]
    return dict12

def delete_item(
    dict1,
    keys
):
    '''Удаляет элемент из словаря по заданному ключу
    :param dict1: словарь    
    :param key: ключ элемента который надо удалить
    :return:
    '''
    for key in keys:
        dict1.pop(key)
    return dict1

def reverse_dict(dict1):
    '''Разворачивает словарь
    :param dict1: словарь    
    :return: развернутый словарь
    '''
    reverse_dict = dict()
    for key in dict1.keys():
        reverse_dict[dict1[key]] = key
    return reverse_dict

def max_value_in_dict(dict1):
    '''Ищет наибольшее значение в словаре
    :param dict1: словарь    
    :return: наибольшее значение
    '''
    max_value = max(dict1.values())
    return max_value
