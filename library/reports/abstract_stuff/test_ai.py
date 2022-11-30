#!/usr/local/bin/python
# coding: utf-8
#pip install mypy
#pip install pylint
"""работа с абстрактными классами"""
from abc import ABCMeta, abstractmethod
#---------------------------------------------
class Test(metaclass=ABCMeta):
    """ абстрактный класс -  интерфейс (ну, я надеялся) """
    @abstractmethod
    def a_method(self):
        """ просто метод, без параметров """
    @abstractmethod
    def a_second_method(self, parameter:bool) -> bool:
        """ метод с параметрами. указанные типы используются только для справочной информации"""
#--------------------------------------------
class TestChild(Test):
    """ конкретный класс, реализующий интерфейс, задаваемый абстрактным классом """
    def a_method(self):
        """ реализация простого метода"""
        print('a_method')
    def a_second_method(self, parameter:bool) -> bool:
        """ реализация метода с параметрами """
        print('a_second_method')
        return parameter
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
    """ функция, вызываемая при выполнении модуля """
    test_class = TestChild()
    test_class.a_method()
    #param = str('jiggles') #нормально
    #t.foo_par(param)       #нормально, но не сработает когда foo_par это property
    print(test_class.a_second_method(True))
#--------------------------------------------
if __name__ == '__main__':
    main()
