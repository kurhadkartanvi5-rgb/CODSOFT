import random

print("Password Generator")

length = int(input("Enter the password length: "))

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

password = ""

for i in range(length):
    random_char = random.choice(characters)
    password = password + random_char

print("\nGenerated Password:", password)