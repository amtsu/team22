#!/usr/local/bin/python
# coding: utf-8
#если списки еще пригодятся, то выделю их отдельно.
#так, чтобы все максимально само работало
#todo = ['купить хлеб','помыть полы', 'дернуть']#['buy bread','clean the floor','fap']
#timetobedone = ['28-2-2022','28-2-2022','28-2-2022']
#timedone = ['28-2-2022','','1-3-2022']
class MyListData:
    # формирует строку с датой из 3 чисел - дня,месяца и года
    def make_date(self,day, month, year):
        return str(day)+'-'+str(month)+'-'+str(year)
    
    def __init__(self):
        self.__TODO = ['купить хлеб','помыть полы', 'дернуть']
        self.__TIMETOBEDONE = ['28-2-2022','28-2-2022','28-2-2022']
        self.__TIMEDONE = ['28-2-2022',' ','1-3-2022']
        self.fill_this_shit()
        self.set_all_actions_done()
        return None    
    
    @property
    def TODO(self):
        return self.__TODO    
    @property
    def TIMETOBEDONE(self):
        return self.__TIMETOBEDONE    
    @property
    def TIMEDONE(self):
        return self.__TIMEDONE
    
    # печатает fuck
    def print_fuck(self):
        print('fuck')
        return None
    
    # добавляет действие в конец списка действий, на вход подаются две строки, одна с действием, вторая с датой
    def add_action(self,whattodo,whenitshoudbedone,whenitsdone = ''):
        self.__TODO.append(whattodo)
        self.__TIMETOBEDONE.append(whenitshoudbedone)
        self.__TIMEDONE.append(whenitsdone)
        return None
    
    # выставляет для нужного действия время окончания
    def set_action_done(self,numberoftheaction, timeithasbeendone):
        if numberoftheaction < len(self.__TIMEDONE):
            self.__TIMEDONE[numberoftheaction] = timeithasbeendone;
        return None
    
    # печатает содержимое расписания действий (то есть, этих трех списков)
    def print_lists(self):
        print('---------------------------------------------------')
        count = len(self.__TODO)
        for i in range(0,count):
            print(str(i) + ': ' + self.__TIMETOBEDONE[i] + ' собирался '+self.__TODO[i]+', выполнил '+  self.__TIMEDONE[i])
        print('---------------------------------------------------')
        return None
    
    # выводит на печать массив с действиями
    def print_TODO_with_indexes(self):
        count = len(self.__TODO)
        for i in range(0,count):
            print(str(i) + ' ' + self.__TODO[i])
        return None
    
    # заполнить списки всякой фигней
    def fill_this_shit(self):
        i=1
        while i < 7:
            self.add_action('промыть полы', self.make_date(i*2,3,2022))
            i=i+1
        i=1
        while i < 7:
            self.add_action('купить хлеб', self.make_date(i*3,3,2022))
            i=i+1
        i=1
        while i < 8:
            self.add_action('дернуть', self.make_date(i*4,3,2022))
            i=i+1
        return None 
    
    #отметить все действия выполненными
    def set_all_actions_done(self):
        count = len(self.__TODO)
        for i in range(0,count):
            self.set_action_done(i,self.make_date((i+1)%30,3,2022))
        return None
    #конец описания класса
    pass