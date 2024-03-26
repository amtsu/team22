import pytest
from functions_hw_4 import (add_item_to_list, add_item_to_lists, create_list, symbol_of_separate_element, word_of_separate_element, create_poem_list, create_solyanka_list, solyanka_list_length, print_type_of_fifth_element, add_list_to_solyanka, print_type_of_last_element, create_fibbonachi_list, count_fibonacci_numbers, count_ones_in_fibonacci, create_a_list, swap_elements, string_in_order, append_third_line_from_poem, append_fourth_line_from_poem, append_fourth_fifth_line_from_poem, clear_list, append_first_line, delete_last_elem, append_second_elem, update_true_story_list, remove_fifth_element, print_poem_from_list) # доработать и добавить is_fibonacci_number


def test_add_item_to_list():
    '''Тест на добавление элемента ко второму списку'''
    list_one = [1, 2, 3, 4, 5, 6, 9]
    list_two = [1, 2, 3, 4, 5, 6, 9]
    list_two.append(789)
    assert list_one == [1, 2, 3, 4, 5, 6, 9]
    assert list_two == [1, 2, 3, 4, 5, 6, 9, 789]


def test_add_item_to_lists():
    '''Добавляем элемент к спискам'''
    list_one = [1, 2, 3, 4, 5, 6, 9]
    list_two = list_one
    list_two.append(789)
    assert list_one == [1, 2, 3, 4, 5, 6, 9, 789]
    assert list_two == [1, 2, 3, 4, 5, 6, 9, 789]


def test_create_list():
    '''Создание переменной a_list типа список'''
    a_poem = """За стеклом лежал Питон,
    Большой и толстый, как батон.
    Вверх пополз,
    Затем вернулся,
    Круглым бубликом свернулся."""
    assert a_poem == 'За стеклом лежал Питон,\n    Большой и толстый, как батон.\n    Вверх пополз,\n    Затем вернулся,\n    Круглым бубликом свернулся.'


a_poem = """За стеклом лежал Питон,
    Большой и толстый, как батон.
    Вверх пополз,
    Затем вернулся,
    Круглым бубликом свернулся."""


def test_symbol_of_separate_element():
    '''Каждый символ строки a_poem отдельный элемент списка a_list'''
    a_list = []
    a_list.extend(a_poem) 
    assert a_list == ['З','а',' ','с','т','е','к','л','о','м',' ','л','е','ж','а','л',' ','П','и','т','о','н',',','\n',' ',' ',' ',' ','Б','о','л','ь','ш','о','й',' ','и',' ','т','о','л','с','т','ы','й',',',' ','к','а','к',' ','б','а','т','о','н','.','\n',' ',' ',' ',' ','В','в','е','р','х',' ','п','о','п','о','л','з',',','\n',' ',' ',' ',' ','З','а','т','е','м',' ','в','е','р','н','у','л','с','я',',',
 '\n',
 ' ',
 ' ',
 ' ',
 ' ',
 'К',
 'р',
 'у',
 'г',
 'л',
 'ы',
 'м',
 ' ',
 'б',
 'у',
 'б',
 'л',
 'и',
 'к',
 'о',
 'м',
 ' ',
 'с',
 'в',
 'е',
 'р','н','у','л','с','я','.']
    assert len(a_list) == 127

 
def test_word_of_separate_element():
    '''Создание переменной = a.poem. Каждое слово строки a_poem - отдельный элемент списка another_list'''
    another_list = a_poem.split()
    assert another_list == ['За',
 'стеклом',
 'лежал',
 'Питон,',
 'Большой',
 'и',
 'толстый,',
 'как',
 'батон.',
 'Вверх',
 'пополз,',
 'Затем',
 'вернулся,',
 'Круглым',
 'бубликом',
 'свернулся.']
    assert len(another_list) == 16


def test_create_poem_list():
    '''Создание one_more_list типа список, каждым элементом которой является отдельная строка строфы из a_poem'''
    one_more_list = a_poem.split('\n')
    assert one_more_list == ['За стеклом лежал Питон,',
 '    Большой и толстый, как батон.',
 '    Вверх пополз,',
 '    Затем вернулся,',
 '    Круглым бубликом свернулся.']











