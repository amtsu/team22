https://github.com/amtsu/team22/tree/main/library/working_time/wt240331.py

дело
    название
    приорите
    время запланированное
    время до которого сделать дело


#Регина Марфенкова
#задача 1
my_prioritet = {"f": ("работа", "семья"), "b": ("отдых","друзья")}
def important(my_dict):
    for key in my_prioritet:
        return my_prioritet[key]
        if my_prioritet[key] not in my_prioritet:
            return my_prioritet(key[1])
print(important(my_prioritet))

my_prioritet2 = [("a", "работа", "семья"), ("b", "отдых", "друзья"), ("c", "остальное")]
my_prioritet3 = [["a :работа, семья"], ["b : отдых, друзья"]]
my_prioritet4 = {"a":{"работа": 8}, "b":{"семья": 5}, "c":{"отдых": 3}}
my_prioritet5 = {"a": ["работа", 8, 4], "b": ["семья", 5, 2], "c": ["отдых", 3, 1]}

def my_importent(my_dict):
    for key in my_prioritet4:
        return my_prioritet4[key]
        if 
        
        
        
    

def test_my_prioritet():
    my_prioritet = {"a": ("работа", "семья"), "b": ("отдых","друзья")}
    expected = ('работа', 'семья')
    assert expected == important(my_prioritet)
    
def test_my_prioritet_2():
    my_prioritet = {"с": ("работа", "семья"), "b": ("отдых","друзья")}
    expected = ("отдых","друзья")
    assert expected == important(my_prioritet)




#Аня Морозова 
#задача 1
spis_prior = {"a":"coffee", "b":"eating", "c":"fishing"}
def reserch_prior (my_dict):
    for k,v in spis_prior.items():
        if k == "a":
            return(v)
    for k,v in spis_prior.items():        
        else k == "b":
            return (v)
    for k,v in spis_prior.items():
        else k == "c":
            return (v)
reserch_prior(spis_prior)  

#for range
            
            
def test1():
    spis_prior = {"a":"coffee", "b":"eating", "c":"fishing"}
    expected = "coffee"
    assert expected == reserch_prior(spis_prior)
  
    
    
def test2():
    spis_prior = { "b":"eating", "c":"fishing"}
    expected = "eating"
    assert expected == reserch_prior(spis_prior)

def test3():
    spis_prior = { "b":"eating", "c":"fishing", "a":"coffee"}
    expected = "coffee"
    assert expected == reserch_prior(spis_prior)



                
#Andrey Ivanchenko
#1
deeds_prior = {'a': ['breakfast', 'lunch', 'diiner', 'supper'], 'b': ['feed cats', "cats toilet clean"], 'c': ['study', 'buy food in the store'], 'd': 'play with cat'}
def priority(the_dict):
    for key in the_dict:
        if key == 'a':
            return the_dict['a']
        elif key == 'b':
            return the_dict['b']
        elif key == 'c':
            return the_dict['c']
        elif key == 'd':
            return the_dict['d']

priority(deeds_prior)

def test_priority_a():
    deeds_prior = {'a': ['breakfast', 'lunch', 'diiner', 'supper'], 'b': ['feed cats', "cats toilet clean"], 'c': ['study', 'buy food in the store'], 'd': 'play with cat'}
    assert priority(deeds_prior) == ['breakfast', 'lunch', 'diiner', 'supper']

test_priority_a()

def test_priority_b():
    deeds_prior = {'e': ['breakfast', 'lunch', 'diiner', 'supper'], 'b': ['feed cats', "cats toilet clean"], 'c': ['study', 'buy food in the store'], 'd': 'play with cat'}
    assert priority(deeds_prior) == ['feed cats', "cats toilet clean"]

test_priority_b()

priority = ['a', 'b', 'c', 'd']
deeds = [['breakfast', 'lunch', 'diiner', 'supper'], ['feed cats', "cats toilet clean"], ['study', 'buy food in the store'], ['play with cat']]

dict_priority_deeds_time = {'a': {'breakfast': 20, 'lunch': 30, 'dinner': 45, 'supper': 20}, 'b': {'feed cats': 10, 'cats toilet clean': 15}

dict_priority_deeds_time = {'a': {'breakfast': (20, '10:00'), 'lunch': (30, '15:00'), 'dinner': (45, '21:00'), 'supper': (20, '23:00')}, 'b': {'feed cats': (10, '11:00'), 'cats toilet clean': (15, '11:00')}}

def priority_time(the_dict):
    for key in the_dict:
        if key == 'a':
            return the_dict['a']
        elif key == 'b':
            return the_dict['b']
        elif key == 'c':
            return the_dict['c']
        elif key == 'd':
            return the_dict['d']
priority_time(dict_priority_deeds_time)

#Roman Tarasov
#Задача №1
#my_priorities = {'a': 'cod', 'b': 'coffee', 'c': 'brekfast', 'd': 'work', 'e': 'rdr2'}
my_priorities = {'b': 'coffee', 'c': 'brekfast', 'd': 'work', 'e': 'rdr2', 'a': 'cod'}
def find_most_priority(my_dict):
    for p, r in my_dict.items():
        if p == 'a':
            return(r)
            #break
    for p, r in my_dict.items():
        if p == 'b':
            return(r)
            #break
    for p, r in my_dict.items():
        if p == 'c':
            return(r)
            break
    for p, r in my_dict.items():
        if p == 'd':
            return(r)
            break
    for p, r in my_dict.items():
        if p == 'e':
            return(r)
            break
            
            
find_most_priority(my_priorities)


def test_my_priorities():
    my_priorities = {'a': 'cod', 'b': 'coffee', 'c': 'brekfast', 'd': 'work', 'e': 'rdr2'}
    expected = 'cod'
    assert find_most_priority(my_priorities) == expected

test_my_priorities()
  
def test_my_priorities_2():
    my_priorities = { 'b': 'coffee', 'c': 'brekfast', 'd': 'work', 'e': 'rdr2'}
    expected = 'coffee'
    assert find_most_priority(my_priorities) == expected

test_my_priorities() 
test_my_priorities_2()


def test_my_priorities_3():
    my_priorities = { 'b': 'coffee', 'c': 'brekfast', 'd': 'work', 'e': 'rdr2', 'a': 'cod'}
    expected = 'cod'
    assert find_most_priority(my_priorities) == expected
test_my_priorities_3()


#Jamshid
#Задача №1
#Создать список дел. У каждого дела будет описание и приоритет от А до I. Вывести самое приоритетное для вас дело
print('---------------------------------')
print('Jamshid Tashpulatov')

spisok_del_1 = {'A': ('breakfast', 'dinner'),
'B': ('study', 'work'),
'C': ('walk', 'hobby')
}

def find_priority(some_dict):
    list_of_iter = []
    for priority in some_dict:
        list_of_iter += [priority]
    list_of_iter.sort()
    print(some_dict[list_of_iter[0]])

find_priority(spisok_del_1)

def test_find_priority_1(): #Стандартный тест
    spisok_del_1 = {'A': ('breakfast', 'dinner'),
'B': ('study', 'work'),
'C': ('walk', 'hobby')
}
    result = ('breakfast', 'dinner')
    assert result == find_priority(spisok_del_1)

test_find_priority_1()

def test_find_priority_2(): #Тест на случай, если бы не было приоритета А
    spisok_del_1 = {'B': ('study', 'work'),
'C': ('walk', 'hobby')
}
    result = ('study', 'work')
    assert result == find_priority(spisok_del_1)

test_find_priority_2()


# Другая структура - строка
spisok_del_str = '''A-breakfast, dinner-30
B-study, work-100
C-walk, hobby-50'''

# Другая структура - словарь со временами (затраченное, граничное)
spisok_del_dict = {'A': {'breakfast': (30, '7:30'), 'dinner': (30, '13:30')}, 'B': {'study': (100, '12:00'), 'work': (300, '19:00')}, 'C': {'walk': (60, '20:00'), 'hobby': (60, '21:00')}}

def find_priority_dict(some_dict):
    list_of_iter = []
    for key in some_dict:
        list_of_iter += [key]
    list_of_iter.sort()
    return print(f"Приоритетные дела - {some_dict[list_of_iter[0]].keys()}")
    
find_priority_dict(spisok_del_dict)    

print('---------------------------------')

    

#Anhzela
#Задача №1
my_prioritet_1 = {'breakfast':'a', 'lunch':'b', 'dinner':'c'}

def my_prioritet (dict_my_prioritet):
    my_list_prioritet = []
    for i in dict_my_prioritet.values():
        my_list_prioritet.append(i)
    my_list_sort = sorted(my_list_prioritet)
    print (my_list_sort[0])
print (my_prioritet(my_prioritet_1))

def my_prioritet (dict_my_prioritet):
    my_list_prioritet = []
    for i in dict_my_prioritet.values():
        my_list_prioritet.append(i)
    my_list_sort = sorted(my_list_prioritet)
    if my_list_sort[0] == 'a':
        print ('приоритет - breakfast')
    elif my_list_sort[1] == 'b':
        print ('приоритеное дело - lunch')
    elif my_list_sort[2] == 'c':
        print ('приоритеное дело - dinner')
print (my_prioritet(my_prioritet_1))


def test_my_prioritet_1():
    my_prioritet_1 = {'breakfast':'a', 'lunch':'b', 'dinner':'c'}
    assert 'приоритет - breakfast' == my_prioritet(my_prioritet_1)
    
my_prioritet_2 = {'lunch':'b', 'dinner':'c','breakfast':'a'}    
my_prioritet_3 = {'lunch':'b', 'dinner':'c'}     

def test_my_prioritet_2():
    my_prioritet_2 = {'lunch':'b', 'dinner':'c','breakfast':'a'} 
    assert 'приоритет - breakfast' == my_prioritet(my_prioritet_2)

def test_my_prioritet_3():
    my_prioritet_3 = {'lunch':'b', 'dinner':'c'}
    assert 'приоритеное дело - lunch' == my_prioritet(my_prioritet_3)
test_my_prioritet_3()

#Антон Кувалда

dict_del = {'1':'python', '2':'music', '3':'bike'}
'''
просмотреть ключи
выбрать наименьший ключ
напечатать дело с наименьшим ключом


1) перейти на буквы
2) если не одно дело с макс приоритетом. Печатать все.
'''
def prior (di):
    a = 6678
    for i in di.keys():
        #print (i)
        b = int(i)
        if b < a:
            a = b
        
    print (di[str(a)])

            
prior (dict_del)     
#print (dict_del['1'])

   
    

#Аня Арисова 
#задача 1
#приоритеты от a-высок c-низк. вывести самое приоритет дело. 


# def priority_list(my_list):
#     for key, value in my_list.items():
#         if key == 'a':
#             return value
#         elif key == 'b':
#             return value
#         else:
#             return value

def priority_list(my_list):
    if 'a' in my_list:
        return my_list['a']
    elif 'b' in my_list:
        return my_list['b']
    else:
        return my_list['c']
         
            
def test_priority_list_1():
    my_list = {'a': 'спать', 'b': 'пить', 'c': 'есть'}
    assert priority_list(my_list) == 'спать'
            
            
#в списке нет дел с приоритетом 'а' тест
def test_priority_list_2():
    my_list = {'b': 'пить', 'c': 'есть'}
    assert priority_list(my_list) == 'пить'
            

def test_priority_list_3():
    my_list = { 'b': 'пить', 'c': 'есть', 'a': 'спать'}
    assert priority_list(my_list) == 'спать'



