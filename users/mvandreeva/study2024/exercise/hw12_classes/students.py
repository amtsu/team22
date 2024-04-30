class Student:
    """
    Класс представляет студента. 
    Имеет атрибуты для хранения имени, фамилии, возраста, адреса и список оценок.
    """
    def __init__(self, name, surname, age, address, record_book = []):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__address = address
        self.__record_book = record_book