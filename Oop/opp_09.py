class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful!")
            print(f"Updated Balance: {self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
            print(f"Remaining Balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance}")


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

if balance < 0:
    print("Initial balance cannot be negative!")
else:
    account = BankAccount(name, balance)

    while True:
        print("\n----- ATM MENU -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("Thank you for using our bank!")
            break

        else:
            print("Invalid choice! Please try again.")
