from main import SingletonPhonebook

second_obj = SingletonPhonebook()
second_obj.add("Goshan", "84567435674", "Vladivostok")
print(second_obj.load_from_file())