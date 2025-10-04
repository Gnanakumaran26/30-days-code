print("🏦 Bank Management System - Day 28")

# Bank accounts stored as dictionary
bank_accounts = {}

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        acc_num = input("Enter new account number: ")
        if acc_num in bank_accounts:
            print("❌ Account already exists!")
        else:
            bank_accounts[acc_num] = 0
            print(f"✅ Account {acc_num} created successfully!")

    elif choice == "2":
        acc_num = input("Enter account number: ")
        if acc_num in bank_accounts:
            amount = float(input("Enter deposit amount: ₹"))
            bank_accounts[acc_num] += amount
            print(f"💰 Deposited ₹{amount}. New Balance: ₹{bank_accounts[acc_num]}")
        else:
            print("❌ Account not found!")

    elif choice == "3":
        acc_num = input("Enter account number: ")
        if acc_num in bank_accounts:
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount <= bank_accounts[acc_num]:
                bank_accounts[acc_num] -= amount
                print(f"💸 Withdrawn ₹{amount}. New Balance: ₹{bank_accounts[acc_num]}")
            else:
                print("⚠️ Insufficient balance!")
        else:
            print("❌ Account not found!")

    elif choice == "4":
        acc_num = input("Enter account number: ")
        if acc_num in bank_accounts:
            print(f"📊 Balance for {acc_num}: ₹{bank_accounts[acc_num]}")
        else:
            print("❌ Account not found!")

    elif choice == "5":
        print("👋 Exiting Bank System...")
        break

    else:
        print("❌ Invalid choice, try again.")
