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


def add_in_file(file_name: str, adding_name: str):
    """
    Добавляет в конец введенного файла введенную строку
    :param file_name: file name in str
    :param adding_name: adding name in str
    """
    file_descriptor = open(file_name, "a")
    file_descriptor.write(f" {adding_name}")
    file_descriptor.close()


print_file("names.txt", 200)
add_in_file("names.txt", "Evgeny")
print_file("names.txt", 300)
