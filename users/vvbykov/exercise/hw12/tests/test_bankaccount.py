import pytest
import sys
sys.path.append("..") 
from bankaccount import *

def test_bankaccount():

    cl = BankAccount(1, "Pavel", "Marakin")
    
    assert cl.id == 1
    assert cl.full_name == "Pavel Marakin"
    assert cl.balance == 0

    assert cl.deposit(55) == 55
    assert cl.balance == 55
    assert cl.withdraw(5) == 50
    assert cl.balance == 50
    
    
