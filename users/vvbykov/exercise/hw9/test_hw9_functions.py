import pytest
from hw9_functions import *


@pytest.mark.parametrize("input_hour, input_minutes, expected", 
                         [(5, 0, "morning"),
                          (5, 31, "morning"),
                          (10, 18, "morning"),
                          (11, 12, "morning"),
                          (13, 1, "afternoon"),
                          (12, 12, "afternoon"),
                          (14, 55, "afternoon"),
                          (15, 33, "afternoon"),
                          (18, 0, "evening"),
                          (23, 15, "night"),
                          (0, 0, "midnight"),
                          (0, 10, "night"),
                          (1, 13, "night"),
                          (3, 10, "night"),
                          (4, 59, "night")
                         ])
def test_define_times_of_day_positive(input_hour, input_minutes, expected):
    assert define_times_of_day(input_hour, input_minutes) == expected



@pytest.mark.parametrize("input_hour, input_minutes, expected", 
                         [(27, 16, "incorrect time"),
                          (15, 131, "incorrect time"),
                          (-15, -13, "incorrect time"),
                          (14, -20, "incorrect time"),
                          (-2, -48, "incorrect time")
                         ])
def test_define_times_of_day_negative(input_hour, input_minutes, expected):
    assert define_times_of_day(input_hour, input_minutes) == expected

#@pytest.mark.skip
@pytest.mark.parametrize("input_hour, input_minutes", 
                         [(10.0, 18.0),
                          ("11", "12"),
                          ("13", 1)
                         ])
def test_define_times_of_day_exception(input_hour, input_minutes):
#    with pytest.raises(TypeError):
#        hw9_functions.define_times_of_day(input_hour, input_minutes)
    pytest.raises(TypeError, define_times_of_day, input_hour, input_minutes)



@pytest.mark.parametrize("input, expected", 
                         [("aassdd", {"a": 2, "s": 2, "d": 2}),
                          ("qwerR EEasd ddd", {"r": 2, " ": 2, "e": 3, "d": 4}),
                          ("фывВы лор Ффак", {"ф": 3, "ы": 2, "в": 2, " ": 2}),
                          ("фы2вВы3 л2ор Фф2ак33", {"ф": 3, "ы": 2, "в": 2, " ": 2, "2": 3, "3": 3}),
                          ("кринж этот ваш ####, где $$$!!!!", {" ": 5, "т": 2, "#": 4, "$": 3, "!": 4}),
                          ("qwertyu iop[]", {})
                         ])
def test_check_repeated_symbols_positive(input, expected):
    assert check_repeated_symbols(input) == expected

@pytest.mark.parametrize("input, expected", 
                         [("", {})
                         ])
def test_check_repeated_symbols_negative(input, expected):
    assert check_repeated_symbols(input) == expected



db_students = {1: "Ivanov", 2: "Petrov", 3: "Sidorov", 4: "Borzov"}

@pytest.mark.parametrize("input_id, input_name, expected", 
                         [(5, "Vavilov", "OK"),
                          (6, "Юрочкин", "OK"),
                          (7, "Алимбетов-99", "invalid name"),
                          (8, "", "invalid name"),
                          (22, "£££_Slik", "invalid name"),
                          (5, "__Slik", "invalid name"),
                          (5, "Лет ми спик фром май харт", "invalid name"),
                          (-44, "chernyshov", "invalid id"),
                          (3, "Shov", "id is already exist"), 
                          (1, "Anybody", "id is already exist"), 
                          (10000, "Pasichnik", "OK") 
                          ])
def test_add_student_positive(input_id, input_name, expected):
    assert add_student(db_students, input_id, input_name) == expected


@pytest.mark.parametrize("input_id, input_name", 
                         [(0.2, "Chernyshov"),
                          ("1", "Morningov"),
                          (1, ["One", "Two"]), 
                          (1, 11)
                         ])
def test_add_student_execption(input_id, input_name):
    with pytest.raises(TypeError):
        add_student(input_id, input_name)


db_students = {1: "Ivanov", 2: "Petrov", 3: "Sidorov", 4: "Borzov", 1000: "Solo"}

@pytest.mark.parametrize("input_id, expected", 
                         [(1, "OK"),
                          (3, "OK"),
                          (37, "id doesn't exist"),
                          (8, "id doesn't exist"),
                          (-22, "invalid id"),
                          (0, "invalid id"),
                          (1000, "OK") 
                          ])
def test_remove_student_positive(input_id, expected):
    assert remove_student(db_students, input_id) == expected

@pytest.mark.parametrize("input_id", 
                         [(0.2),
                          ("1"),
                          ([1, 2, 3]), 
                          ((1, 2, 3))
                         ])
def test_remove_student_execption(input_id):
    with pytest.raises(TypeError):
        remove_student(input_id)


@pytest.mark.parametrize("input, expected", 
                         [("Ännä", True),
                          ("A man, a plan, a canal Panama", True),
                          ("123AA321", True),
                          ("Saippuakivikauppias", True),
                          ("Аргентина манит негра", True),
                          ("СОС", True),
                          ("", False),
                          ("Sofa", False),
                          ("Sofa 2", False)
                          ])
def test_check_palidrome_positive(input, expected):
    assert check_palidrome(input) == expected


@pytest.mark.parametrize("input_a, input_b, input_c, expected", 
                         [(464, 311, 690, "тупоугольный"),
                          (288, 307, 490, "тупоугольный"),
                          (327, 692, 672, "остроугольный"),
                          (130.3833, 98.8297, 163.6066, "прямоугольный"),
                          (403.39, 185.72, 375.04, "остроугольный"),
                          (327, 692.15, 672, "остроугольный")
                          ])
def test_triangle_type_positive(input_a, input_b, input_c, expected):
    assert triangle_type(input_a, input_b, input_c) == expected

@pytest.mark.parametrize("input_a, input_b, input_c, expected", 
                         [(327, -692, 672, "не треугольник"),
                          (327, 692, "672", "не треугольник"),
                          ("a2", "b17", "c34", "не треугольник"),
                          ])
def test_triangle_type_negative(input_a, input_b, input_c, expected):
    assert triangle_type(input_a, input_b, input_c) == expected


@pytest.mark.parametrize("input, expected", 
                         [(1900, False),
                          (1904, True),
                          (1928, True),
                          (1980, True),
                          (1948, True),
                          (1984, True),
                          (1996, True),
                          (2000, True),
                          (2016, True),
                          (1915, False),
                          (1925, False),
                          (1937, False),
                          (1999, False),
                          (2015, False),
                          (24, True),
                          (1937, False),
                          (1999, False),
                          (2015, False),
                          (1700, False),
                          (2100, False),
                          (1856, True),
                          (2164, True),
                          ("1900", False), 
                          ("1996", True),
                          ("2124", True),                          
                          ])
def test_check_leap_year_positive(input, expected):
    assert check_leap_year(input) == expected

#@pytest.mark.skip
@pytest.mark.parametrize("input", 
                         [(""),
                          ("nineteen twenty eight"),
                          ("y1980"),
                          ("1923.4"),
                          (1924.5),
                          ])
def test_remove_student_execption(input):
    with pytest.raises(TypeError):
        check_leap_year(input)
