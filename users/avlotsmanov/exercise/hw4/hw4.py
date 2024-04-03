def count_in_poem(poem):
    '''Считает количество строк, слов и букв в стихотворении.
    param poem: стихотворение 
    return: кортеж из количества строк, слов и букв
    '''
    if type(poem) is not str:
        raise TypeError
    letters_list = list(poem)
    words_list = poem.split()
    lines_list = poem.split('\n')
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
