
def calculate_result():
    """
    функция операций над числовыми значениями
    """
    result1 = 10 * (5 + 3)
    result2 = (20 - 6) / 2
    result3 = 2 ** 5
    result4 = 25 // 4
    result5 = 25 % 4
    return result1, result2, result3, result4, result5
    
def fractional_calculation():
    """
    функция округления дробного числа и остатка от деления
    """
    number = -3.14
    rounded_number = int(number)
    remainder_of_the_number = round(number % -1, 2)
    return rounded_number, remainder_of_the_number

def calculat_air_volume_for_conditioner():
    """
    функция вычисления оъема воздуха для кондиционера
    """
    living_room_length = 3.5
    living_room_width = 6.4
    bedroom_length = 3.4
    bedroom_width = 4
    not_residential = 11 #м2
    ceiling_height = 3.1
    v = ((living_room_length * living_room_width) + (bedroom_length * bedroom_width) + not_residential) * ceiling_height
    return v
    
def quadratic_equation_solution():
    """
    функция решения квадравтного уровнения через дискриминант
    """
    a = 2
    b = 9
    c = 10
    D = b ** 2 - 4 * a * c
    if D < 0:
        return "Корней нет"
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return x1, x2
def string_concatenation_function():
    """
    функция объединения строк, где первая буква заглавная
    """
    string1 = "hello, " .capitalize()
    string2 = "world!"
    return string1 + string2

def string_multiplication_function():
    """
    функция умножения строк
    """
    string = "la "
    return string * 25

def list_modification():
    """
    функция модификации списка
    """
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        numbers[1] = "hi"
        numbers[3] = [8, 6, 4]
    return numbers
    
    
