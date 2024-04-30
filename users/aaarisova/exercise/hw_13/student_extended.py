'''2. Расширьте класс Student, добавив методы сохранения и загрузки обекта студент из памяти в фаил и обратно. Создав тест который загружет студента из файла, добаляет новую оценку и сохраняет в фаил.'''
   
import pickle 

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

    
    def save_students(self, file_name): #задание 2
        with open(file_name, 'wb') as f:
            pickle.dump(self,f)

    @staticmethod
    def load_students(file_name):
        with open(file_name, 'rb') as f:
            return pickle.load(f)









