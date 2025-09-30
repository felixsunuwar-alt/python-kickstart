#!/usr/bin/env python3
"""
Exercise 1: Personal Profile Builder

Create an interactive program that collects user information 
and displays a formatted profile.
"""

# Write your code here
# 1. Print a welcome message
# 2. Ask for name, age, height, and hobby using input()
# 3. Convert age to int and height to float
# 4. Calculate birth year (2024 - age)
# 5. Display formatted profile using f-stri
import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("välkomen")

name = input("vad är ditt namn? ")
clear()
age = int(input("hur gammal är du? "))
clear()
height = float(input("hur lång är du? "))
clear()
hobby = input("vad är din hobby? ")
clear()
birth_year = 2025 - age 
f
print(f"hej {name}!")
print(f"du är {height}m lång!")
print(f"du föddes {birth_year}")
print(f"och jag gillar också {hobby}")


