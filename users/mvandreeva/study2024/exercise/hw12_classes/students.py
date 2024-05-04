class Student:
    """
    Класс представляет студента. 
    Имеет атрибуты для хранения имени, фамилии, возраста, адреса и список оценок.
    """
    def __init__(self, name, surname, age, address, record_book = {}):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.record_book = record_book

    def get_mark(self, subject, mark):
        self.record_book[subject] = mark

    def count_avg_score(self):
        avg_score = sum(self.record_book.values())/len(self.record_book)
        return avg_score