from todo import todo
import csv

#task1 = todo("go_office", "13-09-2022", None)
#task2 = todo("covid_check", "16-09-2022", "13-09-2022")
#
#print(task1)
#print(task2)


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

print(str(spisok_spiskov[0]))
task1 = todo(*spisok_spiskov[0])
print(task1)