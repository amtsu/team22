

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
    
#############################


def add_student(students_dict, student_id, student_name):
    """
    функция добавления студента в заданный словарь. 
    """
    students_dict[student_id] = student_name
    return students_dict
    
#############################    

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
#############################


def remove_item(dictionary, key):
    """
    Функция удаляет элемент из заданого словаря по ключу
    """
    if key in dictionary:
        del dictionary[key]
    return dictionary
    
#############################


def reverse_dict(input_dict):
    """
    функия переворачивает значение и ключ в словаре
    """
    return {value: key for key, value in input_dict.items()}
    
#############################


def sort_dict_reverse(input_dict):
    """
    функция для сортировки ключей в словаре, в обратном порядке
    """
    sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[0], reverse=True))
    return sorted_dict
#############################


def max_value_in_dict(input_dict):
    """
    функция возвращает наибольшее значение словаря
    """
    if not input_dict:
        return None
    return max(input_dict.values())
    
#############################

def check_age(students_dict, student_name):
    """
    функция проверяет совершеннолетний ли студент.
    принимает словарь и имя студента.
    """
    age = students_dict.get(student_name)
    if age is None:
        return "Студент не найден в базе данных"
    
    elif age >= 18:
        return f"{student_name} совершеннолетний"
   
    else:
        return f"{student_name} несовершеннолетний"
        
#############################

def compare_sets_length(set1, set2):
    """
    функция сравнивает длинну множества и выводит, какое множество длиннее.
    """
    if isinstance(set1, set) or isinstance(set2, set):
        if len(set1) > len(set2):
            return f"{set1} длиннее {set2}"
        elif len(set1) < len(set2):
            return f"{set2} длиннее {set1}"
        else:
            return f"{set2} равно {set1}"
    else:
        return f"{set1} или {set2} не множество"
        
#############################

def check_even_odd(number):
    """
    функция проверяет четное ли число.
    """
    if type(number) is int:
        if number % 2 == 0:
            return "Число {} является четным".format(number)
        else:
            return "Число {} является нечетным".format(number)
    else:
        return f"'{number}' может быть только типа int"
        
#############################


def is_leap_year(year):
    """
    функция проверяет високостность года
    """
    if type(year) is int and year >= 0:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return f"{year} - високосный"
        else:
            return f"{year} - не високосный"
    else:
        return "Введены неверные данные"
        
#############################

def is_palindrome(s):
    """
    функция проверяет, является ли строка полиандропом
    """
    if type(s) is str:
        s = s.lower().replace(" ", "") 
        if s == s[::-1]:
            return f"{s} Строка является палиндромом"
        else:
            return f"{s} Строка не является палиндромом"
    else:
        return f"{s} не строка"
        
#############################

def is_prime(number):
    """
    функция проверяет является ли число простым
    """
    if type(number) != int or number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
    
#############################


def check_date(day, month, year):
    """
    функция проверяет, является ли введенная дата корректной
    """
    if day < 1 or day > 31:
        return False
        
    if month < 1 or month > 12:
        return False
        
    if year < 1582 and year > 2024:
        return False
        
    if month in [4, 6, 9, 11] and day > 30:
        return False
        
    elif  month == 2:
        
        if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
            
            if day > 29 or day > 28:
                return False
    return True
    
#############################

def check_date(day, month, year):
    """
    функция проверяет, является ли введенная дата корректной
    """
    if type(day) is int and type(month) is int and type(year) is int:
        if day < 1 or day > 31:
            return False
        
        if month < 1 or month > 12:
            return False
        
        if year < 1582 or year > 2024:
            return False
        
        if month in [4, 6, 9, 11] and day > 30:
            return False
        
        elif  month == 2:
        
            if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
            
                if day > 29 or day > 28:
                  return False
    else:
        return "Вы можете ввести только числа"
    return True

#############################

