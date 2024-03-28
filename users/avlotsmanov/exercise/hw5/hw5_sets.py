def set_union(
    set_1,
    set_2
):
    '''Операция объединения двух множеств
    :param set1: первое множество
    :param set2: второе множество
    :return: объединенное множество
    '''
    sum_set = set([])
    for s1 in set_1:
        sum_set.add(s1)
    for s2 in set_2:
        sum_set.add(s2)
    return sum_set


def set_difference(
    set_1,
    set_2
):
    '''Операция разности двух множеств
    :param set1: первое множество
    :param set2: второе множество
    :return: разность множеств в виде множества
    '''
    dif_set = []
    for s1 in set_1:
        dif_set += [s1]
    for s2 in set_2:
        if s2 in dif_set:
            dif_set.remove(s2)
        else:
           continue
    return set(dif_set)


def is_subset(
    set_1, 
    set_2
):
    '''Проверяет является ли первое множество подмножеством второго
    :param set1: первое множество
    :param set2: второе множество
    :return: True or False
    '''    
    ret = False
    if len(set_1) <= len(set_2):
        temp_set = set_1 - set_2
        if len(temp_set) == 0:
            print(f'Множество {set_1} является подмножеством {set_2}')
            ret = True
        else:
            print(f'Множество {set_1} не является подмножеством {set_2}')
    else:
        temp_set = set_2 - set_1
        if len(temp_set) == 0:
            print(f'Множество {set_2} является подмножеством {set_1}')
        else:
            print(f'Множество {set_2} не является подмножеством {set_1}')
    return ret

def combine_sets(
    *sets
):
    '''Объединенияет нескольких множеств
    :param *set: некоторое количество множеств
    :return: объединенное множество
    '''    
    sum_set = set()
    for s in sets:
        sum_set = sum_set.union(s)
    return sum_set

def intersect_sets(
    *sets
):
    '''Ищет пересечение нескольких множеств
    :param *set: некоторое количество множеств
    :return: Пересечение нескольких множеств
    ''' 
    sum_set = set()
    for s in sets:
        sum_set = sum_set.union(s)
    for s in sets:
        sum_set = sum_set & s
    return sum_set

def delete_value(
    x,
    set1
):
    '''Удаляет заданный элемент из множества
    :param x:   элемент, который надо удалить
    :param set: некоторое количество множеств
    :return: множество без заданного элемента
    '''  
    for s in set1:
        if s == x:
            set2 = set1 - set([x])
        else:
            continue
    return set2

def equal_sets(
    set_1,
    set_2
):
    '''Проверяет равны ли два множества
    :param set1: первое множество
    :param set2: второе множество
    :return: True or False
    ''' 
    if len(set_1) >= len(set_2):
        x = len(set_1 - set_2)
    else:
        x = len(set_2 - set_1)
    if x == 0 and len(set_1) != 0:
        print(f'Множества {set_1} и {set_2} равны')
        return True
    elif len(set_1) == 0 and len(set_2) == 0:
        print(f'Множества {set_1} и {set_2} равны, они пустые')
        return True
    else:
        print(f'Множества {set_1} и {set_2} не равны')
        return False

def combine_3sets(
    set1,
    set2,
    set3
):
    '''Складывает три множества
    :param set1: первое множество
    :param set2: второе множество
    :param set3: третье множество
    :return: суммарное множество
    ''' 
    sum_set = set1 | set2 | set3
    return sum_set

def diffrent_sets(
    set1,
    set2
):
    '''Проверяет являются ли два множества дизъюнктивными
    :param set1: первое множество
    :param set2: второе множество
    :return: True or False
    ''' 
    dif_set = set1 - set2
    if len(dif_set) == len(set1):
        print(f'Множества {set1} и {set2} являются дизъюнктивными')
        return True
    else:
        print(f'Множества {set1} и {set2} не являются дизъюнктивными')
        return  False

def symm_difference_sets(
    set1,
    set2
):
    '''Ищет симметричную разность двух множеств
    :param set1: первое множество
    :param set2: второе множество
    :return: Симметричная разность двух множеств
    ''' 
    dif_set = (set1 - set2) | (set2 - set1)
    return dif_set

def create_set(*values):
    '''Содает множество из заданных элементов
    :param *set1: элементы
    :return: множество переданных элементов
    ''' 
    m = []
    for value in values:
        m.append(value)
    return set(m)

