# Chapter 09: Lists

## Learning Objectives

By the end of this chapter, you will be able to:
- Create and manipulate lists to store collections of data
- Access and modify list elements using indexing
- Use list methods to add, remove, and organize data
- Iterate through lists with loops
- Work with parallel lists for related data
- Apply lists to solve real-world problems

## Introduction

Lists are one of Python's most powerful and versatile data structures. They allow you to store multiple items in a single variable, making it easy to work with collections of related data. Lists are ordered, changeable, and allow duplicate values.

Think of lists like:
- A shopping list with multiple items
- A class roster with student names
- A collection of test scores
- A playlist of songs
- A list of temperatures recorded over a week

## Core Concepts

### Creating Lists

Lists are created using square brackets `[]`:

```python
# Empty list
empty_list = []

# List with initial values
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]

print(fruits)   # Output: ['apple', 'banana', 'orange']
print(numbers)  # Output: [1, 2, 3, 4, 5]
print(mixed)    # Output: ['hello', 42, 3.14, True]
```

### Accessing List Elements

Use indexing to access individual elements (starting from 0):

```python
fruits = ["apple", "banana", "orange", "grape"]

# Positive indexing (from the beginning)
print(fruits[0])   # Output: apple
print(fruits[1])   # Output: banana
print(fruits[3])   # Output: grape

# Negative indexing (from the end)
print(fruits[-1])  # Output: grape (last item)
print(fruits[-2])  # Output: orange (second to last)

# Getting list length
print(len(fruits))  # Output: 4
```

### Modifying Lists

Lists are mutable (changeable):

```python
fruits = ["apple", "banana", "orange"]

# Change an element
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'orange']

# Add elements
fruits.append("grape")  # Add to end
print(fruits)  # Output: ['apple', 'blueberry', 'orange', 'grape']

fruits.insert(1, "kiwi")  # Insert at specific position
print(fruits)  # Output: ['apple', 'kiwi', 'blueberry', 'orange', 'grape']

# Remove elements
fruits.remove("orange")  # Remove by value
print(fruits)  # Output: ['apple', 'kiwi', 'blueberry', 'grape']

removed_item = fruits.pop()  # Remove and return last item
print(f"Removed: {removed_item}")  # Output: Removed: grape
print(fruits)  # Output: ['apple', 'kiwi', 'blueberry']
```

### List Slicing

Extract portions of lists using slicing:

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing [start:end]
print(numbers[2:5])    # Output: [2, 3, 4]
print(numbers[:4])     # Output: [0, 1, 2, 3] (from beginning)
print(numbers[6:])     # Output: [6, 7, 8, 9] (to end)

# Step slicing [start:end:step]
print(numbers[::2])    # Output: [0, 2, 4, 6, 8] (every 2nd element)
print(numbers[1::2])   # Output: [1, 3, 5, 7, 9] (every 2nd, starting at 1)
print(numbers[::-1])   # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)
```

## Essential List Methods

### Adding Elements

```python
shopping_list = ["milk", "bread"]

# append() - add single item to end
shopping_list.append("eggs")
print(shopping_list)  # Output: ['milk', 'bread', 'eggs']

# extend() - add multiple items to end
shopping_list.extend(["butter", "cheese"])
print(shopping_list)  # Output: ['milk', 'bread', 'eggs', 'butter', 'cheese']

# insert() - add item at specific position
shopping_list.insert(0, "apples")  # Insert at beginning
print(shopping_list)  # Output: ['apples', 'milk', 'bread', 'eggs', 'butter', 'cheese']
```

### Removing Elements

```python
items = ["apple", "banana", "orange", "banana", "grape"]

# remove() - remove first occurrence of value
items.remove("banana")
print(items)  # Output: ['apple', 'orange', 'banana', 'grape']

# pop() - remove and return item at index (default: last)
last_item = items.pop()
print(f"Removed: {last_item}")  # Output: Removed: grape
print(items)  # Output: ['apple', 'orange', 'banana']

second_item = items.pop(1)
print(f"Removed: {second_item}")  # Output: Removed: orange
print(items)  # Output: ['apple', 'banana']

# clear() - remove all elements
items.clear()
print(items)  # Output: []
```

### Finding and Counting

```python
numbers = [1, 3, 5, 3, 7, 3, 9]

# count() - count occurrences of value
count_3 = numbers.count(3)
print(f"Number 3 appears {count_3} times")  # Output: Number 3 appears 3 times

# index() - find first index of value
index_5 = numbers.index(5)
print(f"Number 5 is at index {index_5}")  # Output: Number 5 is at index 2

# Check if item exists
if 7 in numbers:
    print("7 is in the list")  # Output: 7 is in the list

if 10 not in numbers:
    print("10 is not in the list")  # Output: 10 is not in the list
```

### Organizing Lists

```python
names = ["Charlie", "Alice", "Bob", "Diana"]
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - sort list in place
names.sort()
print(names)  # Output: ['Alice', 'Bob', 'Charlie', 'Diana']

numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# sort in reverse order
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 6, 5, 4, 3, 2, 1, 1]

# reverse() - reverse the order
names.reverse()
print(names)  # Output: ['Diana', 'Charlie', 'Bob', 'Alice']

# sorted() - return new sorted list (doesn't modify original)
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)
print(f"Original: {original}")      # Output: Original: [3, 1, 4, 1, 5]
print(f"Sorted copy: {sorted_copy}") # Output: Sorted copy: [1, 1, 3, 4, 5]
```

## Lists and Loops

### Iterating Through Lists

```python
fruits = ["apple", "banana", "orange", "grape"]

# Method 1: Direct iteration (most common)
print("Fruits in the basket:")
for fruit in fruits:
    print(f"- {fruit}")

# Method 2: Using index
print("\nFruits with positions:")
for i in range(len(fruits)):
    print(f"{i + 1}. {fruits[i]}")

# Method 3: Using enumerate() for both index and value
print("\nFruits with indices:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

### Processing List Data

```python
# Calculate statistics
test_scores = [85, 92, 78, 96, 88, 91, 84]

total = 0
for score in test_scores:
    total += score

average = total / len(test_scores)
highest = max(test_scores)
lowest = min(test_scores)

print(f"Test Scores: {test_scores}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

# Count items meeting criteria
passing_scores = 0
for score in test_scores:
    if score >= 80:
        passing_scores += 1

print(f"Passing scores (≥80): {passing_scores}")
```

### Building Lists with Loops

```python
# Create list of squares
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)  # Output: [1, 4, 9, 16, 25]

# Filter data into new list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Transform data
names = ["alice", "bob", "charlie"]
capitalized_names = []
for name in names:
    capitalized_names.append(name.capitalize())
print(capitalized_names)  # Output: ['Alice', 'Bob', 'Charlie']
```

## Working with Parallel Lists

Parallel lists store related data at the same indices:

```python
# Student data using parallel lists
students = ["Alice", "Bob", "Charlie", "Diana"]
ages = [20, 19, 21, 20]
grades = [85, 92, 78, 96]

# Display student information
print("Student Information:")
for i in range(len(students)):
    print(f"{students[i]}: Age {ages[i]}, Grade {grades[i]}")

# Find student with highest grade
highest_grade_index = grades.index(max(grades))
best_student = students[highest_grade_index]
best_grade = grades[highest_grade_index]
print(f"\nHighest grade: {best_student} with {best_grade}")

# Calculate average age
total_age = sum(ages)
average_age = total_age / len(ages)
print(f"Average age: {average_age:.1f}")
```

## Practical Applications

### Shopping List Manager

```python
def shopping_list_manager():
    shopping_list = []
    
    while True:
        print("\n=== Shopping List Manager ===")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Clear list")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"Added '{item}' to the list")
            
        elif choice == "2":
            if shopping_list:
                print("Current items:")
                for i, item in enumerate(shopping_list):
                    print(f"{i + 1}. {item}")
                try:
                    index = int(input("Enter item number to remove: ")) - 1
                    if 0 <= index < len(shopping_list):
                        removed = shopping_list.pop(index)
                        print(f"Removed '{removed}' from the list")
                    else:
                        print("Invalid item number")
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("List is empty")
                
        elif choice == "3":
            if shopping_list:
                print("\nYour shopping list:")
                for i, item in enumerate(shopping_list):
                    print(f"{i + 1}. {item}")
            else:
                print("Your shopping list is empty")
                
        elif choice == "4":
            shopping_list.clear()
            print("Shopping list cleared")
            
        elif choice == "5":
            print("Thank you for using Shopping List Manager!")
            break
            
        else:
            print("Invalid choice. Please try again.")

# shopping_list_manager()  # Uncomment to run
```

### Grade Tracker

```python
def grade_tracker():
    subjects = []
    grades = []
    
    def add_grade():
        subject = input("Enter subject: ")
        try:
            grade = float(input("Enter grade (0-100): "))
            if 0 <= grade <= 100:
                subjects.append(subject)
                grades.append(grade)
                print(f"Added {subject}: {grade}")
            else:
                print("Grade must be between 0 and 100")
        except ValueError:
            print("Please enter a valid number")
    
    def view_grades():
        if subjects:
            print("\nYour Grades:")
            for i in range(len(subjects)):
                print(f"{subjects[i]}: {grades[i]}")
        else:
            print("No grades recorded yet")
    
    def calculate_average():
        if grades:
            average = sum(grades) / len(grades)
            print(f"Average grade: {average:.1f}")
            
            if average >= 90:
                print("Excellent work!")
            elif average >= 80:
                print("Good job!")
            elif average >= 70:
                print("Keep it up!")
            else:
                print("You might want to study more")
        else:
            print("No grades to calculate average")
    
    while True:
        print("\n=== Grade Tracker ===")
        print("1. Add grade")
        print("2. View all grades")
        print("3. Calculate average")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_grade()
        elif choice == "2":
            view_grades()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            print("Thank you for using Grade Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

# grade_tracker()  # Uncomment to run
```

### Data Analysis Example

```python
def analyze_sales_data():
    # Sample sales data
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [15000, 18000, 22000, 19000, 25000, 28000]
    
    print("=== Sales Data Analysis ===")
    
    # Display data
    print("\nMonthly Sales:")
    for i in range(len(months)):
        print(f"{months[i]}: ${sales[i]:,}")
    
    # Calculate statistics
    total_sales = sum(sales)
    average_sales = total_sales / len(sales)
    best_month_index = sales.index(max(sales))
    worst_month_index = sales.index(min(sales))
    
    print(f"\nSales Summary:")
    print(f"Total Sales: ${total_sales:,}")
    print(f"Average Monthly Sales: ${average_sales:,.0f}")
    print(f"Best Month: {months[best_month_index]} (${sales[best_month_index]:,})")
    print(f"Worst Month: {months[worst_month_index]} (${sales[worst_month_index]:,})")
    
    # Growth analysis
    print(f"\nGrowth Analysis:")
    for i in range(1, len(sales)):
        growth = sales[i] - sales[i-1]
        growth_percent = (growth / sales[i-1]) * 100
        print(f"{months[i-1]} to {months[i]}: ${growth:,} ({growth_percent:+.1f}%)")

analyze_sales_data()
```

## List Comprehensions (Preview)

Python offers a concise way to create lists:

```python
# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)  # Output: [1, 4, 9, 16, 25]

# List comprehension (more advanced)
squares = [i ** 2 for i in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Filter with list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

## Common Mistakes

### Index Out of Range

```python
fruits = ["apple", "banana", "orange"]

# Wrong - index 3 doesn't exist (only 0, 1, 2)
# print(fruits[3])  # IndexError!

# Correct - check length first
if len(fruits) > 3:
    print(fruits[3])
else:
    print("Index 3 is out of range")
```

### Modifying List While Iterating

```python
numbers = [1, 2, 3, 4, 5]

# Wrong - modifying list while iterating can cause issues
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)  # Problematic!

# Correct - iterate over a copy or use different approach
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]  # Keep odd numbers
print(numbers)  # Output: [1, 3, 5]
```

### Confusing append() and extend()

```python
list1 = [1, 2, 3]
list2 = [4, 5]

# append() adds the entire list as a single element
list1.append(list2)
print(list1)  # Output: [1, 2, 3, [4, 5]]

# extend() adds each element individually
list1 = [1, 2, 3]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5]
```

## Best Practices

### Use Meaningful Names

```python
# Poor
data = [85, 92, 78, 96]

# Good
test_scores = [85, 92, 78, 96]
student_names = ["Alice", "Bob", "Charlie"]
```

### Keep Related Data Together

```python
# Good - using parallel lists for related data
students = ["Alice", "Bob", "Charlie"]
grades = [85, 92, 78]
ages = [20, 19, 21]

# Even better - consider using dictionaries (future topic)
# student_data = [
#     {"name": "Alice", "grade": 85, "age": 20},
#     {"name": "Bob", "grade": 92, "age": 19},
#     {"name": "Charlie", "grade": 78, "age": 21}
# ]
```

### Validate Input When Building Lists

```python
def get_positive_numbers():
    numbers = []
    while True:
        user_input = input("Enter a positive number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            if number > 0:
                numbers.append(number)
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")
    return numbers
```

## Practice

Try these exercises to practice what you've learned:

1. Create a program that manages a playlist of songs
2. Build a simple inventory system using lists
3. Write a program that finds the most common element in a list
4. Create a function that merges two sorted lists into one sorted list

## Summary

In this chapter, you learned:
- How to create and manipulate lists to store collections of data
- How to access and modify list elements using indexing and slicing
- Essential list methods for adding, removing, and organizing data
- How to iterate through lists with loops for data processing
- How to work with parallel lists for managing related information
- Practical applications of lists in real-world programming scenarios

Lists are fundamental to Python programming and essential for managing collections of data. They provide the foundation for more advanced data structures and algorithms.

Congratulations! You've completed the Python Kickstart course and learned all the fundamental concepts needed to start building your own programs. You're now ready to tackle more advanced Python topics and real-world programming challenges!