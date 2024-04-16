import pytest
from student import Student


Olga = Student('Olga', 'Ivanova', 18.0, 'F.Street, Samara, 144987', (10,9,10))

def test_petya_surname():
    expected = 'Ivanova'
    assert expected == Olga.surname


def test_student_1():
    student_1 = Student('Peter', 'Smith', '23.0', 'M Street, Washington 20036', [5, 7, 10])
    assert student_1.name == 'Peter'
    assert student_1.surname == 'Smith'
    assert student_1.age == '23.0'
    assert student_1.address == 'M Street, Washington 20036'
    assert student_1.grades == [5, 7, 10]


def test_student_2():  #float и tuple
    student_2 = Student('Olga', 'Ivanova', 18.0, 'F.Street, Samara, 144987', (10,9,10))
    assert student_2.name == 'Olga'
    assert student_2.surname == 'Ivanova'
    assert student_2.age == 18.0
    assert student_2.address == 'F.Street, Samara, 144987'
    assert student_2.grades == [10,9,10]


@pytest.mark.parametrize('name, surname, age, address, grades, expected', [   
    ('Galya', 'Petrova', 44, 'Lenina Street, Kaliningrad, 16, 431510', [0,0,0], ('Galya', 'Petrova', 44, 'Lenina Street, Kaliningrad, 16, 431510', [0,0,0])),
    ('Fedor', 'Dostoevsky', 18.0, 'F.Street, Samara, 144987', (10,9,10), ('Fedor', 'Dostoevsky', 18.0, 'F.Street, Samara, 144987', [10,9,10])),
    ('Alexander', 'Pushkin', 37, 'St. Petersburg', [10], ('Alexander', 'Pushkin', 37, 'St. Petersburg', [10])),
])


def test_init_students(name, surname, age, address, grades, expected):
    students = Student(name, surname, age, address, grades)
    assert (students.name, students.surname, students.age, students.address, students.grades) == expected, 'Ошибка'


def test_init_stud_negative():
    with pytest.raises(NameError):
        stud_negative == Student(Lena, 'Holms', '19.0', 'London', [-2, -1]), 'Ошибка'

                                
