import pytest

from HW_07 import Phone_book


phone_book_test = [
    {
        "name": "Aleksey",
        "phone": "888888888",
        "city": "Moscow"
    },
    {
        "name": "Sveta",
        "phone": "9999999",
        "city": "Chelyaba"
    },
    {
        "name": "Anna",
        "phone": "7777777",
        "city": "Murom"
    },
    {
        "name": "Sergey",
        "phone": "66666666",
        "city": "Vladik"
    },
]

phonebook_contacts = [
    ["Alexander", "123321", "Moscow"],
    ["Oleg", "43241121", "Moscow"],
    ["Anna", "901329439", "Ryazan"],
    ["Olga", "0331111134e121", "Khimki"]
]


@pytest.fixture
def phonebook() -> Phone_book:
    pb = Phone_book()
    for item in phone_book_test:
        pb.add_contact(item["name"], item["phone"], item["city"])
    return pb

def test_add_contact(phonebook: Phone_book):
    """Проверка добавления записей"""
    assert phonebook.phone_book_list() == phone_book_test


def test_sort_phone_book_by_name(phonebook: Phone_book):
    """Телефонная книга сортируется по имени по алфавиту."""
    result = sorted(phone_book_test, key=lambda record: record["name"])
    phonebook.sort_phone_book("name")
    assert phonebook.phone_book_list() == result


def test_sort_phone_book_by_name_assert_with_sort_by_phone(phonebook: Phone_book):
    """Телефонная книга отсортированная по городу не совпадает
    с отсортированной по номеру телефона."""
    result = sorted(phone_book_test, key=lambda phone: phone["city"])
    phonebook.sort_phone_book("phone")
    assert phonebook.phone_book_list() != result


def test_search_by_name_lower_case(phonebook: Phone_book):
    """Поиск по части имени совпадает с ожидаемым результатом"""
    result = [
        {
            "phone": "888888888",
            "name": "Aleksey",
        },
        {
            "phone": "7777777",
            "name": "Anna",
        },
    ]
    assert phonebook.search_by_name("a") == result


def test_search_by_name_upper_case(phonebook: Phone_book):
    """Поиск в справочнике по части имени заглавными буквами
    выполняется корректно."""
    result = [
        {
            "phone": "888888888",
            "name": "Aleksey",
        },
        {
            "phone": "7777777",
            "name": "Anna",
        },
    ]
    assert phonebook.search_by_name("A") == result


def test_search_by_city_with_lower_case(phonebook: Phone_book):
    """Поиск по части города маленькими буквами"""
    result = [
        {
            "name": "Aleksey",
            "phone": "888888888",
            "city": "Moscow"
        },
        {
            "name": "Anna",
            "phone": "7777777",
            "city": "Murom"
        },
    ]

    assert phonebook.search_by_city("m") == result


def test_search_by_city_with_upper_case(phonebook: Phone_book):
    """Поиск по части города большими буквами"""
    result = [
        {
            "name": "Aleksey",
            "phone": "888888888",
            "city": "Moscow"
        },
        {
            "name": "Anna",
            "phone": "7777777",
            "city": "Murom"
        },
    ]
    assert phonebook.search_by_city("M") == result


def test_search_by_name_empty_string(phonebook: Phone_book):
    """Поиск в телефонной книге по пустой строке
    возвращает все контакты"""
    empty_search = phonebook.search_by_name("")
    assert empty_search == phonebook.phone_book_list()


def test_search_by_city_with_empty_string(phonebook: Phone_book):
    """Поиск в телефонной книге по пустой строке
    возвращает все контакты"""
    empty_city = phonebook.search_by_city("")
    assert empty_city == phonebook.phone_book_list()


def test_search_by_city_with_not_match_string(phonebook: Phone_book):
    """Поиск по несовпадающему городу вернет пустой список"""
    result = phonebook.search_by_city("aaaaaaaa")
    assert result == []


def test_search_by_name_with_not_match_string(phonebook: Phone_book):
    """Поиск в телефонной книге по несуществующему имени ничего не вернет"""
    result = phonebook.search_by_name("aaaaaaaa")
    assert result == []


def test_search_by_city_with_not_string(phonebook: Phone_book):
    """Поиск в справочнике по части города не строкой."""
    with pytest.raises(TypeError):
        phonebook.search_by_city(111)


def test_search_by_name_with_not_string(phonebook: Phone_book):
    """Поиск в справочнике по части имени не строкой."""
    with pytest.raises(TypeError):
        phonebook.search_by_name(111)
