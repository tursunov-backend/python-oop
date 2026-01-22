class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Yangi balans: {self.balance}')
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Pul yechildi. Yangi balans: {self.balance}")
        else:
            print("Xato: balans yetarli emas")

account = BankAccount('Abdujalol', 1000)

account.deposit(500)   
account.withdraw(300)  
account.withdraw(2000)  
