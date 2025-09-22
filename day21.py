import random

print("😂 Random Joke Generator - Day 21")

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why was the math book sad? Because it had too many problems.",
    "Why did the student eat his homework? Because the teacher said it was a piece of cake!",
    "Why did the programmer quit his job? Because he didn’t get arrays (a raise)."
]

while True:
    choice = input("\nDo you want a joke? (yes/no): ").lower()
    if choice == "no":
        print("👋 Exiting Joke Generator...")
        break
    elif choice == "yes":
        print("😂 " + random.choice(jokes))
    else:
        print("❌ Invalid choice, type yes or no.")
