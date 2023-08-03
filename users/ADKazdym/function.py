# -*- coding: utf-8 -*-

def double_string(string):
    return string * 2

def double_string1(string):
    return string + " " + string

def arithmetic(a,b,z):
    if z=="+":
        return a+b
    elif z=="-":
        return a-b
    elif z=="*":
        return a*b
    elif z=="/":
        return a/b
    else:
        return ("Неизвестная операция")

def summ_sqrt(x, y):
    return x**2 + y**2

def gipotenuza(a,b):
    return (a**2 + b**2)**0.5
def square_parameters(a):
    return 4*a , a**2 , a*(2**0.5)
