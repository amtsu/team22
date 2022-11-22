#!/usr/local/bin/python
# coding: utf-8
"""
Модуль описывает абстрактный интерфейс элемента списка дел AbstractTaskListElement и его реализацию TaskListElement
"""
from usefulstuff import LocalLog
from usefulstuff import ColoredStr
llog = LocalLog(False)


# для того, чтобы создавать НАСТОЯЩИЕ абстрактные классы, нужно наследовать их от abc.ABC
from abc import ABC, abstractmethod
class AbstractTaskListElement(ABC):
    """
    попробую проверить методологию создания абстрактного интерфейса и отдельно её реализации
    Данный класс определяет, как должно обеспечиваться взаимодействие одного элемента 
    списка дел (то есть, тройки [Название/дата по плану/ дата готовности]) с внешним миром.
    делать оно это конечно будет через соответствующие методы;
    наконец ещё выяснил что наше дело корректно называть task. это было очевидно с самого начала, но что-то мешало
    использовать это слово.
    https://docs-python.ru/tutorial/klassy-jazyke-python/abstraktnye-klassy/ - первая ссылка в яндексе по теме.
    https://habr.com/ru/post/72757/ третья ссылка в яндексе.
    пример из первой ссылки не работает.
    также видно что есть много способов делать одно и то же.
    """
    #AbstractTaskListElement(ABCMeta) тоже работает. достаточно чего-то одно или можно оба?
    __metaclass__=ABC # можно указать тут метакласс, а можно наверное от него наследовать. это одно и то же?
    # фигачим абстрактный состав класса
    # интересно, могу ли я объявить абстрактный метод __eq__ - могу
    @abstractmethod
    def __eq__(self, other):
        pass
    #преобразовать данные в список 
    @abstractmethod
    def _as_list(self): # кто-то определяет список параметров прямо тут в абстракте, кто-то этого не делает.
        pass
    
    #взять из списка, состоящего из трех строчек
    @abstractmethod
    def _from_list(self, list_of_three_strings): #как указать, что я хочу тут именн лист а не что-то ещё?
        pass    
    #вывести результат как строку
    @abstractmethod
    def _as_string(self):
        pass
    #добавить делу время выполнения
    @abstractmethod
    def _set_done(self, timetobedone):
        pass
    #добавить дело и планируемое его время выполнения
    @abstractmethod
    def _add_task(self, task_name, task_date_planned):
        pass    
    # возвращает имя дела
    @abstractmethod
    def _name(self):
        pass
    # теперь пусть будет интерфейс в рамках NVI (ему всё-таки быть)
    # возвращает дело в виде списка
    def as_list(self): 
        return self._as_list()
    #считывает дело из списка трех элементов. НЕ ПРОВЕРЯЕТ НИЧЕГО, считается что всё нормально, все проверки снаружи
    def from_list(self,list_of_three_strings):
        llog('parent from_list called')
        return self._from_list(list_of_three_strings) 
    #возвращает дело в виде строки
    def as_string(self):
        return self._as_string()
    #устанавливает данному делу дату завершения
    def set_done(self, timetobedone):
        return self._set_done(timetobedone)
    #подумать надо 
    #def (self, task_name, task_date_planned):
    #    return self.__add_task(task_name, task_date_planned)
    #возвращает имя дела
    def name(self):
        return self._name()
    pass # закончили
    
#=================================================================================================================================    
class TaskListElement(AbstractTaskListElement):
    """
    это реализация интерфейса взаимодействия списка дел с внешним миром
    """
    #пустой конструктор
    #def __init__(self):
    #    self.__task = u""
    #    self.__date_planned = u""
    #    self.__date_completed = u""   # забыл что тут нельзя несколько конструкторов
    
    #конструктор    
    def __init__(self,list_of_three_strings=["","",""]):
        #self.__init__(self)  # вот так вообще нормально делать? я как-то напарывался на приколы, но не помню уже о чем там шла речь
        self.__task = ""
        self.__date_planned = ""
        self.__date_completed = ""
        self.from_list(list_of_three_strings)
        
    #user friendly output
    def __str__(self):
        result = (("| %25s | %10s | %10s |") % (self.__task, self.__date_planned, self.__date_completed))
        return result
    
    #debug output
    def __repr__(self):
        result = ("id = " + str(id(self)) + ", task = " + self.__task + ", date_planned = " + self.__date_planned + 
                  ", date_completed = " + self.__date_completed + ";") 
        return result
    
    #вынужден определить __eq__
    #проверка экземпляров на равенство друг другу
    def __eq__(self, other):
        return ((type(self) == type(other)) and (self.__task == other.__task))
    
    #проверяет является ли параметр функции списком из трех строк.
    #можно добавлять до бесконечности
    def __is_input_list_correct(self, list_of_three_strings):
        correct_data = True
        if((type(list_of_three_strings) != type(list()))and (len(list_of_three_strings) != 3)):
            correct_data = False
        else:            
            for element in list_of_three_strings:
                if(type(element) != type(str())):
                    correct_data = False
        return correct_data
    
    #вынужден определить as_list и прочее
    #возвращает содержимое класса в виде списка из трех строк
    def _as_list(self):
        return [self.__task,self.__date_planned,self.__date_completed]
    
    #загружает данные класса из списка из трех строк
    def _from_list(self, list_of_three_strings):
        if(self.__is_input_list_correct(list_of_three_strings)):        
            self.__task = list_of_three_strings[0]
            self.__date_planned = list_of_three_strings[1]
            self.__date_completed = list_of_three_strings[2]
        else:
            print('incorrect input, list of three strings is required, but' )
            print(list_of_three_strings)
            print('given. class data initialized with empty strings')
            self.__task = ""
            self.__date_planned = ""
            self.__date_completed = ""
        return None
    
    #возвращает содержимое класса в виде строки        
    def _as_string(self):
        return self.__str__()

    #добавить делу время выполнения
    def _set_done(self, timetobedone):
        self.__date_completed = (timetobedone) # и никаких проверок
        return None
    
    #добавить дело и  время его  выполнения
    def _add_task(self, task_name, task_date_planned):
        self.__task = task_name
        self.__date_planned = task_date_planned
        return None
    
    # возвращает имя дела
    def _name(self):
        return (self.__task)
    pass
#==================================================================================================================================
#напишу тесты прямо в модуле
def main():
    rbstr = ColoredStr("red, bold")
    gbstr = ColoredStr("green, bold")
    testiter = ('test {} '.format(i) for i in range(1,100))
    failed = rbstr("!!!FAILED!!! : ")
    worked = gbstr("PASSED : ")
    print('begin testing')
    #------------------------------------------------
    result = worked
    tle = TaskListElement(['жуй', 'всегда', 'сковорода'])
    # смысл теста - просто чтобы хоть что-то вызывалось и не падало. что именно создалось потом в as_list() проверю
    print(next(testiter) + result + "tle = TaskListElement(['жуй', 'всегда', 'сковорода'])") 
    print(next(testiter) + result + "tle.__str__(): " + tle.__str__() ) # смысл теста - просто чтобы хоть что-то вызывалось и не падало
    print(next(testiter) + result + "tle.__repr__(): " + tle.__repr__() ) # смысл теста - просто чтобы хоть что-то вызывалось и не падало
    #------------------------------------------------
    if(tle.as_list() == ['жуй', 'всегда', 'сковорода']):
        result = worked
    else:
        result = failed
    print(next(testiter) + result + "tle.as_list(): " + str(tle.as_list()))
    #------------------------------------------------
    if(tle.as_string() == '|                       жуй |     всегда |  сковорода |'):
        result = worked
    else:
        result = failed
    print(next(testiter) + result + "tle.as_string(): " + tle.as_string())
    #------------------------------------------------
    if(tle.name() == 'жуй'):
        result = worked
    else:
        result = failed
    print(next(testiter) + result + "tle.name(): " + tle.name())
    #------------------------------------------------
    tle.from_list(['dick','cunt',''])
    if((tle.as_list()[0] == 'dick') and (tle.as_list()[1] == 'cunt') and (tle.as_list()[2] == '')):
        result = worked
    else:
        result = failed
    print(next(testiter) + result + "tle.from_list(['dick','cunt','']); str(tle): " + str(tle))
    #------------------------------------------------
    tle.set_done('frying pan')
    if(tle.as_list()[2] == 'frying pan'):
        result = worked
    else:
        result = failed
    print(next(testiter) + result + "tle.set_done('frying pan'); str(tle): " + str(tle))
    #------------------------------------------------
    tle_2 = tle
    if(tle_2.as_list() == tle.as_list()):
        result = worked
    else:
        result = failed
    print(next(testiter) + result + "tle_2 = tle; str(tle_2.__repr__()): " + str(tle_2.__repr__()))
    #------------------------------------------------
    tle_3 = TaskListElement(['жуй', 'всегда', 'сковорода'])
    if(tle_3.as_list() == ['жуй', 'всегда', 'сковорода']):
        result = worked
    else:
        result = failed
    print(next(testiter) + result + "tle_3 = TaskListElement(['жуй', 'всегда', 'сковорода']); str(tle_3): " + str(tle_3))
    #------------------------------------------------
    if( (tle_3 == tle_2) == False):
        result = worked
    else:
        result = failed
    print(next(testiter) + result + "tle_3 == tle_2 : " + str(tle_3 == tle_2))
    #------------------------------------------------
    if( (tle == tle_2) == True):
        result = worked
    else:
        result = failed
    print(next(testiter) + result + "tle == tle_2 : " + str(tle == tle_2))
    #------------------------------------------------
    if( (tle_3 != tle_2) == True):
        result = worked
    else:
        result = failed
    print(next(testiter) + result + "tle_3 != tle_2 : " + str(tle_3 != tle_2))
    #------------------------------------------------
    if( (tle != tle_2) == False):
        result = worked
    else:
        result = failed
    print(next(testiter) + result + "tle != tle_2 : " + str(tle != tle_2))
    #------------------------------------------------
    print('end testing')
    return
#==================================================================================================================================
if __name__ == '__main__':
    #llog = LocalLog(True)
    main()
pass    