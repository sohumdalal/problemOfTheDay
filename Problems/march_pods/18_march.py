'''
Problem Of The Day - 3/18/2025

Part 1: Create a BankAccount class with the following:

- Attributes: 
--- owner (str)
--- balance (float, default is 0)

- Methods:
--- deposit(amount): Adds to balance & prints "Deposited X".
--- withdraw(amount): Deducts balance (if sufficient funds) & prints "Withdrew X".
--- get_balance(): Returns balance.

Part 2: Modify BankAccount to store a history of all transactions.

- Attributes to add:
--- transactions (list of strings) → Keeps track of all deposits/withdrawals.

- Methods to add:
--- print_transactions(): Prints all transactions in order.

Example Usage:
account = BankAccount("Alice", 100)
account.deposit(50)   # Deposited 50
account.withdraw(20)  # Withdrew 20
account.print_transactions()

# Output:
# Deposited 50
# Withdrew 20

Part 3: Bonus - Store a timestamp alongside each transaction

'''