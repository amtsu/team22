import math


def get_hypotenuse_length(cathet_one: int | float, cathet_two: int | float) -> int | float:
    """Рассчитывается длина гипотенузы прямоугольного треугольника."""
    # Если любой из катетов меньше или равен 0
    if not cathet_one >= 1 and cathet_two >= 1:
        raise ValueError("Катет должен быть больше 0")
    return math.sqrt(cathet_one**2 + cathet_two**2) 

def get_hypotenuse_length_2(cathet_one: int | float, cathet_two: int | float) -> int | float:
    """Рассчитывается длина гипотенузы прямоугольного треугольника
    с возведением в степень 0.5, вместо взятия корня."""
    # Если любой из катетов меньше или равен 0
    if not cathet_one >= 1 and cathet_two >= 1:
        raise ValueError("Катет должен быть больше 0")
    return (cathet_one**2 + cathet_two**2)**0.5 

def arithmetic(num_one: int | float, num_two: int | float, operator: str) -> int | float:
    """Производится четыре арифметические операции: сложение, вычетание,
    умножение и деление."""
    arithmetic_action = {
        "+": (num_one + num_two),
        "-": (num_one - num_two),
        "*": (num_one * num_two),
        "/": (num_one / num_two)
    }

    return arithmetic_action[operator]

def square_parameters(side_length: int | float) -> list[int | float]:
    """Функция считает периметр, площадь и диагональ квадрата."""
    # Если сторона квадрата меньше или равна 0
    if not side_length >= 1:
        raise ValueError("Длина должна быть больше 0")
    perimeter = side_length * 4
    square_are = side_length**2
    diagonal = math.sqrt(2) * side_length
    return [perimeter, square_are, diagonal]

def is_prime(number: int) -> bool:
    pass

def is_palindrome(input_string: str) -> bool:
    """Функция возвращает True, если слово - полиндром, False - если нет."""
    if " " in input_string:
        raise ValueError("Не должно быть пробелов")
    for letter in input_string:
        if letter.isupper():
            raise ValueError("Все буквы должны быть маленькими")
    if input_string == input_string[::-1]:
        return True
    return False

def is_palindrome_string(input_string: str) -> bool:
    """Возвращает True, если строка палиндром, False - если нет."""
    result_string = input_string.lower().replace(" ", "")
    if result_string == result_string[::-1]:
        return True
    return False
