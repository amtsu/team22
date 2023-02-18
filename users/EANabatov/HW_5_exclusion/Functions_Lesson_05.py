def search_by_name(name: str) -> str:
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
        result = dictionary[name.title()]
    except KeyError:
        result = 'Такого имени нет'
    except AttributeError:
        result = "Некорректный тип данных, принимаются только строки"
    finally:
        print('Конец работы программы.')
    return result


def safe_divide(dividend, divider):
    """
    Takes two integer or float numbers to divide with exceptions ZeroDivisionError and ValueError
    """
    try:
        result = f"{dividend / divider:.3f}"
    except ZeroDivisionError:
        result = "На ноль делить нельзя"
    except TypeError:
        result = "Некорректный тип данных, принимаются только числа"
    return result


def interactive_calculator(input_box):
    """
    A function that summarizes or subtracts or multiplies or divides two integers
    """
    try:
        splitting_box = input_box.split(" ")  # Разделяет полученное выражение на числа и математический оператор
        if len(splitting_box) != 3:  # Проверка введенного выражения на корректность
            result = """Введено неверное выражение! \nВыражение должно иметь вид: А +/- В ! \nГде А и В целые числа! 
                \nЗнак математической операции должен быть отделен пробелами!"""
        else:
            if splitting_box[1] == "+":
                result = int(int(splitting_box[0]) + int(splitting_box[2]))
            elif splitting_box[1] == "-":
                result = int(splitting_box[0]) - int(splitting_box[2])
            elif splitting_box[1] == "/":
                result = int(splitting_box[0]) / int(splitting_box[2])
            elif splitting_box[1] == "*":
                result = int(splitting_box[0]) * int(splitting_box[2])
    except ValueError:
        result = "Необходимо ввести целые числа!"
    except AttributeError:
        result = "Принимается только строка!"
    except ZeroDivisionError:
        result = "На ноль делить нельзя!"
    return result
