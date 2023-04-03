"""
Работа с файлами. #HW

Задание √1.
1. Создать файл с именами знакомых: Misha, Vovan, Anakentiy.
2. Прочитать его в питоне. Вывести на экран.
3. Добавить ещё одного знакомого с именем Petya

*нужно написать без использования  “a” (append), то есть только с использованием режимов открытия файла  “r”(read) и “w”(write)
"""
# 1. Создать файл с именами знакомых: Misha, Vovan, Anakentiy.
file = open("imena.txt", "w")
file.write("Misha, Vovan, Anakentiy")
file.close()

# 2. Прочитать его в питоне. Вывести на экран.
file = open("imena.txt", "r")
print(file.read())

# 3. Добавить ещё одного знакомого с именем Petya
# *нужно написать без использования  “a” (append), то есть только с
# использованием режимов открытия файла  “r”(read) и “w”(write)
file = open("imena.txt", "r")
new_line = file.read()
file.close()
file_with_new_line = f"{new_line}, Petya"
file = open("imena.txt", "w")
file.write(file_with_new_line)
file.close()
file = open("imena.txt", "r")
print(file.read())


"""
Задание√2.
1. Создать в питоне телефонный справочник и наполнить его тремя контактами. Сохранить его в файл используя пикл.
2. Распечатать справочник, прочитав его из файла.
3. Добавить в прочитанный из файла телефонный справочник новый контакт и сохранить.

Должно получиться 3 питон скрипта (*.py)
"""
import pickle


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
        ["Anna", "901329439", "Ryazan"]
    ]


pb = Phonebook()
# наполнение объекта записями из подготовленного словаря
for contact in phonebook:
    pb.add_new_record(PhonebookRecord(contact[0], contact[1], contact[2]))

# 1. Создать в питоне телефонный справочник и наполнить его тремя контактами.
# Сохранить его в файл используя пикл.
with open("pickle_file.pickle", "wb") as pickle_file:
    pickle.dump(pb, pickle_file)

# 2. Распечатать справочник, прочитав его из файла.
with open("pickle_file.pickle", "rb") as pickle_file:
    print("Записи из файла pickle", pickle.load(pickle_file).all_records())

# 3. Добавить в прочитанный из файла телефонный справочник новый контакт и сохранить.
new_contact = PhonebookRecord("Ivan", "02837393", "Karaganda")

with open("pickle_file.pickle", "rb") as pickle_file:
    ph_book = pickle.load(pickle_file)
    ph_book.add_new_record(new_contact)  # добавил новую запись

with open("pickle_file.pickle", "wb") as pickle_file:
    pickle.dump(ph_book, pickle_file)

with open("pickle_file.pickle", "rb") as pickle_file:
    print("Записи из файла pickle с новым контактом", pickle.load(pickle_file).all_records())
