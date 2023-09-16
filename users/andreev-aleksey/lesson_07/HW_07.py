"""
Задание: Создать класс телефонный справочник с реализованными на уроке функциями.
- sort_phonebook_by_name() - сортировка записей в справочнике по имени по алфавиту
- search_by_name() - поиск человека в справочнике по части имени, в ответ выдавать имя и телефон
- search_by_city() - поиск человека в справочник по части города, в ответ выдавать имя, телефон и гороод
- add_new_record() - добавление новой записи в справочник: имя, телефон, город
- написать тесты
"""

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
                    'phone': person['phone'],
                    'name': person['name'],
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
                    'name': person['name'],
                    'phone': person['phone'],
                    'city': person['city']
                }
                result.append(new_element_phone_book)
        return result
    
    def sort_phone_book(self, key: str) -> None:
        sort_phone_book = sorted(self.__phone_book, key=lambda record: record[key])
        self.__phone_book = sort_phone_book

    def add_contact(self, name: str, phone: str, city: str) -> None:
        self.__phone_book.append({'name': name, "phone": phone, 'city': city})

    def phone_book_list(self) -> list[dict[str, str, str]]:
        return self.__phone_book

# pb = Phone_book()

# pb.add_contact(name="Oksana", phone="111111", city="piter")
# pb.add_contact(name="Aleksey", phone="888888888", city="Moscow")
# pb.add_contact(name="Sveta", phone="9999999", city="Chelyaba")
# pb.add_contact(name="Anna", phone="7777777", city="Murom")
# pb.add_contact(name="Sergey", phone="66666666", city="Vladik")

# print(pb.search_by_name("a"))
# print(pb.search_by_city("Moscow"))
# print(pb.phone_book_list())


# phone_book = [
#     {
#         "name": "Aleksey",
#         "phone": "888888888",
#         "city": "Moscow"
#     },
#     {
#         "name": "Sveta",
#         "phone": "9999999",
#         "city": "Chelyaba"
#     },
#     {
#         "name": "Anna",
#         "phone": "7777777",
#         "city": "Murom"
#     },
#     {
#         "name": "Sergey",
#         "phone": "66666666",
#         "city": "Vladik"
#     },
# ]
