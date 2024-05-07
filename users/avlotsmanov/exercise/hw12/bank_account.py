#Создайте класс BankAccount, который представляет банковский счет.
#У него должны быть атрибуты для хранения номера счета, имени владельца и баланса.
#Добавьте методы для внесения и снятия денег со счета.

class BankAccount:
    def __init__(
            self, number, name, balance = 0
    ):
        self.number = number
        self.name = name
        self.balance = balance

    def put_cash(self, cash):
        self.balance += cash
        return self.balance

    def withdraw_cash(self, cash):
        if cash <= self.balance:
            self.balance -= cash
            return 'ok'
        else:
            return 'not enough cash on bank_account'


acc1 = BankAccount(4276, 'Alex', 300)
print(acc1.balance)
acc1.put_cash(200)
print(acc1.balance)
print(acc1.withdraw_cash(400))
print(acc1.balance)
print(acc1.withdraw_cash(400))
print(acc1.balance)