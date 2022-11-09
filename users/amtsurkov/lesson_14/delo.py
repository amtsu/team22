class Delo():
    def calculate_len(self):
        return len(self.__delo)

    def delo_date(self):
        return self.__delo, self.__date_plan, self.__date_plan, self.__date_plan, self.__date_execute
    
    def __eq__(self, object_2):
        if self.__delo == object_2.__delo:
            return True
        return False
    
    1 == 1 __eq__
    1 > 0  __gt__
    2 < 10 __lt__  delo1 < delo2
    1 != 2 __ne__  delo1 != delo2
    
    
    
    #def get_delo(self):
    #    return self.__delo 
    
    def __hash__(self):
        return 1
        
    def __init__(self, d, plan, execute):
        self.__delo = d
        self.__date_plan = plan
        self.__date_execute = execute
        
    def is_delo_execute_in_plan_date(self):
        if self.__date_plan == self.__date_execute:
            return True
        return False    
    
    def __repr__(self):
        return self.__delo + '=>' + self.__date_plan + '=>' + self.__date_execute 

    def __str__(self):
        return self.__delo + '=>' + self.__date_plan + '=>' + self.__date_execute 
    
    #def uniq_delo():
    
    
    #def __str__(self):
    #    string = u'Delo:' + self.__delo+u' =>' + self.__date_plan+ u'=>' +self.__date_execute
    #    return string