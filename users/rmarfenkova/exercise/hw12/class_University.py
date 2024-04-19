from class_Student import Student
"""
Создайьте класс для учета студентов в учебном заведении.
Реализуйте методы добавления нового студента(указав имя, возраст, ...),
отчисление студента из учебного завдения и вывод списка всех студентов.
"""

class University():
    def __init__(self):
        self.students_list = []

    def add_student(self, student):
        self.students_list.append(student)
        
    def remove_student(self, surname):
        for student in self.students_list:
            if surname == student.surname:
                self.students_list.remove(student)
        return f"Студент {surname} не найден"
        
    def display_students(self):
        result = []
        for student in self.students_list:
            result.append(f"{student.name} {student.surname}")
        return result