def count_in_poem(poem):
    '''Считает количество строк, слов и букв в стихотворении.
    param poem: стихотворение 
    return: кортеж из количества строк, слов и букв
    '''
    letters_list = list(a_poem)
    words_list = a_poem.split()
    lines_list = a_poem.split('\n')
    return (len(lines_list), len(words_list), len(letters_list))

def solyanka(*args):
    '''Делает массив из нескольких переданных данных и возвращает все различные типы элементов 
    param args: данные через запятую
    param return: множество типов
    '''
    solyanka_list = []
    type_solyanka = []
    for arg in args:
        type_solyanka.append(type(arg))
    return set(type_solyanka)

def is_fibonacci(a):
    '''Проверяет является число числом фибоначчи
    '''
def replace_3_5(a):
    '''Меняет 3 и 5 элемент списка
    param m: Список не короче 5 элементов
    '''

def sort_poem()
    '''Выводит в правильном порядке нумерованные строки стхиотворения
    '''
    