'''2. Создайте класс Student, который представляет студент. У него должны быть атрибуты для хранения имени, фамилии, возраста, адреса и список оценок.'''

class Student():
    
    def __init__(self, name: str, surname: str, age: int, address: str, grades: list):
        '''Конструктор класса Student'''
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.grades = list(grades)
        

    def add_grade(self, grade):
        '''метод добавления новой оценки'''
        if grade >= 0:
            self.grades.append(grade)
            return self.grades
        else:
            return self.grades, 'Ошибка. Оценка должна быть >= 0'


    def average_grade(self):
        '''метод для вычисления среднего балла'''
        if not self.grades:
            return None
        
        return sum(self.grades) / len(self.grades)

    
        
