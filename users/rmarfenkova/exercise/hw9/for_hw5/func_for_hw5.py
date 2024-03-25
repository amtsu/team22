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