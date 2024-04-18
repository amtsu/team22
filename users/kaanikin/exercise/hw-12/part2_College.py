from part1_Student import Student

class College:
    """Создайьте класс для учета студентов в учебном заведении. Реализуйте методы добавления нового студента(указав имя, возраст, ...), отчисление студента из учебного завдения и вывод списка всех студентов."""
    def __init__(self):
        self.student_list = []

    def add(self, stud): 
        self.student_list.append(stud) 
 
    def remove(self, stud): 
        if stud in self.student_list:
            self.student_list.remove(stud)
                
        
 
    def get_list(self): 
        lst = [] 
        for item in self.student_list: 
            lst.append(f"{item.name} {item.family_name}") 
        return lst 


