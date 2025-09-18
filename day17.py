import random

print("✊✋✌️ Rock Paper Scissors - Day 17")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower()
    if user == "quit":
        print("👋 Thanks for playing!")
        break
    if user not in choices:
        print("❌ Invalid choice, try again.")
        continue

    computer = random.choice(choices)
    print(f"🖥️ Computer chose: {computer}")

    if user == computer:
        print("🤝 It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("✅ You win!")
    else:
        print("❌ You lose!")
