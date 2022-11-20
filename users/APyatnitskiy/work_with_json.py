# В локальной папке лежит файл 'data.json'

import json
# from pprint import pprint

def write(data, json_file):
    data = json.dumps(data, separators=(',',':')) # separators=(',',':') - заменяет разделители в фале на указанные, в нашем случае мы заменяем стоковые JSON разделители с пробелом [1, 2, 3], на такие же без пробела [1,2,3] для экономии памяти. 
                # dumps - сериализует (приводит) данные (из файла) в json string формат. (если передаём PY объект, то строки 6 и 7 не нужны)
    data = json.loads(data, separators=(',',':'))
                # loads - ериализует (приводит) json string в питонячий объект. Разница например: JSON "", PY ''
    with open(json_file, 'w', encoding = 'utf-8') as write_file:
        json.dump(data, write_file, indent = 4) # damp - преобразует объект PY в json string и записывает в файл.
                                 # indent - отступ. По умолчанию None. Если indent = строчное значение, то оно будет использоваться как отступ. Если indent <= 0, будет использоваться новая строка.
def read(json_file):
    with open(json_file, 'r', encoding = 'utf-8') as read_file:
        return json.load(read_file)

# read(data, 'data.json')
# write(data, 'data.json')

# data = {
#     'tasks_js' : []
# }





# class Task:
#     def __init__(self):
#         self.task = ch(['First', 'Second', 'Third'])
#         self.planned_date = rd(0, 70)
#         self.done_date = rd(0, 1000)

# data = {
#     'tasks_js' : []
# }


# class Task:
#     def __init__(self, task, task_name, planned_date, done_date): #инициирует создание новго экземпляра этого класса
#         task.task_name = task_name
#         task.planned_date = planned_date
#         task.done_date = done_date

#         print(f"Дело записано в лист: {task_name}")  

#     def __str__(task): # (task) - обозначает, что метод принимает в себя экземпляр класса - task
#         return "Дело: " + task.task_name + ", Запланировано: " + task.planned_date + ", Выполнено: " + task.done_date

#     def add_to_data(task):
#         data['tasks_js'].append(Task())

# Ride_1 = Task('Ride_1','Today', 'Taday2')
# Ride_2 = Task('Ride_2','Today', 'Taday2')
# Ride_3 = Task('Ride_3','Today', 'Taday2')

# write(data, 'data.json')
# print(Ride_1)

# n_data = read('data.json')
# print(n_data['tasks'][0][1])
# input()
