from main import SingletonPhonebook

first_obj = SingletonPhonebook()
# first_obj.clear_pickle()
first_obj.add_in_file("Singleton_phonebook.pickle", "Artur", "84852345682", "Moscow")
first_obj.add_in_file("Singleton_phonebook.pickle", "Alexandr", "84953457623", "St.Petersburg")
first_obj.add_in_file("Singleton_phonebook.pickle", "Innokentiy", "80057777777", "Vladikavkaz")
print(first_obj.load_from_file())

