import pickle


class Phonebook:
    def __init__(self):
        """Локальный телефонный справочник в формале словарей в списке"""
        self.__phonebook = []

    def add(self, name: str, phone_number: str, city: str):
        """Добавление в локальный справочник и загрузка локального справочника в пикл"""
        self.__phonebook.append({
            "name": name,
            "phone number": phone_number,
            "city": city
        },)
        with open("pickle_phonebook.pickle", "wb") as file:
            pickle.dump(self.__phonebook, file)

    def load(self) -> list[dict, dict, dict]:
        """Выгрузка данных из пикл"""
        with open("pickle_phonebook.pickle", "rb") as file:
            return pickle.load(file)

    def __str__(self):
        """Строковый вывод локального справочника"""
        return f"Phonebook: {self.__phonebook}"

