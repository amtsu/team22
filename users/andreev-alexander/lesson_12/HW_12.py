"""
Задание.
Каждому контакту в нашей программе с телефонным справочником добавить информацию
- о спорте которым человек занимается
- номер, название и адрес школы в которой учился
- цвет волос
- любимый фрукт
"""


import pickle


class PhonebookRecord:
    """Записи для помещения в телефонную книгу."""
    def __init__(self, name: str, phone: str, city: str, hobby: list[str], age: int, sport: list[str], school: dict[str, str | int], eye_color: str, fruit: str) -> None:
        
        self.__name = name
        self.__phone = phone
        self.__city = city
        self.__hobby = hobby
        self.__age = age
        self.__sport = sport
        self.__school = school
        self.__eye_color = eye_color
        self.__fruit = fruit

    def name(self):
        return self.__name
    
    def phone(self):
        return self.__phone
    
    def city(self):
        return self.__city

    def hobby(self):
        return self.__hobby
    
    def age(self):
        return self.__age
    
    def sport(self):
        return self.__sport
    
    def school(self):
        return self.__school
    
    def eye_color(self):
        return self.__eye_color
    
    def fruit(self):
        return self.__fruit
    
    def attrs(self):
        return {
            "name": self.__name,
            "phone": self.__phone,
            "city": self.__city,
            "hobby": self.__hobby,
            "age": self.__age,
            "sport": self.__sport,
            "school": self.__school,
            "eye_color": self.__eye_color,
            "fruit": self.__fruit
        }


class Phonebook():
    """Телефонная книга, принимающая записи типа PhonebookRecord."""
    def __init__(self) -> None:
        self.__phonebook: list = []

    def add_new_record(self, record: PhonebookRecord) -> None:
        """Добавление записи в телефонную книгу."""
        self.__phonebook.append(record.attrs())

    def sort_phonebook_by_name(self) -> list[dict]:
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
                    {"name": item["name"],
                    "phone": item["phone"]}
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
    
    def all_records(self) -> list[dict]:
        """Возвращает список всех записей в объекте."""
        return self.__phonebook
    
    def search_by_hobby(self, hobby: str) -> list[dict]:
        """Поиск пользователей по полному названию хобби."""
        if not isinstance(hobby, str):
            raise ValueError
        
        items_from_phonebook: list = []
        if hobby == "":
            return items_from_phonebook
        
        for item in self.__phonebook:
            if hobby.lower() in item["hobby"]:
                items_from_phonebook.append(item)
        return items_from_phonebook


phonebook = [
        [
            "Alexander", "932132542", "Moscow", ["programming"], 20, ["football"],
            {"name": "School 12", "number": 12, "address": "Moscow, Lenina, 2"},
            "grey", "apple"
            ],
        [
            "Oleg", "9743241121", "Moscow", ["chess", "book"], 31, ["chess", "football"],
            {"name": "School 2", "number": 2, "address": "Omsk, Mira, 10"},
            "blue", "orange"
            ],
        [
            "Anna", "901329439", "Ryazan", [], 35, ["MMA"],
            {"name": "School 2291", "number": 2291, "address": "Rzhev, Tsentralnaya, 22"},
            "green", "apple"
            ],
        [
            "Olga", "961113121", "Khimki", ["music", "programming"], 48, ["tennis"],
            {"name": "School 2291", "number": 2291, "address": "Rzhev, Tsentralnaya, 20"},
            "grey", "ananas"
            ]
    ]

pb = Phonebook()
for contact in phonebook:
    pb.add_new_record(PhonebookRecord(*contact))
# print(f"Все записи в книге:\n{pb.all_records()}.\n")
