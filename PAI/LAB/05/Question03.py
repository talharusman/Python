class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = "Wednesday, September 11, 2024"
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited in your account.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")

    def check_balance(self):
        print(f"Current balance is ${self.balance}.")

    def print_customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of opening:", self.date_of_opening)
        print(f"Balance: ${self.balance}\n")


account1 = BankAccount(1234, "Talha Rusman", 1000)

account1.print_customer_details()
account1.deposit(500)
account1.check_balance()
account1.withdraw(200)
account1.check_balance()
account1.withdraw(1500)