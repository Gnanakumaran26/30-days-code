print("📝 Flashcard Quiz App - Day 23")

flashcards = {
    "Python is a ______ language.": "programming",
    "The capital of France is ______.": "paris",
    "2 + 2 = ______.": "4",
    "GitHub is mainly used for ______.": "version control",
    "The largest planet in our solar system is ______.": "jupiter"
}

score = 0

for question, answer in flashcards.items():
    print("\n" + question)
    user = input("Your answer: ").lower()

    if user == answer:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {answer}")

print(f"\n🎯 Final Score: {score}/{len(flashcards)}")
