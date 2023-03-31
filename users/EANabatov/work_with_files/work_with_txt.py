def print_file(file_name: str, number_of_characters_to_read: int) -> str:
    """
    Печатает необходимое количество символов из введенного файла
    :param file_name:
    :param number_of_characters_to_read:
    :return: string
    """
    file_descriptor = open(file_name, "r")
    print(file_descriptor.read(number_of_characters_to_read))
    file_descriptor.close()


def add_in_file_1_method(file_name: str, adding_name: str):
    """
    Добавляет в конец введенного файла введенную строку с помощью ключа "a"
    :param file_name: file name in str
    :param adding_name: adding name in str
    """
    file_descriptor = open(file_name, "a")
    file_descriptor.write(f" {adding_name}")
    file_descriptor.close()


def add_in_file_2_method(file_name: str, adding_name: str):
    """
    Добавляет в конец файла введенную строку с помощью ключа "w+"
    :param file_name: file name in str
    :param adding_name: adding name in str
    """
    with open(file_name, "r+") as file:
        file.seek(0, 2)
        file.write(f" {adding_name}")


def add_in_file_3_method(file_name: str, adding_name: str):
    """
    Добавляет в конец файла введенную строку используя ключи "r" и "w"
    :param file_name:
    :param adding_name:
    """
    with open(file_name, "r") as file:
        kek = file.readline()  # Сохраняем в переменную, что бы потом при вызове файла в режиме записи,
        # восстановить стертые фрагменты
    with open(file_name, "w") as file:
        file.write(f"{kek} {adding_name}")


print_file("names.txt", 200)
add_in_file_1_method("names.txt", "Viktor")
print_file("names.txt", 300)
add_in_file_2_method("names.txt", "Evgeny")
print_file("names.txt", 300)
add_in_file_3_method("names.txt", "Keker")
print_file("names.txt", 300)
