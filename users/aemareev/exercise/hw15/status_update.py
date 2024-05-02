import csv


class CsvHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self):
        data = []
        with open(self.file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)
        return data

    def write_csv(self, data: list[list]):
        with open(self.file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in data:
                csv_writer.writerow(row)

    def get_user_index(self, name) -> int:
        """Метод возвращает номер строки пользователя."""

        data = self.read_csv()
        for n, row in enumerate(data):
            if row[0] == name:
                index = n
                break
        else:
            raise ValueError(f'Некорректный запрос: {name} нет в таблице!')

        return index

    def get_column_index(self, request: str) -> int:
        """Метод возвращает индекс столбца по запросу пользователя."""

        data = self.read_csv()
        for n, cell in enumerate(data[0]):
            if request in cell:
                index = n
                break
        else:
            raise ValueError(f'Некорректный запрос: {request} нет в таблице!')

        return index

    def show_user_info(self, name):
        """Метод выводит на экран информацию пользователя из файла."""

        data = self.read_csv()
        user_index = self.get_user_index(name)
        for h, v in zip(data[0], data[user_index]):
            print(f'{h:<23}{v}')


class UserMenu:
    """Класс пользовательского интерфейса для работы с файлами статусов."""

    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path
        self.visits_status: CsvHandler = CsvHandler(f'{file_path}visits_status.csv')
        self.hw_status: CsvHandler = CsvHandler(f'{file_path}hw_status.csv')

    def show_menu(self):
        """Метод запускает меню для пользователя."""

        while True:
            user_menu: str = input(
                "\nВозможные действия:\n"
                "1 - visits_status.csv - посмотреть свои данные\n"
                "2 - visits_status.csv - редактировать свои данные\n"
                "3 - hw_status.csv - посмотреть свои данные\n"
                "4 - hw_status.csv - редактировать свои данные\n"
                "Введите номер действия или q для выхода: "
            )

            if user_menu not in '1234q' or len(user_menu) != 1:
                print("\nУпс! Введите номер соответствующего меню (1-8) или q")
                continue

            try:
                match user_menu:
                    case '1':
                        self.visits_status.show_user_info(self.name)
                    case '2':
                        self.visits_status.show_user_info(self.name)
                        date = input('Введите дату для редактирования в формате ДД-ММ-ГГГГ: ')
                        user_index = self.visits_status.get_user_index(self.name)
                        column_index = self.visits_status.get_column_index(date)
                        data = self.visits_status.read_csv()
                        data[user_index][column_index] = input(f'Введите значение для {data[0][column_index]}: ')
                        self.visits_status.write_csv(data)
                        print('Изменение внесено! Результат:')
                        data = self.visits_status.read_csv()
                        print(f'{data[0][column_index]} -> {data[user_index][column_index]}')
                    case '3':
                        self.hw_status.show_user_info(self.name)
                    case '4':
                        self.hw_status.show_user_info(self.name)
                        date = input('Введите номер домашнего задания для редактирования: ')
                        user_index = self.hw_status.get_user_index(self.name)
                        column_index = self.hw_status.get_column_index(date)
                        data = self.hw_status.read_csv()
                        data[user_index][column_index] = input(f'Введите значение для {data[0][column_index]}: ')
                        self.hw_status.write_csv(data)
                        print('Изменение внесено! Результат:')
                        data = self.hw_status.read_csv()
                        print(f'{data[0][column_index]} -> {data[user_index][column_index]}')
                    case 'q':
                        print('\nВыполнен выход из программы"')
                        break
            except Exception as e:
                print(f'Произошла ошибка: {e}!')


login = input('Введите ваш GitHub-логин: ')
start = UserMenu(login, f'/home/jupyter-{login.lower()}/github/team22/library/streams/2024/')
start.show_menu()
