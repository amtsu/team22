import pytest

from HW_09 import Phonebook, PhonebookRecord


phonebook_test_cases = [
        {
        "name": "Alexander",
        "phone": "932132542",
        "city": "Moscow",
        "hobby": ["programming"],
        "age": 20
        },
        {
        "name": "Oleg",
        "phone": "9743241121",
        "city": "Moscow",
        "hobby": ["chess", "book"],
        "age": 31
        },
        {
        "name": "Anna",
        "phone": "901329439",
        "city": "Ryazan",
        "hobby": [],
        "age": 35
        },
        {
        "name": "Olga",
        "phone": "961113121",
        "city": "Khimki",
        "hobby": ["music", "programming"],
        "age": 48
        }
    ]

phonebook_contacts = [
        ["Alexander", "932132542", "Moscow", ["programming"], 20],
        ["Oleg", "9743241121", "Moscow", ["chess", "book"], 31],
        ["Anna", "901329439", "Ryazan", [], 35],
        ["Olga", "961113121", "Khimki", ["music", "programming"], 48]
    ]

@pytest.fixture
def phonebook() -> Phonebook:
    pb = Phonebook()
    for item in phonebook_contacts:
        pb.add_new_record(PhonebookRecord(item[0], item[1], item[2], item[3], item[4]))
    return pb

def test_create_phonebook_record_with_not_string():
    """Создание объекта Запись не строкой."""
    with pytest.raises(ValueError):
        PhonebookRecord(name=123, phone=[], city={}, hobby="", age=())

def test_add_new_record(phonebook: Phonebook):
    """В справочник добавляются записи."""
    assert phonebook.all_records() == phonebook_test_cases

def test_sort_phonebook_by_name(phonebook: Phonebook):
    """Справочник сортируется по имени по алфавиту."""
    expected = sorted(phonebook_test_cases, key=lambda name: name["name"])
    assert phonebook.sort_phonebook_by_name() == expected

def test_sort_phonebook_by_name_assert_with_sort_by_phone(phonebook: Phonebook):
    """Справочник отсортированный по имени по алфавиту не совпадает
    с отсортированным по номеру телефона."""
    expected = sorted(phonebook_test_cases, key=lambda phone: phone["phone"])
    assert phonebook.sort_phonebook_by_name() != expected

def test_search_by_name_with_lowercase_letters(phonebook: Phonebook):
    """Поиск в справочнике по части имени строчными буквами
    выполняется корректно."""
    expected = [
        {
        "name": "Oleg",
        "phone": "9743241121"
        },
        {
        "name": "Olga",
        "phone": "961113121"
        }
    ]

    assert phonebook.search_by_name("ol") == expected

def test_search_by_name_with_uppercase_letters(phonebook: Phonebook):
    """Поиск в справочнике по части имени заглавными буквами
    выполняется корректно."""
    expected = [
        {
        "name": "Oleg",
        "phone": "9743241121"
        },
        {
        "name": "Olga",
        "phone": "961113121"
        }
    ]

    assert phonebook.search_by_name("OL") == expected

def test_search_by_name_with_uppercase_and_lowercase_letters(phonebook: Phonebook):
    """Поиск в справочнике по части имени заглавными и строчными
    буквами выполняется корректно."""
    expected = [
        {
        "name": "Oleg",
        "phone": "9743241121"
        },
        {
        "name": "Olga",
        "phone": "961113121"
        }
    ]

    assert phonebook.search_by_name("Ol") == expected

def test_search_by_name_with_empty_string(phonebook: Phonebook):
    """Поиск в справочнике по части имени с пустой строкой
    возвращает пустой список."""
    result = phonebook.search_by_name("")
    assert result == []

def test_search_by_name_with_not_match_string(phonebook: Phonebook):
    """Поиск в справочнике по части имени без совпадения в имени
    в справочнике возвращает пустой список."""
    result = phonebook.search_by_name("hasn't name")
    assert result == []

def test_search_by_name_with_not_string(phonebook: Phonebook):
    """Поиск в справочнике по части имени не строкой."""
    with pytest.raises(ValueError):
        phonebook.search_by_name(123)

def test_search_by_city_with_lowercase_letters(phonebook: Phonebook):
    """Поиск в справочнике по части города строчными буквами
    выполняется корректно."""
    expected = [
        {
        "name": "Alexander"
        },
        {
        "name": "Oleg"
        }
    ]

    assert phonebook.search_by_city("mos") == expected

def test_search_by_city_with_uppercase_letters(phonebook: Phonebook):
    """Поиск в справочнике по части города заглавными буквами
    выполняется корректно."""
    expected = [
        {
        "name": "Alexander"
        },
        {
        "name": "Oleg"
        }
    ]

    assert phonebook.search_by_city("MOS") == expected

def test_search_by_name_with_uppercase_and_lowercase_letters(phonebook: Phonebook):
    """Поиск в справочнике по части города заглавными и строчными
    буквами выполняется корректно."""
    expected = [
        {
        "name": "Alexander"
        },
        {
        "name": "Oleg"
        }
    ]

    assert phonebook.search_by_city("Mos") == expected

def test_search_by_city_with_empty_string(phonebook: Phonebook):
    """Поиск в справочнике по части города с пустой строкой
    возвращает пустой список."""
    result = phonebook.search_by_city("")
    assert result == []

def test_search_by_city_with_not_match_string(phonebook: Phonebook):
    """Поиск в справочнике по части имени без совпадения в имени
    в справочнике возвращает пустой список."""
    result = phonebook.search_by_city("hasn't city")
    assert result == []

def test_search_by_city_with_not_string(phonebook: Phonebook):
    """Поиск в справочнике по части города не строкой."""
    with pytest.raises(ValueError):
        phonebook.search_by_city(123)

def test_search_by_hobby(phonebook: Phonebook):
    """Поиск в справочнике по полному названию хобби."""
    expected = [
        {
        "name": "Alexander",
        "phone": "932132542",
        "city": "Moscow",
        "hobby": ["programming"],
        "age": 20
        },
        {
        "name": "Olga",
        "phone": "961113121",
        "city": "Khimki",
        "hobby": ["music", "programming"],
        "age": 48
        }
    ]
    assert phonebook.search_by_hobby("programming") == expected

def test_search_by_hobby_not_string(phonebook: Phonebook):
    """Поиск в справочнике по названию хобби не строкой."""
    with pytest.raises(ValueError):
        phonebook.search_by_city(123)

def test_search_by_hobby_not_hobby_in_phonebook(phonebook: Phonebook):
    """Поиск в справочнике по названию хобби, которого не в списке."""
    assert phonebook.search_by_hobby("unknown") == []
