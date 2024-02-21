from time import time
from timeit import timeit
from inspect import getsource

def count_time(func, comment):
    "Рассчет времени сортировки с помощью time()"
    start = time() # время начала
    execution = func
    end = time() # время завершения
    total_time = end - start  # время выполнения
    print(f"Время выполнения 'time()' ({comment}): {total_time}") 
    return total_time

def count_timeit(sort_func, sorting_array): # не работает - ругается на недопустимый отступ 
    "Рассчет времени сортировки с помощью timeit"
    "Вычисляет только время выполнения конкретных операций, исключая системные процессы"
    func_text = getsource(sort_func)
    print(func_text)
    test_code = f"""
    func_text
    sort_func(sorting_array)
    """
    total_time = timeit(test_code, number=1)
    print(f"Время выполнения 'timeit()' ({len(sorting_array)}): {total_time}")
    return total_time