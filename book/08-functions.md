# Chapter 08: Functions

## Learning Objectives

By the end of this chapter, you will be able to:
- Define your own functions using the `def` keyword
- Use parameters to pass data into functions
- Return values from functions to get results back
- Understand function scope and variable visibility
- Organize code into logical, reusable functions
- Apply functions to solve complex problems

## Introduction

Functions are reusable blocks of code that perform specific tasks. They help you organize your code, avoid repetition, and make programs easier to understand and maintain. Functions are like recipes - they take ingredients (parameters), follow steps (the function body), and produce a result (return value).

Think of functions like:
- A recipe that takes ingredients and produces a dish
- A calculator function that takes numbers and returns a result
- A greeting function that takes a name and returns a personalized message
- A validation function that checks if data is correct

## Core Concepts

### Defining Functions

Use the `def` keyword to create a function:

```python
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
```

### Functions with Parameters

Parameters allow you to pass data into functions:

```python
def greet_person(name):
    print(f"Hello, {name}!")

# Call with different arguments
greet_person("Alice")  # Output: Hello, Alice!
greet_person("Bob")    # Output: Hello, Bob!
```

### Multiple Parameters

Functions can accept multiple parameters:

```python
def calculate_area(length, width):
    area = length * width
    print(f"The area is {area} square units")

calculate_area(5, 3)   # Output: The area is 15 square units
calculate_area(10, 7)  # Output: The area is 70 square units
```

### Return Values

Functions can return values using the `return` keyword:

```python
def add_numbers(a, b):
    result = a + b
    return result

# Store the returned value
sum_result = add_numbers(5, 3)
print(sum_result)  # Output: 8

# Use directly in expressions
total = add_numbers(10, 20) + add_numbers(5, 15)
print(total)  # Output: 50
```

### Functions with Multiple Return Values

Python functions can return multiple values:

```python
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Unpack multiple return values
area, perimeter = calculate_rectangle(5, 3)
print(f"Area: {area}, Perimeter: {perimeter}")
# Output: Area: 15, Perimeter: 16
```

## Function Scope

Variables inside functions have local scope:

```python
def my_function():
    local_variable = "I'm local"
    print(local_variable)

my_function()  # Output: I'm local
# print(local_variable)  # Error! Variable not accessible outside function

# Global vs Local variables
global_variable = "I'm global"

def scope_example():
    local_variable = "I'm local"
    print(f"Inside function: {global_variable}")  # Can access global
    print(f"Inside function: {local_variable}")

scope_example()
print(f"Outside function: {global_variable}")  # Can access global
# print(f"Outside function: {local_variable}")  # Error! Local not accessible
```

## Practical Applications

### Mathematical Functions

```python
def calculate_bmi(weight, height):
    """Calculate Body Mass Index"""
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Determine BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Using the functions together
weight = 70  # kg
height = 1.75  # meters

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"BMI: {bmi:.1f}")
print(f"Category: {category}")
```

### Input Validation Functions

```python
def get_positive_number(prompt):
    """Get a positive number from user with validation"""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

def get_yes_no(prompt):
    """Get yes/no input from user"""
    while True:
        response = input(prompt).lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

# Using validation functions
age = get_positive_number("Enter your age: ")
has_license = get_yes_no("Do you have a driver's license? (yes/no): ")

if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive yet.")
```

### Text Processing Functions

```python
def count_words(text):
    """Count the number of words in text"""
    words = text.split()
    return len(words)

def count_vowels(text):
    """Count vowels in text"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def analyze_text(text):
    """Provide comprehensive text analysis"""
    word_count = count_words(text)
    vowel_count = count_vowels(text)
    char_count = len(text)
    
    return {
        'words': word_count,
        'characters': char_count,
        'vowels': vowel_count
    }

# Using text functions
sample_text = "Python programming is fun and powerful"
analysis = analyze_text(sample_text)

print(f"Text: '{sample_text}'")
print(f"Words: {analysis['words']}")
print(f"Characters: {analysis['characters']}")
print(f"Vowels: {analysis['vowels']}")
```

## Default Parameters

Functions can have default parameter values:

```python
def greet_with_title(name, title="Mr./Ms."):
    return f"Hello, {title} {name}!"

# Using default parameter
print(greet_with_title("Smith"))  # Output: Hello, Mr./Ms. Smith!

# Overriding default parameter
print(greet_with_title("Smith", "Dr."))  # Output: Hello, Dr. Smith!

def calculate_power(base, exponent=2):
    """Calculate base raised to exponent (default: square)"""
    return base ** exponent

print(calculate_power(5))     # Output: 25 (5^2)
print(calculate_power(5, 3))  # Output: 125 (5^3)
```

## Docstrings

Document your functions with docstrings:

```python
def calculate_compound_interest(principal, rate, time, compounds_per_year=12):
    """
    Calculate compound interest.
    
    Parameters:
    principal (float): Initial amount of money
    rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
    time (float): Time in years
    compounds_per_year (int): Number of times interest compounds per year
    
    Returns:
    float: Final amount after compound interest
    """
    amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * time)
    return amount

# Using the function
initial = 1000
final = calculate_compound_interest(initial, 0.05, 5)
print(f"${initial} becomes ${final:.2f} after 5 years at 5% interest")
```

## Function Organization Patterns

### Helper Functions

```python
def is_prime(number):
    """Check if a number is prime"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a range"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):  # Using helper function
            primes.append(num)
    return primes

# Using organized functions
prime_numbers = find_primes_in_range(1, 20)
print(f"Prime numbers from 1 to 20: {prime_numbers}")
```

### Menu-Driven Programs

```python
def show_menu():
    """Display the main menu"""
    print("\n=== Calculator Menu ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def get_numbers():
    """Get two numbers from user"""
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def calculator():
    """Main calculator program"""
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        elif choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()
            
            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} × {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} ÷ {num2} = {result}")
        else:
            print("Invalid choice. Please try again.")

# Run the calculator
# calculator()  # Uncomment to run
```

## Common Mistakes

### Forgetting to Return Values

```python
# Wrong - function doesn't return anything
def add_wrong(a, b):
    result = a + b
    print(result)  # Only prints, doesn't return

# Correct - function returns the result
def add_correct(a, b):
    result = a + b
    return result

# Usage difference
value1 = add_wrong(5, 3)    # value1 is None
value2 = add_correct(5, 3)  # value2 is 8
```

### Modifying Global Variables

```python
# Problematic - modifying global variable
counter = 0

def increment_global():
    global counter  # Avoid this when possible
    counter += 1

# Better - return new value
def increment_local(value):
    return value + 1

# Usage
counter = increment_local(counter)  # Clear and predictable
```

### Not Using Parameters

```python
# Poor - hardcoded values
def calculate_circle_area_bad():
    radius = 5  # Hardcoded!
    area = 3.14159 * radius ** 2
    return area

# Good - parameterized
def calculate_circle_area_good(radius):
    area = 3.14159 * radius ** 2
    return area

# Usage
area1 = calculate_circle_area_good(5)
area2 = calculate_circle_area_good(10)  # Reusable!
```

## Best Practices

### Single Responsibility

```python
# Good - each function has one clear purpose
def calculate_tax(income, tax_rate):
    """Calculate tax amount"""
    return income * tax_rate

def calculate_net_income(gross_income, tax_amount):
    """Calculate income after tax"""
    return gross_income - tax_amount

def format_currency(amount):
    """Format amount as currency"""
    return f"${amount:,.2f}"

# Usage
gross = 50000
tax = calculate_tax(gross, 0.25)
net = calculate_net_income(gross, tax)

print(f"Gross Income: {format_currency(gross)}")
print(f"Tax: {format_currency(tax)}")
print(f"Net Income: {format_currency(net)}")
```

### Meaningful Names

```python
# Poor function names
def calc(x, y):  # What does this calculate?
    return x * y

def process(data):  # What kind of processing?
    return data.upper()

# Good function names
def calculate_area(length, width):
    return length * width

def convert_to_uppercase(text):
    return text.upper()
```

### Input Validation

```python
def safe_divide(dividend, divisor):
    """Safely divide two numbers with error handling"""
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        return "Error: Both arguments must be numbers"
    
    if divisor == 0:
        return "Error: Cannot divide by zero"
    
    return dividend / divisor

# Usage
print(safe_divide(10, 2))    # Output: 5.0
print(safe_divide(10, 0))    # Output: Error: Cannot divide by zero
print(safe_divide(10, "2"))  # Output: Error: Both arguments must be numbers
```

## Practice

Try these exercises to practice what you've learned:

1. Create a function that converts temperature between Celsius and Fahrenheit
2. Write a function that checks if a password meets security requirements
3. Build a function that calculates the factorial of a number
4. Create a function that finds the largest number in a list of numbers

## Summary

In this chapter, you learned:
- How to define functions using `def` and call them
- How to use parameters to pass data into functions
- How to return values from functions to get results back
- How function scope works and why it matters
- How to organize code using functions for better structure
- Best practices for writing clean, reusable functions

Functions are essential for writing organized, maintainable code. They help you break complex problems into smaller, manageable pieces and avoid code repetition.

You're now ready to move on to lists, where you'll learn how to work with collections of data!