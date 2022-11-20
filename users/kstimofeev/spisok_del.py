class SpisokDel():
    def __init__(self):
        self.__list = []

    def append(self, element):
        self.__list.append(element)

    def __str__(self):
        r = ''
        for d in self.__list:
            r = r + str(d) + '__|__'
        return r

    def done_last_day(self):
        for task in self.__list:
            if task.eq_plane_exec():
                print(task)

    def check_task_match_value(self, task_name):
        for task in self.__list:
            if task.task_name_match(task_name):
                print(task)

    def tasks_length_more_than(self, amount):
        for task in self.__list:
            if task.task_symbol_count() > int(amount):
                print(task)

    def uniq_tasks(self):
        uniq_tasks = []
        for task in self.__list:
            if task not in uniq_tasks:
                uniq_tasks.append(task)
        return uniq_tasks

    def count_dupl_tasks(self):
        duplicate_list = []
        for uniq_task in self.uniq_tasks():
            count = 0
            for task in self.__list:
                if uniq_task == task:
                    count += 1
            if count > 1:
                duplicate_list.append([uniq_task.task_name(), count])
        return duplicate_list

    def count_dupl_tasks2(self):
        duplicate_dict = {}
        for task in self.__list:
            if task.task_name() in duplicate_dict:
                duplicate_dict[task.task_name()] += 1
            else:
                duplicate_dict[task.task_name()] = 1
        duplicate_dict = {task: count for task, count in duplicate_dict.items() if count > 1}
        return duplicate_dict

    def read_file(self, filename):
        with open(filename, 'rb') as handle:
            self.__list = pickle.load(handle)

    def write_file(self, filename):
        with open(filename, 'wb') as handle:
            pickle.dump(self.__list, handle)