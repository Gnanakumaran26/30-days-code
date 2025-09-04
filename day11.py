print("🪞 Palindrome Checker - Day 11")

def is_palindrome(word):
    # Remove spaces and make lowercase
    cleaned = word.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

while True:
    text = input("\nEnter a word or sentence (or 'exit' to quit): ")
    if text.lower() == "exit":
        print("👋 Exiting Palindrome Checker...")
        break

    if is_palindrome(text):
        print(f"✅ '{text}' is a Palindrome!")
    else:
        print(f"❌ '{text}' is NOT a Palindrome.")
