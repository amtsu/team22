import csv


class CsvHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self) -> list[list]:
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

    def get_user_index(self, name: str) -> int:
        """Метод возвращает номер строки пользователя."""

        data = self.read_csv()
        for n, row in enumerate(data[1:]):
            if row[0] == name:
                index = n + 1
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

    def show_user_info(self, name: str):
        """Метод выводит на экран информацию пользователя из файла."""

        data = self.read_csv()
        user_index = self.get_user_index(name)
        for h, v in zip(data[0], data[user_index]):
            print(f'{h:<23}{v}')

    def edit_user_info(self, name: str, request: str):
        """Метод позволяет обновлять информацию в строке пользователя."""

        user_index = self.get_user_index(name)
        column_index = self.get_column_index(request)
        data = self.read_csv()
        data[user_index][column_index] = input(f'Введите значение для {data[0][column_index]}: ')
        self.write_csv(data)
        print('Изменение внесено! Результат:')
        data = self.read_csv()
        print(f'{data[0][column_index]} -> {data[user_index][column_index]}')


class UserMenu:
    """Класс пользовательского интерфейса для работы с файлами статусов."""

    def __init__(self, name: str, file_path: str = ''):
        self.name = name
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
                print("\nУпс! Введите номер соответствующего меню (1-4) или q")
                continue

            try:
                match user_menu:
                    case '1':
                        self.visits_status.show_user_info(self.name)
                    case '2':
                        self.visits_status.show_user_info(self.name)
                        date = input('Введите дату для редактирования в формате ДД-ММ-ГГГГ: ')
                        self.visits_status.edit_user_info(self.name, date)
                    case '3':
                        self.hw_status.show_user_info(self.name)
                    case '4':
                        self.hw_status.show_user_info(self.name)
                        hw_num = input('Введите номер домашнего задания для редактирования: ')
                        self.hw_status.edit_user_info(self.name, hw_num)
                    case 'q':
                        print('\nВыполнен выход из программы"')
                        break
            except Exception as e:
                print(f'Произошла ошибка: {e}!')


login = input('Введите ваш GitHub-логин: ')
start = UserMenu(login, f'/home/jupyter-{login.lower()}/github/team22/library/streams/2024/')
start.show_menu()