def check_repeated_chars(input_str):
    if type(input_str) is not str:
        raise TypeError

    char_count = {}

    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    if len(char_count) == 0:
        result = -1
    else:
        result = [(k, v) for k, v in char_count.items() if v > 1]
        if len(result) == 0:
            result = -1

    return result


def get_nod(num1, num2):
    if type(num1) is not int or type(num1) is not int:
        raise TypeError
    if num1 == 0 or num2 == 0:
        raise ZeroDivisionError
    if num1 < 0 or num2 < 0:
        raise ValueError

    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def is_palindrome(string):
    if type(string) is not str:
        raise TypeError

    res_str = ''.join(char for char in string if char.isalpha() or char.isdigit()).lower()
    return res_str == res_str[::-1]


def day_of_week(num):
    if type(num) is not int:
        raise TypeError
    result = 'не день недели'
    match num:
        case 1:
            result = 'понедельник'
        case 2:
            result = 'вторник'
        case 3:
            result = 'среда'
        case 4:
            result = 'четверг'
        case 5:
            result = 'пятница'
        case 6:
            result = 'суббота'
        case 7:
            result = 'воскресенье'

    return result
