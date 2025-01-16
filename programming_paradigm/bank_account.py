class BankAccount:
    def __init__(self, account_balance: int = 0):  # Default balance is 0 if no value is provided
        self.account_balance = account_balance  # Set initial balance to the argument provided

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True  
        else:
            return False

    def display_balance(self):
      print(f"Current Balance: ${self.account_balance:.2f}")
