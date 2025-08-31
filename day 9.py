print("🧮 Calculator with History - Day 9")

history = []

while True:
    print("\nOptions: add | sub | mul | div | history | exit")
    choice = input("Choose operation: ").lower()

    if choice == "exit":
        print("Exiting... 👋")
        break

    elif choice == "history":
        print("\n📜 Calculation History:")
        if history:
            for h in history:
                print(h)
        else:
            print("No history yet.")
        continue

    if choice in ["add", "sub", "mul", "div"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input, enter numbers only.")
            continue

        if choice == "add":
            result = a + b
            symbol = "+"
        elif choice == "sub":
            result = a - b
            symbol = "-"
        elif choice == "mul":
            result = a * b
            symbol = "*"
        elif choice == "div":
            if b == 0:
                print("❌ Division by zero not allowed!")
                continue
            result = a / b
            symbol = "/"

        record = f"{a} {symbol} {b} = {result}"
        history.append(record)
        print("✅", record)
    else:
        print("❌ Invalid choice, try again.")
