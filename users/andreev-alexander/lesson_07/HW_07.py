"""
Задание: создать класс телефонный справочник с реализованными на уроке функциями.
- add_new_record() - добавление новой записи в справочник: имя, телефон, город
- sort_phonebook_by_name() - сортировка записей в справочнике по имени по алфавиту
- search_by_name() - поиск человека в справочнике по части имени, в ответ выдавать имя и телефон
- search_by_city() - поиск человека в справочник по части города, в ответ выдавать имя, телефон и гороод
- написать тесты
"""


class Phonebook():
    def __init__(self) -> None:
        self.__phonebook: list = []

    def add_new_record(self, name: str, phone: str, city: str) -> None:
        """Добавление записи в телефонную книгу."""
        if not (isinstance(name, str) or isinstance(phone, str) or isinstance(city, str)): 
            raise ValueError
        self.__phonebook.append({"name": name, "phone": phone, "city": city})

    def sort_phonebook_by_name(self) -> list[dict[str, str]]:
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

    def search_by_city(self, part_city: str) -> list[dict[str, str]]:
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
    
    def person_list(self) -> list[dict[str, str, str]]:
        """Возвращает список всех записей в объекте."""
        return self.__phonebook

phonebook = [
        {
        "name": "Alexander",
        "phone": "123321",
        "city": "Moscow"
        },
        {
        "name": "Oleg",
        "phone": "43241121",
        "city": "Moscow"
        },
        {
        "name": "Anna",
        "phone": "901329439",
        "city": "Ryazan"
        },
        {
        "name": "Olga",
        "phone": "0331111134e121",
        "city": "Khimki"
        }
    ]

pb = Phonebook()

# наполнение объекта записями из подготовленного словаря
for contact in phonebook:
    pb.add_new_record(**contact)
print(pb.sort_phonebook_by_name())
print(pb.search_by_name(""))
print(pb.search_by_city("Moscow"))
