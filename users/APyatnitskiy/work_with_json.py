import json
from pprint import pprint


def write(data, json_file):
    data = json.dumps(data) # dumps and dump - разница в чем?
    data = json.loads(str(data))  # зачем
    with open(json_file, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)

def read(json_file): 
    with open(json_file, 'r', encoding = 'utf-8') as file: 
        return json.load(file)

data = {
    'tasks_js' : []
}

 # Решение без классов.


# class Task:
#     def __init__(self):
#         self.task = ch(['First', 'Second', 'Third'])
#         self.planned_date = rd(0, 70)
#         self.done_date = rd(0, 1000)


# data = {
#     'tasks_js' : []
# }

class Task:
    def __init__(self, task, task_name, planned_date, done_date): #инициирует создание новго экземпляра этого класса
        task.task_name = task_name
        task.planned_date = planned_date
        task.done_date = done_date

        print(f"Дело записано в лист: {task_name}")  

    def __str__(task): # (task) - обозначает, что метод принимает в себя экземпляр класса - task
        return "Дело: " + task.task_name + ", Запланировано: " + task.planned_date + ", Выполнено: " + task.done_date

    def add_to_data(task):
        data['tasks_js'].append(Task())

Ride_1 = Task('Ride_1','Today', 'Taday2')
Ride_2 = Task('Ride_2','Today', 'Taday2')
Ride_3 = Task('Ride_3','Today', 'Taday2')


write(data, 'data.json')
print(Ride_1)


# data = {
#     'tasks_js' : []
# }

# for i in range(100):
#     data['tasks_js'].append(Task().__dict__)

# n_data = read('data.json')
# print(n_data['tasks'][0][1])
# input()
