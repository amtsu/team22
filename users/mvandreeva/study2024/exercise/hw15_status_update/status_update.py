import csv

class UserStatus:
    """
    Класс для чтения файлов visits_status.csv и hw_status.csv как csv-формат.
    Имеет возможность редактировать значение статуса для определенной даты.
    Имеет возможность сохранения валидного для github csv-формата - 
		* разделители - запятые (,)
		* количество "колонок" одинаково для всех "строчек"
    """

    def __init__(self, file_to_edit, user_login): #file_to_edit должен содержать относительный путь от папки team22, включать название файла, в формате str
        # self.__clear_data()
        if isinstance(user_login, str) and isinstance(file_to_edit, str):
            self.__login = user_login 
            self.__file = f"/home/jupyter-{self.__login.lower()}/github/team22/{file_to_edit}"
        self.__user_row_num = None #номер ряда с логином пользователя
        self.__full_data = [] #полный список данных из файла
        self.__user_data = {} #строка данных пользователя
        self.__headers = [] #список заголовков файла
        self.__read_csv()

    def __read_csv(self):
        """Метод читает файл csv"""
        with open(self.__file, 'r') as csv_file: #Открываем файл
            csv_reader = csv.DictReader(csv_file, delimiter = ",")
            self.__headers = csv_reader.fieldnames
            row_num = 1 
            for row in csv_reader:    
                self.__full_data.append(row)
                row_num += 1
                if row["login in git hub"] == self.__login: #cверяем, есть ли в этой строке логин пользователя
                    self.__user_data = row #если есть, то записываем строку в переменную
                    print(f"self.__user_data: {self.__user_data}")
                    self.__user_row_num = row_num #записываем номер соответствующей строки
            if not self.__user_data: #если логин не найден, а строки закончились, выводим сообщение, что данного пользователя нет в списке
                print(f"Пользователя с логином {self.__login} нет в списке")
                self.__login = input("Введите логин")
                self.__clear_data()
                self.__read_csv()

    def update(self, changes_dict):
        """Метод редактирует данные пользователя, в соответствии с пользовательским вводом"""
        for k, v in changes_dict.items(): # для каждого переданного значения ищем совпадения с заголовками и заменяем значение в соответстыующем столбце
            if k in self.__user_data:
                self.__user_data[k] = v #заменяем значение в строке данных пользователя на пользовательский ввод
            else: 
                print(f"Значение {k} не найдено")
        # print(self.__user_row_num)
        i = 0
        for user_data in self.__full_data:
            if user_data["login in git hub"] == self.__login:
                self.__full_data[i] = self.__user_data # записываем изменения строки пользователя в общий список
                self.__save() #Сохраняем изменение в файл.
            i += 1
                
    def __save(self):
        """Метод сохранения данных в файл csv"""
        # print(self.__full_data)
        with open(self.__file, 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, delimiter = ",", fieldnames = self.__headers)
            csv_writer.writeheader()
            for row in self.__full_data:
                csv_writer.writerow(row)

    def __clear_data(self):
        self.__user_row_num = 1 #номер ряда с логином пользователя
        self.__full_data = [] #полный список данных из файла
        self.__user_data = {} #строка данных пользователя
        self.__headers = []

    def __str__(self):
        return f"{self.__full_data}"

    def show_info(self):
        # print(self.__user_data)
        return self.__user_data

