import pytest

from bank import BankAccount

@pytest.mark.parametrize("start_balance, income, expected",[
    (0, 1000, 1000),
    (159, 300, 459),
    (-128, 1000, 872),
    (-500, 500, 0)
])

def test_bank_account_add_to_acc(start_balance, income, expected):
    my_account = BankAccount(21687954, 'Mary', start_balance)
    my_account.add_to_acc(income)
    assert my_account.show_balance() == expected

@pytest.mark.parametrize("start_balance, outcome, expected",[
    (1000, 100, 900),
    (300, 159, 141),
    (-128, -100, -28),
    (500, 500, 0),
    (500, -500, 1000)
    
])

def test_bank_account_sub_from_acc(start_balance, outcome, expected):
    my_account = BankAccount(21687955, 'Mary', start_balance)
    my_account.sub_from_acc(outcome)
    assert my_account.show_balance() == expected