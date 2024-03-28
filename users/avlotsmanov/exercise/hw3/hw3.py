def calculate(a, b, operation):
    '''Выполняет операции сложения, вычитания умножение, деление, возведение в степень, целая часть от деления, остаток от деления, для двух чисел.
    param a: первое число (int, float)
    param b: второе число (int, float)
    param operation: операция, передается знак операции в строков виде 
    return: результат действия 
    '''
    match operation:
        case '+':
            res = a + b
        case '-':
            res = a - b
        case '*':
            res = a * b
        case '/':
            res = a / b
        case '**':
            res = a ** b
        case '//':
            res = a // b
        case '%':
            res = a % b
    return res

def round_remains_number(a):
    '''Округляет дробное число и берет от него остаток
    param a: число (float)
    return: кортеж округленное число и остаток от деления
    '''
    return (round(a),"%.2f"%(a % round(a)))

def conditioner(t):
    '''Округляет дробное число и берет от него остаток
    param t: Кортеж параметров квартиры (a1,b1,a2,b2,h,s1) (стороны 1 команты, стороны 2 команты, высота потолков, нежжилая площадь)
    return: Объем на который расчитан кондей
    '''
    a1, b1, a2, b2, h, s1 = t
    return round((a1 * b1 + a2 * b2 + s1) * h, ndigits = 2)

def q_equation(a, b, c):
    '''Решает квадратное уравнение
    param a: коэффициент при x^2 (int, float)
    param b: коэффициент при x (int, float)
    param c: свободный член (int, float)
    return: кортеж из двух корней уравнения
    '''
    d = b ** 2 - 4 * a * c 
    x1 = (- b + d ** 0.5) / (2 * a)
    x2 = (- b - d ** 0.5) / (2 * a)
    return (x1, x2)

def slice_3_7(numbers):
    '''Возвращает подсписок массива с 3 по 7 элемент включительно
    param numbers: массив элементов, не меньше 7
    return: массив из 5 элементов(срез с 3 по 7)
    '''
    return numbers[3:8]