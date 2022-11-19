class Todo():
    def __init__(self, task, plan, executed):
        self.__task_name = task
        self.__plane_date = plan
        self.__executed_date = executed

    def __str__(self):
        return f'todo({self.__task_name}, {self.__plane_date}, {self.__executed_date})'

    def __repr__(self):
        return f'todo({self.__task_name}, {self.__plane_date}, {self.__executed_date})'

    def __eq__(self, object_2):
        if self.__task_name == object_2.__task_name:
            return True
        return False

    def __hash__(self):
        return 1

    def eq_plane_exec(self):
        if self.__plane_date == self.__executed_date:
            return True
        return False

    def task_name_match(self, task_name):
        if self.__task_name == task_name:
            return True
        return False

    def task_symbol_count(self):
        return len(self.__task_name)

    def task_name(self):
        return str(self.__task_name)