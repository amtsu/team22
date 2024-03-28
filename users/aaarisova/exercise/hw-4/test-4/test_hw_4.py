import pytest
from functions_hw_4 import (add_item_to_list, add_item_to_lists, create_list, symbol_of_separate_element, word_of_separate_element, create_poem_list, create_solyanka_list, solyanka_list_length, print_type_of_fifth_element, add_list_to_solyanka, print_type_of_last_element, create_fibbonachi_list, count_ones_in_fibonacci, is_fibonacci_number, create_a_list, swap_elements, string_in_order, transform_poem_data)


a_poem = """За стеклом лежал Питон,
    Большой и толстый, как батон.
    Вверх пополз,
    Затем вернулся,
    Круглым бубликом свернулся."""

fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]

poem = '''Кто битым за дедлайн был,
тот больше не сольется.
Пуд багов съевший, выше ценит чистый код.
Кто дошик ел, тот рейтинг ценит свой.
Кто крашился, тот знает, что живой.'''


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
    '''Тест. Создание переменной = a.poem. Каждое слово строки a_poem - отдельный элемент списка another_list'''
    assert word_of_separate_element(a_poem)[0] ==['За','стеклом','лежал','Питон,','Большой','и','толстый,','как','батон.','Вверх','пополз,','Затем','вернулся,','Круглым','бубликом','свернулся.']
    assert word_of_separate_element(a_poem)[1] == 16


def test_create_poem_list():
    '''Тест.Создание one_more_list типа список, каждым элементом которой является отдельная строка строфы из a_poem'''
    assert create_poem_list() == ['За стеклом лежал Питон,',
 '    Большой и толстый, как батон.',
 '    Вверх пополз,',
 '    Затем вернулся,',
 '    Круглым бубликом свернулся.']


def test_create_solyanka_list():
    '''Тест.Создание список solyanka_list,его элементы - значения каждого из известных типов данных python.'''    
    assert create_solyanka_list() == [2, 2.0, 'str', [2, 0, -5], (1, 'abc'), {12.0, 'frt'}, {1: 'str'}, True]


def test_solyanka_list_length():
    '''Тест. Количество элементов списка solyanka_list.'''
    assert solyanka_list_length() == 8


def test_print_type_of_fifth_element():
    '''Тест. Выведите на экран тип пятого от начала списка элемента.'''
    assert print_type_of_fifth_element() == tuple


def test_add_list_to_solyanka():
    '''Тест. Добавьте в конец списка solyanka_list элемент типа "список" из одного элемента'''
    assert add_list_to_solyanka() == [2,2.0,'str',[2, 0, -5],(1, 'abc'),{12.0, 'frt'},{1: 'str'},True,[2, 45]]


def test_print_type_of_last_element():
    '''Тест - выведите на экран тип последнего элемента списка solyanka_list'''
    assert print_type_of_last_element() == list


def  test_create_fibbonachi_list():
    '''Тест. Создайте список fibonacci_list, элементами которого будут числа Фибонначи из задания.
       Посчитайте и выведите на экран, сколько чисел Фибоначчи в последовательности'''    
    assert create_fibbonachi_list()[0] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
    assert create_fibbonachi_list()[1] == 23


def test_count_ones_in_fibonacci():       
    '''Тест -посчитайте и выведите на экран, сколько раз число 1 входит в заданную последовательность Фибоначчи.'''
    assert count_ones_in_fibonacci(fibonacci_list) == 2

def test_is_fibonacci_number():    #*     
    '''Тест - проверьте, является ли число 21 числом Фибоначчи. Число 33? Число 987? число 9999?'''     
    assert is_fibonacci_number(fibonacci_list)[21] == True
    assert is_fibonacci_number(fibonacci_list)[33] == False
    assert is_fibonacci_number(fibonacci_list)[987] == True
    assert is_fibonacci_number(fibonacci_list)[9999] == False


def test_create_a_list():
    '''Тест -создание переменной a_list типа "список" '''
    assert create_a_list() == [1,2,5,4,3,6]


def test_swap_elements():
    '''Тест - поменяйте местами третий и пятый элементы a_list'''
    a_list = [1,2,5,4,3,6]
    assert swap_elements(a_list) == [1, 2, 3, 4, 5, 6]



def test_string_in_order():
    '''Тест - вывод на экран строки Омара Хайама в правильном порядке, используя список.''' 
    assert string_in_order() == [(1, 'Кто битым жизнью был,'),
                    (2, 'тот большего добьётся,'),
                    (3, 'Пуд соли съевший выше ценит мёд.'),
                    (4, 'Кто слёзы лил, тот искренней смеётся,'),
                    (5, 'Кто умирал, тот знает, что живёт.')]


def test_transform_poem_data():
    assert transform_poem_data()[0] == ['Кто битым за дедлайн был,',
  'тот больше не сольется.',
  'Пуд багов съевший, выше ценит чистый код.',
  'Кто дошик ел, тот рейтинг ценит свой.',
  'Кто крашился, тот знает, что живой.']
    assert transform_poem_data()[1] == 5
    






