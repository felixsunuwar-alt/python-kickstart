#!/usr/bin/env python3
"""
Solution for Exercise 5.1: Personal Profile Builder
"""

# Welcome message
print("=== Personal Profile Builder ===")

# Collect user information
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
hobby = input("Enter your favorite hobby: ")

# Calculate birth year
birth_year = 2024 - age

# Display formatted profile
print("\n=== Your Profile ===")
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Height: {height}m")
print(f"Birth Year: {birth_year}")
print(f"Hobby: {hobby}")
print("=" * 19)