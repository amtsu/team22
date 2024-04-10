import pytest
from bank_account import BankAccount

@pytest.mark.parametrize("accaunt_number, owner_name, starting_balance, deposit_amount, expected_balance", [
    (12345, "Oleg", 1000, 500, 1500),
    (12346, "Stas", 0, 1000, 1000),
    (12347, "Vlad", -500, 1000, 500)
])

def test_deposit(accaunt_number, owner_name, starting_balance, deposit_amount, expected_balance):
    """
    позитивный тест на пополнение счета
    """
    account = BankAccount(accaunt_number, owner_name, starting_balance)
    account.deposit(accaunt_number, deposit_amount)
    assert account.balance == expected_balance
    

@pytest.mark.parametrize("accaunt_number, owner_name, starting_balance, deposit_amount, expected_error", [
    (12345, "Oleg", 1000, 500, ValueError),
    (12345, "Stas", 0, 1000, ValueError),
    (12349, "Vlad", -500, "1000", TypeError)
])

def test_deposit_negativ(accaunt_number, owner_name, starting_balance, deposit_amount, expected_error):
    """
    негативные тесты:
    попытка пополнения счета в уже существующий счет с другим именем.
    пополнение баланса строкой
    """
    with pytest.raises(expected_error):
        account = BankAccount(accaunt_number, owner_name, starting_balance)
        account.deposit(accaunt_number, deposit_amount)
        assert account.accaunt_number == expected_error

@pytest.mark.parametrize("accaunt_number, owner_name, starting_balance, cash_withdrawal, expected_result",[
    (12351, "Oleg", 3000, 1500, 1500),
    (12352, "Stas", 1000, 500, 500)
    #(12353, "Anna", 1000, 2000, "Недостаточно средств")
])

def test_withdraw(accaunt_number, owner_name, starting_balance, cash_withdrawal, expected_result):
    
    account = BankAccount(accaunt_number, owner_name, starting_balance)
    account.withdraw(accaunt_number, cash_withdrawal)
    assert account.balance == expected_result
    
    
        
    
    
