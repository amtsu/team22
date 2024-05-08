import csv


class CsvHandler:
    def __init__(self, file_path):
        self.input_file_path = file_path

    def read_csv(self):
        data = []
        with open(self.input_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)

        return data

    @staticmethod
    def get_index_by_string(lst: list, string: str) -> int:
        """Функция ищет индекс столбца по запросу пользователя."""

        for n, v in enumerate(lst):
            if string in v:
                index = n
                break
        else:
            raise ValueError('Вы ввели некорректный запрос!')

        return index


class HwStatusHandler(CsvHandler):
    """Класс для обработки данных выполнения домашних заданий."""

    def __init__(self, file_path):
        super().__init__(file_path)
        self.data = self.read_csv()

    def who_do_hw(self, hw_num: str) -> int:
        """Метод получает номер задания и возвращает то, сколько человек приступали к этому заданию."""

        index = self.get_index_by_string(self.data[0], hw_num)

        count = 0
        for row in self.data[1:]:
            if not row[index] or row[index] == '0' or row[index] == '0%':
                continue
            count += 1

        return count

    def hw_avg(self, hw_num) -> int | float:
        """Метод получает номер задания и возвращает средний процент выполнения задания у всех,
        кто к нему приступал."""

        index = self.get_index_by_string(self.data[0], hw_num)

        res_list = []
        for row in self.data[1:]:
            if not row[index] or row[index] == '0' or row[index] == '0%':
                continue
            if '%' in row[index]:
                res_list.append(row[index][:-1])
            else:
                res_list.append(row[index])

        try:
            final_res_list = list(map(int, res_list))
        except:
            raise ValueError('Данные в таблице заполнены не верно и не могут быть обработанны!')

        return round(sum(final_res_list) / len(final_res_list), 2)

    def get_ranked_list(self) -> list[list]:
        """Метод возвращает отранжированный список учеников от лучшего к худшему."""

        res_list = []
        for row in self.data[1:]:
            name = row[0]
            name_list = [name]
            for el in row[2:]:
                if not el or el == '0' or el == '0%':
                    continue
                if '%' in el:
                    name_list.append(el[:-1])
                else:
                    name_list.append(el)
            if len(name_list) > 1:
                res_list.append(name_list)

        res_list.sort(key=lambda x: (-x.count('100'), -sum(list(map(float, x[1:]))), x[0]))

        return res_list

    def get_pos_in_rank(self, name: str) -> int:
        """Метод принимает GitHub-логин ученика и возвращает его позицию в рейтинге."""

        data = self.get_ranked_list()

        for n, row in enumerate(data):
            if name in row:
                return n + 1
        else:
            raise ValueError('Такого ученика нет в таблице, или ученик не приступал к выполнению заданий!')

    def avg_count_completed_tasks(self) -> float:
        """Метод считает среднее количество выполненных группой заданий."""

        data = self.get_ranked_list()
        lst = [len(row[1:]) for row in data]
        return round(sum(lst) / len(lst), 1)

    def get_student_activity(self, name: str) -> bool:
        """Метод возвращает True, если успеваемость студента выше средней."""

        data = self.get_ranked_list()

        for row in data:
            if name in row:
                count = len(row[1:])
                break
        else:
            raise ValueError('Такого ученика нет в таблице, или ученик не приступал к выполнению заданий!')

        return count >= self.avg_count_completed_tasks()


class VisitsStatusHandler(CsvHandler):
    """Класс для обработки данных посещения занятий."""

    def __init__(self, file_path):
        super().__init__(file_path)
        self.data = self.read_csv()

    def who_visited(self, num: str) -> int:
        """Метод на вход получает дату или номер лекции и возвращает количество человек,
        которые были на этой лекции в этот день."""

        if len(num) <= 3:
            try:
                index = int(num) + 1
            except:
                raise ValueError('Введен некорректный запрос!')
        else:
            index = self.get_index_by_string(self.data[0], num)

        count = 0
        for row in self.data[1:]:
            if not row[index] or row[index] == '0':
                continue
            count += 1

        return count

    def get_count_visits(self, name: str) -> int:
        """Метод выводит сколько занятий посетил ученик."""

        for row in self.data[1:]:
            if name in row:
                name_list = [el for el in row[2:] if el]
                break
        else:
            raise ValueError(f'Пользователь с логином {name} не найден!')

        try:
            name_list = list(map(float, name_list))
        except:
            raise ValueError(f'Для пользователя {name} некорректно заполнены данные!')

        return int(round(sum(name_list)))


if __name__ == '__main__':
    hw = HwStatusHandler('test_hw_status.csv')
    assert hw.who_do_hw('11') == 2
    assert hw.hw_avg('9') == 70.45
    assert hw.get_ranked_list()[1][0] == 'Re-gi-na'
    assert hw.get_pos_in_rank('Re-gi-na') == 2
    assert hw.avg_count_completed_tasks() == 6.7
    assert hw.get_student_activity('Re-gi-na') == 1

    vs = VisitsStatusHandler('test_visits_status.csv')
    assert vs.who_visited('1') == 22
    assert vs.who_visited('4') == 27
    assert vs.get_count_visits('theRate') == 14
    assert vs.get_count_visits('VladimirVBykov') == 8
