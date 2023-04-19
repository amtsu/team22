from main import Phonebook

main_obj = Phonebook()
main_obj.add("Artur", "84852345682", "Moscow")
main_obj.add("Alexandr", "84953457623", "St.Petersburg")
main_obj.add("Innokentiy", "80057777777", "Vladikavkaz")
print(main_obj.load())