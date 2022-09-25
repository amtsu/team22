#!/usr/local/bin/python
# coding: utf-8
# что можно сделать для тестирования:
#функция batch_test_call вызывает функции с именем test_func_pattern и следующим за ним номером, 
#начинающимся с нуля и до test_func_count-1. Функции являются тестами для чего-то и возвращают строку,
# в которой должно содержаться либо значение "выполнено", либо значение "не выполнено"
class btc:
    @staticmethod
    def batch_test_call(test_func_pattern, test_func_count):
        i=0
        while(i < test_func_count):
            exec('tmpstr ='+test_func_pattern+str(i)+'()')
            print('результат выполнения теста #'+str(i)+': ' + tmpstr)
            i += 1
        return
# пример исходных данных:
#def test0():
#    return 'done'
#def test1():
#    return 'done'
#def test2():
#    return 'not done'
#def test3():
#    return 'done'
#def test4():
#    return 'not done'
#def test5():
#    return 'done'

# пример вызова:
#btc.batch_test_call('test',6)

# результат вызова для данного набора исходных данных:

#результат выполнения теста #0: done
#результат выполнения теста #1: done
#результат выполнения теста #2: not done
#результат выполнения теста #3: done
#результат выполнения теста #4: not done
#результат выполнения теста #5: done
