#Создайте класс Student, который представляет студент.
# У него должны быть атрибуты для хранения имени, фамилии, возраста, адреса и список оценок.

#part2 Расширьте класс Student, создав метод добавления новой оценки и метод вычисления среднего бала.

class Student:
    def __init__(
            self, name, last_name, age, address, grades = []
    ):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)
        return self

    def average(self):
        sum = 0
        for i in self.grades:
            sum += i
        return sum / len(self.grades)


'''lotsmanov = Student(
    name = "Alex",
    last_name = "Lotsmanov",
    age = 34,
    address = "Dolgoprudniy",
    grades = [4,4,5,5,3]
)

print(lotsmanov.grades)
lotsmanov.add_grade(5)
print(lotsmanov.grades)
print(lotsmanov.average())'''