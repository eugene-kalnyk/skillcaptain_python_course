# Creating the `BankAccount` class
class BankAccount:
    def __init__ (self, account_number, account_holder_name, account_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance

    def deposit_money(self, amount):
        self.account_balance = self.account_balance + amount
        return f"{amount} dollars added to your account. Current account balance is: {self.account_balance} dollars"
    
    def withdraw_money(self, amount):
        self.account_balance = self.account_balance - amount
        return f"{amount} dollars withdrawn from your account. Current account balance is: {self.account_balance} dollars"

    def info(self):
        return f"Account number: {self.account_number}. Account holder name: {self.account_holder_name}. Account balance: {self.account_balance} dollars"

account = BankAccount (12345, "James", 1000)

# Testing class and methods
print(account.info())
print(account.deposit_money(600))
print(account.withdraw_money(700))
