#Создайте класс Student, который представляет студент.
# У него должны быть атрибуты для хранения имени, фамилии, возраста, адреса и список оценок.

class Student:
    grades = []
    def __init__(
            self, name, last_name, age, address, grades
    ):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)
        return self


lotsmanov = Student(
    name = "Alex",
    last_name = "Lotsmanov",
    age = 34,
    address = "Dolgoprudniy",
    grades = [4,4,5,5,3]
)

print(lotsmanov.grades)
lotsmanov.add_grade(5)
print(lotsmanov.grades)