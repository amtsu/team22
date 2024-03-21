'''I. ИЗ hw-5-part-1.ipynb '''

def create_set_1():
    '''Создает множество set1 из целых чисел: 1, 2, 3, 4, 5'''
    set1 = {1, 2, 3, 4, 5}
    return set1

set1 = {1, 2, 3, 4, 5}
def add_element_to_set(set1):
    '''Добавляем в это множество элемент 6'''
    set1.add(6)
    return set1

def remove_element_from_set(set1):
    '''Удаляем элемент 2 из множества '''
    set1.remove(2)
    return set1  


x = 3
def has_element_in_set(set1, x):
    '''Проверьте, содержит ли множество элемент 3'''
    result = x in set1
    return result


def create_set_2():
    '''Создайте второе множество set2 с элементами 4, 5, 6, 7, 8'''
    set2 = {4, 5, 6, 7, 8}
    return set2

set2 = {4, 5, 6, 7, 8}
def find_union_sets(set1, set2):
    '''Найдите объединение множеств set1 и set2'''
    union_sets = set1 | set2
    return union_sets 


def difference_sets(set1, set2):
    '''Найдите разность множеств set1 и set2'''
    difference = set1 - set2
    return difference


def create_sets_of_rainbows(set1, set2):
    ''' Создайте два множества set1 и set2, содержащие цвета радуги: 
    "красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый" 
    и "оранжевый", "зеленый", "голубой", "синий", "Мальвиновый".'''

    set1 = {"красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"}
    set2 = {"оранжевый", "зеленый", "голубой", "синий", "Мальвиновый"}
    return set1, set2


set1 = {"красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"}
set2 = {"оранжевый", "зеленый", "голубой", "синий", "Мальвиновый"}

def intersection_of_sets(set1, set2):
    '''Найдите пересечение множеств set1 и set2'''
    intersection_set = set1 & set2
    return intersection_set


def union_sets_in_new_set(set1, set2):
    '''Объедините множества set1 и set2 и сохраните результат в новое множество rainbow_colors'''
    rainbow_colors = set1 | set2
    return rainbow_colors



'''II. ИЗ hw-5-part-2.ipynb '''


