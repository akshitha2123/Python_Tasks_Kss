# Bank Account System (Class, Object, Constructor)


class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)

b1 = BankAccount(12345, 5000)

b1.deposit(2000)
b1.withdraw(1000)
b1.display()
