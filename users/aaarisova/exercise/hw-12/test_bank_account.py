import pytest
from bank_account import BankAccount


def test_bank_account_initialization():
    bank_account = BankAccount(12345678, 'Ivanov', 100.00)
    assert (bank_account.account_number, bank_account.holder_name, bank_account.card_balance) == (12345678, 'Ivanov', 100.00)


def test_deposit_money_1():   
    '''тест на внесение денег >0'''
    bank_account = BankAccount(12345678, 'Ivanov', 100.00)
    deposit = 50
    assert bank_account.deposit_money(deposit) == 150


def test_deposit_money_2():   
    '''тест на внесение денег <0'''
    bank_account = BankAccount(12345678, 'Ivanov', 100.00)
    deposit = 0
    assert bank_account.deposit_money(deposit) == 'Ошибка. Проверьте, что ваша сумма для внесения больше 0'
        

def test_withdraw_money_1():
    '''тест снятие денег сумма < баланса'''
    bank_account = BankAccount(12345678, 'Ivanov', 100.00)
    money = 90
    assert bank_account.withdraw_money(money) == 10.00


def test_withdraw_money_1():
    '''тест снятие денег сумма > баланса'''
    bank_account = BankAccount(12345678, 'Ivanov', 100.00)
    money = 200
    assert bank_account.withdraw_money(money) == 'Ошибка. Запрашиваемая сумма выше баланса на счету'

