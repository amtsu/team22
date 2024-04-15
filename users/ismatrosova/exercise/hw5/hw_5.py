def set_union(set1,set2):
    return set1|set2

def set_difference (set1,set2):
    return set1 - set2

def set_union_many (*sets):
    resultat = set () #empty set
    for i in sets :
        resultat = resultat.union(i)
    return resultat

def delete_value (set, var):
    if (var in set):
        set.remove(var)
    return set

def set_intersection_many (*sets):
    resultat = sets[0]
    for i in sets :
        resultat = resultat.intersection(i)
    return resultat

def equality_sets (set1, set2):
    return set1==set2

def disjunctive (set1,set2):
    if (set1 == set()) and (set2 == set()):
        return False
    result = set1&set2
    if (result==set()):
        return True
    else:
        return False

def create_set (*elements):
    return set(elements)

def merge_dict(dict1,dict2):
    return dict1|dict2 # произойдет перезапись 2 словарем

def revert_dict (dict):
    new_dict = {}
    #for i in dict.items():
    #    new_dict[i[1]]=i[0]
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict

def max_element_v(dict1):
    #if (dict1==dict()):
    if not dict1:
        return None
    return max(dict1.values())

def check_age(dict1, key):
    if not dict1.get(key):
        return "нет такого студента в базе"
    elif dict1[key] >= 18:
        return "Совершеннолетний"
    else:
        return "Несовершеннолетний"

def compare_sets_length(set1, set2):
    #if len(set1) > len(set2):
    #    return "set1 больше set2"
    #else:
    #    if len(set1) < len(set2):
    #        return "set1 меньше set2"
    #    else:
    #        return "set1 и set2 одинаковы"
    if len(set1) > len(set2):
        return "set1 больше set2"
    elif len(set1) < len(set2):
        return "set1 меньше set2"
    #else:
    #    return "set1 и set2 одинаковы"
    return "set1 и set2 одинаковы"

def even_or_odd_number (val):
    if val%2==0:
        return ("%s четное" % (val))
    #else:
    #    return ("%s нечетное" % (val))
    return ("%s нечетное" % (val))

def is_palindrome(str1):
    return str1 == str1[::-1]

def times_of_day (hour,minute):
    result = hour*60+minute
    if (0<=result) and (result<6*60) or (result == 24*60):
        return 'ночь'
    elif (6*60<=result) and (result<12*60):
        return 'утро'
    elif (12*60<=result) and (result<18*60):
        return 'день'
    elif (18*60<=result) and (result<24*60):
        return 'вечер'

def day_week (num):
    match num:
        case 1:
            return 'понедельник'
        case 2:
            return 'вторник'
        case 3:
            return 'среда'
        case 4:
            return 'четверг'
        case 5:
            return 'пятница'
        case 6:
            return 'суббота'
        case 7:
            return 'воскресенье'
        case _:
            return 'не номер дня недели'

def povtor(stroka):
    list1 = list(stroka)
    list1.sort()
    result = {}
    for i in range (len(list1)-1):
        if list1[i] == list1[i+1]:
            if not result.get(list1[i]):
                result[list1[i]] = 2
            else:
                result[list1[i]] += 1
    return result
    '''
        print(povtor('fgdgfgdgdg'))      #= {'d': 3, 'f': 2, 'g': 5}
        print(povtor('ftlj'))            #= {}
        print(povtor('rrr444u7fffff'))   #= {'4': 3, 'f': 5, 'r': 3}
    '''
    '''
    def povtor2(stroka):
        result = {}
        for char in set(stroka):
            result[char] = stroka.count(char)
        return result
    '''
    '''
        print(povtor2('fgdgfgdgdg'))     #= {'f': 2, 'd': 3, 'g': 5}
        print(povtor2('ftlj'))           #= {'f': 1, 'l': 1, 'j': 1, 't': 1}
        print(povtor2('rrr444u7fffff'))  #= {'7': 1, '4': 3, 'f': 5, 'r': 3, 'u': 1}
    '''