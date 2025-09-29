#!/usr/bin/env python3
"""
Solution for Exercise 7.1: Times Table Generator
"""

# Get number from user
number = int(input("Enter a number: "))

# Print header
print(f"=== Times Table for {number} ===")

# Generate times table using for loop
for i in range(1, 11):
    result = number * i
    print(f"{number} × {i} = {result}")