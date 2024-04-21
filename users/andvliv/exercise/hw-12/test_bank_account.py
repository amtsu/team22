import pytest
from bank_account import BankAccount

def test_bank_deposit():
    bank_acc1 = BankAccount(123456, 'Andrey Ivanchenko', 500)
    assert bank_acc1.deposit_money(100) == 600

def test_bank_withdrawal():
    bank_acc1 = BankAccount(123456, 'Andrey Ivanchenko', 500)
    assert bank_acc1.withdrawal_money(100) == 400