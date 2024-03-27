import pytest
from functions_hw_4 import (add_item_to_list, add_item_to_lists, create_list, symbol_of_separate_element, word_of_separate_element, create_poem_list, create_solyanka_list, solyanka_list_length, print_type_of_fifth_element, add_list_to_solyanka, print_type_of_last_element)


#, create_fibbonachi_list, count_ones_in_fibonacci, create_a_list, swap_elements, string_in_order, #append_third_line_from_poem, append_fourth_line_from_poem, append_fourth_fifth_line_from_poem, clear_list, append_first_line, #delete_last_elem, append_second_elem, update_true_story_list, remove_fifth_element, print_poem_from_list, my_fixture_fibonacci, #is_fibonacci_number, poem_fixture


a_poem = """За стеклом лежал Питон,
    Большой и толстый, как батон.
    Вверх пополз,
    Затем вернулся,
    Круглым бубликом свернулся."""

# fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]


def test_add_item_to_list():
    '''Тест на добавление элемента ко второму списку'''
    assert add_item_to_list()[0] == [1, 2, 3, 4, 5, 6, 9]
    assert add_item_to_list()[1] == [1, 2, 3, 4, 5, 6, 9, 789]


def test_add_item_to_lists():
    '''Добавляем элемент к спискам'''
    assert add_item_to_lists()[0] == [1, 2, 3, 4, 5, 6, 9, 789]
    assert add_item_to_lists()[1] == [1, 2, 3, 4, 5, 6, 9, 789]


def test_create_list():
    '''Тест на создание переменной a_list типа список'''
    assert create_list() == 'За стеклом лежал Питон,\n    Большой и толстый, как батон.\n    Вверх пополз,\n    Затем вернулся,\n    Круглым бубликом свернулся.'


def test_symbol_of_separate_element():
    '''Тест на вывод каждого символа строки a_poem как отдельный элемент списка'''
    assert symbol_of_separate_element()[0] == ['З','а',' ','с','т','е','к','л','о','м',' ','л','е','ж','а','л',' ','П','и','т','о','н',',','\n',' ',' ',' ',' ','Б','о','л','ь','ш','о','й',' ','и',' ','т','о','л','с','т','ы','й',',',' ','к','а','к',' ','б','а','т','о','н','.','\n',' ',' ',' ',' ','В','в','е','р','х',' ','п','о','п','о','л','з',',','\n',' ',' ',' ',' ','З','а','т','е','м',' ','в','е','р','н','у','л','с','я',',','\n',' ',' ',' ',' ','К','р','у','г','л','ы','м',' ','б','у','б','л','и','к','о','м',' ','с','в','е','р','н','у','л','с','я','.']
    assert symbol_of_separate_element()[1] == 127

 
def test_word_of_separate_element():
    '''Создание переменной = a.poem. Каждое слово строки a_poem - отдельный элемент списка another_list'''
    assert word_of_separate_element(a_poem)[0] ==['За','стеклом','лежал','Питон,','Большой','и','толстый,','как','батон.','Вверх','пополз,','Затем','вернулся,','Круглым','бубликом','свернулся.']
    assert word_of_separate_element(a_poem)[1] == 16


def test_create_poem_list():
    '''Создание one_more_list типа список, каждым элементом которой является отдельная строка строфы из a_poem'''
    assert create_poem_list() == ['За стеклом лежал Питон,',
 '    Большой и толстый, как батон.',
 '    Вверх пополз,',
 '    Затем вернулся,',
 '    Круглым бубликом свернулся.']


def test_create_solyanka_list():
    '''Создание список solyanka_list,его элементы - значения каждого из известных типов данных python.'''    
    assert create_solyanka_list() == [2, 2.0, 'str', [2, 0, -5], (1, 'abc'), {12.0, 'frt'}, {1: 'str'}, True]


def test_solyanka_list_length():
    '''Количество элементов списка solyanka_list.'''
    assert solyanka_list_length() == 8


def test_print_type_of_fifth_element():
    '''Выведите на экран тип пятого от начала списка элемента.'''
    assert print_type_of_fifth_element() == tuple


def test_add_list_to_solyanka():
    '''Добавьте в конец списка solyanka_list элемент типа "список" из одного элемента'''
    assert add_list_to_solyanka() == [2,2.0,'str',[2, 0, -5],(1, 'abc'),{12.0, 'frt'},{1: 'str'},True,[2, 45]]


def test_print_type_of_last_element():
    '''Выведите на экран тип последнего элемента списка solyanka_list'''
    assert print_type_of_last_element() == list


# def  test_create_fibbonachi_list():
#     '''Создайте список fibonacci_list, элементами которого будут числа Фибонначи из задания.
#        Посчитайте и выведите на экран, сколько чисел Фибоначчи в последовательности'''    
#     assert create_fibbonachi_list() == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
#     assert count_fibonacci_numbers() == 23


# def test_count_ones_in_fibonacci():       
#     '''Посчитайте и выведите на экран, сколько раз число 1 входит в заданную последовательность Фибоначчи.'''
#     assert count_ones_in_fibonacci(fibonacci_list) == 2

# def test_is_fibonacci_number():    #*     
#     '''Проверьте и верните результат, является ли число 21 числом Фибоначчи. Число 33? Число 987? число 9999?'''     
#     assert is_fibonacci_number(fibonacci_list)[21] == True
#     assert is_fibonacci_number(fibonacci_list)[33] == False
#     assert is_fibonacci_number(fibonacci_list)[987] == True
#     assert is_fibonacci_number(fibonacci_list)[9999] == False


# def test_create_a_list():
#     '''Создание переменной a_list типа "список" '''
#     assert create_a_list() == [1,2,5,4,3,6]


# def test_swap_elements():
#     '''Поменяйте местами третий и пятый элементы a_list'''
#     assert test_swap_elements(a_list) == [1, 2, 3, 4, 5, 6]



# def test_string_in_order():
#     '''Вывод на экран строки Омара Хайама в правильном порядке, используя список.''' 
#     assert poem == [(1, 'Кто битым жизнью был,'),
#                     (2, 'тот большего добьётся,'),
#                     (3, 'Пуд соли съевший выше ценит мёд.'),
#                     (4, 'Кто слёзы лил, тот искренней смеётся,'),
#                     (5, 'Кто умирал, тот знает, что живёт.')]


# def test_poem_fixture(poem):
#     assert poem_fixture(poem) == 'Кто битым за дедлайн был,\nтот больше не сольется.\nПуд багов съевший, выше ценит чистый код.\nКто дошик ел, тот рейтинг ценит свой.\nКто крашился, тот знает, что живой.'



# def test_append_third_line_from_poem(poem):
#     '''Создайте переменную true_story_list типа список, занесите в неё третью строку из стихотворения выше.'''
#     assert true_story_list == ['Пуд багов съевший, выше ценит чистый код.']
#     assert append_third_line_from_poem(poem) == 1

# def test_append_fourth_line_from_poem(poem_fixture):
#     '''Добавление 4й строки в конец списка true_story_list.'''
#     assert append_fourth_line_from_poem()[0] == ['Пуд багов съевший, выше ценит чистый код.',
#   'Кто дошик ел, тот рейтинг ценит свой.']
#     assert append_fourth_line_from_poem()[1] == 2


# # def test_append_fourth_fifth_line_from_poem(poem_fixture):
# #     '''Создайте переменную true_story_slice типа список, 
# #        занесите в неё четвертую и пятую строки из стихотворения выше. 
# #        Добавьте содержимое true_story_slice как один последний элемент списка true_story_list.'''
# #     poem_lines = poem_fixture.splitlines()
# #     true_story_list == ['Пуд багов съевший, выше ценит чистый код.',
# #   'Кто дошик ел, тот рейтинг ценит свой.']
# #     true_story_slice = []
# #     true_story_slice.append(poem_lines[3])    #4я стр из стих.
# #     true_story_slice.append(poem_lines[4])    #5я стр из стих.
# #     true_story_slice.extend(true_story_list)
# #     assert true_story_slice == 
# #     assert len(true_story_slice) == 
    






