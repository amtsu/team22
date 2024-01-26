"""
Задание: создать класс телефонный справочник с реализованными на уроке функциями.
- add_new_record() - добавление новой записи в справочник: имя, телефон, город
- sort_phonebook_by_name() - сортировка записей в справочнике по имени по алфавиту
- search_by_name() - поиск человека в справочнике по части имени, в ответ выдавать имя и телефон
- search_by_city() - поиск человека в справочник по части города, в ответ выдавать имя, телефон и гороод
- написать тесты
"""


class PhonebookRecord:
    def __init__(self, name: str, phone: str, city: str) -> None:
        if not (isinstance(name, str) and isinstance(phone, str) and isinstance(city, str)): 
            raise ValueError("Must be str")
        self.__name = name
        self.__phone = phone
        self.__city = city

    def name(self):
        return self.__name
    
    def phone(self):
        return self.__phone
    
    def city(self):
        return self.__city


class Phonebook():
    def __init__(self) -> None:
        self.__phonebook: list = []

    def add_new_record(self, record: PhonebookRecord) -> None:
        """Добавление записи в телефонную книгу."""
        self.__phonebook.append(
            {
            "name": record.name(),
            "phone": record.phone(),
            "city": record.city()
            }
        )

    def sort_phonebook_by_name(self) -> list[dict[str, str, str]]:
        """Сортировка записей в справочнике по имени по алфавиту."""
        sorted_phonebook = sorted(self.__phonebook, key=lambda name: name["name"])
        return sorted_phonebook
    
    def search_by_name(self, part_name: str) -> list[dict[str, str]]:
        """Поиск записи в справочнике по части имени."""
        if not isinstance(part_name, str):
            raise ValueError
        
        items_from_phonebook: list = []
        if part_name == "":
            return items_from_phonebook
        
        for item in self.__phonebook:
            if part_name.lower() in item["name"].lower():
                items_from_phonebook.append(
                    {"phone": item["phone"],
                    "name": item["name"]}
                    )
        return items_from_phonebook

    def search_by_city(self, part_city: str) -> list[dict[str]]:
        """Поиск человека в справочник по части города."""
        if not isinstance(part_city, str):
            raise ValueError
        
        items_from_phonebook: list = []
        if part_city == "":
            return items_from_phonebook
        
        for item in self.__phonebook:
            if part_city.lower() in item["city"].lower():
                items_from_phonebook.append(
                    {"name": item["name"]}
                    )
        return items_from_phonebook
    
    def all_records(self) -> list[dict[str, str, str]]:
        """Возвращает список всех записей в объекте."""
        return self.__phonebook

phonebook = [
        ["Alexander", "123321", "Moscow"],
        ["Oleg", "43241121", "Moscow"],
        ["Anna", "901329439", "Ryazan"],
        ["Olga", "0331111134e121", "Khimki"]
    ]


# pb = Phonebook()
# наполнение объекта записями из подготовленного словаря
# for contact in phonebook:
#     pb.add_new_record(PhonebookRecord(contact[0], contact[1], contact[2]))
# print(pb.sort_phonebook_by_name())
# print(pb.search_by_name("A"))
# print(pb.search_by_city("Moscow"))
