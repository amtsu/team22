import pickle
from hw13_part1_Student import Student

class University():
    def __init__(self):
        self.students_list = []

    def __str__(self):
        students_str = "\n".join(str(student) for student in self.students_list)
        return f"{students_str}"

    def add_student(self, student: Student):
        """метод добавления нового студента"""
        self.students_list.append(student)
        
    def remove_student(self, surname):
        """метод удаления студента"""
        for student in self.students_list:
            if surname == student.surname:
                self.students_list.remove(student)
                break
        else:
            print(f"Cтудент {surname} не найден.")

    def count_students(self):
        """метод подсчета студентов в уч. заведении"""
        return len(self.students_list)
        
    def save_to_file(self, file_name):
        """
        сохраняем объект в файл с помощью сериализиции
        (преобразования объекта в поток байтов)
        """
        with open(file_name, "wb") as f:
            pickle.dump(self, f)
            
    def load_from_file(sels, file_name):
        """
        загружаем объект автомобиля из файла с помощью дессириализации
        (восстановление объекта их потока байтов)
        """
        with open(file_name, "rb") as f:
            return pickle.load(f)

