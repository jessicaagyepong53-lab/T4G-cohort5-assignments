from bank_account import BankAccount


class SavingsAccount(BankAccount):
    """A BankAccount that also earns interest on its balance."""

    def __init__(self, holder_name, starting_balance=0, interest_rate=0):
        super().__init__(holder_name, starting_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Calculate interest on the current balance and deposit it."""
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)

    def __str__(self):
        return (
            f"SavingsAccount[{self.holder_name}] | "
            f"Balance: GHS {self.balance:.2f} | Rate: {self.interest_rate}%"
        )


if __name__ == "__main__":
    # 1. Create a SavingsAccount and make two deposits
    savings = SavingsAccount("Agyepong Jessica", 500, interest_rate=5)
    savings.deposit(100)
    savings.deposit(50)
    print(savings)

    # 2. Call apply_interest and print the account to show the balance changed
    savings.apply_interest()
    print(savings)

    # 3. Make a withdrawal and confirm it still works correctly
    savings.withdraw(200)
    print(savings)

    # Confirm inherited error handling still works
    try:
        savings.withdraw(-10)
    except ValueError as error:
        print(f"Transaction failed: {error}")