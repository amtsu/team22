'''2. Создайте класс Student, который представляет студент. У него должны быть атрибуты для хранения имени, фамилии, возраста, адреса и список оценок.'''

class Student():
    def __init__(self, name, surname, age, address, grades):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__address = address
        self.__grades = grades


    def new_student(self):
        return self.__name, self.__surname, self.__age, self.__address, self.__grades



    