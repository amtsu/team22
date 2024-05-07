'''4. Расширьте класс для учета студентов в учебном заведении, добавьте методы сохранения и загрузки. Напишите тест в котром в загружает из файла, потом отчисляет студента и записывает назад в фаил.'''

import pickle 
from student_extended import Student 


class StudentRegistry():

    def __init__(self):
        self.students = []

  
    def add_student(self, student):
        self.students.append(student)

    
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
   

    def get_list_student(self):
        students_list = []
        for student in self.students:
            students_list.append(f'{student.name} {student.surname} {student.grades}')
        return students_list

    def save_to_file(self, file_name): #задание 2
        '''методы сохранения и загрузки обекта из памяти в файл'''
        with open(file_name, 'wb') as f:
            pickle.dump(self,f)

    @staticmethod
    def load_from_file(file_name):
        '''метод загрузки объекта из файла в память.'''
        with open(file_name, 'rb') as f:
            return pickle.load(f)

