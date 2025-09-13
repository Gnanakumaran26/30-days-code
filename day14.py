import random

print("🪙 Coin Toss Game - Day 14")

while True:
    choice = input("\nToss the coin? (yes/no): ").lower()
    if choice == "no":
        print("👋 Exiting Coin Toss...")
        break
    elif choice == "yes":
        toss = random.choice(["Heads", "Tails"])
        print(f"🎯 Result: {toss}")
    else:
        print("❌ Invalid choice, type 'yes' or 'no'.")
