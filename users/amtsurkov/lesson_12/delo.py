class Delo():
    def calculate_len(self):
        return len(self.__delo)

    def delo_date(self):
        return self.__delo, self.__date_plan, self.__date_plan, self.__date_plan, self.__date_execute
        
    def __init__(self, d, plan, execute):
        self.__delo = d
        self.__date_plan = plan
        self.__date_execute = execute
        
    def is_delo_execute_in_plan_date(self):
        if self.__date_plan == self.__date_execute:
            return True
        return False    
    
    def __str__(self):
        return self.__delo + '=>' + self.__date_plan + '=>' + self.__date_execute 
    #def __str__(self):
    #    string = u'Delo:' + self.__delo+u' =>' + self.__date_plan+ u'=>' +self.__date_execute
    #    return string