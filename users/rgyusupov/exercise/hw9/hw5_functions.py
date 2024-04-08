def set_union(set1, set2):
    return set1 | set2


def set_difference(set1, set2):
    return set1.symmetric_difference(set2)


def is_subset(A, B):
    for x in A:
        if not x in B:
            return False
    return True


def union_sets(*sets):
    result = set()

    for sett in sets:
        result = result | sett

    return result


def remove_element(set, element):
    set.remove(element)
    return set


def find_intersection(set1, set2, *sets):
    result = set1.intersection(set2, *sets)
    return result


def is_equal(set1, set2):
    return set1 == set2


def union_3_sets(set1, set2, set3):
    return union_sets(set1, set2, set3)


def is_disjoint(set1, set2):
    for elem1 in set1:
        if elem1 in set2:
            return False

    return True


def find_difference(set1, set2):
    result = set()

    for elem in set1:
        if not (elem in set2):
            result.add(elem)

    return result


def find_symmetric_difference(set1, set2):
    result = set()

    for elem in set1:
        if not (elem in set2):
            result.add(elem)

    for elem in set2:
        if not (elem in set1):
            result.add(elem)

    return result


def create_set(*elements):
    return set(elements)


def create_dictionary(data):
    return dict(data)


def add_student(students_dict, student_name, student_age):
    students_dict[student_name] = student_age


def remove_student(students_dict, student_name):
    if student_name in students_dict:
        del students_dict[student_name]


def add_fruit(fruits_quantity, fruits_prices, fruit_name, quantity, price):
    fruits_quantity[fruit_name] = quantity
    fruits_prices[fruit_name] = price


def remove_fruit(fruits_quantity, fruits_prices, fruit_name):
    if fruit_name in fruits_quantity:
        del fruits_quantity[fruit_name]
    if fruit_name in fruits_prices:
        del fruits_prices[fruit_name]


def merge_dictionaries(dict1, dict2):
    return {**dict1, **dict2}


def remove_key_from_dict(dictionary, key):
    if key in dictionary:
        del dictionary[key]


def flip_dictionary(input_dict):
    return {value: key for key, value in input_dict.items()}


def sort_dict_by_keys_desc(dictionary):
    return dict(sorted(dictionary.items(), reverse=True))


def max_dict_value(dictionary):
    return max(dictionary.values()) if dictionary else None


def find_key_of_max_value(dictionary):
    if not dictionary:  # Проверка на пустоту словаря
        return None
    max_value = None
    max_key = None
    for key, value in dictionary.items():
        if max_value is None or value > max_value:
            max_value = value
            max_key = key
    return max_key


def check_fruit_price(prices, fruit, *, output_func=print):
    if fruit in prices and prices[fruit] > 1.5:
        output_func("дорогой товар")
    elif fruit in prices:
        output_func("цена приемлемая")
    else:
        output_func("фрукт не найден")


def check_age(students, name):
    if name in students:
        if students[name] >= 18:
            return "совершеннолетний"
        else:
            return "несовершеннолетний"
    else:
        return "Студент не найден"


def compare_sets_length(set1, set2, *, output_func=print):
    if len(set1) > len(set2):
        output_func("Первое множество длиннее")
    elif len(set1) < len(set2):
        output_func("Второе множество длиннее")
    else:
        output_func("Множества равны по длине")


def is_even(number):
    return "четное" if number % 2 == 0 else "нечетное"


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "високосный"
    else:
        return "обычный"


def triangle_type(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return "не треугольник"
    elif sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
        return "прямоугольный"
    elif sides[2] ** 2 < sides[0] ** 2 + sides[1] ** 2:
        return "остроугольный"
    else:
        return "тупоугольный"


def is_palindrome(s):
    return s == s[::-1]


def time_of_day(hours, minutes):
    if 6 <= hours < 12:
        return "утро"
    elif 12 <= hours < 18:
        return "день"
    elif 18 <= hours < 24:
        return "вечер"
    else:
        return "ночь"


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_alpha(s):
    return s.isalpha()


def is_valid_date(day, month, year):
    month_days = [31, 29 if is_leap_year(year) == "високосный" else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= month <= 12:
        return 1 <= day <= month_days[month - 1]
    return False


def is_number_palindrome(n):
    return str(n) == str(n)[::-1]


def print_fruits_info(fruits_quantity, fruits_price, *, output_func=print):
    for fruit, quantity in fruits_quantity.items():
        price = fruits_price.get(fruit)
        if price:
            output_func(f"{fruit}: количество - {quantity}, стоимость - {price * quantity}")
        else:
            output_func(f"{fruit}: нет информации о цене")


def print_squares_while(*, output_func=print):
    i = 1
    while i <= 5:
        output_func(i ** 2)
        i += 1


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def sum_in_range(start, end):
    return sum(range(start, end + 1))


def generate_primes(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes


def is_palindrome_insensitive(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def print_students(students, *, output_func=print):
    for name, age in students.items():
        output_func(f"{name}: {age} лет")


def get_value_from_user(threshold):
    while True:
        user_input = int(input("Введите число: "))
        if user_input > threshold:
            print("Число больше порога")
            break
        else:
            print("Попробуйте снова")


def check_age(*, input_func=input, output_func=print):
    age = int(input_func("Введите ваш возраст: "))
    if age < 18:
        output_func("Пользователь несовершеннолетний.")
    elif 18 <= age <= 65:
        output_func("Пользователь взрослый.")
    else:
        output_func("Пользователь пенсионер.")


def find_repeated_characters(*, input_func=input, output_func=print):
    user_input = input_func("Введите строку: ")

    character_counts = {}
    for character in user_input:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    repeated_characters = {char: count for char, count in character_counts.items() if count > 1}
    if repeated_characters:
        output_func("Повторяющиеся символы и количество их повторов:")
        for char, count in repeated_characters.items():
            form = 'раза' if 2 <= count % 10 <= 4 and not 11 <= count % 100 <= 19 else 'раз'
            output_func(f"Символ '{char}' повторяется {count} {form}.")
    else:
        output_func("Повторяющихся символов не найдено.")
