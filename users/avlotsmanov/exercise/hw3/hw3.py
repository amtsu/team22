def calculate(a, b, operation):
    '''Выполняет операции сложения, вычитания умножение, деление, возведение в степень, целая часть от деления, остаток от деления, для двух чисел.
    param a: первое число (int, float)
    param b: второе число (int, float)
    param operation: операция, передается знак операции в строковом виде 
    return: результат действия 
    '''
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError ('Числа должны быть типов int или float')
    if operation not in ('+', '-', '*', '/', '**', '//', '%'):
        raise ValueError ('Такая операция не поддерживается')
    match operation:
        case '+':
            res = a + b
        case '-':
            res = a - b
        case '*':
            res = a * b
        case '/':
            if b == 0:
                raise ZeroDivisionError
            res = a / b
        case '**':
            res = a ** b
        case '//':
            if b == 0:
                raise ZeroDivisionError
            res = a // b
        case '%':
            if b == 0:
                raise ZeroDivisionError
            res = a % b
    return round(res, ndigits = 5)

def round_remains_number(a):
    '''Округляет дробное число и берет от него остаток
    param a: число (float)
    return: кортеж округленное число и остаток от деления
    '''
    if type(a) is not float:
        raise TypeError
    return (round(a),"%.2f"%(a % round(a)))

def conditioner(t):
    '''Считает объем квартиры
    param t: Кортеж параметров квартиры (a1,b1,a2,b2,h,s1) (стороны 1 команты, стороны 2 команты, высота потолков, нежжилая площадь)
    return: Объем на который расчитан кондей
    '''
    if type(t) is not tuple:
        raise TypeError
    a1, b1, a2, b2, h, s1 = t
    return round((a1 * b1 + a2 * b2 + s1) * h, ndigits = 2)

def q_equation(a, b, c):
    '''Решает квадратное уравнение
    param a: коэффициент при x^2 (int, float)
    param b: коэффициент при x (int, float)
    param c: свободный член (int, float)
    return: кортеж из двух корней уравнения
    '''
    if type(a) not in (int, float) or type(b) not in (int, float) or type(c) not in (int, float):
        raise TypeError ('Числа должны быть типов int или float')
    d = b ** 2 - 4 * a * c 
    x1 = (- b + d ** 0.5) / (2 * a)
    x2 = (- b - d ** 0.5) / (2 * a)
    return (round(x1, ndigits = 3), round(x2, ndigits = 3))

def slice_3_7(numbers):
    '''Возвращает подсписок массива с 3 по 7 элемент включительно
    param numbers: массив элементов, не меньше 7
    return: массив из 5 элементов(срез с 3 по 7)
    '''
    if type(numbers) is not list:
        raise TypeError
    if len (numbers) <= 3:
        raise ValueError
    return numbers[3:8]