from status_update import UserStatus

class UserInput:
    """
    Класс обработки сообщений и вовода информации пользователю
    Выводит пользователю меню с полем для ввода информации
    Обрабатывает результат ввода пользователя.
    Производит последующие действия: запись введенных данных в файл
    """
    def __init__(self, file):
        self.__login = input("Введите логин")
        self.__file = file
        self.__user_data = UserStatus(self.__file, self.__login)

    # def input_login(self):
    #     """Метод ввода и обработки логина пользователя"""
    #     user_login = input("Введите логин")

    def show_menu(self):
        """Метод вывода и обработки ввода пользователя"""
        user_menu = input("""Выберите действие:\n
        1 - visits_status.csv - посмотреть свои данные\n
        2 - visits_status.csv - редактировать свои данные\n
        3 - hw_status.csv - посмотреть свои данные\n
        4 - hw_status.csv - редактировать свои данные\n
        q - выход
        """)
        if user_menu not in ['1', '2', '3', '4', 'q'] or len(user_menu) != 1:
            print(f"Значечения {user_menu} нет в меню, попробуйте еще раз")
            show_menu()
        else:
            match user_menu:
                case '1':
                    print(self.__user_data.show_info())
                    return self.__user_data.show_info()
                case '2':
                    data = input('Введите значения в виде "Дата" (ДД-ММ-ГГГГ):"Значение"(число от 0 до 100 включительно). Можно перечислять через ","')
                    
                    
                    
            
            