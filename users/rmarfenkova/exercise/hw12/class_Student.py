class Student():
    """
    Создайте класс Student, который представляет студент.
    У него должны быть атрибуты для хранения имени, фамилии, возраста, адреса и список оценок.
    """
    
    def  __init__(self, name: str, surname: str, age: int, address: str, list_estimates: list ):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.list_estimates = list_estimates


    """Расширьте класс Student, создав метод добавления новой оценки и метод вычисления среднего бала."""

    def add_estimates(self, value):
        """ метод добавления оценки"""
        self.list_estimates.append(value)

    def gpa(self):
        """ метод вычисления среднего балла"""
        if not len(self.list_estimates) == 0:
            gpa = sum(self.list_estimates) / len(self.list_estimates)
            return round(gpa, 2)
        else:
            return "Список пуст"
        

    

    