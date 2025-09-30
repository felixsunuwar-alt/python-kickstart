#!/usr/bin/env python3
"""
Exercise 3: Variable Updates

Write your code below to demonstrate updating variable values.
"""

# Write your code here
score = 0
antal_nivå = 50
for nivå in range(1, antal_nivå + 1):
    score += 15
    print(f"score efter nivå {nivå}:", score)
print("score i slutet", score)
