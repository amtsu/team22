import pytest
from part1_BankAccount import BankAccount


vtb = BankAccount(333, 'Unknown', 1000)

def test_bancAccount_getBalance():
    expected = 1000
    assert expected == vtb.balance 

def test_test_bancAccount_moneyAdd():
    expected = 3000
    vtb.moneyAdd(2000)
    assert expected == vtb.balance 

def test_test_bancAccount_moneyDeduct():
    expected = 2000
    vtb.moneyDeduct(1000)
    assert expected == vtb.balance 

