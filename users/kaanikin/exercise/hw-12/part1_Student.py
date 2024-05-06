class Student:
   """
    Создайте класс Student, который представляет студент. У него должны быть атрибуты для хранения имени, фамилии, возраста, адреса и список оценок.
   """
   def __init__(self, name, family_name , age, address, marks_list):
       self.name = name
       self.family_name = family_name
       self.age = age
       self.address = address
       self.marks_list = marks_list

   def addMark(self, x):
       self.marks_list.append(x)

   def averageMark(self):
        total = 0
        for item in self.marks_list:
            total += item

        average = total/len(self.marks_list)
        return average



