from handlers import HwStatusHandler, VisitsStatusHandler


class UserMenu:
    """Класс создает пользовательское меню для работы с файлами статистики посещений и выполнения заданий."""

    def __init__(self, hw_status: HwStatusHandler, visits_status: VisitsStatusHandler):
        self.hw_status = hw_status
        self.visits_status = visits_status

    def show_menu(self):
        """Метод запускает меню для пользователя."""

        while True:
            user_menu: str = input(
                "\nВозможные действия:\n"
                "1 - Сколько человек были на лекции\n"
                "2 - Сколько человек приступали к заданию\n"
                "3 - Средний процент выполнения задания\n"
                "4 - ТОП-5 учеников по выполнению заданий\n"
                "5 - Узнать позицию ученика в рейтинге по его логину на GitHub\n"
                "6 - Узнать позицию ученика в рейтинге и кол-во посещенных занятий\n"
                "7 - Среднее количество выполненных заданий по группе\n"
                "8 - Успеваемость ученика (выше/ниже средней) по его логину на GitHub\n"
                "Введите номер действия или q для выхода: "
            )

            if user_menu not in '12345678q' or len(user_menu) != 1:
                print("\nУпс! Введите номер соответствующего меню (1-8) или q")
                continue

            try:
                match user_menu:
                    case '1':
                        input_message = 'Введите номер лекции или дату в формате ДД-ММ-ГГГГЖ: '
                        output_message = 'Кол-во учеников на лекции:'
                        print(output_message, self.visits_status.who_visited(input(input_message)))
                    case '2':
                        input_message = 'Введите номер домашнего задания: '
                        output_message = 'Кол-во учеников, приступавших к домашнему заданию:'
                        print(output_message, self.hw_status.who_do_hw(input(input_message)))
                    case '3':
                        input_message = 'Введите номер домашнего задания: '
                        output_message = 'Средний процент выполнения задания:'
                        print(output_message, self.hw_status.hw_avg(input(input_message)))
                    case '4':
                        print('ТОП-5 по успеваемости:')
                        for row in self.hw_status.get_ranked_list()[:5]:
                            print(row[0])
                    case '5':
                        input_message = 'Введите логин ученика: '
                        output_message = 'Позиция ученика в рейтинге:'
                        print(output_message, self.hw_status.get_pos_in_rank(input(input_message)))
                    case '6':
                        student = input('Введите логин ученика: ')
                        print('Позиция ученика в рейтинге:', self.hw_status.get_pos_in_rank(student))
                        print('Кол-во посещенных занятий:', self.visits_status.get_count_visits(student))
                    case '7':
                        output_message = 'Среднее количество выполненных заданий по группе:'
                        print(output_message, self.hw_status.avg_count_completed_tasks())
                    case '8':
                        student = input('Введите логин ученика: ')
                        if self.hw_status.get_student_activity(student):
                            print(f'Успеваемость {student} выше средней =)')
                        else:
                            print(f'Успеваемость {student} ниже средней =(')
                    case 'q':
                        print('\nВыполнен выход из программы"')
                        break
            except Exception as e:
                print(f'Произошла ошибка "{e}"')


start = UserMenu(HwStatusHandler('test_hw_status.csv'), VisitsStatusHandler('test_visits_status.csv'))
start.show_menu()
