# ============================================
#       BANKING MANAGEMENT SYSTEM
#       Developed using Basic Python
# ============================================

accounts = []


# -------------------------------
# Generate Account Number
# -------------------------------
def generate_account_number():
    return 5551101 + len(accounts)


# -------------------------------
# Find Account
# -------------------------------
def find_account(account_no):
    for account in accounts:
        if account["account_no"] == account_no:
            return account

    return None


# -------------------------------
# Login Function
# -------------------------------
def login():

    try:
        account_no = int(input("Enter account number: "))
        pin = input("Enter your 4-digit PIN: ")

    except ValueError:
        print("Invalid input!")
        return None

    account = find_account(account_no)

    if account is not None and account["pin"] == pin:
        return account

    print("Invalid account number or PIN!")
    return None


# -------------------------------
# Create Account
# -------------------------------
def create_account():

    print("\n========== CREATE ACCOUNT ==========")

    name = input("Enter your name: ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    mobile = input("Enter 10-digit mobile number: ").strip()

    if len(mobile) != 10 or not mobile.isdigit():
        print("Mobile number must be exactly 10 digits!")
        return

    pin = input("Create a 4-digit PIN: ").strip()

    if len(pin) != 4 or not pin.isdigit():
        print("PIN must be exactly 4 digits!")
        return

    try:
        balance = float(input("Enter initial deposit: "))

    except ValueError:
        print("Please enter a valid amount!")
        return

    if balance < 0:
        print("Initial deposit cannot be negative!")
        return

    account_no = generate_account_number()

    account = {
        "account_no": account_no,
        "name": name,
        "mobile": mobile,
        "pin": pin,
        "balance": balance,
        "transactions": []
    }

    accounts.append(account)

    print("\nAccount created successfully!")
    print("Your Account Number:", account_no)
    print("Please remember your account number and PIN.")


# -------------------------------
# View Account
# -------------------------------
def view_account():

    print("\n========== VIEW ACCOUNT ==========")

    account = login()

    if account is None:
        return

    print("\n----- ACCOUNT DETAILS -----")
    print("Account Number :", account["account_no"])
    print("Name           :", account["name"])
    print("Mobile Number  :", account["mobile"])
    print("Balance        : ₹", account["balance"])


# -------------------------------
# Deposit Money
# -------------------------------
def deposit_money():

    print("\n========== DEPOSIT MONEY ==========")

    account = login()

    if account is None:
        return

    try:
        amount = float(input("Enter deposit amount: "))

    except ValueError:
        print("Please enter a valid amount!")
        return

    if amount <= 0:
        print("Amount must be greater than 0!")
        return

    account["balance"] = account["balance"] + amount

    account["transactions"].append(
        "Deposited: ₹" + str(amount)
    )

    print("\nMoney deposited successfully!")
    print("Deposited Amount : ₹", amount)
    print("Updated Balance  : ₹", account["balance"])


# -------------------------------
# Withdraw Money
# -------------------------------
def withdraw_money():

    print("\n========== WITHDRAW MONEY ==========")

    account = login()

    if account is None:
        return

    try:
        amount = float(input("Enter withdrawal amount: "))

    except ValueError:
        print("Please enter a valid amount!")
        return

    if amount <= 0:
        print("Amount must be greater than 0!")
        return

    if amount > account["balance"]:
        print("Insufficient balance!")
        return

    account["balance"] = account["balance"] - amount

    account["transactions"].append(
        "Withdrawn: ₹" + str(amount)
    )

    print("\nMoney withdrawn successfully!")
    print("Withdrawn Amount : ₹", amount)
    print("Remaining Balance: ₹", account["balance"])


# -------------------------------
# Check Balance
# -------------------------------
def check_balance():

    print("\n========== CHECK BALANCE ==========")

    account = login()

    if account is None:
        return

    print("\n----- BALANCE DETAILS -----")
    print("Account Number :", account["account_no"])
    print("Account Holder :", account["name"])
    print("Available Balance: ₹", account["balance"])


# -------------------------------
# Transfer Money
# -------------------------------
def transfer_money():

    print("\n========== TRANSFER MONEY ==========")

    sender = login()

    if sender is None:
        return

    try:
        receiver_no = int(input("Enter receiver account number: "))
        amount = float(input("Enter transfer amount: "))

    except ValueError:
        print("Please enter valid input!")
        return

    receiver = find_account(receiver_no)

    if receiver is None:
        print("Receiver account not found!")
        return

    if sender["account_no"] == receiver["account_no"]:
        print("Cannot transfer money to the same account!")
        return

    if amount <= 0:
        print("Amount must be greater than 0!")
        return

    if amount > sender["balance"]:
        print("Insufficient balance!")
        return

    sender["balance"] = sender["balance"] - amount
    receiver["balance"] = receiver["balance"] + amount

    sender["transactions"].append(
        "Transferred: ₹" + str(amount)
        + " to Account "
        + str(receiver["account_no"])
    )

    receiver["transactions"].append(
        "Received: ₹" + str(amount)
        + " from Account "
        + str(sender["account_no"])
    )

    print("\nMoney transferred successfully!")
    print("Transferred Amount : ₹", amount)
    print("Remaining Balance  : ₹", sender["balance"])


# -------------------------------
# Search Account
# -------------------------------
def search_account():

    print("\n========== SEARCH ACCOUNT ==========")

    try:
        account_no = int(input("Enter account number: "))

    except ValueError:
        print("Please enter a valid account number!")
        return

    account = find_account(account_no)

    if account is None:
        print("Account not found!")
        return

    print("\n----- ACCOUNT FOUND -----")
    print("Account Number :", account["account_no"])
    print("Name           :", account["name"])
    print("Mobile Number  :", account["mobile"])
    print("Balance        : ₹", account["balance"])


# -------------------------------
# Transaction History
# -------------------------------
def transaction_history():

    print("\n========== TRANSACTION HISTORY ==========")

    account = login()

    if account is None:
        return

    print("\n----- TRANSACTION HISTORY -----")

    if len(account["transactions"]) == 0:
        print("No transactions found.")
        return

    for transaction in account["transactions"]:
        print("-", transaction)


# -------------------------------
# Main Menu
# -------------------------------
while True:

    print("\n")
    print("==========================================")
    print("       BANKING MANAGEMENT SYSTEM")
    print("==========================================")

    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Transfer Money")
    print("7. Search Account")
    print("8. Transaction History")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Please enter a number from 1 to 9!")
        continue

    if choice == 1:
        create_account()

    elif choice == 2:
        view_account()

    elif choice == 3:
        deposit_money()

    elif choice == 4:
        withdraw_money()

    elif choice == 5:
        check_balance()

    elif choice == 6:
        transfer_money()

    elif choice == 7:
        search_account()

    elif choice == 8:
        transaction_history()

    elif choice == 9:
        print("\nThank you for using Banking Management System!")
        print("Have a great day!")
        break

    else:
        print("Invalid choice! Please select 1 to 9.")