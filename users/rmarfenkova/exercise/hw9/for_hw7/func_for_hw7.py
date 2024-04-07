def print_matrix(matrix):
    '''
    это функция, печатающая двумерный список matrix по столбцам
    '''
    column_element = []
    for column in zip(*matrix):
        for element in column:
            column_element.append(element)
    return column_element


def print_haiku1(haiku):
    upper_haiku = []
    for line in haiku:
        upper_haiku.append(line.upper())
    return upper_haiku


def print_haiku2(haiku):
    every_third_element = []
    for line in haiku:
        every_third_element.append(line[::3])
    return every_third_element

#def print_haiku(haiku):
#    haiku_string = ""
#    for line in haiku:
#        haiku_string += "\033[91m{}\n".format(line)
#    return haiku_string