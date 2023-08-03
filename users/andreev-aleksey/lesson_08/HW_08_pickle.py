
# Задание 2
import pickle


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
        sort_phone_book = sorted(
            self.__phone_book, key=lambda record: record[key])
        self.__phone_book = sort_phone_book

    def add_contact(self, name: str, phone: str, city: str) -> None:
        self.__phone_book.append({'name': name, "phone": phone, 'city': city})

    def phone_book_list(self) -> list[dict[str, str, str]]:
        return self.__phone_book

pb = Phone_book()

pb.add_contact(name="Oksana", phone="111111", city="piter")
pb.add_contact(name="Aleksey", phone="888888888", city="Moscow")
pb.add_contact(name="Sveta", phone="9999999", city="Chelyaba")


# 1. Создать в питоне телефонный справочник и наполнить его тремя контактами.
# Сохранить его в файл используя пикл.
with open("phone_book.pickle", "wb") as f:
    pickle.dump(pb, f)

# 2. Распечатать справочник, прочитав его из файла.
with open("phone_book.pickle", "rb") as f:
    print("Записи из файла phone_book", pickle.load(f).phone_book_list())

# 3. Добавить в прочитанный из файла телефонный справочник новый контакт и сохранить.
new_contact =  {
        "name": "Anna",
        "phone": "7777777",
        "city": "Murom"
    }

with open("phone_book.pickle", "rb") as f:
    ph_book = pickle.load(f)
    ph_book.add_contact(new_contact["name"], new_contact["phone"], new_contact["city"]) 

with open("phone_book.pickle", "wb") as f:
    pickle.dump(ph_book, f)

with open("phone_book.pickle", "rb") as f:
    print("Записи из файла phone_book с новым контактом",
          pickle.load(f).phone_book_list())
