class BankAccount:
    
    def __init__(self, account_owner, balance):
        self.owner = account_owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(self.owner, "balance", self.balance)

account1 = Bank_account("tom", 50000)
account2 = Bank_account("Bob", 500)

account1.deposit(2000)
account1.withdraw(300)
account1.display_balance()
