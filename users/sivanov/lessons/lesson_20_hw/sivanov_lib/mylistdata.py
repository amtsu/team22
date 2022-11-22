#!/usr/local/bin/python
# coding: utf-8
'''
ДОБАВИТЬ КОММЕНТАРИЙ
это модуль с классом про список дел
'''
from usefulstuff import LocalLog
from usefulstuff import ColoredStr
from usefulstuff import make_date_ustring_from_numbers 
from usefulstuff import sprint
from taskliststuff import TaskListElement
import json
import pickle
#===================================================================================================================================
class MyTaskList:
    
    def __init__(self):
        self.__tasks = list()
        return None    
    #--------------------------------------------------------------------------------------------
    # добавляет действие в конец списка 
    def append(self, task_name, task_date_planned):
        task = TaskListElement()
        task.from_list([task_name, task_date_planned,''])
        self.__tasks.append(task)
        return None
    #--------------------------------------------------------------------------------------------
    # выставляет для нужного действия время окончания
    def set_action_done(self,numberoftheaction, timeithasbeendone):
        if numberoftheaction < len(self.__tasks):
            self.__tasks[numberoftheaction].set_done(timeithasbeendone);
        return None
    #--------------------------------------------------------------------------------------------
    # печатает содержимое расписания действий 
    def show(self, Indexed = False):
        i=(j for j in range(len(self.__tasks)))
        if(Indexed):
            for task in self.__tasks:
                print('%5d : %-1s ' % (next(i)+1, task.name()))
        else:
            for task in self.__tasks:
                print('%5d : %-1s'  % (next(i)+1, task.as_string()))
        return None
    #--------------------------------------------------------------------------------------------
    # заполнить списки всякой фигней
    def test_fill(self):
        i=1
        while i < 7:
            self.append('промыть полы', make_date_ustring_from_numbers(i*2,3,2022))
            i+=1
        i=1
        while i < 7:
            self.append('купить хлеб', make_date_ustring_from_numbers(i*3,3,2022))
            i+=1
        i=1
        while i < 8:
            self.append('дернуть', make_date_ustring_from_numbers(i*4,3,2022))
            i+=1
        return None 
    #--------------------------------------------------------------------------------------------
    #отметить все действия выполненными
    def set_all_actions_done(self):
        i=0
        for task in self.__tasks:
            task.set_done(make_date_ustring_from_numbers((i+1)%30,3,2022))
            i += 1
        return None
    #--------------------------------------------------------------------------------------------
    #загрузить списки в json
    def save_to_json(self, filename):
        #теперь наконец-то можно слить три списка в один
        data = []
        for task in self.__tasks:
            data.append(task.as_list())
        rez = json.dumps(data)
        fout = open(filename,"w")
        fout.write(rez) # byte str
        fout.close()        
        return rez
    #--------------------------------------------------------------------------------------------
    #прочесть списки из json
    def load_from_json(self, filename):
        fin = open(filename, "r")
        indata = json.loads(fin.read())
        for taskdata in indata:
            onetask = TaskListElement(taskdata)      
            self.__tasks.append(onetask)         
        return indata
    #--------------------------------------------------------------------------------------------
    #очистить списки
    def clear(self):
        self.__tasks = []
        return None
    #--------------------------------------------------------------------------------------------
    def pickle(self, filename):
        outputfile = open(filename, 'wb')
        pickle.dump(self.__tasks, outputfile)
        outputfile.close()
        return None
    #--------------------------------------------------------------------------------------------
    def unpickle(self, filename):
        inputfile = open(filename, 'rb')
        self.__tasks = pickle.load(inputfile)
        inputfile.close()
        return None
    
    #конец описания класса
    pass
#==================================================================================================================================
def main():
    r = (i for i in range(1,100))# устарело
    rbstr = ColoredStr("red, bold")
    gbstr = ColoredStr("green, bold")
    testiter = ('test {} '.format(i) for i in range(1,100))
    failed = rbstr("!!!FAILED!!! : ")
    worked = gbstr("PASSED : ")
    print('begin testing')
    
    #создать экземпляр хранилища
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print('begin testing')
    datastorage = MyTaskList()
    #закинуть что-то
    datastorage.append('buy bread','5-3-2022')
    print('--show()------------------------%d-----------------------------------------' % (next(r)))
    datastorage.show()
    print('-----test_fill()----------------%d-----------------------------------------' % (next(r)))
    datastorage.test_fill()
    datastorage.set_all_actions_done()
    print('-----set_all_actions_done()-----%d---show()--------------------------------' % (next(r)))
    datastorage.show() 
    print('-----show(Indexed = True)-------%d-----------------------------------------' % (next(r)))
    datastorage.show(Indexed = True)
    #Сохранить в файл, почистить списки, показать результат
    tmp = datastorage.save_to_json('./json/base_actions.json')
    datastorage.clear()
    print('-----clear()---show()-----------%d-----------------------------------------' % (next(r)))    
    datastorage.show()
    print('-----load_from_json-------------%d---show()--------------------------------' % (next(r)))    
    #sprint(datastorage.load_from_json('./json/base_actions.json'),';')
    datastorage.load_from_json('./json/base_actions.json')
    datastorage.show()
    print('-----pickle---------------------%d-----------------------------------------' % (next(r))) 
    datastorage.pickle('./pickle/task_list.pickle')
    datastorage.clear()
    print('-----clear()-------show()-------%d-----------------------------------------' % (next(r)))    
    datastorage.show()
    print('-----unpickle------show()-------%d-----------------------------------------' % (next(r)))
    datastorage.unpickle('./pickle/task_list.pickle')
    datastorage.show()
    print('testing end')
    return None
#==================================================================================================================================
if __name__ == '__main__':
    #llog = LocalLog(True)
    main()
pass    