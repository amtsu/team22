'''
1.Сделать класс швейных машинок с весом, цветом, возможностью шить двумя строчками (x и y)
'''
'''
2.Сделать класс сфер, с методом подсчета площади
'''
#Артем Цурков
#########


#Аня Марголина
class SewingMachine:
    def __init__(self, weihgt, color):
        self.weight = weight
        self.color = color
        
    def x_type_of_sew(self, x):
        self.x = type_of_sew
        
    def y_type_of_sew(self, y):
        self.y = type_of_sew
 
SM_x = SewingMachine(5, "white")

TS = SM_x.x_type_of_sew()


########
class Sphera:
    def __init__(self, r):
        self.r = r
    
    def square(self):
        return 4 * 3.14 * self.r ** 2
        
    def leinght(self):
       return 4 * 3.14 * self.r

sphera1 = Sphera(2)
res1 = sphera1.square()
res2 = sphera1.leinght()
print(res1, res2)

sphera2 = Sphera(5)
res3 = sphera2.square()
res4 = sphera2.leinght()

print(res3, res4)
   # создатьдве сферы
  #  радиус 2
  #  радиус 5
    
 

# Ruslan Yuspov
class SewingMachine:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print("перемещена в {self.x} {self.y}")
        
    def sew_shirt(self, sew_type, textile):
        if sew_type != "крестиком" and  sew_type != "игреком":
            raise Exception("могу шить только креситиком и игреком") 
            
        print(f"пошита футболка типом {sew_type} из {textile}")
        
    def  __str__(self):
        return f"Швейная машинка цвета {self.color}, текущее положение {self.x} {self.y}"

sewing = SewingMachine('белая', 1, 1)

sewing.sew_shirt("крестиком", "хлопок")
sewing.sew_shirt("игреком", "хлопок")
sewing.sew_shirt("игреком", "хлопок")

############################################################################
# класс Sphere
# принимает параметр радиус
# метод площадь сферы
# создать 2 сферы - радиусом 2 и радиусом 5 и вычислить площадь

PI = 3.14159

class Sphere:
    def __init__(self, r)
        self.r = r
        
    def area(self):
        return 4 * PI * self.r ** 2
    
sphere1 = Sphere(2)
sphere2 = Sphere(5)

area1 = sphere1.area()
area2 = sphere2.area()

print(area1, area2)



#Татьяна Щербакова
class SewingMachine:
    '''Швейная машинка'''
    
    def __init__(self, price=0, color="white", avalibleSewingTypes = ["X", "Y"], isPortable=true):
        self.price = price
        self.color = color
        self.avalibleSewingTypes = avalibleSewingTypes
        self.isPortable = isPortable
        
    def getPrice(self):
        return self.price
        
    def sewWithX()
        if 'X' in avalibleSewingTypes:
            return "Vjuh: shito!"
        else:
            return "ERROR: Don't have sewing type X!"
    
    def sewWithType(self, sewingType: str)
        if sewingType in self.avalibleSewingTypes:
            return "Vjuh: shito!"
        else:
            return "ERROR: Don't have sewing type" + sewingType + "!"
    
SM = SewingMach(avalibleSewingTypes = ["X", "Y"])
SM.sewWithType("X")
        
        
        
        
#Костя Максимов
class SewingMachine():
    def __init__(self, id, strochka, mobolity, color)
        self.id = id
        self.mobility = mobility
        self.strochka = strochka
        self.color = color
        
    def SetStr(id):
        a = input()
        if (a="x") or (a="y"): 
            self.strochka = a
        else: print ("Wrong str") 
        
    def Sew (strochka):
        if self.strochka = strochka: print(str(strochka))
        else: "Str fault"
        
        
        
        
class SphereKM():
    def __init__(self, r):
        self.r = r
        
    def volume(self):
        return 4*3.14*(self.r)**3/3
        
    def square(self):
        return 4*3.14*(self.r)**2

sp1 = SphereKM(3)
print (sp1.volume)
print (sp1.square)





#Maria Andreeva
class SewingMachine:
    """
    Швейная машинка
    Шить крестиком и игриком
    Может перемещаться
    Имеет цвет
    Шьет футболки из какой ткани
    """
    def __init__(self, color, weight, sewing_type_list):
        self.__color = color
        self.__weight = weight
        self.__sewing_types = sewing_type_list
        
    def sew(self, clother_name, material, sewing_type):
        if sewing_type in self.__sewing_types:
            sewing_result = f"Сшили {clother_name} из {material}, строчка {sewing_type}"
        else:
            sewing_result = None
            print("Нет такой строчки")
        return sewing_result
        
    def move(self):
        mobility = False
        if self.__weight < 5:
            mobility = True
        return mobility
        
    new_sewing_machine = SewingMachine(red, 3, ['x', 'y'])
        
        
    ############################################################################
    #Andrey Ivanchenko
class Sphere():
    def __init__(self, radius):
        self.radius = radius
    
    def sphere_area(self):
        return 4 * 3.14 * (self.radius ** 2)
        
radius1 = Sphere(2)
radius2 = Sphere(5)
print(radius1.sphere_area())
print(radius2.sphere_area())





#Андрей Каздым

class Shveinaya_Mashinka():
    #цвет типы строчек(х,у) переносная
    def __init__(self):
        self.color = 'color
        self.mobility = mobility

    def type_of_sewing(self, type_of_sewing)
        self.type_of_sewing = x
        self.type_of_sewing = y

______________________________________________________________

#класс сфера который может вычислить площать сферы и длину окружности. объект сфера с радиусом 2 и радиусом 5. и вычислить площадь

class Sphere():
    
    def __init__(self, R):
        self.R = R
    
    def square(self):
        return 4 * 3.14 * (self.R**2)
sphere1 = Sphere(2)
print(sphere1.square())

# ANTON_KUVALDA_START_____________________________

'''
радиус
считаем площадь сферы
делаем две сферы
'''

class sphere:
    
    def __init__(self, r):
        self.r = r

    def square(self):
       return 4 * 3.14 * self.r**3

s1 = sphere(2)
s2 = sphere(5)
#s1.r
print(s1.square())
print(s2.square())


'''
class Sewing_Machine():
    
    
        '''две программы, 
    
        переносная, 
    
        белая
    
    
        возвращает футболки
    
        '''
    
    
def __init__(self):
    self.color = 'white'
    self.portable = true
    
def programm(self, type):
    self.programm_1 = 'x'
    self.programm_2 = 'y'
 '''

# ANTON_KUVALDA_END ______________________________


#Аникин Костя
3##class Sawing_mach():
   def__init__(self, color, portable, program):     
  3  self.ts=cot= 



#Andrey Ivanchenko
class SawingMachine():
    """
    можеть шить
    перемещаться
    иметь цвет
    разные программы
    шить крестиком и тд
    """
    def __init__():
        self.color = color
        self.portable = portable
        self.programs = programs
        self.sewcross = sewcross
        
    def 10futbolok(self):
        for i in range(10):
            return (sewcross, color)
    10futbolok(x, white)
#########

class Sphere():
    """
    радиус
    метод вычисления площади сферы
    2 сферы: радиусом 2 и 5
    """"
    def __init__():
        self.radius = radius
    
    def sphere_square(self, radius):
        return 3.14 * (self.radius ** 2)
        
    sphere_square(2)
    sphere_square(5)
        





#Лоцманов Саша

class SewingMashineSerg:
    """
    что-то там про строчки
    переносная/не переносная
    какого-то цвета может быть
    """
    def __init__(self, color:str, portable:bool, ):
        
    


#Лоцманов Саша
class SewingMachine():
    '''Класс швейных машинок
    param:
    color:  цвет
    тип строчки: x y
    переносная
    шить
    пермещаться
    '''
    coordinat_x0 = 0
    coordinat_y0 = 0
    coordinat_z0 = 0
    seam_x = 'x'
    seam_y = 'y'
    
    cloth = '100% хлопок'
    
    def __init__(self, seam, color, weight, coordinat_x = coordinat_x0, coordinat_y = coordinat_y0, coordinat_z = coordinat_z0):        
        self.seam = seam
        self.color = color
        self.weight = weight
        self.coordinat_x = coordinat_x
        self.coordinat_y = coordinat_y
        self.coordinat_z = coordinat_z
    
    def sew(self):
        return f'Сшила футболку из "{self.cloth}". Использовала шов "{self.seam}"'
        
    def position(self):
        return (self.coordinat_x, self.coordinat_y, self.coordinat_z)
        
    def move(self, step_x, step_y, step_z):
        print(f'Перемещаем машинку на {step_x} по х, {step_y} по y, {step_z} по z')
        self.coordinat_x = self.coordinat_x + step_x
        self.coordinat_y = self.coordinat_y + step_y
        self.coordinat_z = self.coordinat_z + step_z
        

sewing_machine_x = SewingMachine('x', 'Red', '2', 1, 2, 3)
    
sewing_machine_y = SewingMachine('y', 'Red', '2', 3, 5, 4 )

sewing_machine_y_0 = SewingMachine('y', 'Red', '2')

t_shirt_x = sewing_machine_x.sew()

t_shirt_y = sewing_machine_y.sew()

print(t_shirt_x, t_shirt_y, sep = '\n')

print(sewing_machine_x.position(), sewing_machine_y.position(),sewing_machine_y_0.position(), sep = '\n')












#Матросова Ирина
class SewingMachine(): 
#я толклм не могу печатать с клавиатуры на планшете ;()
#шить 2 видами: крестик и игрик
#перемешаться
#цвет
#параметр:переносная да нет. может перенести или нет
#шьет футболки и есть ткань
    def __init__(self, ismove, color, sewingType)
        self.ismove=ismove
        self.color=color
        self.sewingType=sewingType
        
    def outIsMove(self)
        return self.ismove
        
    def setColor(self,col)
        self.color=col
        
    def getColor(self)
        return self.color

objectMyMachine=SewingMachine(True,black,2)




## фу фу фу писать с планшета :) :) :)
# сфера
#радиус
# метод площадь сферы
# создать 2 сферы ; радиус 2 и 5 . вычислить площадь

class Sphere():
    area_sphere = 0
    
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area_sphere(self):
        self.area_sphere=4*3.14*(self.radius**2)
        
    def out_area_sphere(self):
        self.calculate_area_sphere()
        return self.area_sphere
        
objectMyShere = Sphere(2)
s1 = objectMyShere.out_area_sphere()
objectMyShere2 = Sphere(5)
s2 =  objectMyShere2.out_area_sphere()

















___________________________________________________________________________________
# Roman Tarasov
# швейная машина (белая, шьет крестиком и игриком, переносная)
class Shweinaya_mashina():
    
    def __init__(self, color, work1, work2, pickabilyty):
        self.__color = color
        self.__work1 = work1
        self.__work2 = work2
        self.__pickabilyty = pickabilyty
        
    def sewing_type1(self):
        return 'шьем рубашку с помощью стяжка ' + self.__work1

    def sewing_type2(self):
        return 'шьем рубашку с помощью стяжка ' + self.__work2
        
    def what_doing():
        return print('shyot')
        
    def weight():
        return print('not heavy')

stiag1 = Shweinaya_mashina('белый', 'х', 'у', 'переносная')
print(stiag1.sewing_type1())
print(stiag1.sewing_type2())
        
        
        
#############################
# создать класс сфера с параметром радиус. вычислить площадь. создать две сферы и вычислить площадь. радиус 2 и 5

class Sphere():
    
    
    def __init__ (self, radius):
        self.radius = radius
        
    def count_ploshad(self):
        return 4 * 3.14 * (self.radius**2)

radius1 = Sphere(2)
print(radius1.count_ploshad())
radius2 = Sphere(5)
print(radius2.count_ploshad())
        
        
    
        
 _____________________________________________________________________________






# Jamshid Tashpulatov
# Класс - швейная машинка. Умеет шить двумя строчками (крести, игрик), будет переносной, имеет белый цвет
# Атрибуты - модель, мощность, цвет, вес
#class SewingMachine():
#    def __init__(self, variable, transportable, color)L
    
#Сфера
class Sphere():
    def __init__(self, r):
        self.radius = r
    def square(self):
        return f"Площадь сферы = {4 * 3.14 * self.radius ** 2}"

s1 = Sphere(2)
print(s1.square())
s2 = Sphere(5)
print(s2.square())







#Ruslan Yunusov

    



#--------------------------
# Vera Tarasova
class S()SewingM
#--------------------------


#Регина Марфенкова
# 2 типа строчки
#будет переносной
# белый цвет
class Sewingchine():
    def __init__(self, color, portable, ):
        self.color = white
        self.portable
    def   portable()  
############## 
import math
class Sphere():
    def __init__(self, radius):
        self.radius = radius
    def square(self):
        return 4  * math.pi * self.radius ** 2
sphere1 = Sphere(2)
sphere2 = Sphere(5)

square1 = sphere1.square()
square2 = sphere2.square()




#Serg Maltsev
class SwingMachine():


#---------------------------------------
#serg
class SewingMa