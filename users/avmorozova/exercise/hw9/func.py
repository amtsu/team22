def make_set(number):
    my_set = set(number)
    return my_set

def element_in_set(my_set, element):
    if element in my_set:
        return True
    else:
        return False

def create_lists():
    list_one = [1, 2, 3, 4, 5, 6, 9]
    list_one.append(789)
    return list_one
    
def creat_list(abc): 
    creat1 = list(abc)
    creat2 = (abc).split(" ")
    creat3 = (abc).split("\n")
    return creat1, creat2, creat3
    
def len_list(abc):
    len_creat1 = len(abc)
    len_creat2 = len((abc).split(" "))
    len_creat3 = len((abc).split("\n"))
    return len_creat1, len_creat2, len_creat3

def cycle_number(a, b):
    squares = []
    while a <= b:
        squares.append(a ** 2)
        a += 1
    return squares

def opr_person(my_dict,my_key):
    if my_dict[my_key] >=18:
        return True
    if my_dict[my_key]< 18:
        return False

def podset(set1, set2):
    return set1.issubset(set2)

def add_element(my_list, element):
    my_list.append([element])
    return my_list, type(my_list[-1])

def swap_elements(my_list):
    if len(my_list) >= 5:
        my_list[2], my_list[4] = my_list[4], my_list[2]
    return my_list

def fibonacci_list_check(my_list):
    len_sequence = len(my_list)
    repeating_element = my_list.count(1)
    return len_sequence, repeating_element

def fractional_calculation():
    number = -3.14
    rounded_number = int(number)
    remainder_of_the_number = round(number % -1, 2)
    return rounded_number, remainder_of_the_number

def calculat_air_volume_for_conditioner():
    living_room_length = 3.5
    living_room_width = 6.4
    bedroom_length = 3.4
    bedroom_width = 4
    not_residential = 11 #м2
    ceiling_height = 3.1
    v = ((living_room_length * living_room_width) + (bedroom_length * bedroom_width) + not_residential) * ceiling_height
    return v
    

def check_fibonacci_numbers(my_list):
    numbers_to_check = [21, 33, 987, 9999]
    results = {}
    for number in numbers_to_check:
        results[number] = number in my_list
    return results
    

def sravn_set(set1,set2):
    if len(set1) > len(set2) :
        return True
    elif len(set1) < len(set2) :
        return False

def union_sets(*sets):
    itog_set = set()
    for s in sets:
        itog_set.update(s)
    return itog_set

def dorog_prod(my_dict):
    for key, value in my_dict.items():
        if value > 1.5:
            return True


def raznost_set(set1, set2):
   return set1 - set2


def student18(my_dict,my_key):
    if my_dict[my_key] >=18:
        return True
    elif my_dict[my_key]< 18:
        return False

def add_student(my_dict,my_key,my_value):
    my_dict[my_key] = my_value
    return my_dict

def is_disjoint(set1,set2):
    return set1.isdisjoint(set2) #проверяет содержит ли общие элементы,еслинет,то тру,если да то фальш

def set_difference(set1, set2):
    return set1 - set2

#4 Создайте функцию для удаления конкретного элемента из множества.
def remove_element(some_set, element):
    if element in some_set:
        some_set .remove(element)
        return True
    else:
        return False

#5 Создайте функцию для поиска пересечения нескольких множеств
def find_intersection(set1, set2):
    return set1 .intersection(set2)

#6 Создайте функцию для проверки на равенство двух множеств.
def check_equality(set1, set2):
    return set1 == set2

#7 Создайте функцию для нахождения объединения трех множеств.
def union_of_sets(set1, set2, set3):
    return set1 .union(set1, set2, set3)

def quadratic_equation_solution():
    a = 2
    b = 9
    c = 10
    D = b ** 2 - 4 * a * c
    if D < 0:
        return "Корней нет"
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2
def string_concatenation_function():
    string1 = "hello, " .capitalize()
    string2 = "world!"
    return string1 + string2

def string_multiplication_function():
    string = "la "
    return string * 25

def list_modification():
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        numbers[1] = "hi"
        numbers[3] = [8, 6, 4]
    return numbers

def add_in_set(my_set, number):
    my_set.add(number)
    return my_set
    





 





