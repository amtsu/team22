"""
Создайьте класс для учета студентов в учебном заведении. Реализуйте методы добавления нового студента(указав имя, возраст, ...), отчисление студента из учебного завдения и вывод списка всех студентов.
Измените класс учебного заведния чтобы они внутри себя для хранния информации о студентах использовал класс Student.
"""
from Student import Student


class MAI:

    def __init__(self):
        self.students = []

    def add_student(self, name, surname, age, address, rates):
        student = Student(name, surname, age, address, rates)
        self.students.append(student)
        #print(f"Студент {name} {surname} добавлен.")
        return self.students

    def remove_student(self, name, surname):
        for student in self.students:
            if student.name == name and student.surname == surname:
                self.students.remove(student)
                #print(f"Студент {name} {surname} удален.")
                return
        print(f"Студент {name} {surname} не найден.")

    def list_students(self):
        print("Список студентов:")
        for student in self.students:
            print(
                f"{student.name} {student.surname}, Возраст: {student.age}, Адрес: {student.address}, Оценки: {student.rates}")
        return self.students


# Пример использования:
mai = MAI()
mai.add_student("Иван", "Иванов", 20, "Москва", [4, 5, 4, 3])
mai.add_student("Петр", "Петров", 22, "Санкт-Петербург", [5, 5, 4, 5])
mai.add_student("Маша", "Смирнова", 19, "Забобруйск", [3, 2, 4, 3])
mai.list_students()
mai.remove_student("Иван", "Иванов")
mai.list_students()
