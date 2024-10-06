import sys
from bank_account import BankAccount

# Global variable for the balance
account_balance = 100

def main():
    global account_balance
    # Create a BankAccount instance using the global balance
    account = BankAccount(account_balance)

    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and optional amount from the command-line arguments
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Perform the appropriate action based on the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        account_balance = account._account_balance  # Update the global balance
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            account_balance = account._account_balance  # Update the global balance
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()