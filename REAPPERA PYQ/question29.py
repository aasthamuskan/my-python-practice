class BankAccount:
    def __init__(self, name, initial_balance):
        self._name = name
        self._balance = initial_balance

    def get_name(self):
        return self._name

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(self._balance)
        else:
            print("Invalid withdrawal amount")

# Example usage (provided in the editor)
name = input()
initial_balance = float(input())
withdraw_amount = float(input())

account = BankAccount(name, initial_balance)
print(account.get_name())
print(account.get_balance())
account.withdraw(withdraw_amount)
