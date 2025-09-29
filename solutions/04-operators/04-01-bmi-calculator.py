#!/usr/bin/env python3
"""
Solution for Exercise 4.1: BMI Calculator
"""

# Store weight and height
weight = 70  # kg
height = 1.75  # meters

# Calculate BMI using the formula: weight / (height ** 2)
bmi = weight / (height ** 2)

# Determine category using comparison operators
if bmi < 18.5:
    category = "Underweight"
elif bmi >= 18.5 and bmi < 25:
    category = "Normal weight"
elif bmi >= 25 and bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Print the results
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.1f}")
print(f"Category: {category}")