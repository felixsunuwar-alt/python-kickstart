# Chapter 07: Iterations

## Learning Objectives

By the end of this chapter, you will be able to:
- Use `for` loops to repeat code a specific number of times
- Use `while` loops to repeat code while a condition is true
- Understand Python's `range()` function for generating sequences
- Apply loops to solve practical problems
- Use `break` and `continue` to control loop execution

## Introduction

Iterations (loops) allow programs to repeat code efficiently. Instead of writing the same code multiple times, you can use loops to execute code repeatedly. This is essential for processing lists of data, performing calculations, and creating interactive programs.

Think of iterations like:
- Counting from 1 to 100
- Processing each item in a shopping list
- Asking for user input until they enter "quit"
- Calculating the sum of all numbers in a list

## Core Concepts

### For Loops with range()

The `for` loop is perfect when you know how many times you want to repeat something:

```python
# Print numbers 1 to 5
for i in range(1, 6):
    print(i)
```

#### Understanding range()

```python
# range(stop) - starts at 0, goes to stop-1
for i in range(5):
    print(i)  # Prints: 0, 1, 2, 3, 4

# range(start, stop) - starts at start, goes to stop-1
for i in range(1, 6):
    print(i)  # Prints: 1, 2, 3, 4, 5

# range(start, stop, step) - with custom step
for i in range(0, 10, 2):
    print(i)  # Prints: 0, 2, 4, 6, 8

# Counting backwards
for i in range(10, 0, -1):
    print(i)  # Prints: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### For Loops with Lists

```python
# Loop through a list of items
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop through characters in a string
name = "Python"
for letter in name:
    print(letter)
```

### While Loops

Use `while` loops when you don't know exactly how many times to repeat:

```python
# Count down from 5
count = 5
while count > 0:
    print(count)
    count = count - 1  # or count -= 1
print("Blast off!")
```

#### While Loop with User Input

```python
# Keep asking until user enters "quit"
user_input = ""
while user_input != "quit":
    user_input = input("Enter a command (or 'quit' to exit): ")
    if user_input != "quit":
        print(f"You entered: {user_input}")
```

### Loop Control: break and continue

#### break - Exit the loop early
```python
# Find the first even number
for i in range(1, 10):
    if i % 2 == 0:
        print(f"First even number: {i}")
        break  # Exit the loop
```

#### continue - Skip to next iteration
```python
# Print only odd numbers
for i in range(1, 10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Only prints odd numbers
```

## Practical Applications

### Multiplication Table
```python
print("=== Multiplication Table ===")
number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")
```

### Password Attempts
```python
print("=== Login System ===")
correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    attempts += 1
    
    if password == correct_password:
        print("Login successful!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts remaining.")
        else:
            print("Too many failed attempts. Account locked.")
```

### Number Guessing Game
```python
import random

print("=== Number Guessing Game ===")
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
```

### Sum Calculator
```python
print("=== Sum Calculator ===")
total = 0
count = 0

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    
    if user_input.lower() == "done":
        break
    
    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Please enter a valid number or 'done'.")

if count > 0:
    average = total / count
    print(f"Sum: {total}")
    print(f"Count: {count}")
    print(f"Average: {average:.2f}")
else:
    print("No numbers entered.")
```

### Pattern Generator
```python
print("=== Pattern Generator ===")
size = int(input("Enter pattern size: "))

# Triangle pattern
print("\nTriangle:")
for i in range(1, size + 1):
    print("*" * i)

# Square pattern
print(f"\nSquare:")
for i in range(size):
    print("*" * size)

# Countdown pattern
print(f"\nCountdown:")
for i in range(size, 0, -1):
    print("*" * i)
```

## Python's Unique Loop Features

### enumerate() - Get index and value
```python
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: orange
```

### zip() - Loop through multiple lists
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### List Comprehensions (Preview)
```python
# Create a list of squares
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]
```

## Common Mistakes

### Infinite Loops
```python
# Wrong - infinite loop!
count = 5
while count > 0:
    print(count)
    # Forgot to decrease count!

# Correct - loop will end
count = 5
while count > 0:
    print(count)
    count -= 1
```

### Off-by-One Errors
```python
# Wrong - prints 0 to 9 (10 numbers)
for i in range(10):
    print(i)

# If you want 1 to 10 (10 numbers)
for i in range(1, 11):
    print(i)
```

### Modifying List While Looping
```python
numbers = [1, 2, 3, 4, 5]

# Wrong - can cause issues
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Don't modify list while looping

# Better - create new list or loop backwards
numbers = [num for num in numbers if num % 2 != 0]
```

### Using Wrong Loop Type
```python
# Inefficient - using while when for is better
i = 0
while i < 10:
    print(i)
    i += 1

# Better - use for loop for known iterations
for i in range(10):
    print(i)
```

## Best Practices

### Choose the Right Loop Type
```python
# Use for loop when you know the number of iterations
for i in range(10):
    print(i)

# Use while loop when condition-based
while user_input != "quit":
    user_input = input("Command: ")
```

### Use Descriptive Variable Names
```python
# Poor
for i in range(len(students)):
    print(students[i])

# Better
for student in students:
    print(student)

# Or if you need the index
for index, student in enumerate(students):
    print(f"{index}: {student}")
```

### Avoid Deep Nesting
```python
# Hard to read
for i in range(10):
    for j in range(10):
        for k in range(10):
            if i + j + k == 15:
                print(f"{i}, {j}, {k}")

# Better - break into functions or use different approach
```

## Practice

Try these exercises to practice what you've learned:

1. Create a program that prints the times tables for any number
2. Build a simple menu system that keeps running until the user chooses to exit
3. Make a program that finds all prime numbers up to a given number

## Summary

In this chapter, you learned:
- How to use `for` loops with `range()` for counted iterations
- How to use `while` loops for condition-based iterations
- How to control loop execution with `break` and `continue`
- Python-specific features like `enumerate()` and `zip()`
- How to choose the right loop type for different situations
- Common mistakes to avoid when working with loops

You now have all the fundamental programming concepts needed to build more complex programs!