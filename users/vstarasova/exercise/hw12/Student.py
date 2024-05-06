"""
Создайте класс Student, который представляет студент. У него должны быть атрибуты для хранения имени, фамилии, возраста, адреса и список оценок
"""
class Student:
    
    def __init__(self, name, surname, age, address, rates):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.rates = rates

# Пример использования класса
student1 = Student("Иван", "Иванов", 20, "ул. Пушкина, д. 10", [4, 5, 3, 4, 5])

# Получаем информацию о студенте
print("ФИО студента:", student1.name, student1.surname)
print("Возраст студента:", student1.age)
print("Адрес студента:", student1.address)
print("Список оценок:", student1.rates)

# Пример создрания списка студентов
students_MAI = [Student("Иван", "Иванов", 20, "ул. Пушкина, д. 10", [4, 5, 3, 4, 5]), Student("Петр", "Петров", 19, "ул. Гоголя, д. 10", [3, 2, 3, 4, 3])]