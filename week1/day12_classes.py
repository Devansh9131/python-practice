class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            self.balance += amount
            print(f"Deposit: {amount}, Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdraw: {amount}, Balance: {self.balance}")

    def account_details(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")


account1 = BankAccount("John")
account1.account_details()
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(300)
account1.deposit(0)
account1.deposit(-50)
account1.withdraw(0)
account1.withdraw(-50)
account1.withdraw(200)
account1.account_details()
