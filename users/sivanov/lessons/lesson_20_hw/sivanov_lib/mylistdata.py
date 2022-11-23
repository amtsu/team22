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
llog = LocalLog(True)
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
        return task
    #--------------------------------------------------------------------------------------------
    # выставляет для нужного действия время окончания
    def set_done(self,numberoftheaction, timeithasbeendone):
        if numberoftheaction < len(self.__tasks):
            self.__tasks[numberoftheaction].set_done(timeithasbeendone);
        return None
    #--------------------------------------------------------------------------------------------
    # возвращает строку с названиями дел
    def names(self):
        return [task.name() for task in self.__tasks]
    #--------------------------------------------------------------------------------------------
    def one_day_tasks(self):
        result = list()
        for task in self.__tasks:
            if(task.is_done_same_day()):
                result.append(task)
        return result        
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
    #-------------------------------------------------------------------------------------------- 
    def __len__(self):
        return len(self.__tasks)
    #-------------------------------------------------------------------------------------------- 
    def __str__(self):
        very_long_str = ""
        i=(j for j in range(len(self.__tasks)))
        for task in self.__tasks:
            very_long_str += ('%5d : %-1s'  % (next(i)+1, task.as_string())) + '\n'
        return very_long_str
    #--------------------------------------------------------------------------------------------
    def __getitem__(self, index):
        return self.__tasks[index]
    #--------------------------------------------------------------------------------------------
    def __in__(self, request):
        result = False
        for item in self.__tasks:
            if(request == item):
                result = True
                break
        return result
    #--------------------------------------------------------------------------------------------
    def index(self, an_item):
        return self.__tasks.index(an_item)
    #--------------------------------------------------------------------------------------------
    def check_by_name(self, name):
        yesyes = ''
        tmp_task = TaskListElement([name, '', ''])
        for item in self.__tasks:
            if item.has_same_name_as(tmp_task):
                yesyes += ('Yes ')
        return yesyes
    #--------------------------------------------------------------------------------------------
    # выводит Yes если имя здачи больше заданного
    def check_by_namelen(self, limit_len):
        yesyes = ''
        for task in self.__tasks:
            if(len(task.name()) > limit_len):
                yesyes += 'Yes '
        return yesyes        
    #--------------------------------------------------------------------------------------------
    def repeaties(self):
        reps = dict()
        names = self.names()
        keys = set(names)
        for key in keys:
            reps[key] = names.count(key)
        return reps
    #--------------------------------------------------------------------------------------------
    #конец описания класса
    pass
    
#==================================================================================================================================
def files_work():
    r = (i for i in range(1,100))# устарело
    #rbstr = ColoredStr("red, bold")
    #gbstr = ColoredStr("green, bold")
    #testiter = ('test {} '.format(i) for i in range(1,100))
    #failed = rbstr("!!!FAILED!!! : ")
    #worked = gbstr("PASSED : ")
    #создать экземпляр хранилища
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print('begin testing')
    datastorage = MyTaskList()
    #закинуть что-то
    datastorage.append('buy bread','5-2-2022')
    print('---append(buy bread,5-2-2022)---%d--show()---------------------------------' % (next(r)))
    print(datastorage)
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    #datastorage.test_fill()
    datastorage.append('buy car','12-2-2022')
    datastorage.append('go jym','23-2-2022')
    datastorage.append('поспать','24-2-2022')
    print('--append-some-data--------------%d--set_all_actions_done-show()------------' % (next(r)))
    datastorage.set_all_actions_done()
    print(datastorage) 
    print('-save_to_json-clear()-show()----%d-----------------------------------------' % (next(r)))    
    #Сохранить в файл, почистить списки, показать результат
    tmp = datastorage.save_to_json('./json/base_actions.json')
    datastorage.clear()
    print(datastorage)
    print('-----load_from_json---show()----%d---show()--------------------------------' % (next(r)))    
    #sprint(datastorage.load_from_json('./json/base_actions.json'),';')
    datastorage.load_from_json('./json/base_actions.json')
    print(datastorage)
    print('---pickle--clear()---show()-----%d-----------------------------------------' % (next(r)))    
    datastorage.append('проснуться','24-2-2022')
    datastorage.set_done
    datastorage.pickle('./pickle/task_list.pickle')
    datastorage.clear()
    print(datastorage)
    print('-----unpickle------show()-------%d-----------------------------------------' % (next(r)))
    datastorage.unpickle('./pickle/task_list.pickle')
    print(datastorage)
    print('testing end')
    return None
#==================================================================================================================================
def work():

    bstr = ColoredStr("blue, back_white")
    print('begin HW')
    
    hw_list =  [        
    'Нужно посчитать общее количество дел в списке.',
    'Напечатать все дела',
    'Напечатать только 2 и 5 дело',
    'Сравнить каждое дело из списка с строкой “buy bread” и если оно совпадает то напечатать YES',
    'Если каждое дело из списка ваших дела написано на английском и является строкой то вывести длину каждой из этих строк',
    'Напечатать yes если длина строки в которой записано дело больше 10',
    'Напечатать дела индекс которых в списке делится без остатка на 2',
    'Напечатать дело с индексом 1 и 4 из списка запланированных дел',
    'Напечатать те индексы у которых значения в списке запланированных дат и списке реализованных дат равны друг другу',
    'Вывести только те дела которые вы сделали в тот же день в который их запланировали',
    'Посчитать сколько дел у вас было одинаковых ( т.е. если есть запись “купить хлеб” 28-08-2022 и “купить хлеб” 14-08-2022 то финально нужно вывести “купить хлеб” 2 (можно сделать 2 варианта без использования словарей и с испольщованием словарям)'
    ]
    hw_list_iter = (item for item in hw_list)
    r = (i for i in range(1,100))# устарело
    # инициализируем хранилище списка дел
    datastorage = MyTaskList()
    datastorage.append('buy bread','5-3-2022')
    datastorage.append('buy bread','10-3-2022')
    datastorage.test_fill() # заполняем тестовыми данными
    datastorage.set_all_actions_done() # отмечаем все дела выполненными
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print(bstr(next(hw_list_iter)))
    print('Всего дел в списке : %d.' % len(datastorage))
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print(bstr(next(hw_list_iter)))
    print(datastorage)
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print(bstr(next(hw_list_iter)))
    print('Второе дело: ' + datastorage[1].as_string())
    print('Пятое дело : ' + datastorage[4].as_string())
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print(bstr(next(hw_list_iter)))
    print(datastorage.check_by_name('buy bread').upper())
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print(bstr(next(hw_list_iter)))
    print((', ').join(('длина(%s) =  %d' % (name, len(name))) for name in datastorage.names()))
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print(bstr(next(hw_list_iter)))
    print(datastorage.check_by_namelen(10).lower())
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print(bstr(next(hw_list_iter)))
    print(('\n').join(('%3d : %s' % (i, datastorage[i])) for i in range(0,len(datastorage),2)))
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print(bstr(next(hw_list_iter)))
    print(('\n').join(('%3d : %s' % (i, datastorage[i])) for i in [1,4]))
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print(bstr(next(hw_list_iter)))
    #print(datastorage.one_day_tasks())
    print(('\n').join((str(datastorage.index(task)) for task in datastorage.one_day_tasks())))
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print(bstr(next(hw_list_iter)))
    print(('\n').join((str(task) for task in datastorage.one_day_tasks())))
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    print(bstr(next(hw_list_iter)))
    reps = datastorage.repeaties()
    print(('\n').join(('Сколько раз дело "%s" внесено в список? %d! ' % (key,reps[key] )) for key in reps.keys()))
    print('--------------------------------%d-----------------------------------------' % (next(r)))
    #print('--------------------------------%d-----------------------------------------' % (next(r)))
    print('end HW')    
    return None

#==================================================================================================================================
def main():
    return work()
#==================================================================================================================================
if __name__ == '__main__':
    #llog = LocalLog(True)
    main()
pass    