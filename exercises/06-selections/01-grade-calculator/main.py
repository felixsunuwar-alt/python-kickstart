#!/usr/bin/env python3
"""
Exercise 1: Grade Calculator

Convert numeric scores to letter grades with feedback.
"""

    # Write your code here
    # 1. Ask user for a score (0-100)
    # 2. Convert score to letter grade using if/elif/else:
    #    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
    # 3. Provide appropriate feedback for each grade
    # 4. Display the grade and feedback
number = int(input("skriv in ditt prov resultat 0-100 med siffror"))
if (90 <= number <= 100):
    print("Du har betyg A! ")
    print("Snyggt jobbat")
elif (80 <= number <= 89):
    print("Du har B! " )
    print("bra jobbat, nästa gång blir de A! ")
elif (70 <= number <= 79):
    print("Du har C! " )
    print("king")
elif (60 <= number <= 69):
    print("Du har D! " )
    print("bättre kan du ")
elif (0 <= number <= 50):
    print("Du har F! " )
    print("du suger")
elif (number < 0):
    print("sluta larva dig")
elif (100 < number):
    print("sluta larva dig")
