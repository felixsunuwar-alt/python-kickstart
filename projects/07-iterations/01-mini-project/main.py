# Mini-Project: Smart Password Generator
# Build upon the times-table exercise by creating a practical security tool!

# 📖 IMPORTANT: Read the README.md file first for detailed instructions,
#    examples, and ideas on how to approach this project!

# This project builds on what you learned in the times-table exercise:
# - Using for loops for known iterations (password length)
# - Using while loops for unknown iterations (user sessions)
# - Combining loops with conditional logic
# - Building strings character by character (accumulation pattern)

import random
import string

# TODO: Create your Smart Password Generator here!

# Here's a simple example to get you started:
print("=== Smart Password Generator ===")
print("Create secure passwords for your accounts!\n")

# Get basic requirements
length = int(input("Enter desired password length (8-20): "))

# Simple character sets
lowercase = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
uppercase = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = string.digits            # '0123456789'

# Build a basic character pool
char_pool = lowercase + uppercase + numbers

# Generate password using a for loop
password = ""
for i in range(length):
    password += random.choice(char_pool)

print(f"\nGenerated Password: {password}")

# Basic strength check
has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)

print(f"\nPassword Analysis:")
print(f"- Length: {length} characters")
print(f"- Contains lowercase: {'Yes' if has_lower else 'No'}")
print(f"- Contains uppercase: {'Yes' if has_upper else 'No'}")
print(f"- Contains numbers: {'Yes' if has_digit else 'No'}")

print("\nThank you for using Smart Password Generator!")

# YOUR TURN: 
# 1. Add user preferences for character types (uppercase, symbols, etc.)
# 2. Create a while loop to allow multiple password generation
# 3. Add password strength analysis and scoring
# 4. Include symbols and special characters
# 5. Add input validation for password length
# 6. Create different security levels or presets

# HINTS:
# - Use string.ascii_lowercase, string.ascii_uppercase, string.digits
# - Use random.choice() to pick random characters
# - Use any() function to check if password contains certain character types
# - Use while loops for "generate another password?" functionality
# - Build character pools based on user preferences

# Remember: This is YOUR project - make it secure and user-friendly!