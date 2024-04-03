def print_matrix(matrix):
    '''
    Функция, печатающая двумерный список matrix по столбцам
    '''
    i = 0
    j = 0
    k = 0
    m = 0
    mat = []
    while k <= m:
        for elem in matrix:
            m = len(elem)
            for e in elem:
                if i == j:
                    mat.append(e)
                i += 1
            i = 0
        j += 1
        k += 1
    j = 0
    return mat
    
def ten_times(i = 0):
    '''
    Вызывает сама себя 10 раз
    '''
    if i < 10:
        i += 1
        return ten_times(i)
    else:
        return f'Запустили {i} раз'