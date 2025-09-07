print("📝 Word Counter - Day 12")

def count_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower().strip(".,!?")  # clean punctuation
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

while True:
    text = input("\nEnter a sentence/paragraph (or 'exit' to quit): ")
    if text.lower() == "exit":
        print("👋 Exiting Word Counter...")
        break

    counts = count_words(text)
    print("\n📊 Word Frequency:")
    for word, count in counts.items():
        print(f"{word}: {count}")
