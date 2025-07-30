class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner}: {self.balance}")

    def get_balance(self):
        return self.balance

accounts = [
    BankAccount("Aziz", 1000),
    BankAccount("Sardor", 1500),
    BankAccount("Laylo", 800),
    BankAccount("Jasur", 1200),
    BankAccount("Javlon", 950)
]

total_balance = sum(acc.get_balance() for acc in accounts)
print(f"Jami balans: {total_balance}")