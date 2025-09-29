# Mini-Project: Smart Password Generator

## 🎯 Goal

Create an intelligent password generator that uses loops to create secure passwords based on user preferences. This project builds upon the iteration concepts from Chapter 7 and demonstrates how loops can be used for practical security applications.

## 📖 Project Description

Build a password generator that:
- Uses loops to generate passwords of specified length
- Allows users to customize password requirements (uppercase, numbers, symbols)
- Generates multiple passwords in one session using iteration
- Validates password strength and provides feedback
- Demonstrates different types of loops for different purposes

This shows how loops can solve real-world security problems!

## 🎮 Example Interaction

```
=== Smart Password Generator ===
Create secure passwords for your accounts!

Password Requirements:
Enter desired password length (8-20): 12
Include uppercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include symbols? (yes/no): no

Generating your password...

Generated Password: aB7kL9mP2nQ8
Password Strength: Strong ✓

Password Analysis:
- Length: 12 characters ✓
- Contains lowercase: Yes ✓
- Contains uppercase: Yes ✓
- Contains numbers: Yes ✓
- Contains symbols: No
- Estimated crack time: 2,000 years

Generate another password? (yes/no): yes

Password Requirements:
Enter desired password length (8-20): 16
Include uppercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include symbols? (yes/no): yes

Generating your password...

Generated Password: K9#mL2@pQ7$nR4!s
Password Strength: Very Strong ✓

Password Analysis:
- Length: 16 characters ✓
- Contains lowercase: Yes ✓
- Contains uppercase: Yes ✓
- Contains numbers: Yes ✓
- Contains symbols: Yes ✓
- Estimated crack time: 50 million years

Generate another password? (yes/no): no

Thank you for using Smart Password Generator!
Stay secure online! 🔒
```

## 🧠 What You'll Practice

This project reinforces concepts from **Chapter 7: Iterations**:
- Using [`for` loops](../../../book/07-iterations.md#for-loops) for known iterations (password length)
- Using [`while` loops](../../../book/07-iterations.md#while-loops) for user session management
- [Loop patterns](../../../book/07-iterations.md#common-loop-patterns) for character selection and validation
- [Accumulation](../../../book/07-iterations.md#accumulation-pattern) to build passwords character by character

**Building on previous exercises:**
- Unlike [`times-table`](../../exercises/07-iterations/01-times-table/) which uses simple counting, this uses loops for practical generation
- Combines loops with selection logic from Chapter 6 for character type choices
- Uses loops for both password generation and user session management
- Demonstrates nested loops and complex iteration patterns

## 🚀 Getting Started

1. **Open `main.py` in this folder**

2. **Follow the step-by-step approach:**
   - Start by creating a simple password of fixed length
   - Add user input for password requirements
   - Implement character type selection with loops
   - Add password strength analysis
   - Add session management for multiple passwords
   - Test thoroughly with different requirements

3. **Test your project:** `python main.py`

## 💡 Implementation Ideas

### Approach 1: Basic Password Generation Loop
```python
import random
import string

print("=== Smart Password Generator ===")

# Get user requirements
length = int(input("Enter desired password length (8-20): "))

# Character sets
lowercase = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
uppercase = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = string.digits            # '0123456789'
symbols = "!@#$%^&*"

# Build character pool
char_pool = lowercase + uppercase + numbers + symbols

# Generate password using a loop
password = ""
for i in range(length):
    password += random.choice(char_pool)

print(f"Generated Password: {password}")
```

### Approach 2: Customizable Character Selection
```python
# Get user preferences
include_upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
include_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

# Build custom character pool
char_pool = string.ascii_lowercase  # Always include lowercase

if include_upper:
    char_pool += string.ascii_uppercase
if include_numbers:
    char_pool += string.digits
if include_symbols:
    char_pool += "!@#$%^&*"

# Generate password with custom requirements
password = ""
for i in range(length):
    password += random.choice(char_pool)
```

### Approach 3: Password Strength Analysis
```python
def analyze_password_strength(password):
    """Analyze password and return strength rating"""
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 12:
        score += 2
        feedback.append("Good length ✓")
    elif len(password) >= 8:
        score += 1
        feedback.append("Adequate length")
    
    # Check character types using loops
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*" for c in password)
    
    if has_lower: score += 1
    if has_upper: score += 1
    if has_digit: score += 1
    if has_symbol: score += 1
    
    # Determine strength
    if score >= 6:
        return "Very Strong", feedback
    elif score >= 4:
        return "Strong", feedback
    elif score >= 3:
        return "Medium", feedback
    else:
        return "Weak", feedback
```

### Approach 4: Session Management with While Loop
```python
# Main program loop
continue_generating = True
while continue_generating:
    # Generate password (previous code here)
    
    # Ask if user wants another password
    again = input("Generate another password? (yes/no): ").lower()
    if again != "yes":
        continue_generating = False

print("Thank you for using Smart Password Generator!")
```

## ✅ Success Criteria

Your project is successful when:
- [ ] You use a `for` loop to generate passwords character by character
- [ ] You allow users to specify password length and character requirements
- [ ] You use a `while` loop to allow multiple password generation in one session
- [ ] You provide password strength analysis and feedback
- [ ] You handle user input validation appropriately
- [ ] You can generate different types of passwords based on user preferences

## 🎨 Creative Extensions (Optional)

Want to make your password generator even better? Try these ideas:
- Add password memorability options (pronounceable passwords)
- Create different security levels (basic, standard, high, military)
- Add password history to avoid duplicates
- Include estimated crack time calculations
- Add password saving/export functionality
- Create themed passwords (only letters, only numbers, etc.)
- Add password strength visualization (progress bar)

## 🔗 Concepts Applied

This project demonstrates mastery of:
- **Variables** (Chapter 3) → Storing password requirements and generated passwords
- **Operators** (Chapter 4) → String concatenation and logical operations
- **Input/Output** (Chapter 5) → Interactive requirement gathering and feedback
- **Selections** (Chapter 6) → Character type selection and strength analysis
- **Iterations** (Chapter 7) → Password generation loops and session management

## 🎉 What You've Accomplished

By completing this project, you've shown you can:
- Use loops for practical problem-solving (security)
- Combine different types of loops for different purposes
- Create interactive applications with session management
- Apply programming concepts to real-world security needs
- Build user-friendly tools with customizable options

This is a significant step up from simple counting exercises and demonstrates how loops can solve practical problems. You're now ready for the code organization concepts in Chapter 8!

## 🚀 Next Steps

Ready for more? The next project will introduce functions, allowing you to organize your password generation logic into reusable, modular components!