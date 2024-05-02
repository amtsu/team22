# Функция для определения времени суток по введенному времени 
# (принимает текущее время в формате часы, минуты, возвращает утро, день, вечер, ночь)
def define_times_of_day(hh: int, mm: int) -> str:
    if not (type(hh) is int) or not (type(mm) is int):
        raise TypeError("Only integers are allowed")
        
    result = "incorrect time"
    input_is_correct = (hh >= 0) and (hh <= 24) and (mm >= 0) and (mm < 60)
    if input_is_correct:
        t = float(hh + mm/60)
        is_morning = (t >= 5.0) and (t < 12.0)
        is_afternoon = (t >= 12.0) and (t < 17.0)
        is_evening = (t >= 17.0) and (t < 21.0)
        is_night = ((t >= 21.0) and (t <= 24.0)) or ((t > 0) and (t < 5.0))
        is_midnight = t == 0.0

        if is_morning:
            result = "morning"
        elif is_afternoon:
            result = "afternoon"
        elif is_evening:
            result = "evening" 
        elif is_night:
            result = "night" 
        elif is_midnight:
            result = "midnight" 
    
    return result


# Функция, которая проверяет введенную пользователем строку на наличие повторяющихся символов
def check_repeated_symbols(s: str) -> dict:
    strList = list(s.lower())
    outDict = {}
    for char in strList:
        amount = strList.count(char)
        if (amount > 1) and not (char in outDict.keys()):
            outDict[char] = amount

    return outDict

# Функция, которая добавляет студента в БД
def add_student(db_dict: dict, id: int, name: str) -> str:
    
    if not (type(id) is int):
        raise TypeError("Only integers are allowed for id")
        
    if not (type(name) is str):
        raise TypeError("Only strings are allowed for name")

    
    result = "OK"
    if id <= 0: 
        result = "invalid id"
    if id in db_dict.keys():
        result = "id is already exist"
    if not name.isalpha():
        result = "invalid name"

    if result == "OK":
        db_dict[id] = name

    return result 


# Функция, которая удаляет студента из БД
def remove_student(db_dict: dict, id: int) -> str:
    
    if not (type(id) is int):
        raise TypeError("Only integers are allowed for id")
    
    result = "OK"
    if id <= 0: 
        result = "invalid id"
    elif not (id in db_dict.keys()):
        result = "id doesn't exist"

    if result == "OK":
        del db_dict[id]

    return result 

# Функция, которая проверят строку на полиндромность
def check_palidrome(s: str) -> bool:
    if len(s) > 0:
        s1 = str(s.replace(" ", "")).replace(",", "")
        return s1.casefold() == s1[::-1].casefold()    
    else:
        return False

# Функция, которая определяет тип треугольника
def triangle_type(a: float, b: float, c: float) -> str:
    """
    Функция, определяющая тип треугольника по длинам его сторон
    """
    result = "не треугольник"
    
    triangle_exist = not (type(a) is str) and not (type(b) is str) and not (type(c) is str)
    triangle_exist = triangle_exist and (a < (b + c)) and (b < (a + c)) and (c < (a + b))
    
    if triangle_exist:
        sides = [a, b, c]
        sides.sort()
        acuteTriangle = (sides[0]**2 + sides[1]**2) > sides[2]**2
        obtuseTriangle = (sides[0]**2 + sides[1]**2) < sides[2]**2
        rightTriangle = abs(sides[2] - (sides[0]**2 + sides[1]**2)**0.5) <= 0.1

        if rightTriangle:
            result  = "прямоугольный"
        elif acuteTriangle:
            result = "остроугольный"
        elif obtuseTriangle:
            result = "тупоугольный"
    return result


# Функция, которая определяет весокосность года
def check_leap_year(y: int) -> bool:
    if type(y) is str:
        try: 
            y = int(y)
        except:
            raise TypeError("Input should be integer value")
    
    if not (type(y) is int):
        raise TypeError("Input should be integer value")
    
    if y < 0:
        is_leap_year = False
    elif (y % 400 == 0) and (y % 100 == 0):
        is_leap_year = True
    elif (y % 4 == 0) and (y % 100 != 0):
        is_leap_year = True
    else:
        is_leap_year = False
    return is_leap_year
