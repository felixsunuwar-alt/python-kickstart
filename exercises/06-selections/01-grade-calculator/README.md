# Exercise 1: Grade Calculator

Create a program that converts numeric scores to letter grades with personalized feedback.

## 📖 Before You Start

**⚠️ IMPORTANT: Read Chapter 6 first!**

Before attempting this exercise, make sure you have:
- ✅ Read **Chapter 6: Selections** in the `book/06-selections.md` file
- ✅ Understood how to use `if`, `elif`, and `else` statements
- ✅ Learned about comparison operators in conditions
- ✅ Practiced with logical operators and indentation rules

This exercise will help you practice making decisions in your programs using conditional statements.

## 🎯 Goal

Create a program that takes a numeric score (0-100) and converts it to a letter grade with appropriate feedback messages.

## 📚 What You'll Learn

- How to use `if`, `elif`, and `else` for multiple conditions
- How to structure conditions from most specific to least specific
- How to provide different outputs based on input ranges
- How to combine user input with conditional logic

## 📝 Instructions

1. **Open the file**: Look at the `main.py` file in this folder
2. **Write your code**: Create a grade calculator that:
   - Asks the user for a numeric score (0-100)
   - Converts the score to a letter grade using these ranges:
     - A: 90-100
     - B: 80-89
     - C: 70-79
     - D: 60-69
     - F: 0-59
   - Provides appropriate feedback for each grade level
   - Displays both the letter grade and feedback message
3. **Test your code**: Run your script to see if it works:
   ```bash
   python exercises/06-selections/01-grade-calculator/main.py
   ```
4. **Check with tests**: Run the automated test to verify your solution:
   ```bash
   pytest tests/test_06_selections.py::TestExercise06_01::test_grade_calculator_output -v
   ```

## 💡 Hints

- Use `float(input(...))` to get the score as a number
- Start with the highest grade (A) and work down
- Use `elif` for the middle grades and `else` for the failing grade
- Include encouraging messages for good grades and supportive messages for lower grades
- Make sure your conditions don't overlap

## ✅ Expected Output

When you run your program with different scores, you should see something like:
```
Enter your score (0-100): 85
Grade: B
Feedback: Good job! You're doing well.
```

```
Enter your score (0-100): 95
Grade: A
Feedback: Excellent work! Keep it up!
```

```
Enter your score (0-100): 55
Grade: F
Feedback: Don't give up! Study more and try again.
```

## 🎉 Success!

Once your program works, you've successfully:
- ✅ Used conditional statements to make decisions
- ✅ Implemented multiple conditions with `elif`
- ✅ Created a program that responds differently to different inputs
- ✅ Combined user input with conditional logic

Ready for the next exercise? Great work! 🚀