from student import Student

class StudentList:
    """
    класс для учета студентов в учебном заведении. 
    Имеет методы добавления нового студента(указав имя, возраст, ...), отчисление студента из учебного завдения и вывод списка всех студентов.
    """
    def __init__(self, students_list = []):
        self.__students_list = []
        if students_list and isinstance(students_list, list):
            for student in students_list:
                self.__students_list.append(student.info())

    def add_student(self, name, surname, age, address, record_book = {}):
        new_student = Student(name, surname, age, address, record_book)
        self.__students_list.append(new_student.info())
        

    def expel(self, name, surname, age, address, record_book = {}):
        student_to_expel = Student(name, surname, age, address, record_book = {})
        for stud in self.__students_list:
            if student_to_expel.info() == stud:
                self.__students_list.remove(stud)

    def show_students(self):
        return self.__students_list