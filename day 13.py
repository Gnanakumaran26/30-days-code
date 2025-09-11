import random

print("🎲 Dice Roller - Day 13")

while True:
    choice = input("\nRoll the dice? (yes/no): ").lower()
    if choice == "no":
        print("👋 Exiting Dice Roller...")
        break
    elif choice == "yes":
        dice = random.randint(1, 6)
        print(f"🎯 You rolled: {dice}")
    else:
        print("❌ Invalid choice, type 'yes' or 'no'.")
