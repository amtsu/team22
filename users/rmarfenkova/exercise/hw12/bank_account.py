class BankAccount:
    all_account_numbers = []
    
    def __init__(self, account_number, owner_name, balance=0):
        if account_number in BankAccount.all_account_numbers:
            raise ValueError("Номер счета уже используется")
        else:
            self.account_number = account_number
            BankAccount.all_account_numbers.append(account_number)
        
            self.owner_name = owner_name
            self.balance = balance

    def deposit(self, account, amount):
        if account in BankAccount.all_account_numbers:
            self.balance += amount
        
    def withdraw(self, account, amount):
        if account in BankAccount.all_account_numbers:
            if amount <= self.balance:
                self.balance -= amount
            elif amount > self.balance:
                return "Недостаточно средств"  # в юпитере радотает, когда сумма снятия больше чем баланс, а тест почему то не проходит


            


            
            
        