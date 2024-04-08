from hw5_fuctions import set_union, set_difference, is_subset, union_sets, remove_element, find_intersection, is_equal, \
    union_3_sets, is_disjoint, find_difference, find_symmetric_difference, create_set, create_dictionary, add_student, \
    remove_student, add_fruit, remove_fruit, merge_dictionaries, remove_key_from_dict, flip_dictionary, \
    sort_dict_by_keys_desc, max_dict_value, find_key_of_max_value, check_fruit_price, check_age, compare_sets_length, \
    is_even, is_leap_year, triangle_type, is_palindrome, time_of_day, is_prime, is_alpha, is_valid_date, \
    is_number_palindrome, factorial, sum_in_range, generate_primes, is_palindrome_insensitive, gcd, \
    find_repeated_characters, print_students, print_squares_while, print_fruits_info


def test_set_union():
    assert set_union({1, 2, 3}, {4, 5, 6}) == {1, 2, 3, 4, 5, 6}
    assert set_union({1, 2}, {2, 3}) == {1, 2, 3}


def test_set_difference():
    assert set_difference({1, 2, 3}, {2, 3, 4}) == {1, 4}
    assert set_difference({1, 2, 3}, {1, 2, 3}) == set()


def test_is_subset():
    assert is_subset({1, 2}, {0, 1, 2, 3}) is True
    assert is_subset({1, 2}, {0, 2, 3}) is False
    assert is_subset(set(), {1, 2, 3}) is True
    assert is_subset({1, 2}, set()) is False


def test_union_sets():
    assert union_sets({1, 2}, {3, 4}, {5, 6}) == {1, 2, 3, 4, 5, 6}
    assert union_sets({1, 2}, set(), {5, 6}) == {1, 2, 5, 6}
    assert union_sets(set(), set(), set()) == set()


def test_remove_element():
    assert remove_element({1, 2, 3}, 1) == {2, 3}


def test_find_intersection():
    assert find_intersection({1, 2, 3}, {1, 4, 5}, {1, 5, 6}) == {1}
    assert find_intersection({1, 2}, {3, 4}, {5, 6}) == set()
    assert find_intersection({1, 2, 3}, set(), {1, 2}) == set()


def test_is_equal():
    assert is_equal({1, 2}, {2, 1}) is True
    assert is_equal({1, 2}, {1, 2, 3}) is False


def test_union_3_sets():
    assert union_3_sets({1, 2}, {3, 4}, {5, 6}) == {1, 2, 3, 4, 5, 6}
    assert union_3_sets(set(), {1, 2}, {3}) == {1, 2, 3}


def test_is_disjoint():
    assert is_disjoint({1, 2}, {3, 4}) is True
    assert is_disjoint({1, 2}, {2, 3}) is False


def test_find_difference():
    assert find_difference({1, 2, 3}, {2, 3, 4}) == {1}
    assert find_difference({1, 2, 3}, {1, 2, 3}) == set()


def test_find_symmetric_difference():
    assert find_symmetric_difference({1, 2, 3}, {2, 3, 4}) == {1, 4}
    assert find_symmetric_difference({1, 2, 3}, {1, 2, 3}) == set()


def test_create_set():
    assert create_set(1, 2, 3, 4) == {1, 2, 3, 4}
    assert create_set(1, 2, 2, 3) == {1, 2, 3}
    assert create_set(1, "two", 3) == {1, "two", 3}


def test_create_dictionary():
    data = [('key1', 'value1'), ('key2', 'value2')]
    assert create_dictionary(data) == {'key1': 'value1', 'key2': 'value2'}


def test_add_student():
    students = {}
    add_student(students, 'Питонов', 18)
    add_student(students, 'Жаваскриптов', 19)
    assert students == {'Питонов': 18, 'Жаваскриптов': 19}


def test_remove_student():
    students = {'Питонов': 18, 'Жаваскриптов': 19}
    remove_student(students, 'Питонов')
    assert students == {'Жаваскриптов': 19}
    remove_student(students, 'Неизвестный')
    assert students == {'Жаваскриптов': 19}


def test_add_and_remove_fruit():
    fruits_quantity = {"яблоко": 5, "банан": 10, "апельсин": 7}
    fruits_prices = {"яблоко": 1.5, "банан": 2, "апельсин": 1.2}
    add_fruit(fruits_quantity, fruits_prices, 'яблоко', 10, 2.5)
    assert fruits_quantity == {"яблоко": 10, "банан": 10, "апельсин": 7}
    assert fruits_prices == {"яблоко": 2.5, "банан": 2, "апельсин": 1.2}
    remove_fruit(fruits_quantity, fruits_prices, 'яблоко')
    assert fruits_quantity == {"банан": 10, "апельсин": 7}
    assert fruits_prices == {"банан": 2, "апельсин": 1.2}


def test_merge_dictionaries():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    assert merge_dictionaries(dict1, dict2) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def test_remove_key_from_dict():
    dictionary = {'a': 1, 'b': 2, 'c': 3}
    remove_key_from_dict(dictionary, 'b')
    assert dictionary == {'a': 1, 'c': 3}


def test_flip_dictionary():
    input_dict = {'a': 1, 'b': 2, 'c': 3}
    assert flip_dictionary(input_dict) == {1: 'a', 2: 'b', 3: 'c'}


def test_sort_dict_by_keys_desc():
    dictionary = {'a': 3, 'b': 1, 'c': 2}
    assert sort_dict_by_keys_desc(dictionary) == {'c': 2, 'b': 1, 'a': 3}


def test_max_dict_value():
    dictionary = {'a': 10, 'b': 40, 'c': 30}
    assert max_dict_value(dictionary) == 40
    assert max_dict_value({}) is None


def test_find_key_of_max_value():
    dictionary = {'a': 10, 'b': 20, 'c': 30}
    assert find_key_of_max_value(dictionary) == 'c'
    assert find_key_of_max_value({}) is None


def test_check_age():
    students = {'Питонов': 18, 'Жаваскриптов': 19, 'Сишарпов': 17}
    assert check_age(students, 'Жаваскриптов') == "совершеннолетний"
    assert check_age(students, 'Сишарпов') == "несовершеннолетний"
    assert check_age(students, 'Рубинов') == "Студент не найден"


def test_check_fruit_price():
    outputs = []

    def custom_output_func(message):
        outputs.append(message)

    fruit_prices = {'яблоко': 1.2, 'банан': 2.0, 'киви': 1.8}

    # Test for a fruit with a high price
    check_fruit_price(fruit_prices, 'банан', output_func=custom_output_func)
    assert outputs == ["дорогой товар"], "должен быть дорогой товар"

    # Test for a fruit with an acceptable price
    outputs.clear()  # Clearing previous messages
    check_fruit_price(fruit_prices, 'яблоко', output_func=custom_output_func)
    assert outputs == ["цена приемлемая"], "должен быть цена приемлемая"

    # Test for a fruit that is not in the dictionary
    outputs.clear()  # Clearing previous messages
    check_fruit_price(fruit_prices, 'манго', output_func=custom_output_func)
    assert outputs == ["фрукт не найден"], "должен быть фрукт не найден"


def test_compare_sets_length():
    outputs = []

    def custom_output_func(message):
        outputs.append(message)

    compare_sets_length({1, 2, 3}, {4, 5, 6, 7}, output_func=custom_output_func)
    assert outputs == ["Второе множество длиннее"], "ожидалось, что второе множество длиннее"
    outputs.clear()

    compare_sets_length({1, 2, 3, 4}, {5, 6}, output_func=custom_output_func)
    assert outputs == ["Первое множество длиннее"], "ожидалось, что первое множество длиннее"
    outputs.clear()

    compare_sets_length({1, 2}, {3, 4}, output_func=custom_output_func)
    assert outputs == ["Множества равны по длине"], "ожидалось, что множества равны по длине"


def test_is_even():
    assert is_even(4) == "четное"
    assert is_even(5) == "нечетное"


def test_is_leap_year():
    assert is_leap_year(2020) == "високосный"
    assert is_leap_year(2021) == "обычный"


def test_triangle_type():
    assert triangle_type(3, 4, 5) == "прямоугольный"
    assert triangle_type(10, 10, 10) == "остроугольный"
    assert triangle_type(10, 10, 30) == "не треугольник"


def test_is_palindrome():
    assert is_palindrome("abcdcba") == True
    assert is_palindrome("abcde") == False


def test_time_of_day():
    assert time_of_day(11, 30) == "утро"
    assert time_of_day(23, 45) == "вечер"


def test_is_prime():
    assert is_prime(5) == True
    assert is_prime(4) == False
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-3) == False


def test_is_alpha():
    assert is_alpha("Hello") == True, "Ошибка: Hello должно быть алфавитным"
    assert is_alpha("123Hello") == False, "Ошибка: 123Hello не должно быть алфавитным"


def test_is_valid_date():
    assert is_valid_date(29, 2, 2020) == True, "Ошибка: 29 февраля 2020 года должна быть допустимой датой"
    assert is_valid_date(29, 2, 2021) == False, "Ошибка: 29 февраля 2021 года не должно существовать"
    assert is_valid_date(31, 12, 2020) == True, "Ошибка: 31 декабря 2020 года должна быть допустимой датой"
    assert is_valid_date(31, 4, 2020) == False, "Ошибка: 31 апреля 2020 года не должно существовать"


def test_is_number_palindrome():
    assert is_number_palindrome(12321) == True, "Ошибка: 12321 должно быть палиндромом"
    assert is_number_palindrome(1234) == False, "Ошибка: 1234 не должно быть палиндромом"


def test_factorial():
    assert factorial(5) == 120, "Ошибка: факториал 5 должен быть 120"
    assert factorial(3) == 6, "Ошибка: факториал 3 должен быть 6"


def test_sum_in_range():
    assert sum_in_range(1, 5) == 15, "Ошибка: сумма чисел от 1 до 5 должна быть 15"
    assert sum_in_range(10, 15) == 75, "Ошибка: сумма чисел от 10 до 15 должна быть 75"


def test_generate_primes():
    assert generate_primes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23,
                                   29], "Ошибка: список простых чисел до 30 не соответствует ожиданиям"


def test_is_palindrome_insensitive():
    assert is_palindrome_insensitive(
        "Madam, I'm Adam") == True, "Ошибка: 'Madam, I'm Adam' должно быть палиндромом при игнорировании регистра и неалфавитных символов"
    assert is_palindrome_insensitive("Hello") == False, "Ошибка: 'Hello' не должно быть палиндромом"


def test_gcd():
    assert gcd(54, 24) == 6, "Ошибка: НОД 54 и 24 должен быть 6"
    assert gcd(17, 5) == 1, "Ошибка: НОД 17 и 5 должен быть 1"


def test_print_fruits_info():
    outputs = []

    def custom_output_func(message):
        outputs.append(message)

    fruits_quantity = {'яблоко': 10, 'банан': 5}
    fruits_price = {'яблоко': 0.5, 'банан': 0.8}
    print_fruits_info(fruits_quantity, fruits_price, output_func=custom_output_func)
    assert outputs == [
        "яблоко: количество - 10, стоимость - 5.0",
        "банан: количество - 5, стоимость - 4.0"
    ], "Ошибка: неверная информация о фруктах"


def test_print_squares_while():
    outputs = []

    def custom_output_func(message):
        outputs.append(message)

    print_squares_while(output_func=custom_output_func)
    assert outputs == [1, 4, 9, 16, 25], "Ошибка: квадраты чисел от 1 до 5 неверны"


def test_print_students():
    outputs = []

    def custom_output_func(message):
        outputs.append(message)

    students = {'Иванова': 22, 'Петрова': 19}
    print_students(students, output_func=custom_output_func)
    assert outputs == ["Иванова: 22 лет", "Петрова: 19 лет"], "Ошибка: неверная информация о студентах"


def test_check_age():
    outputs = []

    def fake_input(prompt):
        return "18"

    def fake_output(message):
        outputs.append(message)

    check_age(input_func=fake_input, output_func=fake_output)
    assert outputs == ["Пользователь взрослый."], "Ошибка: возраст 18 должен быть взрослым"


def test_find_repeated_characters():
    outputs = []

    def fake_input(prompt):
        return "hello, world!"

    def fake_output(message):
        outputs.append(message)

    find_repeated_characters(input_func=fake_input, output_func=fake_output)
    assert "Символ 'l' повторяется 3 раза." in outputs, "Ошибка: неверное количество повторений для 'l'"
