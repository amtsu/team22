def print_squares_while(n):
    i = 1
    ret = []
    while i <= n:
        ret.append(i*i)
        i += 1
    return ret

def print_factorial(n):
    i = 1
    f = 1
    if n < 0:
        ret = 'Ошибка! Отрицательное число'
    elif n == 0:
        ret = n
    else:
        while i <= n:
            f = f * i
            i += 1
        ret = f
    return ret

def sum_in_range(
    n1,
    n2
):
    sum = 0
    i = n1
    while i <= n2:
        sum += i
        i += 1
    return sum

def primes(N):
    primes = []
    for n in range(2, N):
        for d in range(2, n):
            if n % d == 0:
                break
        else:
            primes.append(n)
    return primes

def is_it_pallindrom(string1):
    ret = False
    string2 = []
    for char in string1.lower():
        if str(char).isalnum() == True:
            string2.append(char)
        else: 
            continue
    if ''.join(string2[::-1]) == ''.join(string2):
        ret = True
    return ret

def gsv (
    num1, 
    num2
):
    '''Функция для поиска наибольшего общего делителя
    :param num1: целое число
    :param num2: целое число
    :return: наибольший общий делитель
    '''
    i = 1
    nod = []
    while i <= min(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            nod.append(i)
        sorted(nod)
        i += 1
    return nod[-1]
