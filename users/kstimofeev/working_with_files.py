import csv
import pickle
from todo import Todo
from spisok_del import SpisokDel

with open('tasks_lists', mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    all_strings = list(csv_reader)
    #print(all_strings)

    spisok_spiskov = []
    for task_number in range(len(all_strings[0])):
        spisok_iz3 = []
        for strings in all_strings:
            spisok_iz3.append(strings[task_number])
        #print(spisok_iz3)
        spisok_spiskov.append(spisok_iz3)
    #print(spisok_spiskov)

    todo_list = all_strings[0]
    deadline = all_strings[1]
    done_date = all_strings[2]


spisok_spiskov.append(["buy_flight_ticket", "27-09-2022", "29-09-2022"])
spisok_spiskov.append(["leave_russia", "24-02-2022", "04-10-2022"])

new_obj_list = []
for entry in range(len(spisok_spiskov)):
    new_obj_list.append(Todo(*spisok_spiskov[entry]))

#print(new_obj_list)

#print(spisok_spiskov)

#todo_list.extend(("buy_flight_ticket", "leave_russia"))
#deadline.extend(("27-09-2022", "24-02-2022"))
#done_date.extend(("29-09-2022", "04-10-2022"))

#print(todo_list)
#print(deadline)
#print(done_date)

#def check_task_match_value_(given_list, task_value):
#    list_indexes = []
#    for index in range(len(given_list)):
#        if given_list[index] == task_value:
#            list_indexes.append(index)
#    return list_indexes
#
#
#print(check_task_match_value_(todo_list, 'buy_food'))
#
#
#def task_symbol_count_(given_list):
#    list_indexes = []
#    for index in given_list:
#        list_indexes.append(len(index))
#    return list_indexes
#
#
#print(task_symbol_count_(todo_list))

spisok_del_obj = SpisokDel()

for task in new_obj_list:
    spisok_del_obj.append(task)

print(spisok_del_obj)

spisok_del_obj.done_last_day()
print("----------------")

spisok_del_obj.check_task_match_value("buy_flight_ticket")
print("----------------")

spisok_del_obj.tasks_length_more_than(10)
print("----------------")

print(spisok_del_obj.count_dupl_tasks())
print("----------------")

print(spisok_del_obj.count_dupl_tasks2())
print("----------------")

#with open('task_list.pickle', 'wb') as handle:
#    pickle.dump(spisok_del_obj, handle)

with open('task_list.pickle', 'rb') as handle:
    readed_spisok_del_obj = pickle.load(handle)
print(readed_spisok_del_obj)

#spisok_del_obj.write_file("test_write.pickle")
