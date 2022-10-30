class todo():
    def __init__(self, task, plan, executed):
        self.__task_name = task
        self.__plane_date = plan
        self.__executed_date = executed

    def __str__(self):
        return f'todo({self.__task_name}, {self.__plane_date}, {self.__executed_date})'

