import sys

def menu():
    print("\nWelcome to the SMBI Bank")
    print("1. Create a New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

# Dictionary to store account details
accounts = {}

def create_account():
    account_number = input("Enter a unique account number: ")
    if account_number in accounts:
        print("Account number already exists. Try a different one.")
        return
    name = input("Enter account holder's name: ")
    try:
        initial_deposit = float(input("Enter initial deposit amount (minimum 10000): "))
        if initial_deposit < 10000:
            print("Initial deposit must be at least 10000.")
            return
        accounts[account_number] = {"name": name, "balance": initial_deposit}
        print(f"Account created successfully! Account Number is: {account_number}")
    except ValueError:
        print("Invalid amount. Try again.")

def deposit_money():
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        accounts[account_number]["balance"] += amount
        print(f"Successfully deposited {amount:.2f}. New balance: {accounts[account_number]['balance']:.2f}")
    except ValueError:
        print("Invalid amount. Try again.")

def withdraw_money():
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("Account not found.")
        return
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0 or amount > accounts[account_number]["balance"]:
            print("Insufficient balance.")
            return
        accounts[account_number]["balance"] -= amount
        print(f"Successfully withdrow {amount:.2f}. Remaining balance: {accounts[account_number]['balance']:.2f}")
    except ValueError:
        print("Invalid amount. Try again.")

def check_balance():
    account_number = input("Enter your account number: ")
    if account_number not in accounts:
        print("Account not found.")
    else:
        print(f"Account Holder: {accounts[account_number]['name']}")
        print(f"Current Balance: {accounts[account_number]['balance']:.2f}")

# Function mapping for menu options
menu_functions = {
    "1": create_account,
    "2": deposit_money,
    "3": withdraw_money,
    "4": check_balance,
    "5": lambda: (print("Thank you for using the SMBI Bank. Have a Good Day!"), sys.exit())
}

# Main function
def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")
        action = menu_functions.get(choice, lambda: print("Invalid choice. Please try again."))
        action()

if __name__ == "__main__":
    main()
