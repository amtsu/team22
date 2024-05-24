'''Напишите тест в котром в загружает из файла, потом отчисляет студента и записывает назад в фаил.'''

import pytest
import pickle
from student_extended import Student
from stud_registr_extended import StudentRegistry


def test_load_del_return():
    student1 = Student('Ivan', 'Ivanov', 22, 'Ivanovo', [5,4,5,3])
    student2 = Student('Petr', 'Petrov', 23, 'Petropalovsk', [3,3,4,5])

    student_registry = StudentRegistry()
    student_registry.add_student(student1) #добавила студента в реестр
    student_registry.add_student(student2)
    
    file = 'students_registry.pkl' 
    
    student_registry.save_to_file('students_registry.pkl')   #сохр реестр в файл 
    load_file = student_registry.load_from_file('students_registry.pkl') #выгрузила реестр из файла

    assert len(load_file.students) == 2
    
    student_registry.remove_student(student1)   #удалила студента из реестра 
    student_registry.save_to_file('students_registry.pkl') #сохр изменения в файл
    update_load_file = student_registry.load_from_file('students_registry.pkl') #выгрузила обновленный файл

    assert len(update_load_file.students) == 1
    


   

 
