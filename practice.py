# Определите класс Account, имитирующий банковский счет. Класс должен включать атрибуты для хранения идентификатора владельца, баланса счета и методы для депозита (пополнения) и снятия средств, если на счету достаточно средств.

class Account:
    def __init__(self, owner_id, balance=0):
        self.owner_id = owner_id
        self.balance = balance

        self.owner_id = owner_id  # атрибут
        self.balance = balance  # атрибут
        
    def deposit(self, amount):  # метод для депозита
        if amount > 0:
            self.balance += amount
            print(f"Внесено {amount}. Твой баланс - {self.balance}.")
            
            
    def withdraw(self, amount):  # метод для снятия средств
        if amount > self.balance:
            print("Недостаточно средств на счету.")
        elif amount <= amount:
            self.balance -= amount
            print(f"Снято {amount}. Твой баланс - {self.balance}.")
            
    def info(self):  # метод для отображения информации о счете
        print(f"Идентификатор владельца: {self.owner_id}")
        print(f"Баланс счета: {self.balance}")
        
man = Account("12345", 1000)  # создание объекта класса Account
man.info()  # отображение информации о счете
man.deposit(500)  # пополнение счета
man.info()  # отображение информации о счете
man.withdraw(200)  # снятие средств
man.info()  # отображение информации о счете

