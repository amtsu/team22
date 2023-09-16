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
        "phone": "+79165556688",
        "city": "Ulitsa lenina d 1",
        "name": "Artem",
        "year": 1912,
        "hobby": ["sport", "programming"]
    },
]
"""
import pickle
import datetime

class Phone_book:

    def __init__(self):
        self.__phone_book = []

    def search_by_name(self, name_part: str) -> list[dict[str, str]]:
        result = []
        if name_part == "":
            return self.__phone_book
        for person in self.__phone_book:
            len_part = len(name_part)
            if name_part.lower() in (person["name"][:len_part]).lower():
                new_element_phone_book = {
                    "phone": person["phone"],
                    "name": person["name"],
                }
                result.append(new_element_phone_book)
        return result

    def search_by_city(self, city: str) -> list[dict[str, str]]:
        result = []
        if city == "":
            return self.__phone_book
        for person in self.__phone_book:
            len_part = len(city)
            if city.lower() in (person["city"][:len_part]).lower():
                new_element_phone_book = {
                    "name": person["name"],
                    "phone": person["phone"],
                    "city": person["city"]
                }
                result.append(new_element_phone_book)
        return result

    def sort_phone_book(self, key: str) -> None:
        sort_phone_book = sorted(
            self.__phone_book, key=lambda record: record[key])
        self.__phone_book = sort_phone_book

    def add_contact(self, name, phone, city, year,  hobby) -> None:
        self.__phone_book.append({
            "name": name,
            "phone": phone,
            "city": city,
            "year": year,
            "hobby": hobby
        })

    def phone_book_list(self) -> list[dict[str, str, str]]:
        return self.__phone_book

    def search_by_hobby(self, hobby: str) -> list[dict[str, str]]:
        result = []
        if hobby == "":
            return self.__phone_book
        for person in self.__phone_book:
            if hobby.lower() in person["hobby"]:
                new_element_phone_book = {
                    "name": person["name"],
                    "phone": person["phone"],
                    "hobby": person["hobby"],
                    "year": person["year"],
                }
                result.append(new_element_phone_book)
        return result


pb = Phone_book()


# 1.1. Создать телефонный справочник содержащий минимум три контакта.
phone_book = [
    {
        "phone": "+111111",
        "city": "Ulitsa lenina d 1",
        "name": "Oksana",
        "year": 1983,
        "hobby": ["sport", "programming"]
    },
    {
        "phone": "+888888888",
        "city": "Ulitsa pravdy d 5",
        "name": "Aleksey",
        "year": 1989,
        "hobby": ["eda", "magazin"]
    },
    {
        "phone": "+9999999",
        "city": "ploshad stalina d 6",
        "name": "Sveta",
        "year": 1999,
        "hobby": ["programming", "lego"]
    },
    {
        "phone": "+7777777",
        "city": "derevnya byakino",
        "name": "Anna",
        "year": 1996,
        "hobby": ["knigi", "vyazanie"]
    },
]

for contact in phone_book:
    pb.add_contact(**contact)

# 1.2. Сохранить в файл с помощью функций библиотеки pickle.

def save_to_file(phone_book: Phone_book):
    """Сохранение в файл pickle."""
    with open("phone_book.pickle", "wb") as pickle_file:
        pickle.dump(phone_book, pickle_file)

save_to_file(pb)


# 2.1. Загрузить телефонный справочник, который лежит в файле "название_файла"
def loading_from_file():
    """Читает данные из файла pickle. Если файла нет, то печатается сообщение."""
    try:
        with open("phone_book.pickle", "rb") as pickle_file:
            data_from_file = pickle.load(pickle_file)
            return data_from_file
    except FileNotFoundError:
        print("Файл не найден.")


pb_upload: Phone_book = loading_from_file()
print(f"Все записи в книге после загрузки из файла:\n{pb_upload.phone_book_list()}.\n")


# 2.2. Найти все контакты в справочники у котого есть хобби "программирование"
# и кто старше 22 лет. Для этого нужно будет написать функции.

def get_contact_with_age_more_than(phonebook: Phone_book, age: int, hobby: str):
    """Возвращает записи у которых значение возраста
    больше или равно заданного значения."""
    contacts_hobby = phonebook.search_by_hobby("programming")
    result_contacts: list = []
    for item in contacts_hobby:
        age_to_days = (datetime.datetime.now().date() -
                    datetime.date(year=item["year"], month=1, day=1))
        contact_age = int(age_to_days.days/365)
        if contact_age >= age:
            result_contacts.append(item)
    return result_contacts

print(f"Контакты старше заданного возраста:\n{get_contact_with_age_more_than(phonebook=pb, age=22, hobby='programming')}\n")

# 2.3. Затем добавить в справочник еще один контакт: Программист Вася +7916-222-33-44 27 лет.
pb.add_contact(name="Вася", phone="7916-222-33-44", city="Saratov", hobby=["programming"], year=1996)


# 2.4. Проверить, что вернет функция из 2.2 шага.
print(f"Контакты старше заданного возраста и Вася:\n{get_contact_with_age_more_than(phonebook=pb, age=22, hobby='programming')}\n")


# 2.5. Вывести весь список контактов отсортированный по возрасту.
pb.sort_phone_book("year")
print(f"Отсортированные по возврасту:\n{pb.phone_book_list()}\n")


# 2.6. Сохранить изменния справочника на диск.
save_to_file(pb)
