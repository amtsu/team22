import pytest

from HW_07 import Phonebook


phonebook_test_cases = [
        {
        "name": "Alexander",
        "phone": "123321",
        "city": "Moscow"
        },
        {
        "name": "Oleg",
        "phone": "43241121",
        "city": "Moscow"
        },
        {
        "name": "Anna",
        "phone": "901329439",
        "city": "Ryazan"
        },
        {
        "name": "Olga",
        "phone": "0331111134e121",
        "city": "Khimki"
        }
    ]


pb = Phonebook()

def test_add_new_record():
    """В справочник добавляются записи."""
    for item in phonebook_test_cases:
        pb.add_new_record(**item)
    assert pb.person_list() == phonebook_test_cases

def test_add_new_record_with_not_string():
    """В справочник добавляются записи не строкой."""
    pb_not_string = Phonebook()
    with pytest.raises(ValueError):
        pb_not_string.add_new_record(name=123, phone=[], city={})

def test_sort_phonebook_by_name():
    """Справочник сортируется по имени по алфавиту."""
    expected = sorted(phonebook_test_cases, key=lambda name: name["name"])
    assert pb.sort_phonebook_by_name() == expected

def test_sort_phonebook_by_name_assert_with_sort_by_phone():
    """Справочник отсортированный по имени по алфавиту не совпадает
    с отсортированным по номеру телефона."""
    expected = sorted(phonebook_test_cases, key=lambda phone: phone["phone"])
    assert pb.sort_phonebook_by_name() != expected

def test_search_by_name_with_lowercase_letters():
    """Поиск в справочнике по части имени строчными буквами
    выполняется корректно."""
    expected = [
        {
        "name": "Oleg",
        "phone": "43241121"
        },
        {
        "name": "Olga",
        "phone": "0331111134e121"
        }
    ]

    assert pb.search_by_name("ol") == expected

def test_search_by_name_with_uppercase_letters():
    """Поиск в справочнике по части имени заглавными буквами
    выполняется корректно."""
    expected = [
        {
        "name": "Oleg",
        "phone": "43241121"
        },
        {
        "name": "Olga",
        "phone": "0331111134e121"
        }
    ]

    assert pb.search_by_name("OL") == expected

def test_search_by_name_with_uppercase_and_lowercase_letters():
    """Поиск в справочнике по части имени заглавными и строчными
    буквами выполняется корректно."""
    expected = [
        {
        "name": "Oleg",
        "phone": "43241121"
        },
        {
        "name": "Olga",
        "phone": "0331111134e121"
        }
    ]

    assert pb.search_by_name("Ol") == expected

def test_search_by_name_with_empty_string():
    """Поиск в справочнике по части имени с пустой строкой
    возвращает пустой список."""
    result = pb.search_by_name("")
    assert result == []

def test_search_by_name_with_not_match_string():
    """Поиск в справочнике по части имени без совпадения в имени
    в справочнике возвращает пустой список."""
    result = pb.search_by_name("hasn't name")
    assert result == []

def test_search_by_name_with_not_string():
    """Поиск в справочнике по части имени не строкой."""
    with pytest.raises(ValueError):
        pb.search_by_name(123)

def test_search_by_city_with_lowercase_letters():
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

    assert pb.search_by_city("mos") == expected

def test_search_by_city_with_uppercase_letters():
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

    assert pb.search_by_city("MOS") == expected

def test_search_by_name_with_uppercase_and_lowercase_letters():
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

    assert pb.search_by_city("Mos") == expected

def test_search_by_city_with_empty_string():
    """Поиск в справочнике по части города с пустой строкой
    возвращает пустой список."""
    result = pb.search_by_city("")
    assert result == []

def test_search_by_city_with_not_match_string():
    """Поиск в справочнике по части имени без совпадения в имени
    в справочнике возвращает пустой список."""
    result = pb.search_by_city("hasn't city")
    assert result == []

def test_search_by_city_with_not_string():
    """Поиск в справочнике по части города не строкой."""
    with pytest.raises(ValueError):
        pb.search_by_city(123)
