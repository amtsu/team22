class Delo():
    def __init__(self, task, deadline, done):
        self.__delo = task
        self.__date_plan = deadline
        self.__date_execute = done
        
    def done_same_day(self):
        if self.__date_plan ==  self.__date_execute:
            return True 
        return False
    
    def task_date(self):
        return self.__delo, 'sdelano', self.__date_execute
    
    def __repr__(self):
        return self.__delo + ' => ' + self.__date_plan + ' => ' + self.__date_execute 
    
    def __hash__(self):
        return 1
    
    def __eq__(self, object_2):
        if self.__delo == object_2.__delo:
            return True
        return False
 