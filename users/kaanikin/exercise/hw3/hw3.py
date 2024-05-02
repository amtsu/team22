def calc_result():
    """
    Вычислить результат следующих операций:
    10 * (5 + 3)
    (20 - 6) / 2
    2 ** 5 (возведение 2 в 5-ю степень)
    25 // 4 (целая часть от деления)
    25 % 4 (остаток от деления)
    """
    result1 = 10 * (5 + 3)
    result2 = (20 - 6) / 2
    result3 = 2 ** 5
    result4 = 25 // 4
    result5 = 25 % 4
    return result1, result2, result3, result4, result5
    
def fractional_calc():
    """
    Дано дробное число:
    number = -3.14
    Выполнить следующие операции:
    Округлите число до целого.
    Возьмите остаток числа.
    """
    number = -3.14
    roundNumber = int(number)
    remNumber = round((number%1.0),2)
    return roundNumber, remNumber

def volume_calc():
    """
    На какой обьем воздуха должен быть расчитан кондиционер, если с его помощью хотят охлаждать квартиру 
в которой размер гостинной 3.5 на 6.4 метра, спальни 3.4 на 4 метра и площадь не жилой части 11 метров. 
При том что высота потолков 3,1 метр.
    """
    livng_room_length = 6.4
    living_room_width = 3.5
    bedroom_length = 3.4
    bedroom_width = 4
    closet_square = 11
    height = 3.1
    air_volume = height*((livng_room_length*living_room_width)+(bedroom_length*bedroom_width)) + closet_square
    return (round(air_volume,2))
     
    
def quadratic_eq():
    """
    Дано квадратное уравнение вида ax^2 + bx + c = 0.
    Найти его решения, используя формулу дискриминанта.
    a номер текущего месяца
    b номер вашей группы
    c минус десять (-10)
    """
    a = 2
    b = 9 
    c= -10
    descriminant = b**2 - 4*a*c 
    if descriminant > 0:
            x1 = (-b + descriminant**0.5) / (2*a)
            x2 = (-b - descriminant**0.5) / (2*a)
            return ('Корень уравнения 1 = ' + str(round(x1,2)) + '   ' + 'Корень уравнения 2 = ' + str(round(x2,2)))
    elif descriminant == 0:
            x1 = -b / (2*a)
            return ('Корень уравнения ' + str(x1))
    else:
            return ('Корней нет')

def string_concat():
    """
   Даны строки:
    string1 = "hello, "
    string2 = "world!"
    Объединить строки string1 и string2 и результат вывести на экран так чтобы первая буква в предложент стала заглавной.

    Сколько символов было в предыдущей строке?
    """
    string1 = "hello, "
    string2 = "world!"
    result = (string1 + string2) #конкотинация строк
    final_result1 = (result.capitalize() + ' ' + ('Длина строки = ' + str(len(result))))
    return final_result1

def string_multiply():
    """
    Выведите на экран строку la 25 раз.
    """
    string = "la "
    return string * 25

def list_mod_1():
    """
    Дан список чисел:
    numbers = [1, 2, 3, 4, 5]
    Выполнить следующие операции:
    1. Измените число 2 на строку "hi" 
    2. Выведите значение, находящееся на позиции 2.
    3. Изменить значение на позиции 4 на список из 3 элементов [8, 6, 4].
    Результаты вывести на экран.
    """
    
    numbers = [1, 2, 3, 4, 5]
    numbers[1] = "hi" 
    numbers[3] = [8, 6, 4]

    return numbers

def list_mod_2():
    """
    Дан список чисел:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Извлеките подсписок с 3-го по 7-й элемент включительно.
    """
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_numbers = numbers[2:7]
    return new_numbers
    