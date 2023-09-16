# -*- coding: utf-8 -*-
from function import arithmetic
def test1_arithmetic():
    assert arithmetic(1,2,"+")==3
    
def test2_arithmetic():
    assert not arithmetic(1,2,"+")==2
    
def test3_arithmetic():
    assert arithmetic(1,2,"-")==-1
    
def test4_arithmetic():
    assert arithmetic(2,2,"*")==4
    
def test5_arithmetic():
    assert arithmetic(6,2,"/")==3
    
def test6_arithmetic():
    assert arithmetic(6,2,"b")=="Неизвестная операция"