class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner} ning balansi: {self.balance} so'm")

    def get_balance(self):
        return self.balance


a1 = BankAccount("Abdujalol", 1200)
a2 = BankAccount("Ali", 2300)
a3 = BankAccount("Vali", 900)
a4 = BankAccount("Sami", 1500)
a5 = BankAccount("Gani", 600)

accounts = [a1, a2, a3, a4, a5]

total_balance = 0

for account in accounts:
    total_balance += account.get_balance()

print(f"Jami balans: {total_balance} so'm")
