import pytest

# Задание 1.
def add_item_to_list():
	'''Добавление элемента ко второму списку'''
	list_one = [1, 2, 3, 4, 5, 6, 9]
	list_two = [1, 2, 3, 4, 5, 6, 9]
	list_two.append(789)
	return list_one, list_two


def add_item_to_lists():
    '''Добавляем элемент к спискам'''
    list_one = [1, 2, 3, 4, 5, 6, 9]
    list_two = list_one
    list_two.append(789)
    return list_one, list_two


# Задание 2.
a_poem = """За стеклом лежал Питон,
    Большой и толстый, как батон.
    Вверх пополз,
    Затем вернулся,
    Круглым бубликом свернулся."""

def create_list():
    '''Создание переменной a_list типа список'''
    a_poem = """За стеклом лежал Питон,
    Большой и толстый, как батон.
    Вверх пополз,
    Затем вернулся,
    Круглым бубликом свернулся."""
    return a_poem

    
def symbol_of_separate_element():
    '''Вывод каждого символа строки a_poem как отдельный элемент списка'''
    a_list = []
    a_list.extend(a_poem) 
    return a_list, len(a_list)

    
def word_of_separate_element(a_poem):
    '''Создание переменной = a.poem. Каждое слово строки a_poem - отдельный элемент списка another_list'''
    another_list = a_poem.split()
    return another_list, len(another_list)
    

def create_poem_list():
    '''Создание one_more_list типа список, каждым элементом которой является отдельная строка строфы из a_poem'''
    one_more_list = a_poem.split('\n')
    return one_more_list


#Задание 3.

def create_solyanka_list():
    '''Создание список solyanka_list,его элементы - значения каждого из известных типов данных python.'''
    solyanka_list = [2, 2.0, 'str', [2,0,-5], (1, "abc"), {'frt', 12.0}, {1: "str"}, True]
    return solyanka_list

def solyanka_list_length():
    '''Количество элементов списка solyanka_list.'''
    solyanka_list = [2, 2.0, 'str', [2,0,-5], (1, "abc"), {'frt', 12.0}, {1: "str"}, True]
    return len(solyanka_list)

def print_type_of_fifth_element():
    '''Выведите на экран тип пятого от начала списка элемента.'''
    solyanka_list = [2, 2.0, 'str', [2,0,-5], (1, "abc"), {'frt', 12.0}, {1: "str"}, True]
    return type(solyanka_list[4])


def add_list_to_solyanka():
    '''Добавьте в конец списка solyanka_list элемент типа "список" из одного элемента'''
    solyanka_list = [2, 2.0, 'str', [2,0,-5], (1, "abc"), {'frt', 12.0}, {1: "str"}, True]
    solyanka_list.append([2,45])
    return solyanka_list
    
 
def print_type_of_last_element():
    '''Выведите на экран тип последнего элемента списка solyanka_list'''
    solyanka_list = [2, 2.0, 'str', [2, 0, -5], (1, 'abc'), {12.0, 'frt'}, {1: 'str'}, True, [2, 45]]
    last_element = solyanka_list[-1] 
    element_type = type(last_element)
    return element_type


# Задание 4.

def  create_fibbonachi_list():
    '''Создайте список fibonacci_list, элементами которого будут числа Фибонначи из задания'''
    fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
    fibonacci_lenght = len(fibonacci_list)
    return fibonacci_list, fibonacci_lenght
    
fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]

def count_ones_in_fibonacci(fibonacci_list):       
    '''Посчитайте и выведите на экран, сколько раз число 1 входит в заданную последовательность Фибоначчи.'''
    count_of_1 = fibonacci_list.count(1)
    return count_of_1


def is_fibonacci_number(fibonacci_list):    #*     
    '''Проверьте и верните результат, является ли число 21 числом Фибоначчи. Число 33? Число 987? число 9999?'''     
    numbers_to_check = [21, 33, 987, 9999]
    def fibonacci_number(number):
        a, b = 0, 1
        while a < number:
            a, b = b, a + b
        return a == number
     
    results = {}
    for number in numbers_to_check:
        results[number] = fibonacci_number(number)
    return results


# Задание 5.

def create_a_list():
    '''Создание переменной a_list типа "список" '''
    a_list = [1,2,5,4,3,6]
    return a_list

def swap_elements(a_list):
    '''Поменяйте местами третий и пятый элементы a_list'''
    a_list = [1,2,5,4,3,6]
    a_list[2], a_list[4] = a_list[4], a_list[2]
    return a_list



# Задание 6.

def string_in_order():
    '''Вывод на экран строки Омара Хайама в правильном порядке, используя список.''' 
    poem = [(2, "тот большего добьётся," ),
        (5, "Кто умирал, тот знает, что живёт."),
        (1, "Кто битым жизнью был," ),
        (3, "Пуд соли съевший выше ценит мёд."),
        (4, "Кто слёзы лил, тот искренней смеётся,")]
    poem.sort()
    return poem


# Задание 7.

poem = '''Кто битым за дедлайн был,
тот больше не сольется.
Пуд багов съевший, выше ценит чистый код.
Кто дошик ел, тот рейтинг ценит свой.
Кто крашился, тот знает, что живой.'''


def append_third_line_from_poem(poem):
    '''Создайте переменную true_story_list типа список, занесите в неё третью строку из стихотворения выше.'''
    poem_lines = poem.splitlines()
    true_story_list = []
    true_story_list.append(poem_lines[2])     #3я стр из стих.
    return true_story_list, len(true_story_list)


def append_fourth_line_from_poem():
    '''Добавление 4й строки в конец списка true_story_list.'''
    poem_lines = poem.splitlines()
    true_story_list = ['Пуд багов съевший, выше ценит чистый код.']
    true_story_list.append(poem_lines[3])     #4я стр из стих.
    return true_story_list, len(true_story_list)


# ########## ОСТАНОВИЛАСЬ ТУТ: #################################################
# def append_fourth_fifth_line_from_poem(poem):
#     '''Создайте переменную true_story_slice типа список, 
#        занесите в неё четвертую и пятую строки из стихотворения выше. 
#        Добавьте содержимое true_story_slice как один последний элемент списка true_story_list.'''
#     poem_lines = poem.splitlines()
#     true_story_slice = []
#     true_story_slice.append(poem_lines[3])    #4я стр из стих.
#     true_story_slice.append(poem_lines[4])    #5я стр из стих.
#     true_story_slice.extend(true_story_list)
#     return true_story_slice, len(true_story_slice)


# def clear_list(poem):
#     '''Очистите весь список true_story_slice, выведите его содержимое на экран.'''
#     true_story_slice.clear() 
#     return true_story_slice, len(true_story_slice)

# def append_first_line(poem):
#     '''Добавьте первую строку из стихотворение в начало списка true_story_list'''
#     true_story_list.insert(0, poem_lines[0])   #1ю стр в начало списка
#     return true_story_list, len(true_story_list)


# def delete_last_elem(poem):
#     '''Удалите последний элемент списка true_story_list'''
#     true_story_list.pop()                
#     return true_story_list, len(true_story_list)


# def append_second_elem(poem):
#     '''Добавьте вторым элементом списка true_story_list вторую строчку стихотворения'''
#     true_story_list.insert(1, poem_lines[1])  #II элем во 2ю стр
#     return true_story_list, len(true_story_list)


# def update_true_story_list(poem):
#     '''Создайте переменную true_story_tail типа список, занесите в него пятую строку стихотворения дважды. 
#        Скопируйте элементы списка true_story_tail в конец списка true_story_list.'''
#     true_story_tail = [poem_lines[4], poem_lines[4]]  #5я стр * 2
#     true_story_list.extend(true_story_tail)
#     return true_story_list, len(true_story_list)


# def remove_fifth_element(poem):
#     '''Удалите 5 элемент списка true_story_list.'''
#     true_story_list.pop(4) #Удалить 5й эл
#     return true_story_list, len(true_story_list)


# def print_poem_from_list(poem):
#     '''Выведите список true_story_list красиво в виде стихотворения.'''
#     true_story_list = poem_lines
#     return true_story_list, len(true_story_list)










 
