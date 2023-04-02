"""
Посчитать сколько дел у вас было одинаковых ( т.е. если есть запись “купить хлеб” 28-08-2022 и “купить хлеб” 14-08-2022 то финально нужно вывести “купить хлеб” 2 
(можно сделать 2 варианта без использования словарей и с испольщованием словарям)"""


delo1=["buy bread"," 28-08-2022"," 28-08-2022"]
delo2=["buy bread"," 28-08-2022"," -"]
delo3=["sold milk"," 28-08-2022"," 29-08-2022"]
delo4=["sold milk"," 28-08-2022"," 30-08-2022"]
delo5=["sold milk"," 28-08-2022"," 30-08-2022"]

spisok_del = [delo1, delo2,delo3,delo4, delo5]

"""
Первый способ через словарь
"""
dic = {}
for delo in spisok_del:
    #print(delo[0])
    if not delo[0] in dic:
        dic[delo[0]] = 1
       # print(dic)
    else:
       dic[delo[0]] += 1
print(dic)

# {'buy bread': 2, 'sold milk': 3}
"""
Второй способ через список и множество set()
"""
lst = []
for delo in spisok_del:
    lst.append(delo[0]) # ['buy bread', 'buy bread', 'sold milk', 'sold milk', 'sold milk']

for element in set(lst): # {'buy bread', 'sold milk'}
    lst.count(element)
    print(element , lst.count(element))

# как работает set
# aaa = ['buy bread', 'buy bread', 'sold milk', 'sold milk', 'sold milk']
# bbb = {'buy bread', 'buy bread', 'sold milk', 'sold milk', 'sold milk'}
# print("aaa",  aaa)
# print("bbb", bbb)

