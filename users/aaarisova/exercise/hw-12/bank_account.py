'''8.Создайте класс BankAccount, который представляет банковский счет. У него должны быть атрибуты для хранения номера счета, имени владельца и баланса. Добавьте методы для внесения и снятия денег со счета.'''


class BankAccount:

    def __init__(self, account_number, holder_name, card_balance):
        self.account_number = int(account_number)
        self.holder_name = str(holder_name)
        self.card_balance = float(card_balance)

    
    def deposit_money(self, deposit):
        if deposit > 0:
            self.card_balance += deposit
            return self.card_balance
        else:
            return 'Ошибка. Проверьте, что ваша сумма для внесения больше 0'
        

    def withdraw_money(self, money):
        if self.card_balance >= float(money):
             self.card_balance -= float(money)
             return self.card_balance
        else:
            return 'Ошибка. Запрашиваемая сумма выше баланса на счету'