def search_by_name(name: str) -> str | int:
    """
    Search by name in dictionary with exceptions and output of the end of the program
    """
    dictionary = {
        "Alex": 8_915_356_6547,
        "John": 8_912_456_3456,
        "Cops": 911,
        "DnKr": 7_007_007_7777,
    }
    try:
        return dictionary[name.title()]
    except KeyError:
        return 'Такого имени нет'
    except AttributeError:
        return "Некорректный тип данных, принимаются только строки"
    # finally:
    # return 'Конец работы программы.'


def safe_divide(dividend: int | float, divider: int | float) -> float | str:
    """
    Takes two integer or float numbers to divide with exceptions ZeroDivisionError and ValueError
    """
    try:
        return f"{dividend / divider:.3f}"
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    except TypeError:
        return "Некорректный тип данных, принимаются только числа"


def interactive_calculator(input_box: str) -> int | float | str:
    """
    A function that summarizes or subtracts or multiplies or divides two integers
    """
    try:
        splitting_box = input_box.split(" ")  # Разделяет полученное выражение на числа и математический оператор
        if len(splitting_box) != 3:  # Проверка введенного выражения на корректность
            return """Введено неверное выражение! \nВыражение должно иметь вид: А +/- В ! \nГде А и В целые числа! 
                \nЗнак математической операции должен быть отделен пробелами!"""
        else:
            if splitting_box[1] == "+":
                return int(int(splitting_box[0]) + int(splitting_box[2]))
            elif splitting_box[1] == "-":
                return int(splitting_box[0]) - int(splitting_box[2])
            elif splitting_box[1] == "/":
                return int(splitting_box[0]) / int(splitting_box[2])
            elif splitting_box[1] == "*":
                return int(splitting_box[0]) * int(splitting_box[2])
    except ValueError:
        return "Необходимо ввести целые числа!"
    except AttributeError:
        return "Принимается только строка!"
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
