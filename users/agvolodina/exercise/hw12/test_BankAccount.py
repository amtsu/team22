from func_BankAccount import BankAccount

account = BankAccount(123456, "Ivanov Ivan Ivanovich", 1000)

#тест для проверки вызова атрибутов объекта account класса BankAccount   
def test_account_number():
    assert account.account_number == 123456
    
def test_name():
    assert account.name == "Ivanov Ivan Ivanovich"
    
def test_name():
    assert account.balance == 1000
    
#тест для проверки внесения денег на счет
def test_add_money():
    assert account.add_money (100)== 1100

#метод для снятия денег со счета
def test_del_money():
    assert account.del_money(100) == 900

    