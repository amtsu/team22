#Создайьте класс для учета студентов в учебном заведении.
# Реализуйте методы добавления нового студента(указав имя, возраст, ...),
# отчисление студента из учебного завдения и вывод списка всех студентов.

#part2
#Измените класс учебного заведния чтобы они внутри себя для хранния информации о студентах использовал класс Student.
from student import Student

class University(Student):
    def __init__(self, list_students = {}):
        self.list_students = list_students
        #def add_student(self, name, last_name, age, address, grades):
    #    self.list_students[last_name] = (name, last_name, age, address, grades)
    def add_student(self, student):
        self.list_students[student.last_name] = student

    def del_student(self, name_student):
        del self.list_students[name_student]
    def all_students(self):
        answer = list(self.list_students)
        return answer


univer1 = University()

print(univer1.all_students())
lotsmanov = Student(
    name = "Alex",
    last_name = "Lotsmanov",
    age = 34,
    address = "Dolgoprudniy",
    grades = [4,4,5,5,3]
)

korchevaya = Student(
    name = "Olesya",
    last_name = "Korchevaya",
    age = 22,
    address = "Moscow",
    grades = [5,5,5,5,5]
)
univer1.add_student(lotsmanov)
univer1.add_student(korchevaya)
print(*univer1.all_students())
univer1.del_student('Lotsmanov')
print(*univer1.all_students())