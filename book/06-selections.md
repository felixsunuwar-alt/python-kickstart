# Chapter 06: Selections

## Learning Objectives

By the end of this chapter, you will be able to:
- Use `if` statements to make decisions in your programs
- Apply `elif` and `else` for multiple conditions
- Combine conditions using logical operators
- Understand Python's indentation rules for code blocks
- Create programs that respond differently based on user input

## Introduction

Selections allow programs to make decisions and execute different code based on conditions. This is what makes programs intelligent and responsive. Instead of always doing the same thing, programs can adapt their behavior based on the situation.

Think of selections like a flowchart in real life:
- "If it's raining, take an umbrella"
- "If the temperature is below 0°C, wear a winter coat"
- "If the score is above 90, display 'Excellent'"

## Core Concepts

### Basic if Statement

The `if` statement executes code only when a condition is true:

```python
age = 18
if age >= 18:
    print("You can vote!")
    print("You are an adult.")
```

**Important**: Python uses **indentation** (spaces) to group code blocks. All lines that belong to the `if` statement must be indented the same amount (usually 4 spaces).

### if-else Statement

Use `else` to specify what happens when the condition is false:

```python
age = 16
if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet.")
    print(f"Wait {18 - age} more years.")
```

### if-elif-else Statement

Use `elif` (else if) to check multiple conditions:

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
```

### Comparison Operators in Selections

```python
temperature = 25

if temperature > 30:
    print("It's hot!")
elif temperature >= 20:
    print("It's warm.")
elif temperature >= 10:
    print("It's cool.")
else:
    print("It's cold!")
```

### Logical Operators in Selections

#### AND operator
```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive.")
```

#### OR operator
```python
day = "Saturday"
is_holiday = False

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("No work today!")
else:
    print("Time to work.")
```

#### NOT operator
```python
is_raining = False

if not is_raining:
    print("Great weather for a walk!")
else:
    print("Better stay inside.")
```

### Python's Unique Features

#### Chained Comparisons
```python
score = 85

# Python allows chaining comparisons
if 80 <= score < 90:
    print("Grade B")

# This is equivalent to:
if score >= 80 and score < 90:
    print("Grade B")
```

#### in Operator
```python
day = "Monday"

# Check if value is in a list
if day in ["Saturday", "Sunday"]:
    print("Weekend!")
else:
    print("Weekday")

# Check if character is in string
name = "Alice"
if "A" in name:
    print("Name starts with A")
```

## Practical Applications

### Grade Calculator
```python
print("=== Grade Calculator ===")
score = float(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory"
elif score >= 60:
    grade = "D"
    message = "Needs improvement"
else:
    grade = "F"
    message = "Please study more"

print(f"Grade: {grade}")
print(f"Comment: {message}")
```

### Weather Advisor
```python
print("=== Weather Advisor ===")
temperature = float(input("Enter temperature (°C): "))
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"

print("\nRecommendation:")

if is_raining:
    print("- Take an umbrella")
    print("- Wear waterproof shoes")

if temperature < 0:
    print("- Wear a heavy winter coat")
    print("- Be careful of ice")
elif temperature < 10:
    print("- Wear a warm jacket")
elif temperature < 20:
    print("- A light jacket should be fine")
elif temperature < 30:
    print("- Perfect weather for outdoor activities")
else:
    print("- Stay hydrated and seek shade")
```

### Password Strength Checker
```python
print("=== Password Strength Checker ===")
password = input("Enter a password: ")

length = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)

print(f"\nPassword analysis:")
print(f"Length: {length} characters")

if length >= 12 and has_upper and has_lower and has_digit:
    strength = "Strong"
elif length >= 8 and has_upper and has_lower:
    strength = "Medium"
elif length >= 6:
    strength = "Weak"
else:
    strength = "Very Weak"

print(f"Strength: {strength}")

if strength != "Strong":
    print("\nSuggestions:")
    if length < 8:
        print("- Use at least 8 characters")
    if not has_upper:
        print("- Include uppercase letters")
    if not has_lower:
        print("- Include lowercase letters")
    if not has_digit:
        print("- Include numbers")
```

## Common Mistakes

### Incorrect Indentation
```python
# Wrong - inconsistent indentation
age = 18
if age >= 18:
    print("You can vote!")
  print("You are an adult.")  # Error: inconsistent indentation

# Correct - consistent indentation
if age >= 18:
    print("You can vote!")
    print("You are an adult.")
```

### Using Assignment Instead of Comparison
```python
age = 18

# Wrong - assignment instead of comparison
if age = 18:  # SyntaxError!
    print("Eighteen years old")

# Correct - comparison
if age == 18:
    print("Eighteen years old")
```

### Unreachable Code
```python
score = 85

# Wrong - the elif will never execute
if score >= 80:
    print("Good score!")
elif score >= 85:  # This will never run!
    print("Great score!")

# Correct - most specific condition first
if score >= 85:
    print("Great score!")
elif score >= 80:
    print("Good score!")
```

### Forgetting the Colon
```python
# Wrong - missing colon
if age >= 18  # SyntaxError!
    print("Adult")

# Correct - colon required
if age >= 18:
    print("Adult")
```

## Best Practices

### Use Clear Variable Names
```python
# Poor
if x > 18:
    print("OK")

# Better
if age > 18:
    print("Eligible to vote")
```

### Order Conditions Logically
```python
# Check most specific conditions first
if score >= 95:
    grade = "A+"
elif score >= 90:
    grade = "A"
elif score >= 85:
    grade = "B+"
# ... and so on
```

### Use Meaningful Messages
```python
# Poor
if temperature > 30:
    print("Hot")

# Better
if temperature > 30:
    print("It's quite hot today! Stay hydrated and seek shade.")
```

### Combine Related Conditions
```python
# Instead of multiple separate if statements
if day == "Saturday":
    print("Weekend!")
if day == "Sunday":
    print("Weekend!")

# Use logical operators
if day == "Saturday" or day == "Sunday":
    print("Weekend!")

# Or use the 'in' operator
if day in ["Saturday", "Sunday"]:
    print("Weekend!")
```

## Practice

Try these exercises to practice what you've learned:

1. Create a program that determines if a number is positive, negative, or zero
2. Build a simple calculator that performs different operations based on user choice
3. Make a program that categorizes people into age groups (child, teenager, adult, senior)

## Summary

In this chapter, you learned:
- How to use `if`, `elif`, and `else` statements for decision making
- How to combine conditions with logical operators (`and`, `or`, `not`)
- Python's indentation rules for code blocks
- How to use comparison operators in conditional statements
- Python-specific features like chained comparisons and the `in` operator
- Best practices for writing clear, maintainable conditional code

You're now ready to move on to iterations, where you'll learn how to repeat code efficiently!