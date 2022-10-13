# Нужно посчитать общее количество дел в списке.
# Напечатать все дела
# Напечатать только 2 и 5 дело
# Сравнить каждое дело из списка с строкой “buy bread” и если оно совпадает то напечатать YES
# Если каждое дело из списка ваших дела написано на английском и является строкой то вывести длину каждой из этих строк
# Напечатать yes если длина строки в которой записано дело больше 10
# Напечатать дела индекс которых в списке делится без остатка на 2
# Напечатать дело с индексом 1 и 4 из списка запланированных дел
# Напечатать те индексы у которых значения в списке запланированных дат и списке реализованных дат равны друг другу
# Вывести только те дела которые вы сделали в тот же день в который их запланировали
# Посчитать сколько дел у вас было одинаковых ( т.е. если есть запись “купить хлеб” 28-08-2022 и “купить хлеб” 14-08-2022 то финально нужно вывести “купить хлеб” 2 (можно сделать 2 варианта без использования словарей и с испольщованием словарям)



Todo_List = ['Whiskey_Bourbon_10', 'Whiskey_Bourbon_20', 'buy_bread', 'Whiskey', 'Transfer', 'Transfer', 'Hard Work', 'Hard Work', 'Lanch', 'Sleep', 'Wakeup', 'SelfCare']
Planned_Date = ['2022-11-09', '2022-11-09', '2022-11-09', '2022-11-09', '2022-12-09', '2022-12-09', '2022-13-09', '2022-13-09', '2022-11-09', '2022-12-09', '2022-13-09', '2022-14-09']
Done_Date = ['2022-11-09', '2022-11-09', '2022-11-09', '2022-11-09', '2022-12-09', '2022-12-09', '2022-13-09', '2022-13-09', '2022-11-09', '2022-12-09', '2022-13-09', '2022-14-09']

print('------------')
print('1. Нужно посчитать общее количество дел в списке.')
print('Дел в списке: ', len(Todo_List))

print('------------')
print('2. Напечатать все дела.')

print('A. Печать дел в строку:'), '\n'
print(Todo_List), '\n' # Просто печатает список в строку.
print('------------')
print('B. Печать в цикле. Выполняется для каждого элемента, поэтому вывод в столбец.'), '\n'
for Task in Todo_List: # Выполняет принт для каждого значения в списке, поэтому вывод в столбик.
    print(Task)

print('------------')

print('3. Напечатать только 2 и 5 дело.')
print('Дело №2: ' + Todo_List[2], '# Для каждого дела своя строка и команда.') 
print('Дело №5: ' + Todo_List[5])

print('Дело №2: '+Todo_List[2]+',','Дело №5 '+Todo_List[5], '# Команда одной строкой.')

print('------------')

print('4. Сравнить каждое дело из списка с строкой “buy bread” и если оно совпадает то напечатать "Yes".')

print('A. В цикле сравниваем каждое значение с buy_bread и выводим результат в столбик.')

for Task in Todo_List:
    if Task == 'buy_bread':
        print ('Yes')
    else:
        print ('No'), "\n"
        
print('B. Boolean solution: работает неправильно, тк выводит только результат последнего сравнения.'), '\n'

def BuyBreadFinder(bbf_cycle): # Создаём цикл выдающий логическое решение.
    for Task in bbf_cycle:
        if bbf_cycle.count(Task) == 'buy_bread':
            return True
        break
    return False
if BuyBreadFinder(Todo_List): # Если цикл выполнился успешно - Да;
    print("Yes")
else:
    print("No"), "\n" # Иначе - Нет.

print('------------')

print('5. Если каждое дело из списка ваших дела написано на английском и является строкой то вывести длину каждой из этих строк.')

print('A. Simple solution:'), '\n'# Выводим кол-во символов каждого значения списка через  LEN.

for Task in Todo_List:
    print(len(Task))  #?? Как вставить пустую строку?? Есть просто поставить '\n' код исполняется для каждого значения.
    
print('B. Simple solution:'), '\n' #Выводим с именами тасков.

for Task in Todo_List:
    print (Task,'-',len(Task))
    
print('С. Solution for unique tasks only:'), '\n'

UniqTasksList = [] # Создаём пустой список.

def UniqueTasksCycle(UTask): # Создаём цикл, который наполняет пустой список уникальных дел: берёт значение и проверяет, есть ли оно в списке, если нет - добавляет, если нет - пропускает.
    for UTask in Todo_List:
        if UTask not in UniqTasksList:
            UniqTasksList.append(UTask)
            
UniqueTasksCycle(Todo_List) # Вызываем функцию с циклом наполнения списка уникаьных дел, в аргумент кладём изначальный список дел.

for Task in UniqTasksList:
    print (Task,'-',len(Task))

print('------------')

print('6. Напечатать yes если длина строки в которой записано дело больше 10.')

print('A. Simple solution:'), '\n'

for Task in Todo_List:
    if len(Task) > 10:
        print('Yes')
    else:
        print ('No')
        
print('B. Solution with function 1:'), '\n'

def TaskLenComp(Task):
    for Task in Todo_List:
        if len(Task) > 10:
            print('Yes')
        else:
            print('No')
            
TaskLenComp(Todo_List)

print('C. Solution with function 2:'), '\n'

L10TaskList = [] # Создаём пустой список.

def L10TasksCycle(x): # Создаём цикл, который наполняет пустой список дел более 10 букв: берёт значение и проверяет, есть ли оно в списке, если нет - добавляет, если нет - пропускает.
    for Task in Todo_List:
        if len(Task) > 10:
            L10TaskList.append(Task)
            
L10TasksCycle(Todo_List) # Вызываем функцию с циклом наполнения списка уникаьных дел, в аргумент кладём изначальный список дел.

if len(L10TaskList) > 0:
    print('Yes, 10 letters long tasks: ',L10TaskList)
else:
    print('No 10 letters long tasks.')

print('------------')

print('7. Напечатать дела индекс которых в списке делится без остатка на 2')

# def division2(x):

print('8. Напечатать дело с индексом 1 и 4 из списка запланированных дел.')

print('------------')
print('9. Напечатать те индексы у которых значения в списке запланированных дат и списке реализованных дат равны друг другу.')

print('------------')
print('10. Вывести только те дела которые вы сделали в тот же день в который их запланировали.')

SameDayIndexList = []
def SameDayCycle(x):
    for PDate in Planned_Date:
        for DDate in Done_Date:
            if PDate == DDate:
                SameDateIndex = Planned_Date.index(PDate)
                SameDayIndexList.append(SameDateIndex)
print(SameDayIndexList)


print('------------')
print('Вес на луне: на земле 92кг, лунный коэф. 0,165, на 15 лет.')
print('------------')
Weight = 92
MoonWeight = Weight * 0.165
Year = 0

for Year in range (0,15):
    Year = Year + 1
    MoonWeight = MoonWeight + 1
    print(MoonWeight)

print('------------')
print('Вес на луне: через функцию, которая принимает в себя: земной вес, кол-во лет, шаг набора вес а в год.')
print('------------')
def MoonWeightFn(Weight, Years, WeighGainStep):
    YearCount = 0
    MoonWeight = Weight * 0.165
    while YearCount < Years:
        YearCount = YearCount + 1
        MoonWeight = MoonWeight + WeighGainStep
        print(YearCount, '-', MoonWeight, 'kg')

MoonWeightFn(92, 15, 1)


# ------------ ФУНКЦИИ -----------

# from xml.etree.ElementInclude import FatalIncludeError  # Пример функции.


# def has_delo_in_list(title_delo, list_del):
#     for element in list_del:
#         if element == title_delo:
#             return True
#     return False
# ---------------------------------------

print('------------')
print('Функция принимает в себя список цветов и выводит цвет с заданным индексом.')
print('------------')

colors = ['Red', 'Black', 'Pink', 'Brown']  # Исходный лист

def one_color(nomer, colors):
    color = colors[nomer]
    return color

print(one_color(2, colors))

print('------------')
print('Функция принимает два числа и сравнимает их.')
print('------------')

def sravnenie_1(x,y):
    res_1 = False
    if x == y:
        res_1 = True
    return res_1

print('Числа 8 и 9 равны: ',sravnenie_1(8,9))

def sravnenie_2(x,y):
    if x != y:
        return False
    else:
        return True

print('Числа 7 и 7 равны: ',sravnenie_2(7,7))

# ----------- THE END -----------------