

def add_element(set1):
    '''Добавляем в это множество элемент 6'''
    set1.add(6)
    return set1

def remove_element(set1, rem):
    '''Удаляем элемент 2 из множества '''
    if rem in set1:
        set1.remove(rem)
        return set1  



def element_in_set(set1, x):
    '''Проверьте, содержит ли множество элемент 3'''
    result = x in set1
    return result



def union_sets(set1, set2):
    '''Найдите объединение множеств set1 и set2'''
    union_set = set1.union(set2)
    return union_set 


def difference_sets(set1, set2):
    '''Найдите разность множеств set1 и set2'''
    difference_set = set1.difference(set2)
    return difference_set

def intersection_of_sets(set1, set2):
    '''Найдите пересечение множеств set1 и set2'''
    intersection_set = set1.intersection(set2)
    return intersection_set






