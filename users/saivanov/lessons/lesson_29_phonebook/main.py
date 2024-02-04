"""
Модуль, обеспечивающий работу с телефонной книгой
"""
from phonebook import PhoneBook
from phonebookrecord import PhoneBookRecord


def add_record_to_phonebook_interactive() -> PhoneBookRecord:
    """
    интерактивный режим ввода записи в телефонную книгу
    :return:
    """
    name = input("Введите имя абонента: ")
    phone_number = input("Введите телефонный номер абонента: ")
    city = input("Введите город абонента: ")
    return PhoneBookRecord(name, phone_number, city)
    pass


def main() -> None:
    local_phonebook = PhoneBook()
    while True:
        available_user_actions = {
            "1": "Загрузить телефонную книгу",
            "2": "Вывести содержимое телефонной книги на экран",
            "3": "Найти абонента по имени",
            "4": "Найти абонента по городу",
            "5": "Отсортировать телефонную книгу по именам абонентов",
            "6": "Добавить новую запись в телефонную книгу",
            "7": "Сохранить телефонную книгу",
            "8": "Выгрузить данные телефонной книги в csv",
            "9": "Завершить работу",
        }
        print("Добро пожаловать в Телефонную книгу, что бы вы хотели:")
        for number in available_user_actions:
            print(f"{number} : {available_user_actions[number]}")
        user_choice = input("Введите номер действия:")
        user_choice = user_choice.strip()
        # if user_choice not in available_user_actions:
        #    continue
        # загрузить телефонную книгу
        if user_choice == "1":
            local_phonebook.load()
        # распечатать телефонную книгу
        if user_choice == "2":
            print(local_phonebook)
        # Найти абонента телефонной книги по имени
        if user_choice == "3":
            print(local_phonebook.search_by_name(input("Введите имя или его часть для поиска: ")))
        # Найти абонента телефонной книги по городу
        if user_choice == "4":
            print(local_phonebook.search_by_city(input("Введите название города или его часть для поиска: ")))
        # Отсортировать телефонную книгу по имени
        if user_choice == "5":
            local_phonebook.sort_by_name()
        # добавить запись в телефонную книгу
        if user_choice == "6":
            local_phonebook.append(
                add_record_to_phonebook_interactive()
            )
            print("Абонент добавлен!")
        # Сохранить телефонную книгу
        if user_choice == "7":
            local_phonebook.save()
        # Экспортировать телефонную книгу в csv
        if user_choice == "8":
            local_phonebook.export_csv(input("Введите имя файла для экспорта: "))
        # закончить это всё
        if user_choice == "9":
            break


# ---------------------------------------------------------------------
if '__main__' == __name__:
    main()
