import random
import string

print("🔑 Password Generator - Day 15")

# User input for password length
length = int(input("Enter password length: "))

# Characters (letters + digits + symbols)
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = "".join(random.choice(characters) for _ in range(length))

print(f"✅ Your Secure Password: {password}")
