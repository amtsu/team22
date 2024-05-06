'''
Создайте класс BankAccount, который представляет банковский счет. У него должны быть атрибуты для хранения номера счета, имени владельца и баланса. Добавьте методы для внесения и снятия денег со счета.
'''

class BankAccount:
    def __init__(self, number, owner_name, balance):
        self.number = number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Сумма {amount} успешно зачислена на счет.")
        else:
            print("Неверная сумма для зачисления.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Сумма {amount} успешно снята со счета.")
        else:
            print("Недостаточно средств на счете или неверная сумма для снятия.")

    def get_balance(self):
        return self.balance

# Пример использования класса
account1 = BankAccount("123456789", "Иванов Иван", 1000)

print("Текущий баланс:", account1.get_balance())

account1.deposit(500)
print("Текущий баланс после зачисления:", account1.get_balance())

account1.withdraw(200)
print("Текущий баланс после снятия:", account1.get_balance())

account1.withdraw(1500)
