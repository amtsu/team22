
'''Множества'''

#1
def set_union(set1, set2):
    '''функция для объединения множеств'''
    return set1.union(set2)
    
def set_difference(set1, set2):
    '''функция для разности множеств'''
    return set1.difference(set2) 

#2. 

def is_subset(set1, set2):
    '''функцию для проверки, является ли одно множество подмножеством другого.'''
    return set1.issubset(set2)

#3. Создайте 

def set_union(*sets):
    '''функция для объединения нескольких множеств.'''
    result = set()
    for s in sets:
        result = result.union(s)
    return result



'''Словари'''

#1.

def create_dictionary(**kwargs):
    '''функция для создания словаря с заданными ключами и значениями. Должна принимать словарь в формате ключ-значение и возвращать созданный словарь. '''
    return kwargs


#2. 
def add_student(student_dict, name, age, major):
    '''функция добавления студентов в словарь. Принимает словарь студентов и данные для добавления'''
    if name not in student_dict:
        student_dict[name] = {'age': age, 'major': major}
        return f'Student {name} added.'
    else:
        return f'Student {name} already exists.'

        
def remove_student(student_dict, name):
    '''функция удаления студентов из словаря.'''
    if name in student_dict:
        del student_dict[name]
        return f'Student {name} removed.'
    else:
        return f'Student {name} not found.'


'''Условия и циклы'''
#1. Создайте функцию для проверки возраста студента и вывода соответствующего сообщения.Должна принимать словарь студентов и имя студента, а затем выводить сообщение о совершеннолетии или несовершеннолетии.

def check_age(students, name):
    if students[name] >= 18:
        return f'{name} - совершеннолетний'
    else:
        return f'{name} - несовершеннолетний'









