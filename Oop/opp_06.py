class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance+ amount
        print(f"After deposit:{self.balance}")

    def withdraw(self,amount):
        self.balance -= amount
        print(f"After withdrawl:{self.balance}")


A = Bankaccount("Aashu",10000)

print("Account holder:",A.name)
print("Intial Balance:",A.balance)

A.deposit(3000)
A.withdraw(2000)

