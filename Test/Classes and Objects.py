class BankAccount:
    balance = 0

    def __init__(self, i):
       self.balance = i

    def deposit(self, x):

        return self.balance + x

    def withdraw (self, y):

        return self.balance - y

b = BankAccount (10)

b.deposit (25)
b.withdraw(1)

print ("The balance of the bank acount is now " + str(b.balance))