def expand_matrix(matrix):
    new_matrix = []
    for item in zip(*matrix):
        new_matrix.append(list(item))

    return new_matrix


def ten_times(count=10):
    if count > 0:
        print(f'Вызов функции ten_times. Осталось вызвать {count - 1} раз')
        ten_times(count - 1)
    return f'Функция отработала успешно {count} раз'


def print_haiku(haiku, func):
    res_haiku = []
    for line in haiku:
        res_haiku.append(func(line))
    return res_haiku


def every_3rd_char(some_str):
    return some_str[2::3]


def different_color(some_str):
    colors_list = ["\033[31m{}\033[0m", "\033[32m{}\033[0m", "\033[33m{}\033[0m", "\033[34m{}\033[0m"]
    return ' '.join([colors_list[n].format(i) for n, i in enumerate(some_str.split())])


def bold_2nd_word(some_str):
    return ' '.join(["\033[1m{}\033[0m".format(i) if n == 1 else i for n, i in enumerate(some_str.split())])


def blue_and_lower(some_str):
    return "\033[34m{}\033[0m".format(some_str.lower())
