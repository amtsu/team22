"""
Задание 1.
1.1. Создать телефонный справочник содержащий минимум три контакта.
Какждый контакт может иметь следующие параметры:
- имя
- город
- телефон
- хобби (список из 3 элементов)
- возраст (число)
1.2. Сохранить в файл с помощью функций библиотеки pickle.


Задание 2.
2.1. Загрузить телефонный справочник, который лежит в файле "название_файла"
2.2. Найти все контакты в справочники у котого есть хобби "программирование"
и кто старше 22 лет. Для этого нужно будет написать функции.
2.3. Затем добавить в справочник еще один контакт: Программист Вася +7916-222-33-44 27 лет.
2.4. Проверить, что вернет функция из 2 шага.
2.5. Вывести весь список контактов отсортированный по возрасту.
2.6. Сохранить изменния справочника на диск.


Желательно придумать несколько способов сохранения справочника (миниму 2).
Формат данных который можно использовать для спарвочника:

phone_book = [
    {
        'phone': '+79165556688',
        'city': 'Ulitsa lenina d 1',
        'name': 'Artem',
        'year': 1912,
        'hobby': ['sport', 'programming']
    },
]
"""


import pickle


class PhonebookRecord:
    """Записи для помещения в телефонную книгу."""
    def __init__(self, name: str, phone: str, city: str, hobby: list[str], age: int) -> None:
        # валидация входных параметров по типу
        if not (isinstance(name, str) and isinstance(phone, str) and isinstance(city, str)): 
            raise ValueError("Must be str")
        if not isinstance(hobby, list):
            raise ValueError("Must be list") 
        if not isinstance(age, int):
            raise ValueError("Must be int")
        
        self.__name = name
        self.__phone = phone
        self.__city = city
        self.__hobby = hobby
        self.__age = age

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
    
    def attrs(self):
        return {
            "name": self.__name,
            "phone": self.__phone,
            "city": self.__city,
            "hobby": self.__hobby,
            "age": self.__age
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


# 1.1. Создать телефонный справочник содержащий минимум три контакта.
phonebook = [
        ["Alexander", "932132542", "Moscow", ["programming"], 20],
        ["Oleg", "9743241121", "Moscow", ["chess", "book"], 31],
        ["Anna", "901329439", "Ryazan", [], 35],
        ["Olga", "961113121", "Khimki", ["music", "programming"], 48]
    ]

pb = Phonebook()
for contact in phonebook:
    pb.add_new_record(PhonebookRecord(*contact))
print(f"Все записи в книге:\n{pb.all_records()}.\n")

# 1.2. Сохранить в файл с помощью функций библиотеки pickle.
def save_to_file(phonebook: Phonebook):
    """Сохранение в файл pickle."""
    with open("pickle_file.pickle", "wb") as pickle_file:
        pickle.dump(phonebook, pickle_file)
save_to_file(pb)


# 2.1. Загрузить телефонный справочник, который лежит в файле "название_файла"
def extract_from_file():
    """Читает данные из файла pickle. Если файла нет, то печатается сообщение."""
    try:
        with open("pickle_file.pickle", "rb") as pickle_file:
            data_from_file = pickle.load(pickle_file)
            return data_from_file
    except FileNotFoundError:
        print("Файл не найден.")

pb_2: Phonebook = extract_from_file()
print(f"Все записи в книге после загрузки из файла:\n{pb.all_records()}.\n")


# 2.2. Найти все контакты в справочники у котого есть хобби "программирование"
# и кто старше 22 лет. Для этого нужно будет написать функции.
contacts = pb_2.search_by_hobby("programming")

def get_records_with_age_above_value(contacts: list, age: int):
    """Возвращает записи у которых значение возраста
    больше или равно заданного значения."""
    items_from_phonebook: list = []
    for item in contacts:
        if item["age"] >= age:
            items_from_phonebook.append(item)
    return items_from_phonebook

print(f"Контакты с возрастом больше 21:\n{get_records_with_age_above_value(contacts, 21)}\n")


# 2.3. Затем добавить в справочник еще один контакт: Программист Вася +7916-222-33-44 27 лет.
pb_2.add_new_record(PhonebookRecord(
    "Вася", "7916-222-33-44", "Saratov", ["programming"], 27
))

# 2.4. Проверить, что вернет функция из 2.2 шага.
contacts = pb_2.search_by_hobby("programming")
print(f"Контакты с возрастом больше 21:\n{get_records_with_age_above_value(contacts, 21)}\n")


# 2.5. Вывести весь список контактов отсортированный по возрасту.
print(f"Отсортированные по возврасту:\n{pb_2.sort_phonebook_by_name()}\n")


# 2.6. Сохранить изменния справочника на диск.
save_to_file(pb_2)
