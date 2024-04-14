"""
Создайте класс Student, который представляет студент.
У него должны быть атрибуты для хранения имени, фамилии,
возраста, адреса и список оценок.
"""


class Student:
    def __init__(self, name: str, surname: str, age: int, address: str, rating: list):
        self.__validation(self, name, surname, age, address, rating)
        self.__name: str = name.strip()
        self.__surname: str = surname.strip()
        self.__age: int = age
        self.__address: str = address.strip()
        self.__rating: list = rating

    @staticmethod
    def __validation(
        name: str, surname: str, age: int, address: str, rating: list
    ):
        """Валидация данных инициализации объекта класса"""
        is_valid_name: bool = isinstance(name, str)
        is_valid_surname: bool = isinstance(surname, str)

        MAX_HUMAN_AGE = 125
        is_valid_age: bool = (
            isinstance(age, int) and (age > 0) and (age <= MAX_HUMAN_AGE)
        )
        is_valid_address: bool = isinstance(address, str)

        is_valid_rating: bool = isinstance(rating, list)

        is_not_valid: bool = not (
            is_valid_name
            and is_valid_surname
            and is_valid_age
            and is_valid_address
            and is_valid_rating
        )
        if is_not_valid:
            raise TypeError("Ошибка инициализации. Некорректные данные")


st = Student("Вася", " Васильев", 21, "город Москва, улица Старая 5", [1, 2, 3, 4, 5])
