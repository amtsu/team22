import pytest
import sys
sys.path.append("..") 
from institution import *
from student import *

def test_institution():

    s1 = Student("Petr", "Ivanov", 21, "Khimki")
    s2 = Student("Varvara", "Bykova", 19, "Khimki")
    s3 = Student("Marfa", "Bykova", 18, "Khimki")
    s4 = Student("Tsurkov", "Artem", 23, "Moscow")
    
    inst = Institution()
    assert inst.admit(s1) == 1
    assert inst.admit(s2) == 2
    assert inst.admit(s3) == 3
    assert inst.admit(s4) == 4

    assert len(inst) == 4        
    assert inst.exclude(s3.id) == 3
    assert len(inst) == 3
    assert inst.exclude(s2.id) == 2
    assert len(inst) == 2
    
