#!/usr/local/bin/python
# coding: utf-8

class Deal():
    """
    hello
    """
    
    def calc_len(self):
        return len(self.__deal)
    
    def __init__(self, deal_name, deadline, finish_date):
        self.__deal = deal_name
        self.__deadline = deadline
        self.__finished = finish_date
        
    def is_finished_on_deadline(self):
        if self.__deadline == self.__finished:
            return True
        return False
        
    def __repr__(self):
        return self.__deal + ' => ' + self.__deadline + ' => ' + self.__finished 
    
    def __str__(self):
        return str(self.__deal) + ' => ' + str(self.__deadline) + ' => ' + str(self.__finished) 
    
    def show_deal_name(self):
        return self.__deal
    
    def compare_deal(self, compared_str):
        if self.__deal == compared_str:
            return True
        return False
        
    def __eq__(self, compared_object):
        """
        print '__eq__'
        print self.__deal
        print self.__deal == compared_object.__deal
        print compared_object.__deal
        """
        if self.__deal == compared_object.__deal:
            return True
        return False
    
    
class DealList():

    def append(self, deal):
        self.__list.append(deal)
        
    def calc_deals_len(self):
        result = []
        for deal in self.__list:
            result.append(deal.calc_len())
        return result
        
    def count_deals(self):
        return len(self.__list)
    
    def count_repeats(self):
        repeats = {}
        for deal in self.__list:
            repeats[deal.show_deal_name()] = 0
            for i in range(self.count_deals()):
                if self.__list[i].show_deal_name() == deal.show_deal_name():
                    repeats[deal.show_deal_name()] += 1
        result = {}            
        for key, value in repeats.items():
            if value > 1:
                result[key] = value
        return result
        
    def display_done_as_planned(self, index = False):
        result = []
        for i in range(self.count_deals()):
            if self.__list[i].is_finished_on_deadline():
                if index:
                    result.append(i)
                else:
                    result.append(self.__list[i])
        return result
    
    def does_deal_len_exceed(self, number):
        result = []
        for deal in self.__list:
            if deal.calc_len() > number:
                result.append('yes')
            else:
                result.append('no')
        return result
    
    def div_index_2(self):
        result = []
        for i in range(self.count_deals()):
            if i % 2 == 0:
                result.append(self.__list[i])
        return result
    
    def __eq__(self, compared_object):
        if self.__list == compared_object.__list:
            return True
        return False

    def __getitem__(self, item):
        if 0 <= item < self.count_deals():
            return self.__list[item]
        else:
            raise IndexError("Incorrect index")            
        
    def __init__(self, deal):
        if isinstance(deal, list):
            self.__list = deal
        else:
            self.__list = [deal]
        
    def is_deal_name(self, compared_str):
        deal_name_compare_list = []
        for deal in self.__list:
            if deal.compare_deal(compared_str):
                deal_name_compare_list.append('Yes')
            else:
                deal_name_compare_list.append('No')
        return deal_name_compare_list
    
    def read_file(self, file_name):
        import pickle
        with open(file_name, 'rb') as file_read:
            self = pickle.load(file_read)
            return self

    def __str__(self):
        r = ''
        for d in self.__list:
            r = r + str(d) + '\n'
        return r 
    
    def write_to_file(self, file_name):
        import pickle
        with open(file_name, 'wb') as file_write:
            pickle.dump(self, file_write)

    
    
    
    
    
    
    
    
    
    
    
    
    