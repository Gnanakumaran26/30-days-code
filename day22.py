print("💱 Currency Converter - Day 22")

# Predefined conversion rates (example values)
rates = {
    "USD": 83.0,   # 1 USD = 83 INR
    "EUR": 89.0,   # 1 EUR = 89 INR
    "GBP": 102.0,  # 1 GBP = 102 INR
    "JPY": 0.56    # 1 JPY = 0.56 INR
}

print("\nAvailable currencies:", ", ".join(rates.keys()))

while True:
    choice = input("\nDo you want to convert? (yes/no): ").lower()
    if choice == "no":
        print("👋 Exiting Currency Converter...")
        break
    elif choice == "yes":
        amount = float(input("Enter amount in INR: "))
        currency = input("Convert to (USD/EUR/GBP/JPY): ").upper()

        if currency in rates:
            converted = amount / rates[currency]
            print(f"✅ {amount} INR = {round(converted, 2)} {currency}")
        else:
            print("❌ Currency not available.")
    else:
        print("❌ Invalid choice, type yes or no.")
