# Bank Management System

A simple and interactive Bank Management System implemented in Python. This system allows users to perform essential banking operations like creating an account, depositing money, withdrawing money, and checking account balance. The program is designed with modular functions, error handling, and a clean menu-driven interface for ease of use.

---

## Features

- **Create New Account**: Register a new account with a unique account number and initial deposit.
- **Deposit Money**: Add funds to an existing account.
- **Withdraw Money**: Withdraw funds from an account, ensuring sufficient balance.
- **Check Balance**: View account details, including the current balance.
- **Exit**: Safely exit the program with a farewell message.

---

## Key Concepts

- **Data Storage**: Uses Python dictionaries to store account details.
- **Functions**: Modular design for handling each operation independently.
- **Input Validation**: Prevents invalid inputs with appropriate error messages.
- **Exception Handling**: Manages runtime errors like invalid deposits or withdrawals.
- **Dynamic Menu**: Menu-driven system with a dictionary-based function mapping for efficient user interaction.

---

## How to Use

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the project directory**:
   ```bash
   cd bank-management-system
   ```

3. **Run the Python script**:
   ```bash
   python bank_management_system.py
   ```

4. **Follow the menu prompts** to perform operations.

---

## Example Usage

```
Welcome to the Bank Management System
1. Create a New Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Exit
Enter your choice (1-5):
```

### Sample Operations:

1. **Create Account**:
   - Enter account details: Account number, name, and initial deposit.
2. **Deposit Money**:
   - Enter your account number and the amount to deposit.
3. **Withdraw Money**:
   - Enter your account number and the amount to withdraw.
4. **Check Balance**:
   - View the account holder’s name and the current balance.
5. **Exit**:
   - Safely exits the program.

---

## Requirements

- Python 3.6 or higher

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for improvements or bug fixes.
