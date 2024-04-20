#5. Создайте класс для учета студентов в учебном заведении. Реализуйте методы добавления нового студента(указав имя, возраст, ...), отчисление студента из учебного завдения и вывод списка всех студентов.

#6. Измените класс учебного заведния чтобы они внутри себя для хранния информации о студентах использовал класс Student.


from student import Student 

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

        
