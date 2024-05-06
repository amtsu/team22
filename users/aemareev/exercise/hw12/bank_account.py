class BankAccount:
    __account_counter = 0

    def __new__(cls, *args, **kwargs):
        cls.__account_counter += 1
        return super().__new__(cls)

    def __init__(self, owner: str):
        self.account_number = self.__account_counter
        self.owner = owner
        self.__balance = 0

    def __add__(self, money: int | float):
        self.__balance += money

    def __sub__(self, money: int | float):
        if self.__balance >= money:
            self.__balance -= money
        else:
            raise ValueError(f'Недостаточно денег на счете. Баланс: {self.__balance}.')

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account_1 = BankAccount('Иванов')
    account_2 = BankAccount('Петров')
    account_3 = BankAccount('Сидоров')
    assert account_1.account_number == 1
    assert account_2.account_number == 2
    assert account_3.account_number == 3
    account_1 + 100
    assert account_1.get_balance() == 100
    account_1 - 50
    assert account_1.get_balance() == 50
