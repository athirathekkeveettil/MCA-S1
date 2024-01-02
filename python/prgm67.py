# create a bank account with account number,name,type of a account and balance
# write constructor and methods to deposit at the bank and withdraw an account from the bank

class Bank:
    def __init__(self,acc=0,name=None,type=None,balance=0):
        self.account=acc
        self.name=name
        self.type=type
        self.balance=balance
    def display(self):
        print("Account Number:",self.account)
        print("Name:",self.name)
        print("Type:",self.type)
        print("Balance:",self.balance)
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Deposited:",amt,"\nCurrent Balance:",self.balance)
    def withdraw(self,amt):
        if(self.balance>=amt):
            self.balance=self.balance-amt
            print("Withdrawed:",amt,"\nCurrent Balance:",self.balance)
        else:
            print("Insuffient Balance")

a=Bank(165768,'Athira','Fixed',20000)
a.display()
a.deposit(2000)
a.withdraw(2000)
