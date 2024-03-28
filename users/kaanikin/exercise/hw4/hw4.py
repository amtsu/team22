def modify_lists_1():
    """
    Задание 1. выполните следующий код 
    list_one = [1, 2, 3, 4, 5, 6, 9]
    list_two = [1, 2, 3, 4, 5, 6, 9]
    list_two.append(789)
    print(list_one, list_two, sep='\n') 
    """
    list_one = [1, 2, 3, 4, 5, 6, 9]
    list_two = [1, 2, 3, 4, 5, 6, 9]
    list_one.append(789)
    
    return list_one, list_two

def modify_lists_2():
    """
    затем выполните код 
    list_one = [1, 2, 3, 4, 5, 6, 9]
    list_two = list_one
    list_two.append(789)
    print(list_one, list_two, sep='\n')
    """
    list_one = [1, 2, 3, 4, 5, 6, 9]
    list_two = list_one
    list_two.append(789)
    
    return list_one, list_two

def a_poem():
    """
    Задание 2. Задайте переменную a_poem типа строка, со следующим содержимым: 
    За стеклом лежал Питон,
    Большой и толстый, как батон.
    Вверх пополз,
    Затем вернулся,
    Круглым бубликом свернулся.
    
    - Создайте переменную a_list типа список, заполнив ее содержимым строки a_poem так, чтобы каждый символ строки a_poem стал отдельным элементом списка a_list
    - Создайте переменную another_list типа список, заполнив ее содержимым строки a_poem так, чтобы каждое слово строки a_poem стал отдельным элементом списка another_list. Знаки препинания прилипнут к словам, не страшно.
    - Выведите на экран элементы и их количество для списков a_list и another_list.
    """
    a_poem = "За стеклом лежал Питон,\nБольшой и толстый, как батон.\nВверх пополз,\nЗатем вернулся,\nКруглым бубликом свернулся." #Задайте переменную a_poem типа строка, со следующим содержимым: 

    alist = []
    a_list = list(a_poem) #Создайте переменную a_list типа список, заполнив ее содержимым строки a_poem так, чтобы каждый символ строки a_poem стал отдельным элементом списка a_list
    length_a_list = len(a_list)
    
    another_list = []
    another_list = a_poem.split()  #Создайте переменную another_list типа список, заполнив ее содержимым строки a_poem так, чтобы каждое слово строки a_poem стал отдельным элементом списка another_list. Знаки препинания прилипнут к словам, не страшно.
    length_another_list = len(another_list)
    
    

    one_more_list = []  #Создайте переменную one_more_list типа список, каждым элементом которой является отдельная строка строфы из a_poem. Выведите на экран элементы one_more_list и их количество.
    one_more_list = a_poem.split('\n')
    length_one_more_list = len(one_more_list)

    return a_list, length_a_list, another_list, length_another_list, one_more_list, length_one_more_list

def sol_list(val): 
    """
    Задание 3.

    - Создайте список solyanka_list, в качестве его элементов добавьте значения каждого из известных вам типов данных python.
    - Выведите на экран содержимое списка solyanka_list.
    - Посчитайте количество элементов списка solyanka_list.
    - Выведите на экран тип пятого от начала списка элемента.
    - Добавьте в конец списка solyanka_list элемент типа "список" из одного элемента
    - Выведите на экран тип последнего элемента списка solyanka_list
    """
    solyanka_list = list(val)
    #print(solyanka_list)
    len_sol = len(solyanka_list)

    if (len_sol <= 5):
        raise 'Слишком короткий список'
    else:
        type_5 = type(solyanka_list[6])

    
    solyanka_list.append([7])
    elem_type = type(solyanka_list[-1])
    return solyanka_list, len_sol, type_5, elem_type
  



def check_fibonacci_numbers(my_list):
    """
    Задание 4. Дана последовательности чисел Фибоначчи из нескольких элементов: 
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
    
    - Создайте список fibonacci_list, элементами которого будут числа Фибонначи из задания.
    - Посчитайте и выведите на экран, сколько чисел Фибоначчи в последовательности из задания
    - Посчитайте и выведите на экран, сколько раз число 1 входит в заданную последовательность Фибоначчи.
    - Проверьте и выведите на экран результат, является ли число 21 числом Фибоначчи. Число 33? Число 987? число 9999? использование оператора if возможно, но не является необходимым
    """
    
    fib_number = len(my_list)  #Посчитайте и выведите на экран, сколько чисел Фибоначчи в последовательности из задания


    one_value = 0         #Посчитайте и выведите на экран, сколько раз число 1 входит в заданную последовательность Фибоначч
    for i in range(fib_number):
        if my_list[i] == 1:
            one_value +=1
    

    question_value = [21, 33 , 987, 9999]  #Проверьте и выведите на экран результат, является ли число 21 числом Фибоначчи. Число 33? Число 987? число 9999? использование оператора if возможно, но не является необходимым
    result_question = {}
    for elem in question_value:
        if elem in my_list:
            result_question[elem] = True
            
        else: result_question[elem] = False

    return fib_number, one_value, result_question

def switch_pos():
    """
    Задание 5. Задайте переменную a_list типа "список" со следующим содержимым: 
    1,2,5,4,3,6

    - выведите содержимое a_list на экран
    - поменяйте местами третий и пятый элементы a_list и выведите результат на экран
    """
    a_list = [1,2,5,4,3,6]
    temp_value = a_list[2]
    a_list[2] = a_list[4]
    a_list[4] = temp_value
    return a_list

def omar():
    """
    Задание 6. Кто-то перепутал строчки в стихотворении, хорошо что они были пронумерованы. 
    (2, "тот большего добьётся," )
    (5, "Кто умирал, тот знает, что живёт.")
    (1, "Кто битым жизнью был," )
    (3, "Пуд соли съевший выше ценит мёд.")
    (4, "Кто слёзы лил, тот искренней смеётся,") 
    выведите на экран строки Омара Хайама в правильном порядке, используя список.
    """
    string1 = (2, "тот большего добьётся," )
    string2 = (5, "Кто умирал, тот знает, что живёт.")
    string3 = (1, "Кто битым жизнью был," )
    string4 = (3, "Пуд соли съевший выше ценит мёд.")
    string5 = (4, "Кто слёзы лил, тот искренней смеётся,")
    
    propper_order_list = []
    for i in range(5):
        if int(string1[0]) == (i+1):
            propper_order_list.append(string1[1])
        elif int(string2[0]) == (i+1):
            propper_order_list.append(string2[1]) 
        elif int(string3[0]) == (i+1):
            propper_order_list.append(string3[1]) 
        elif int(string4[0]) == (i+1):
            propper_order_list.append(string4[1]) 
        elif int(string5[0]) == (i+1):
            propper_order_list.append(string5[1]) 
    return propper_order_list

def story_of_programmer(poem):
    true_story_list = []
    
    temp_poem = []   #Создайте переменную true_story_list типа список, занесите в неё третью строку из стихотворения выше.
    temp_poem = poem.split('\n')
    
    true_story_list = true_story_list + [temp_poem[2]]
    #print(true_story_list)
   # print(str(len(true_story_list)))
    
    true_story_list = true_story_list + [temp_poem[3]]  #Добавьте четвертую строку в конец списка true_story_list.
    #print(true_story_list)
    #print(str(len(true_story_list)))
    
    true_story_slice = []    #Создайте переменную true_story_slice типа список, занесите в неё четвертую и пятую строки из стихотворения выше. Добавьте содержимое true_story_slice как один последний элемент списка true_story_list.
    true_story_slice = true_story_slice + [temp_poem[3]] + [temp_poem[4]]
    true_story_list = true_story_list + [true_story_slice]
    #print(true_story_list)
    #print(str(len(true_story_list)))
    
    true_story_slice.clear()   #Очистите весь список true_story_slice, выведите его содержимое на экран. 
    #print(true_story_slice)
    
    true_story_list.insert(0, temp_poem[0])    #Добавьте первую строку из стихотворение в начало списка true_story_list
    #print(true_story_list)
    #print(str(len(true_story_list)))
    
    
    true_story_list.pop(-1)    #Удалите последний элемент списка true_story_list
    #print(true_story_list)
    #print(str(len(true_story_list)))
    
    true_story_list.insert(1, temp_poem[0])  #Добавьте вторым элементом списка true_story_list вторую строчку стихотворения
    
    true_story_tail = []   #Создайте переменную true_story_tail типа список, занесите в него пятую строку стихотворения дважды. Скопируйте элементы списка true_story_tail в конец списка true_story_list.
    for i in range (2):
        true_story_tail.insert(0, temp_poem[4])
    
    for i in range (2):
        true_story_list.append(true_story_tail[i])
    #print(true_story_list)
    #print(str(len(true_story_list)))
    
    true_story_list.pop(5)   #Удалите 5 элемент списка true_story_list.
    #print(true_story_list)
    #print(str(len(true_story_list)))
    
    new_poem = ''
    for i in range(len(true_story_list)):
        new_poem = new_poem + true_story_list[i] + '\n'
     
        
    return new_poem