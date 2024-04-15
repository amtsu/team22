import pytest
from bank_account import BankAccount

@pytest.mark.parametrize("initial_balance, deposit_amount, expected_message", [
    (1000, 500, "Вы пополнили счет на 500. Текущий баланс: 1500"),
    (0, 100, "Вы пополнили счет на 100. Текущий баланс: 100"),
    (-500, 1000, "Вы пополнили счет на 1000. Текущий баланс: 500")
])
def test_deposit(initial_balance, deposit_amount, expected_message):
    account = BankAccount(12345, "John Doe", initial_balance)
    assert account.deposit(deposit_amount) == expected_message

@pytest.mark.parametrize("initial_balance, withdrawal_amount, expected_message", [
    (1000, 500, "Вы сняли со счета 500. Текущий баланс: 500"),
    (0, 100, "Недостаточно средств на счете"),
    (500, 1000, "Недостаточно средств на счете")
])
def test_withdraw(initial_balance, withdrawal_amount, expected_message):
    account = BankAccount(12345, "Stas", initial_balance)
    assert account.withdraw(withdrawal_amount) == expected_message    
    
