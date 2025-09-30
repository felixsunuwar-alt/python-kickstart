#!/usr/bin/env python3
"""
Exercise 1: BMI Calculator

Calculate BMI and determine health category using operators.
"""

# Write your code here
# 1. Store weight (kg) and height (m) in variables
# 2. Calculate BMI using: weight / (height ** 2)
# 3. Determine category using comparison operators
# 4. Print weight, height, BMI, and category
vikt = 90000000000000000000000000000000000000
längd = 1.7

bmi = (vikt / (längd**2))

print(bmi)

if (bmi <= 18.5):
    print(" du är smal/ undervikt")
elif (bmi <= 25):
    print("du är normakl vikt")
elif (bmi <= 30):
    print("du är överviktig")
else: 
    print("du är obese")
