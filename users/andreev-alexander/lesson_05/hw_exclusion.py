"""
Создать телефонный справочник на основе словаря Python.
"""
phone_book = {
    "Ivan": "1234",
    "Mihail": "4321",
    "Svetlana": "002211"
}


"""
Попробовать найти в этом справочнике несуществующее имя.
Исследовать полученное исключение.
"""
phone_book = {
    "Ivan": "1234",
    "Mihail": "4321",
    "Svetlana": "002211"
}

# phone_book["Platon"] - KeyError


"""
- Реализовать телефонный справочник, который выводит сообщение
«Такого имени нет» при попытке найти несуществующее имя.
- Ввод имени пользователем реализуется функцией input().
"""
def phone_book_func():

    phone_book = {
        "Ivan": "1234",
        "Mihail": "4321",
        "Svetlana": "002211"
    }
    
    input_name = input("Введите имя: ")
    try:
        return phone_book[input_name]
    except KeyError:
        return "Такого имени нет"
    
# print(phone_book_func())


"""
Реализовать телефонный справочник, который выводит сообщение «Такого имени нет»
при попытке найти несуществующее имя и в любом случае в завершении выводит
сообщение «Конец работы программы.»
"""
def phone_book_func():

    phone_book = {
        "Ivan": "1234",
        "Mihail": "4321",
        "Svetlana": "002211"
    }
    
    input_name = input("Введите имя: ")
    try:
        return phone_book[input_name]
    except KeyError:
        return "Такого имени нет"
    finally:
        return "Конец работы программы."
    
# print(phone_book_func())


"""
- Реализовать функцию safe_divide, которая принимает от пользователя два целых
или вещественных числа и делит одно на другое. Предусмотреть обработку ошибки,
возникающей при делении на 0.
- Ввод числа пользователем реализуется функцией input().
- Синтаксис преобразования типов: a = float(input("Делимое:"))
"""
def safe_divide() -> float:
    
    input_numbers: list = input("Введите два чила через пробел: ").split(" ")
    if len(input_numbers) != 2:
        return "Введите два числа через пробел!"

    try:
        number_one = float(input_numbers[0])
        number_two = float(input_numbers[1])
    except ValueError:
        return "Введите числа, а не слова."

    try:
        return number_one / number_two
    except ZeroDivisionError:
        return "На ноль делить нельзя"

# print(safe_divide())


"""
Доработать функцию safe_divide, чтобы она также обрабатывала ошибки,
возникающие при вводе нечисловых символов.
Подсказка:
- Чтобы проверить, какая ошибка возникает при вводе нечисловых символов,
нужно воспроизвести эту ситуацию и посмотреть на класс ошибки в сообщении
интерпретатора Python (обычно выделяется красным шрифтом).
"""
# Сделал сразу


"""
- Разработать интерактивный калькулятор: пользователь вводит формулу вида
«12 + 8» или «15 - 10», программа вычисляет результат. Достаточно предусмотреть
только сложение и вычитание. Предполагается, что первый операнд, знак операции
и второй операнд обязательно должны быть разделены пробелами.
- Программа должна выводить сообщения об ошибках, если введена неверная формула
или нечисловые символы.
- Ожидаемый результат и часть решения:
"""
def calc_plus_minus() -> float:

    input_data: list = input("Введите операцию, например, '12 + 8': ").split(" ")
    if len(input_data) != 3:
        return "Введите 'число, знак операции, число' через пробел!"

    try:
        number_one = float(input_data[0])
        number_two = float(input_data[2])
    except ValueError:
        return "Введите числа, а не слова."
    
    operator = input_data[1]
    match operator:
        case "+":
            return number_one + number_two
        case "-":
            return number_one - number_two
        case _:
            return "Значение оператора должо быть: + или -."

# print(calc_plus_minus())


"""
Доработать предыдущую программу, чтобы она распознавала операторы деления (/)
и умножения (*), а также выводила сообщение в случае деления на 0.
"""
def calc_all() -> float:

    input_data: list = input("Введите операцию, например, '12 + 8': ").split(" ")
    if len(input_data) != 3:
        return "Введите 'число, знак операции, число' через пробел!"

    try:
        number_one = float(input_data[0])
        number_two = float(input_data[2])
    except ValueError:
        return "Введите числа, а не слова."
    
    operator = input_data[1]
    match operator:
        case "+":
            return number_one + number_two
        case "-":
            return number_one - number_two
        case "*":
            return number_one * number_two
        case "/":
            if number_two == 0:
                return "На ноль делить нельзя."
            return number_one / number_two
        case _:
            return "Значение оператора должо быть: +, -, *, /."

# print(calc_all())
