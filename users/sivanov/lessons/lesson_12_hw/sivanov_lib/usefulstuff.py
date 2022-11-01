#!/usr/local/bin/python
# coding: utf-8
    # формирует строку с датой из 3 чисел - дня,месяца и года
def make_date_ustring_from_numbers(self,day, month, year):
    return unicode(day)+u'-'+unicode(month)+u'-'+unicode(year)
#---------------------------------------------------------------------------------
# эта штука тоже пригодится (печать списков c указанием разделителя)
def sprint(some_list, delimiter=u'\n'):
    Out = ''
    for item in some_list:
        if(type(item) == type([])):
            sprint(item,delimiter)
        else:    
            Out += unicode(item) + delimiter
    print(Out.rstrip(delimiter)) 
    return None