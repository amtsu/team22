#!/usr/local/bin/python
# coding: utf-8
#pip install mypy
#работа с абстрактными классами
from abc import ABCMeta, abstractmethod 
#---------------------------------------------
class Test(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def foo_par(self, parameter:bool) -> bool:
        pass
    pass
#--------------------------------------------
class TestChild(Test):
    def __init__(self):
        return None
    #def foo(self):
    #    print('foo')
    #    return None
    #def foo_par(self, parameter:bool):
    #    print('foo_par')
    #    return parameter
    #def foo_par(self, parameter:bool) -> str: # неверный параметр
    #    print('foo_par %s'%(parameter))
    #    return 'True'
    #def foo_par(self, parameter:bool): # нормально
    #    print('foo_par %s'%(parameter))
    #    return 'True'
    #@property  #https://pythonz.net/references/named/property/
    #def foo_par(self):
    #    return 'foo_par property'
    #pass
#--------------------------------------------
def main():
    t = TestChild()
    t.foo()
    param = str('jiggles') #нормально
    #t.foo_par(param)       #нормально, но не сработает когда foo_par это property
    print(t.foo_par) 
#--------------------------------------------
if __name__ == '__main__':
    main()
pass  