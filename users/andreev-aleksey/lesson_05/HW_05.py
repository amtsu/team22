# Упражнение - исключения
"""
-- 1 --
Создать телефонный справочник на основе словаря Python.
"""
phones = {
    "Vanya": 89008000700,
    "Misha": 88009004552,
    "Sveta": 89065421584,
    "Anna": 65556665662
}


"""
-- 2 --
Попробовать найти в этом справочнике несуществующее имя. Исследовать полученное исключение.
"""
#phones["Anton"]

"""
-- 3 --
- Реализовать телефонный справочник, который выводит сообщение «Такого имени нет» при попытке найти несуществующее имя.
- Ввод имени пользователем реализуется функцией input().
"""
def phone_numbers():
    name = input("введите имя\n")
    try:
        print(phones[name])
        return phones[name]
    except KeyError:
        print("Такого имени нет")
        return "Такого имени нет"

#phone_numbers()
"""
-- 4 --
Реализовать телефонный справочник, который выводит сообщение «Такого имени нет» при попытке найти несуществующее имя и в любом случае в завершении выводит сообщение «Конец работы программы.»
"""
def phone_numbers_finally():
    name = input("введите имя\n")

    try:
        print(phones[name])
        return phones[name]
    except KeyError:
        print("Такого имени нет")
        return "Такого имени нет"
    finally:
        message = "Конец работы программы"
        print(message)
        return message

#phone_numbers_final()


"""
-- 5 --
- Реализовать функцию safe_divide, которая принимает от пользователя два целых или вещественных числа и делит одно на другое. 
Предусмотреть обработку ошибки, возникающей при делении на 0.
- Ввод числа пользователем реализуется функцией input().
- Синтаксис преобразования типов:  
    a = float(input("Делимое:"))
"""

def safe_divide():
    num1 = float(input("Делимое:"))
    num2 = float(input("Делитель:"))

    try:
        result = num1 / num2
        print(result)
        return result
    except ZeroDivisionError:
        print("На 0 делить нельзя")
        return "На 0 делить нельзя"

#safe_divide()

"""
-- 6 --
Доработать функцию safe_divide, чтобы она также обрабатывала ошибки, возникающие при вводе нечисловых символов.

подсказка

- Чтобы проверить, какая ошибка возникает при вводе нечисловых символов, нужно воспроизвести эту ситуацию и посмотреть на класс ошибки в сообщении интерпретатора Python (обычно выделяется красным шрифтом).
"""
def safe_divide_final():
    while True:
        try:
            num1 = float(input("Делимое:"))
            break
        except ValueError:
            print("Введи число")
            return "Введи число"
            #return False
            
    while True:
        try:
            num2 = float(input("Делитель:"))
            break
        except ValueError:
            print("Введи число")
            return "Введи число"

    try:
        result = num1 / num2
        print(result)
        return result
        #return result
    except ZeroDivisionError:
        print("На 0 делить нельзя")
        return "На 0 делить нельзя"

#safe_divide_final()



"""
-- 7 --
- Разработать интерактивный калькулятор: пользователь вводит формулу вида «12 + 8» или «15 - 10», программа вычисляет результат. Достаточно предусмотреть только сложение и вычитание. 
Предполагается, что первый операнд, знак операции и второй операнд обязательно должны быть разделены пробелами.
- Программа должна выводить сообщения об ошибках, если введена неверная формула или нечисловые символы.
- Ожидаемый результат и часть решения:
"""
def calculation() -> float:
    flag = True
    while flag == True:

        formula = input("Введите операцию типа '18 + 2':\n")
        check = formula.split(" ")
        if len(check) == 3:
            try:
                arg1 = float(check[0])
                arg2 = float(check[2])

                if check[1] == "+":
                    print(arg1 + arg2)
                    flag = False
                    return arg1 + arg2

                elif check[1] == "-":
                    print(arg1 - arg2)
                    flag = False
                    return arg1 - arg2

            except ValueError:
                flag == True
                print("Введи числа")
                #return "Введи числа"

        else:
            print("Введите данные вида 'число_+/-_число'")
            #return "Введите данные вида 'число_+/-_число'"
 
#calculation()

"""
-- 8 --
Доработать предыдущую программу, чтобы она распознавала операторы деления (/) и умножения (*), а также выводила сообщение в случае деления на 0.
"""

def calculation_all() -> float:
    flag = True
    while flag == True:

        formula = input("Введите операцию типа '18 + 2':\n")
        check = formula.split(" ")
        if len(check) == 3:
            try:
                arg1 = float(check[0])

                arg2 = float(check[2])
                
                char = check[1]
                if char in ["+", "-", "/", "*"]:

                    if check[1] == "+":
                        print(arg1 + arg2)
                        flag = False
                        return arg1 + arg2

                    elif check[1] == "-":
                        print(arg1 - arg2)
                        flag = False
                        return arg1 - arg2

                    elif check[1] == "*":
                        print(arg1 * arg2)
                        flag = False
                        return arg1 * arg2

                    elif check[1] == "/":
                        if arg2 != 0:
                            print(arg1 / arg2)
                            flag = False
                            return arg1 / arg2
                        else:
                            print("На 0 делить нельзя")
                            return "На 0 делить нельзя"
                else:
                    print("Введи математический знак '/', '+', '-', '*'")
                    #return "Введи математический знак '/', '+', '-', '*'"

            except ValueError:
                flag == True
                print("Введи числа")
                #return "Введи числа"
        else:
            print("Введите данные вида 'число_+/-_число'")
            #return "Введите данные вида 'число_+/-_число'"

#calculation_all()