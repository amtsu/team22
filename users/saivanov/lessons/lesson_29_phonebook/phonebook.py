"""
Модуль с описание класса "Телефонная книга"
"""
import pickle
from phonebookrecord import PhoneBookRecord


class PhoneBook:
    """
    класс, описывающий телефонную книгу
    """

    def __init__(self):
        """
        Конструктор класса
        """
        self.__records: [PhoneBookRecord] = []

    def __str__(self):
        """
        Возвращает строку с содержимым телефонной книги
        :return:
        """
        return "\n".join(str(record) for record in self.__records)

    def append(self, record: PhoneBookRecord) -> None:
        """
        Добавить запись в книгу
        :param record:
        :return:
        """
        self.__records.append(record)

    def save(self):
        """
        Сохранить книгу в файл
        """
        with open("local_phone_book.pickle", "wb") as fout:
            pickle.dump(self.__records, fout)

    def load(self):
        """
        Загрузить книгу из файла
        :return:
        """
        with open("local_phone_book.pickle", "rb") as fin:
            self.__records = pickle.load(fin)

    def search_by_name(self, search_data: str):
        """
        Поиск в телефонной книге по имени абонента
        :param search_data:
        :return:
        """
        result = PhoneBook()
        for record in self.__records:
            if search_data.lower() in record.name.lower():
                result.append(record)
        return result

    def search_by_city(self, search_data: str):
        """
        Поиск в телефонной книге по названию города проживания абонента
        :param search_data:
        :return:
        """
        result = PhoneBook()
        for record in self.__records:
            if search_data.lower() in record.city.lower():
                result.append(record)
        return result


    def export_csv(self, filename):
        """
        выгрузка данных телефонной книги в формат csv
        """
        with open(filename, "w") as fout:
            for record in self.__records:
                print(record.getcsv(), file=fout)

    def sort_by_name(self):
        """
        Сортировка телефонной книги по имени абонента
        :return:
        """
        self.__records.sort(key=lambda record: record.name)
