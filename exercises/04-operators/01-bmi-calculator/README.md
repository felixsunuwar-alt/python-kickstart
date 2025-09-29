# Exercise 1: BMI Calculator

Calculate Body Mass Index (BMI) and categorize the result using operators.

## 📖 Before You Start

**⚠️ IMPORTANT: Read Chapter 4 first!**

Before attempting this exercise, make sure you have:
- ✅ Read **Chapter 4: Operators** in the `book/04-operators.md` file
- ✅ Understood arithmetic operators (`+`, `-`, `*`, `/`, `**`)
- ✅ Learned about comparison operators (`>`, `<`, `>=`, `<=`, `==`, `!=`)
- ✅ Practiced with logical operators (`and`, `or`, `not`)

This exercise will help you practice using operators in a real-world health calculation.

## 🎯 Goal

Create a program that calculates BMI (Body Mass Index) and determines the health category using Python operators.

## 📚 What You'll Learn

- How to use arithmetic operators for calculations
- How to apply comparison and logical operators for categorization
- Working with exponentiation (`**`) operator
- Combining multiple operators in expressions

## 📝 Instructions

1. **Open the file**: Look at the `main.py` file in this folder
2. **Write your code**: Create a BMI calculator that:
   - Stores weight (in kg) and height (in meters) in variables
   - Calculates BMI using the formula: `weight / (height ** 2)`
   - Determines if the BMI indicates underweight, normal, overweight, or obese
   - Prints the BMI value and category
3. **Test your code**: Run your script to see if it works:
   ```bash
   python exercises/04-operators/01-bmi-calculator/main.py
   ```
4. **Check with tests**: Run the automated test to verify your solution:
   ```bash
   pytest tests/test_04_operators.py::TestExercise04_01::test_bmi_calculator_output -v
   ```

## 💡 Hints

- BMI formula: `weight / (height ** 2)`
- BMI categories:
  - Underweight: BMI < 18.5
  - Normal weight: 18.5 ≤ BMI < 25
  - Overweight: 25 ≤ BMI < 30
  - Obese: BMI ≥ 30
- Use comparison operators to check ranges
- Use logical operators (`and`) to check if BMI is between two values

## ✅ Expected Output

When you run your program with weight=70kg and height=1.75m, you should see something like:
```
Weight: 70 kg
Height: 1.75 m
BMI: 22.9
Category: Normal weight
```

## 🎉 Success!

Once your program works, you've successfully:
- ✅ Used arithmetic operators for calculations
- ✅ Applied the exponentiation operator (`**`)
- ✅ Used comparison operators for categorization
- ✅ Combined operators in practical expressions

Ready for the next exercise? Great work! 🚀