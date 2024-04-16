#Расширьте класс Student, создав метод добавления новой оценки и метод вычисления среднего бала.

from student import Student


class Student2(Student):

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
        

