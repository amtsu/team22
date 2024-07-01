class Student:
    def __init__(self, name, surname, age, adress, marks_list):
        self.name = name
        self.surname = surname
        self.age = age
        self.adress = adress
        self.marks_list = marks_list

    def add_mark(self, mark):
        self.marks_list.append(mark)

    def avg_mark(self):
        sum = 0
        for i in marks_list:
            sum = sum + i
        avg = sum / len(marks_list)

S1 = Student('Anna', 'Margolina', 28, 'Moscow', [1,3,5,3])
print (S1.marks_list)
S1.add_mark(5)
print (S1.marks_list)