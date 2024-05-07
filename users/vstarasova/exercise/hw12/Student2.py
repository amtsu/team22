"""
Расширьте класс Student, создав метод добавления новой оценки и метод вычисления среднего бала.
"""
from Student import Student
class Student2(Student):

    def add_rate(self, new_rate):
        self.rates.append(new_rate)
        return self.rates

    def calculateGPA(self):
        sum = 0
        r = 0
        for i in range(len(self.rates)):
            sum = sum + self.rates[i]
            r = r+1
        return (sum/r)

# Пример использования класса
student1 = Student2("Иван", "Иванов", 20, "ул. Пушкина, д. 10", [4, 5, 3, 4, 5])
