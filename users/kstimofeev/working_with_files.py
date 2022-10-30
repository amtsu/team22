import csv

with open('tasks_lists', mode='r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    all_strings = list(csv_reader)
    todo_list = all_strings[0]
    deadline = all_strings[1]
    done_date = all_strings[2]


todo_list.extend(("buy_flight_ticket", "leave_russia"))
deadline.extend(("27-09-2022", "24-02-2022"))
done_date.extend(("29-09-2022", "04-10-2022"))

print(todo_list)
print(deadline)
print(done_date)

def check_task_match_value_(given_list, task_value):
    list_indexes = []
    for index in range(len(given_list)):
        if given_list[index] == task_value:
            list_indexes.append(index)
    return list_indexes


print(check_task_match_value_(todo_list, 'buy_food'))


def task_symbol_count_(given_list):
    list_indexes = []
    for index in given_list:
        list_indexes.append(len(index))
    return list_indexes


print(task_symbol_count_(todo_list))


