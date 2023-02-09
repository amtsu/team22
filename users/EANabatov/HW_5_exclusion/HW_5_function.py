def Search_by_name_ver_2(name: str) -> str:
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
        return (dictionary[name.title()])

    except KeyError:
        return 'Такого имени нет'

    except AttributeError:
        return "Некорректный тип данных, принимаются только строки"

    finally:
        return 'Конец работы программы.'
    

def safe_divide_ver_2(dividend : int | float, divider : int | float) -> int | float:
    """
    Takes two integer or float numbers to divide with exceptions ZeroDivisionError and ValueError
    """

    try:
        return f"{dividend / divider:.3f}"

    except ZeroDivisionError:
        return "На ноль делить нельзя"

    except TypeError:
        return "Некорректный тип данных, принимаются только числа"

    except ValueError:
        return "Принимаются только целые и десятичные числа"