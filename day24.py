print("💰 Personal Expense Tracker - Day 24")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category (food, travel, bills, etc.): ")
        expenses.append({"amount": amount, "category": category})
        print("✅ Expense added!")

    elif choice == "2":
        if not expenses:
            print("📭 No expenses recorded.")
        else:
            print("\n📌 Your Expenses:")
            for i, exp in enumerate(expenses, 1):
                print(f"{i}. ₹{exp['amount']} - {exp['category']}")

    elif choice == "3":
        total = sum(exp["amount"] for exp in expenses)
        print(f"💵 Total Spent: ₹{total}")

    elif choice == "4":
        print("👋 Exiting Expense Tracker...")
        break

    else:
        print("❌ Invalid option, try again.")
