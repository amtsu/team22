import pickle


class SingletonPhonebook:
    __instance = None

    def __new__(cls):
        """
        Проверка на первое создание и присваивание всем последующим
        объектам этого класса этой же ячейки памяти
        """
        if SingletonPhonebook.__instance is None:
            SingletonPhonebook.__instance = super().__new__(cls)
        return SingletonPhonebook.__instance

    def __init__(self):
        """Локальный телефонный справочник в формате списка"""
        self.__phonebook = []

    def add_in_file(self, file_for_open: str, name: str, phone_number: str, city: str):
        self.__copy(file_for_open)
        self.__add_in_phonebook(name, phone_number, city)
        self.__save_in_pickle(file_for_open)

    def __copy(self, file_for_open: str):
        with open(file_for_open, "rb") as file:
            self.__phonebook.extend(pickle.load(file))

    def __add_in_phonebook(self, name: str, phone_number: str, city: str):
        self.__phonebook.append({
            "name": name,
            "phone number": phone_number,
            "city": city},
        )

    def __save_in_pickle(self, file_for_open: str):
        with open(file_for_open, "wb") as file:
            pickle.dump(self.__phonebook, file)

    @staticmethod
    def load_from_file(file_for_open: str):
        """Выгрузка данных из пикл"""
        with open(file_for_open, "rb") as file:
            return pickle.load(file)

    # def clear_pickle(self):
    #     open("Singleton_phonebook.pickle", "wb").close()
