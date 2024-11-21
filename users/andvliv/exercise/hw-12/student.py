#Создайте класс Student, который представляет студент. У него должны быть атрибуты для хранения имени, фамилии, возраста, адреса и список оценок.
#Расширьте класс Student, создав метод добавления новой оценки и метод вычисления среднего бала.
class Student:
    def __init__(self, name, surname, age, adress, marks):
        self.name = name
        self.surname = surname
        self.age = age
        self.adress = adress
        self.marks = marks

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def get_adress(self):
        return self.adress

    def get_marks(self):
        return self.marks

    def new_mark(self, new_mark):
        self.marks.append(new_mark)

    def mean_marks(self):
        return sum(self.marks) / len(self.marks)
