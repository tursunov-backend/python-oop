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
    def show_balance(self):
        print(f"{self.owner} ning yakuniy balansi: {self.balance} so'm")


account1 = BankAccount("Abdujalol", 1000)
account2 = BankAccount("Ali", 2000)
account3 = BankAccount("Vali", 900)

account1.deposit(500)
account1.withdraw(300)

account2.withdraw(1500)
account2.deposit(700)

account3.withdraw(1000)
account3.deposit(200)

