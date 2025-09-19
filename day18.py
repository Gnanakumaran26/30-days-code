import random

print("🎮 Guess the Word Game - Day 18")

words = ["python", "github", "program", "developer", "machine", "learning"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6  # chances

print("\nGuess the word:")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("✅ Correct!")
    else:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")

    print(" ".join(guessed))

if "_" not in guessed:
    print(f"\n🎉 You won! The word was '{word}'")
else:
    print(f"\n😢 You lost! The word was '{word}'")
