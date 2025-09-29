# Chapter 04: Operators

## Learning Objectives

By the end of this chapter, you will be able to:
- Use arithmetic operators to perform mathematical calculations
- Apply comparison operators to compare values
- Combine conditions using logical operators
- Understand operator precedence and use parentheses effectively
- Work with Python's unique operators like `//` and `**`

## Introduction

Operators are symbols that perform operations on values (called operands). Think of them as tools that help you manipulate data in your programs. Python provides several types of operators that make it easy to perform calculations, comparisons, and logical operations.

## Core Concepts

### Arithmetic Operators

Python provides all the standard arithmetic operators plus some unique ones:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `15 / 3` | `5.0` |
| `//` | Floor Division | `15 // 4` | `3` |
| `%` | Modulus (remainder) | `15 % 4` | `3` |
| `**` | Exponentiation | `2 ** 3` | `8` |

#### Basic Arithmetic Examples

```python
# Basic operations
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333333333333335
print(a // b)   # 3 (floor division - rounds down)
print(a % b)    # 1 (remainder)
print(a ** b)   # 1000 (10 to the power of 3)
```

#### Python's Unique Operators

**Floor Division (`//`)**: Returns the largest integer less than or equal to the result
```python
print(15 / 4)   # 3.75 (regular division)
print(15 // 4)  # 3 (floor division)
print(-15 // 4) # -4 (rounds down, not towards zero)
```

**Exponentiation (`**`)**: Raises a number to a power
```python
print(2 ** 3)   # 8 (2 cubed)
print(9 ** 0.5) # 3.0 (square root of 9)
print(27 ** (1/3)) # 3.0 (cube root of 27)
```

### Comparison Operators

Comparison operators compare two values and return `True` or `False`:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `3 <= 5` | `True` |

#### Comparison Examples

```python
age = 18
minimum_age = 18

print(age == minimum_age)  # True
print(age > minimum_age)   # False
print(age >= minimum_age)  # True

# Comparing strings
name1 = "Alice"
name2 = "Bob"
print(name1 == name2)      # False
print(name1 < name2)       # True (alphabetical order)
```

### Logical Operators

Logical operators combine multiple conditions:

| Operator | Name | Description | Example |
|----------|------|-------------|---------|
| `and` | AND | Both conditions must be true | `True and True` → `True` |
| `or` | OR | At least one condition must be true | `True or False` → `True` |
| `not` | NOT | Flips true to false (and vice versa) | `not True` → `False` |

#### Logical Operator Examples

```python
# AND operator
age = 20
has_license = True
can_drive = age >= 18 and has_license
print(can_drive)  # True

# OR operator
is_weekend = True
is_holiday = False
can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)  # True

# NOT operator
is_raining = False
is_sunny = not is_raining
print(is_sunny)  # True
```

### Operator Precedence

Python follows a specific order when evaluating expressions with multiple operators:

1. **Parentheses** `()` - Highest priority
2. **Exponentiation** `**`
3. **Unary operators** `+x`, `-x`, `not x`
4. **Multiplication, Division, Floor Division, Modulus** `*`, `/`, `//`, `%`
5. **Addition, Subtraction** `+`, `-`
6. **Comparison operators** `<`, `<=`, `>`, `>=`, `!=`, `==`
7. **Logical NOT** `not`
8. **Logical AND** `and`
9. **Logical OR** `or` - Lowest priority

#### Precedence Examples

```python
# Without parentheses
result1 = 2 + 3 * 4        # 14 (not 20)
result2 = 10 > 5 and 3 < 7 # True

# With parentheses to change order
result3 = (2 + 3) * 4      # 20
result4 = 2 ** 3 * 4       # 32 (2^3 = 8, then 8*4 = 32)
```

### Practical Applications

#### BMI Calculator Example
```python
# Calculate Body Mass Index
weight = 70  # kg
height = 1.75  # meters

bmi = weight / (height ** 2)
print(f"BMI: {bmi:.1f}")

# Categorize BMI
is_underweight = bmi < 18.5
is_normal = bmi >= 18.5 and bmi < 25
is_overweight = bmi >= 25 and bmi < 30
is_obese = bmi >= 30

print(f"Underweight: {is_underweight}")
print(f"Normal weight: {is_normal}")
print(f"Overweight: {is_overweight}")
print(f"Obese: {is_obese}")
```

#### Temperature Converter
```python
# Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Check if temperature is comfortable
is_comfortable = fahrenheit >= 68 and fahrenheit <= 78
print(f"Comfortable temperature: {is_comfortable}")
```

## Common Mistakes

### Using `=` Instead of `==`
```python
# Wrong - assignment instead of comparison
age = 18
if age = 18:  # SyntaxError!
    print("You can vote!")

# Correct - comparison
if age == 18:
    print("You can vote!")
```

### Forgetting Operator Precedence
```python
# Confusing
result = 5 + 3 * 2  # Is this 16 or 11?

# Clear
result1 = 5 + (3 * 2)  # 11 (multiplication first)
result2 = (5 + 3) * 2  # 16 (addition first)
```

### Integer vs Float Division
```python
# In Python 3, / always returns float
print(10 / 3)   # 3.3333333333333335
print(10 // 3)  # 3 (integer result)

# Be aware of the difference
minutes = 150
hours = minutes / 60    # 2.5 (float)
full_hours = minutes // 60  # 2 (integer)
```

## Practice

Try these exercises to practice what you've learned:

1. Create a program that calculates the area and perimeter of a rectangle
2. Write a program that determines if a year is a leap year
3. Build a simple tip calculator that calculates tip and total bill

## Summary

In this chapter, you learned:
- Arithmetic operators including Python's unique `//` and `**` operators
- Comparison operators for comparing values
- Logical operators for combining conditions
- Operator precedence and the importance of parentheses
- Practical applications of operators in real-world calculations

You're now ready to move on to input and output, where you'll learn how to make your programs interactive!