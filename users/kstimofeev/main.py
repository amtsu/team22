todo_list = ["go_office", "covid_check", "take_lunch", "team_meeting", "buy_food", "bike_training", "buy_skis", "haircut", "buy_food", "call_friend", "learn_english", "buy_laptop", "take_lunch", "go_walk", "learn_python", "buy_food", "gym_training", "pay_bills", "learn_ansible", "bike_training", "some_cleaning", "relax"]
deadline = ["13-09-2022", "16-09-2022", "13-09-2022", "12-09-2022", "13-09-2022", "13-09-2022", "10-11-2022", "24-09-2022", "15-09-2022", "17-09-2022", "13-09-2022", "07-10-2022", "14-09-2022", "16-09-2022", "14-09-2022", "14-09-2022", "20-09-2022", "13-09-2022", "20-09-2022", "15-09-2022", "13-09-2022", "17-09-2022"]
done_date = [None, None, "13-09-2022", "12-09-2022", "13-09-2022", None, "01-09-2022", "17-09-2022", "15-09-2022", "10-09-2022", "13-09-2022", None, "14-09-2022", "14-09-2022", "13-09-2022", "14-09-2022", "21-09-2022", "12-09-2022", "20-10-2022", "17-09-2022", "13-09-2022", "13-09-2022"]

print("count of all tasks in a list:")
print(len(todo_list))

print("-------------------------------------------------------------------------------------------------------------")

print("list of all tasks:")
print(todo_list)

print("-------------------------------------------------------------------------------------------------------------")

print("2nd and 5th tasks:")
print(todo_list[2], todo_list[5])

print("-------------------------------------------------------------------------------------------------------------")

print("check if a task match 'buy_food' value:")


def check_task_match_value_(given_list, task_value):
    list_indexes = []
    for index in range(len(given_list)):
        if given_list[index] == task_value:
            list_indexes.append(index)
    return list_indexes


print(check_task_match_value_(todo_list, 'buy_food'))

print("-------------------------------------------------------------------------------------------------------------")

print("symbol count of each task:")


def task_symbol_count_(given_list):
    list_indexes = []
    for index in given_list:
        list_indexes.append(len(index))
    return list_indexes


print(task_symbol_count_(todo_list))

print("-------------------------------------------------------------------------------------------------------------")

print("check if symbol count of task > 10:")


def list_tasks_length_more_than_(given_list, amount):
    list_indexes = []
    for index in range(len(given_list)):
        if len(given_list[index]) > int(amount):
            list_indexes.append(index)
    return list_indexes


print(list_tasks_length_more_than_(todo_list, 10))

print("-------------------------------------------------------------------------------------------------------------")

print("check if index of a task div by x:")


def list_tasks_which_index_div_by_x_(given_list, x):
    list_divided = []
    for index in range(len(given_list)):
        if index > 0 and index % x == 0:
            list_divided.append(given_list[index])
    return list_divided


print(list_tasks_which_index_div_by_x_(todo_list, 2))

print("-------------------------------------------------------------------------------------------------------------")

print("print tasks with indexes 1 and 3")
print(todo_list[1], todo_list[3])

print("-------------------------------------------------------------------------------------------------------------")

print("print a task if it was done at a deadline date")


def done_at_last_day(todo_list, deadline_list, done_date_list):
    task_list = []
    for index in range(len(todo_list)):
        if deadline[index] == done_date[index]:
            task_list.append(todo_list[index])
    return task_list


print(done_at_last_day(todo_list, deadline, done_date))

print("-------------------------------------------------------------------------------------------------------------")

print("find duplicate tasks with count")


def duplicate_list_with_count_(given_list):
    uniq_list = []
    duplicate_list = []
    for task in given_list:
        if task not in uniq_list:
            uniq_list.append(task)
    for uniq_task in uniq_list:
        task_count = 0
        for task in given_list:
            if uniq_task == task:
                task_count += 1
        if task_count > 1:
            duplicate_list.append([uniq_task, task_count])
    return duplicate_list


print(duplicate_list_with_count_(todo_list))

print("-------------------------------------------------------------------------------------------------------------")

print("find duplicate tasks with count")


def duplicate_dict_by_set_with_count_(given_list):
    duplicate_dict = {}
    uniq_set = set(given_list)
    for item in uniq_set:
        if given_list.count(item) > 1:
            duplicate_dict[item] = given_list.count(item)
    return duplicate_dict


print(duplicate_dict_by_set_with_count_(todo_list))

print("-------------------------------------------------------------------------------------------------------------")

print("find duplicate tasks with count")


def duplicate_dict_by_dict_with_count_(given_list):
    dict_duplicate = {}
    for task in given_list:
        if task in dict_duplicate:
            dict_duplicate[task] += 1
        else:
            dict_duplicate[task] = 1
    dict_duplicate = {task: count for task, count in dict_duplicate.items() if count > 1}
    return dict_duplicate


print(duplicate_dict_by_dict_with_count_(todo_list))

print("-------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------")

transaction_name = ["advance", "rent_apartment", "buy_food", "salary", "buy_food", "side_work_salary", "vacation_pay", "buy_food", "buy_gas", "buy_skis", "buy_beacon", "buy_dh_fork", "buy_dj_fork", "buy_dj_frame", "buy_dh_shox", "buy_shoes", "buy_wearing", "buy_gas", "buy_food"]
transaction_amount = [50,       -120,              -20,         300,    -18,            100,                150,           -21,       -25,      -30,            -20,         -90,          -33,            -32,          -25,            -4,           -9,         -9,         -10]
transaction_date = ["20-06",    "21-06",           "25-06",   "05-07",   "07-07",        "10-07",          "15-07",    "20-07",    "25-07",   "30-07",         "30.07",       "01.09",      "02.09",       "10.09",      "01.09",       "05.09",       "10.09",     "15.09",    "20.09"]

#посчитайте сколько всего вы потратили за все время

total_expense = 0
for transaction in transaction_amount:
    if transaction < 0:
        total_expense += transaction
print("total_expense", abs(total_expense))

print("-------------------------------------------------------------------------------------------------------------")

#посчитать сколько трат было меньше 300 рублей

count_smaller_10 = 0
for transaction in transaction_amount:
    if (transaction < 0) and (transaction > -10):
        count_smaller_10 += 1
print("count_smaller_10", count_smaller_10)

print("-------------------------------------------------------------------------------------------------------------")

#посчитать сколько сумму трат которые были больше 10000 рублей

count_more_30 = 0
for transaction in transaction_amount:
    if (transaction < 0) and (transaction < -30):
        count_more_30 += 1
print("count_more_30", count_more_30)

print("-------------------------------------------------------------------------------------------------------------")

#выдать номера трат которые находятся в диапазоне между 300 и 10000 рублей

numbers_expense_10_30 = []
for transaction_number in range(len(transaction_amount)):
    if (abs(transaction_amount[transaction_number]) < 30) and (abs(transaction_amount[transaction_number]) > 10):
        numbers_expense_10_30.append(transaction_number)
print("numbers_expense_10_30", numbers_expense_10_30)

print("-------------------------------------------------------------------------------------------------------------")

#выбрать из списка на втором шаге самую минимальную трату

minimal_exp_amount = abs(transaction_amount[0])
for transaction in transaction_amount:
    if transaction < 0:
        if abs(transaction) < minimal_exp_amount:
            minimal_exp_amount = abs(transaction)
print("minimal_exp_amount", minimal_exp_amount)

print("-------------------------------------------------------------------------------------------------------------")

#посчитайте сколько заработали за все время

total_salary = 0
for transaction in transaction_amount:
    if transaction > 0:
        total_salary += transaction
print("total_salary", total_salary)

print("-------------------------------------------------------------------------------------------------------------")

#посчитайте какие самые частые у вас траты(можно попробовать с использованием словарей)

print("find most frequent expenses with count")


def frequent_exp_(given_list):
    frequent_dict = {}
    uniq_set = set(given_list)
    for item in uniq_set:
        if given_list.count(item) > 1:
            frequent_dict[item] = given_list.count(item)
    return frequent_dict


print(frequent_exp_(transaction_name))

print("-------------------------------------------------------------------------------------------------------------")
#добавить к списку еще 3 действия
print("-------------------------------------------------------------------------------------------------------------")
#Найти максимальную трату

maximal_exp_amount = abs(transaction_amount[0])
for transaction in transaction_amount:
    if transaction < 0:
        if abs(transaction) > maximal_exp_amount:
            maximal_exp_amount = abs(transaction)
print("maximal_exp_amount", maximal_exp_amount)

print("-------------------------------------------------------------------------------------------------------------")
#Найти минимальный доход

minimal_salary = transaction_amount[0]
for transaction in transaction_amount:
    if transaction > 0:
        if transaction < minimal_salary:
            minimal_salary = abs(transaction)
print("minimal_salary", minimal_salary)

print("-------------------------------------------------------------------------------------------------------------")
#Посчитать среднюю стоимость ваших трат

total_expense = 0
count_expense = 0
for transaction in transaction_amount:
    if transaction < 0:
        total_expense += transaction
        count_expense += 1
average_expense = round(total_expense / count_expense)
print("average_expense", abs(average_expense))

print("-------------------------------------------------------------------------------------------------------------")
