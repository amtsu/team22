#!/usr/local/bin/python
# coding: utf-8
from getdatafrom import webpage
import os
#тесты
def test_webpage_str_1():
    assert str(webpage('test')) == 'url: test, opened: False, error code: 0'
    return None
def test_webpage_str_2():
    assert str(webpage('test')) != 'url: test, opened: True, error code: 0'
    return None
def test_webpage_open_1():
    test_html = '<html><head><meta charset="utf-8"></head><body><div class=\"test\">some text</div><div class=\"price\">1 345р.</div></body></html>'
    filename = os.getcwd() + '/test.html'
    assert (not os.path.exists(filename)) 
    with open(filename,'w') as f:
        f.write(test_html)
    test_page = webpage('file://' + filename)
    
    text = test_page.open().decode('utf-8')
    os.remove(filename)
    assert text == test_html# + 'fail'
    
    return None
#--------------------------------------------------------------------------------------------------------
    
    