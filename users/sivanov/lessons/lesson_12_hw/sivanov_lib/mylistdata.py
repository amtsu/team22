#!/usr/local/bin/python
# coding: utf-8
'''
ДОБАВИТЬ КОММЕНТАРИЙ
это модуль с классом про список дел
'''
from sivanov_lib.usefulstuff import make_date_ustring_from_numbers  #функция
from sivanov_lib.taskliststuff import TaskListElement             #класс
class MyTaskList:
    
    def __init__(self):
        self.__tasks = list()
        return None    
     
    # печатает fuck
    def print_ufuck(self):
        print(u'fuck')
        return None
    
    # добавляет действие в конец списка 
    def append(self, task_name, task_date_planned):
        task = TaskListElement()
        task.add_task(task_name, task_date_planned)
        self.__tasks.append(task)
        return None
    
    # выставляет для нужного действия время окончания
    def set_action_done(self,numberoftheaction, timeithasbeendone):
        if numberoftheaction < len(self.__tasks):
            self.__tasks[numberoftheaction].set_done(timeithasbeendone);
        return None
    
    # печатает содержимое расписания действий 
    def print_lists(self):
        print(u'---------------------------------------------------')
        i=1
        for task in self.__tasks:
            print(unicode(i) + (u': ')+ (task.as_string()).decode('utf-8'))
        print(u'---------------------------------------------------')
        return None
    
    # выводит на печать массив с действиями
    def print_TODO_with_indexes(self):
        i=1
        for task in self.__tasks:
            print(unicode(i) + ': ' + unicode(task.name_as_string()).decode('utf-8'))
        return None
    
    # заполнить списки всякой фигней
    def fill_this_shit(self):
        i=1
        while i < 7:
            self.append(u'промыть полы', make_date_ustring_from_numbers(i*2,3,2022))
            i+=1
        i=1
        while i < 7:
            self.append(u'купить хлеб', make_date_ustring_from_numbers(i*3,3,2022))
            i+=1
        i=1
        while i < 8:
            self.append(u'дернуть', make_date_ustring_from_numbers(i*4,3,2022))
            i+=1
        return None 
    
    #отметить все действия выполненными
    def set_all_actions_done(self):
        i=0
        for task in self.__tasks:
            task.set_done(make_date_ustring_from_numbers((i+1)%30,3,2022))
            i += 1
        return None
    #загрузить списки в json
    def save_to_json(self, filename):
        import json
        #теперь наконец-то можно слить три списка в один
        data = []
        for task in self.__tasks:
            data.append(task.as_list())
        rez = json.dumps(data)
        fout = file(filename,"w")
        fout.write(rez) # byte str
        fout.close()        
        return rez
    #прочесть списки из json
    def load_from_json(self, filename):
        import json
        fin = file(filename, "r")
        indata = json.loads(fin.read())
        for taskdata in indata:
            onetask = TaskListElement(taskdata)      
            self.__tasks.append(onetask)         
        return indata
    #очистить списки
    def clear(self):
        self.__tasks = []
        return None
    #конец описания класса
    pass