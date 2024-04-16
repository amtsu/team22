import pytest 
from student import Student
from p2_student import Student2


def test_add_grade():
    '''тест метода добавления новой оценки'''
    student = Student2('Olga', 'Ivanova', 18.0, 'F.Street, Samara, 144987', [1,2])
    assert student.add_grade(5)== [1,2,5]


def test_add_grade_2():
    '''тест метода добавления новой отрицат оценки'''
    student = Student2('Oleg', 'Petrov', 90, 'Lenina Street, Saratov, 123456', (0, -2))
    student.add_grade(-7)
    assert student.grades == [0, -2], 'Ошибка. Оценка должна быть >= 0' #доработать __init__ чтобы оценки >= 0


def test_average_grade_1():
    '''тест метод для вычисления среднего балла'''
    student = Student2('Oleg', 'Petrov', 90, 'Lenina Street, Saratov, 123456', (0, -5, 5, 10, 10))
    assert student.average_grade() == 4


 
def test_average_grade_2():
    '''тест метод для вычисления среднего балла''' #пустой список
    student = Student2('Oleg', 'Petrov', 90, 'Lenina Street, Saratov, 123456', ())
    assert student.average_grade() == None
   
    




