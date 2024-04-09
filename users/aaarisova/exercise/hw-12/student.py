'''2. Создайте класс Student, который представляет студент. У него должны быть атрибуты для хранения имени, фамилии, возраста, адреса и список оценок.'''

class Student():
    
    def __init__(self, name, surname, age, address, grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.grades = grades

