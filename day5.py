import random
import string

print("🔐 Random Password Generator - Day 5")

# Get length from user
length = int(input("Enter password length: "))

# Define characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))

print(f"Your generated password is: {password}")