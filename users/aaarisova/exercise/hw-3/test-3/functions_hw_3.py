def count_operacions():
    '''
    Вычислить результат следующих операций
    '''
    product = 10 * (5 + 3)
    division = (20 - 6) / 2
    exponentiation = 2 ** 5    #возведение 2 в 5-ю степень
    integer_division = 25 // 4   #целая часть от деления
    remainder = 25 % 4    #остаток от деления
    return product, division, exponentiation, integer_division, remainder


def round_remain_number():
    '''
    Округлите число до целого.
    Возьмите остаток числа
    '''
    number = -3.14
    rounded_number = int(number)
    remainder_number = round(number % -1, 2) 
    return rounded_number, remainder_number


def area_of_rectangle():
    '''Вычислить площадь прямоугольника и вывести результат на экран'''
    a = 5 
    b = 7
    S = a * b
    return S

def air_volume():
    '''Рассчитать объем воздуха для охлождения кв кондиционером'''
    # размеры гостинной:
    living_room_width = 3.5
    living_room_length = 6.4

    # размеры спальни:
    bedroom_width = 3.4 
    bedroom_length = 4 

    non_residential_area = 11 # нежилая часть
    ceiling_height = 3.1 # высота потолка

    v = ((living_room_width * living_room_length) + (bedroom_width * bedroom_length) + non_residential_area) * ceiling_height
    return (round(v,2))


def discriminant_equation():
    '''Найти решение квадратного уравнения, используя формулу дискриминанта.'''
    #ax^2 + bx + c == 0 #квадратное уравнение 

    import math
    a = 2
    b = 7
    c = -10
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + D ** 0.5)/(2 * a)
        x2 = (-b - D ** 0.5)/(2 * a)
        return (round(x1,2)), (round(x2,2))

    elif D == 0:
        x = -b / (2*a)
        return "Уравнение имеет 1 корень. D == 0: ", x
        
    else:
        return "Уравнение не имеет корней. D < 0"



def string_concatenation():
    '''Объединить строки string1 и string2
    результат вывести на экран так, 
    чтобы первая буква в предложении стала заглавной'''
    string1 = "hello, "
    string2 = "world!"
    result_union = (string1 + string2).capitalize()
    return result_union
    

def string_length():
    '''Кол-во символов в "Hello, world!" '''
    strings_union = "Hello, world!"
    result_lenth = len(strings_union)
    return result_lenth


def string_multiple_times():
    '''Вывод на экран строки la 25 раз'''
    string_la = "la "
    result = string_la * 25
    return result


def list_modification():
    '''Модификация списка'''
    numbers = [1, 2, 3, 4, 5]
    numbers[1] = "hi"
    numbers[3] = [8, 6, 4]
    return numbers


def extract_sublist():
    '''Извлеките подсписок с 3-го по 7-й элемент включительно.'''
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sublist = numbers[2:7]
    return sublist




