#!/usr/bin/env python3
"""
Solution for Exercise 6.1: Grade Calculator
"""

# Get score from user
score = float(input("Enter your score (0-100): "))

# Determine grade and feedback using if/elif/else
if score >= 90:
    grade = "A"
    feedback = "Excellent work! Keep it up!"
elif score >= 80:
    grade = "B"
    feedback = "Good job! You're doing well."
elif score >= 70:
    grade = "C"
    feedback = "Satisfactory work. Keep studying!"
elif score >= 60:
    grade = "D"
    feedback = "You passed, but there's room for improvement."
else:
    grade = "F"
    feedback = "Don't give up! Study more and try again."

# Display results
print(f"Grade: {grade}")
print(f"Feedback: {feedback}")