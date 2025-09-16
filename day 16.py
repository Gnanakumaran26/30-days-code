import random

print("🧮 Math Quiz Game - Day 16")

score = 0

for i in range(5):  # 5 questions
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 + num2

    print(f"\nQ{i+1}: {num1} + {num2} = ?")
    user = int(input("Your Answer: "))

    if user == answer:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct Answer = {answer}")

print(f"\n🎯 Final Score: {score}/5")
