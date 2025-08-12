import random

print("🎯 Welcome to Day 3 - Number Guessing Game!")

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Check the guess
if guess == secret_number:
    print("🎉 Correct! You guessed the right number!")
else:
    print(f"❌ Wrong! The number was {secret_number}. Better luck next time!")