class BankAccount:
    """Represents a customer's bank account."""

    def __init__(self, holder_name, starting_balance=0):
        self.holder_name = holder_name
        self.balance = starting_balance

    def deposit(self, amount):
        """Add money to the balance. Rejects amounts of zero or below."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        """Remove money from the balance.Rejects amounts of zero or below, and prevents the balance from going negative."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def __str__(self):
        return f"Account[{self.holder_name}] | Balance: GHS {self.balance:.2f}"


if __name__ == "__main__":
    # 1. Create two accounts with different names and starting balances
    account1 = BankAccount("Fredericka Asam", 30000)
    account2 = BankAccount("Agyepong Jessica", 1000000)

    # 2. Make at least three transactions across the two accounts
    account1.deposit(20000)
    account2.withdraw(3000)
    account1.withdraw(500)

    # 3. Print each account after the transactions
    print(account1)
    print(account2)

    # 4. Attempt a withdrawal that should fail and handle it gracefully
    try:
        account2.withdraw(5000)
    except ValueError as error:
        print(f"Transaction failed: {error}")

    print("\nFinal balances:")
    print(account1)
    print(account2)