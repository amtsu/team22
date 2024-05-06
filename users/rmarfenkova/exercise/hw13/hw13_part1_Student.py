import pickle

class Student():
    def  __init__(self, name: str, surname: str, age: int, address: str, list_estimates: list):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.list_estimates = list_estimates

    def __str__(self):
        return f"{self.name}  {self.surname}  age: {self.age} "

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

    def save_to_file(self, file_name):
        """
        сохраняем объект в файл с помощью сериализиции
        (преобразования объекта в поток байтов)
        """
        with open(file_name, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_file(file_name):
        """
        загружаем объект автомобиля из файла с помощью десириализации
        (восстановление объекта их потока байтов)
        """
        with open(file_name, "rb") as f:
            return pickle.load(f)
            