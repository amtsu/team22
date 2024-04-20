import pytest
from p_2_student_registry import StudentRegistry
from student import Student 



harvard = StudentRegistry()

galya = Student('Galina', 'Petrova', 30, 'Kaliningrad, Lenina St.,16', [9, 7, 10])
fedya = Student('Fedor', 'Ivanov', 48.0, 'F.Street, Samara, 144987', [10, 9, 10])


def test_get_student_list():
    harvard.add_student(galya)
    harvard.add_student(fedya)
    expected = ['Galina Petrova [9, 7, 10]', 'Fedor Ivanov [10, 9, 10]'] #обращать вним на пробелы м/у оценками
    assert harvard.get_list_student() == expected


def test_remove():
    harvard.remove_student(galya) 
    expected = ['Fedor Ivanov [10, 9, 10]']
    assert expected == harvard.get_list_student()
 

