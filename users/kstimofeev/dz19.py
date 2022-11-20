#import csv
import pickle
from todo import Todo
from spisok_del import SpisokDel


#with open('task_list.pickle', 'rb') as handle:
#    spisok_del_obj = pickle.load(handle)
#
#print(spisok_del_obj)

spisok_del_obj = SpisokDel()
spisok_del_obj.read_file("task_list.pickle")
print(spisok_del_obj)