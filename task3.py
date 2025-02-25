class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self):
        amount = 100  # Fixed deposit amount
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self):
        amount = 100  # Fixed withdrawal amount
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

# Creating a bank account
account = BankAccount("12345678", "Mark Anthony Miralles ", 1000.0)

while True:
    print("\nBank Account Menu:")
    print("1. Deposit $100")
    print("2. Withdraw $100")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        account.deposit()
    elif choice == "2":
        account.withdraw()
    elif choice == "3":
        account.display_balance()
    elif choice == "4":
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
