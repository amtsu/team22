import pickle


class Phonebook:

    def __init__(self):
        self.__phonebook = []
        self.__save_phonebook = None

    def add(self, name: str, phone_number: str, city: str):
        self.__phonebook.append({
            "name": name,
            "phone number": phone_number,
            "city": city
        })

    def save(self):
        with open("pickle_phonebook.pickle", "wb") as file:
            pickle.dump(self.__phonebook, file)

    def printing_phonebook(self):
        with open("pickle_phonebook.pickle", "rb") as file:
            return pickle.load(file)


first_obj = Phonebook()
first_obj.add("Artur", "84852345682", "Moscow")
first_obj.add("Alexandr", "84953457623", "St.Petersburg")
first_obj.add("Inokentiy", "80057777777", "Vladikavkaz")
first_obj.save()
print(first_obj.printing_phonebook())
