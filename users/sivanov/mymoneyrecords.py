#!/usr/local/bin/python
# coding: utf-8
#если списки еще пригодятся, то выделю их отдельно.
#так, чтобы все максимально само работало
#todo = ['купить хлеб','помыть полы', 'дернуть']#['buy bread','clean the floor','fap']
#moneyrecords = [-50, -20, 500]
#desc4moneyrecords= ['купил хлеб', 'купил сижки', 'ограбил бабку']
class MyMoneyRecords:
    
    def __init__(self):
        self.__DESC = ['купил хлеб', 'купил сижки', 'ограбил бабку']
        self.__VALUES = [-50, -20, 500]
        self.fill_moneylist_with_some_shit()
        return None    
    
    @property
    def DESC(self):
        return self.__DESC    
    @property
    def VALUES(self):
        return self.__VALUES    
    
    # печатает fuck
    def print_fuck(self):
        print('fuck')
        return None
    
    #добавляет одну запись о тратах в конец списков
    def add_money_record(self,amount,description):
        self.__VALUES.append(amount)
        self.__DESC.append(description)
        return None
    # заполняет списки всяким
    def fill_moneylist_with_some_shit(self):
        self.add_money_record(-60,'заплатил налоги')
        self.add_money_record(-7,'купил хлеб')
        self.add_money_record(-90,'заплатил кварплату')
        self.add_money_record(-698,'ограбили')
        self.add_money_record(4500,'получил пособие')
        self.add_money_record(-7,'купил хлеб')
        self.add_money_record(-90,'заплатил кварплату')
        self.add_money_record(-90,'заплатил кварплату')
        self.add_money_record(-120,'аккаунт на онлифанс')
        self.add_money_record(-600,'купил хорошую вебку')
        self.add_money_record(300,'первые донаты')
        self.add_money_record(1,'нашел на улице')
        self.add_money_record(1,'нашел на улице')
        self.add_money_record(1,'нашел на улице')
        self.add_money_record(1,'нашел на улице')
        self.add_money_record(1,'нашел на улице')
        self.add_money_record(-90,'конченный долбоёб')
        self.add_money_record(-91,'конченный долбоёб')
        self.add_money_record(-92,'конченный долбоёб')
        #self.add_money_record(-93,'конченный долбоёб')
        #self.add_money_record(-94,'конченный долбоёб')
        #self.add_money_record(-95,'конченный долбоёб')
        #self.add_money_record(-96,'конченный долбоёб')
        return None
    #----------------------------------------
    #выводит на списки экран
    def print_money_lists(self,desc4moneyrecords,moneyrecords):
        print('------------------------------')
        for i in range(0,len(moneyrecords)):
            print(desc4moneyrecords[i]+' \t\t:' + str(moneyrecords[i]))
        print('------------------------------')
        return None
    
    
    #конец описания класса
    pass