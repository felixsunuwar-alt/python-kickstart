# Chapter 03: Variables and Data Types

## Learning Objectives

By the end of this chapter, you will be able to:
- Create and use variables to store data
- Understand different data types (integers, floats, strings, booleans)
- Assign values to variables
- Print variable values
- Change variable values

## Introduction

Variables are like labeled boxes where you can store information. Instead of repeating the same value, you can store it in a variable and reuse it throughout your program.

Python has several basic data types:
- **Integers** (int): Whole numbers like 42, -5, 0
- **Floats** (float): Decimal numbers like 3.14, -2.5
- **Strings** (str): Text like "Hello", "Python"
- **Booleans** (bool): True or False values

## Core Concepts

### Creating Variables

Use the assignment operator `=` to create a variable:

```python
age = 25
name = "Anna"
height = 1.75
is_student = True
```

### Variable Names

Variable names should be descriptive and follow these rules:
- Start with a letter or underscore
- Contain only letters, numbers, and underscores
- Be lowercase with underscores (snake_case)
- Be meaningful: `user_age` not `x`

```python
# Good variable names
student_name = "Maria"
total_score = 95
is_passed = True

# Avoid these
s = "Maria"        # Too short
totalScore = 95    # camelCase (not Python style)
1st_score = 95     # Starts with number
```

### Data Types

#### Integers (int)
Whole numbers without decimal points:

```python
apples = 5
temperature = -10
year = 2024
```

#### Floats (float)
Numbers with decimal points:

```python
pi = 3.14159
price = 19.99
weight = 65.5
```

#### Strings (str)
Text enclosed in quotation marks:

```python
message = "Hello, World!"
name = 'Python'
empty_string = ""
```

#### Booleans (bool)
True or False values:

```python
is_raining = True
has_passed = False
is_adult = age >= 18
```

### Printing Variables

Use `print()` to display variable values:

```python
name = "Anna"
age = 25

print(name)        # Output: Anna
print(age)         # Output: 25
print(name, age)   # Output: Anna 25
```

### Changing Variable Values

Variables can be updated:

```python
score = 10
print(score)  # Output: 10

score = 15    # Update the value
print(score)  # Output: 15
```

## Common Mistakes

### Wrong Variable Names

```python
2players = "Anna"    # ❌ Starts with number
my-name = "John"     # ❌ Contains hyphen
class = "Math"       # ❌ Reserved word
```

### Type Confusion

```python
age = "25"           # String, not number
count = 5.0          # Float, not integer

```

### Forgetting Assignment

```python
print(name)          # ❌ Error: name not defined
name = "Anna"        # Variable must be created first
print(name)          # ✅ Now it works
```

### Case Sensitivity

```python
Name = "Anna"
print(name)          # ❌ Error: name vs Name
```

## Practice

Create programs using variables:

1. Store your name, age, and favorite color in variables and print them
2. Create variables for a rectangle's width and height, then calculate the area
3. Store True/False values for different conditions (like "is_weekend", "has_homework")

## Summary

In this chapter, you learned:
- Variables store data for reuse
- Python has four main data types: int, float, str, bool
- Variable names should be descriptive and follow snake_case
- Variables can be updated with new values
- Use `print()` to display variable contents

Variables are essential for writing useful programs. In the next chapter, we'll learn about operators to perform calculations and comparisons.