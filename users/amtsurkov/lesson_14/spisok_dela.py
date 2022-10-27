class SpisokDela():
    
    def append(self, element): # add -
        self.__list.append(element)
        
#    def v1_has_list_duplicate_dela(self):
#        #print(__list)
#        for delo_uniq in self.__uniq_list_del():
#            count_del = 0
#            for delo_from_list in self.__list:
#                if delo_uniq == delo_from_list:
#                    count_del = count_del + 1
#            #print(delo_uniq, count_del)
#            if count_del > 1:
#                return True
#            return False
#        
#    def v2_has_list_duplicate_dela(self):
#        for delo in self.__list:
#            if len(self.__list):
#                return True
#        return False
#    
#    def v3_has_list_duplicate_dela(self):
#        return len(self.__list) != len(self.__uniq_list_del())

    def has_list_duplicate_dela(self):
        return len(set(self.__list)) != len(self.__list)

    def __init__(self, spisok):
        self.__list = spisok   
        #print(__list)
        
    def __uniq_list_del(self):
        list_uniq_del = []
        for x in self.__list:
            if x not in list_uniq_del:
                list_uniq_del.append(x)
        return list_uniq_del
    
    def __str__(self):
        r = ''
        for d in self.__list:
            r = r + str(d) + '__|__'
        return r