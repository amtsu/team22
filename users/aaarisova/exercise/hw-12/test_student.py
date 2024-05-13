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


##########################################################

def test_add_grade():
    '''тест метода добавления новой оценки'''
    student = Student('Olga', 'Ivanova', 18.0, 'F.Street, Samara, 144987', [1,2])
    assert student.add_grade(5)== [1,2,5]


def test_add_grade_2():
    '''тест метода добавления новой отрицат оценки'''
    student = Student('Oleg', 'Petrov', 90, 'Lenina Street, Saratov, 123456', (0, -2))
    student.add_grade(-7)
    assert student.grades == [0, -2], 'Ошибка. Оценка должна быть >= 0'


def test_average_grade_1():
    '''тест метод для вычисления среднего балла'''
    student = Student('Oleg', 'Petrov', 90, 'Lenina Street, Saratov, 123456', (0, -5, 5, 10, 10))
    assert student.average_grade() == 4


 
def test_average_grade_2():
    '''тест метод для вычисления среднего балла''' #пустой список
    student = Student('Oleg', 'Petrov', 90, 'Lenina Street, Saratov, 123456', ())
    assert student.average_grade() == None


