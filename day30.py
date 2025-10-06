import datetime
import random

print("🤖 AI Chatbot - Day 30")
print("Type 'exit' anytime to quit.\n")

responses = {
    "hi": ["Hello!", "Hey there!", "Hi! How are you?"],
    "hello": ["Hi!", "Hello! 😊", "Hey!"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thank you!"],
    "name": ["I'm PyBot, your friendly assistant!", "Call me PyBot 🤖"],
    "time": [f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"],
    "weather": ["I can’t check live weather yet, but it looks great today! 🌤"],
    "bye": ["Goodbye!", "See you soon!", "Take care! 👋"]
}

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("PyBot: Bye! 👋 Have a great day!")
        break

    found = False
    for key in responses:
        if key in user_input:
            print("PyBot:", random.choice(responses[key]))
            found = True
            break

    if not found:
        print("PyBot: I'm not sure about that 🤔")
