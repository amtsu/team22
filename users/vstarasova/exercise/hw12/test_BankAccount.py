import pytest
from BankAccount import BankAccount

def test_deposit():
    # Тестирование внесения положительной суммы
    bank_account = BankAccount("123456789", "Иванов Иван", 100)
    deposit_amount = 50
    bank_account.deposit(deposit_amount)
    assert bank_account.balance == 150

    # Тестирование внесения отрицательной суммы
    deposit_amount = -50
    bank_account.deposit(deposit_amount)
    assert bank_account.balance == 150  # Баланс не должен измениться

    print("Тесты для метода deposit пройдены успешно!")


def test_withdraw():
    # Тестирование снятия средств со счета
    bank_account = BankAccount("123456789", "Иванов Иван", 100)
    withdrawal_amount = 50
    bank_account.withdraw(withdrawal_amount)
    assert bank_account.balance == 50

    # Тестирование снятия суммы больше, чем баланс
    withdrawal_amount = 100
    bank_account.withdraw(withdrawal_amount)
    assert bank_account.balance == 50  # Баланс не должен измениться

    # Тестирование снятия отрицательной суммы
    withdrawal_amount = -50
    bank_account.withdraw(withdrawal_amount)
    assert bank_account.balance == 50  # Баланс не должен измениться

    print("Тесты для метода withdraw пройдены успешно!")


def test_get_balance():
    # Тестирование получения баланса счета
    bank_account = BankAccount("123456789", "Иванов Иван", 100)
    assert bank_account.get_balance() == 100

    print("Тесты для метода get_balance пройдены успешно!")


# Пример вызова тестов
#test_deposit()
#test_withdraw()
#test_get_balance()
