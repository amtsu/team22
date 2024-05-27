def create_dictionary(**kwargs):
    return kwargs

def add_student (dict_student, name, age):
    dict_student[name] = age
    return dict_student

def remove_student (dict_student, name):
    dict_student.pop(name)
    return dict_student

def unification(a,b):
    unification = a|b
    return unification

def del_dict(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

def dict_shift (dict1):
    new_dict = {}
    for k,v in dict1.items():
        new_dict[v] = k
    return new_dict

def dict_sorting(dict1):
    return dict(sorted(dict1.items(), reverse=True))

def max_element(dict):
    max_value = max(dict.items())
    return max_value

def max_element1(dict):
    max_value = max(dict.values())
    return max_value

def check_fruit_price(dict_prices,name_fruit):
    if dict_prices[name_fruit] > 1.5:
        result = 'дорогой товар'
    else: 
        result = 'приемлимая цена'
    return result
    
def check_age(name,age):
    if name [age]>= 18:
        result = ("Совершеннолетний") 
    else:
        result = ("Несовершеннолетний")
    return result 

def compare_sets_length(set1, set2):
    if len(set1) > len(set2):
        result = ("set1 длиннее set2")
        
    elif len(set1) < len(set2):
        result = ("set2 длиннее set1")
     
    else:
        result = ("Оба множества имеют одинаковую длину")
       
    return result

def proverka(chot):
    if chot % 2 == 0:
        result =("Четное число")
        
    else: 
        result =("Нечетное число")
       
    return result

def leap_year (year):
    #result = True 
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        print (year, '-високосный год')
        return True
    else:
        print (year, '- невисокосный год')
        return False

def triangle_type(a: float, b: float, c: float) -> str:
    result = "не треугольник"
    triangle_exist = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
    if triangle_exist:
        sides = [a, b, c]
        sides.sort()
        acuteTriangle = (sides[0]**2 + sides[1]**2) > sides[2]**2
        obtuseTriangle = (sides[0]**2 + sides[1]**2) < sides[2]**2
        rightTriangle = abs((sides[0]**2 + sides[1]**2) - sides[2]**2) <= 0.01

        if acuteTriangle:
            result = "остроугольный"
        elif obtuseTriangle:
            result = "тупоугольный"
        elif rightTriangle:
            result  = "прямоугольный"
    return result

def prover(k):   
    if k == k[::-1]:
       result = 'палиндром'
        #print ('палиндром')
    else:
        result = 'не палиндром'
        #print ('не палиндром')
    return result

def simple(g):
    if g <= 1:
        return 'составное число'
    for i in range(2, g):
        if g % i == 0:
            return 'составное число'
    return 'простое число'

def check_string(string):
    ab = 'abcdefghijklmnopqrstuvwxyz'
    return all([x.lower() in ab for x in string])

def correct_date(input_date):
    try:
        datetime.strptime(input_date, '%Y-%m-%d')
        return "Дата введена корректно"
    except ValueError:     
        return "Дата введена некорректно"
 
def palindrom(f):
    if f == f[::-1]:
         result = 'палиндром'
    else:
        result = 'не палиндром'
    return result    

def weekday(n):
    res = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    return res[n-1]

def factorial(q):
    if q == 0:
        return 1
    else:    
        return q * factorial(q - 1)
