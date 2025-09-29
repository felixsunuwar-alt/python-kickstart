# Exercise 1: Times Table Generator

Create a program that generates and displays multiplication tables using loops.

## 📖 Before You Start

**⚠️ IMPORTANT: Read Chapter 7 first!**

Before attempting this exercise, make sure you have:
- ✅ Read **Chapter 7: Iterations** in the `book/07-iterations.md` file
- ✅ Understood how to use `for` loops with `range()`
- ✅ Learned about loop variables and iteration
- ✅ Practiced with nested loops and formatting output

This exercise will help you practice using loops to generate patterns and perform repeated calculations.

## 🎯 Goal

Create a program that asks the user for a number and generates its multiplication table from 1 to 10.

## 📚 What You'll Learn

- How to use `for` loops to repeat calculations
- How to work with the `range()` function
- How to format output in a readable table format
- How to combine user input with loop iterations

## 📝 Instructions

1. **Open the file**: Look at the `main.py` file in this folder
2. **Write your code**: Create a times table generator that:
   - Asks the user for a number
   - Uses a `for` loop to generate the multiplication table
   - Displays each multiplication from 1 to 10
   - Formats the output clearly (e.g., "5 × 3 = 15")
3. **Test your code**: Run your script to see if it works:
   ```bash
   python exercises/07-iterations/01-times-table/main.py
   ```
4. **Check with tests**: Run the automated test to verify your solution:
   ```bash
   pytest tests/test_07_iterations.py::TestExercise07_01::test_times_table_output -v
   ```

## 💡 Hints

- Use `int(input(...))` to get the number from the user
- Use `for i in range(1, 11):` to loop from 1 to 10
- Use f-strings for clean formatting: `f"{number} × {i} = {result}"`
- Calculate the result inside the loop: `result = number * i`
- Print each line of the table inside the loop

## ✅ Expected Output

When you run your program with the number 5, you should see:
```
Enter a number: 5
=== Times Table for 5 ===
5 × 1 = 5
5 × 2 = 10
5 × 3 = 15
5 × 4 = 20
5 × 5 = 25
5 × 6 = 30
5 × 7 = 35
5 × 8 = 40
5 × 9 = 45
5 × 10 = 50
```

## 🎉 Success!

Once your program works, you've successfully:
- ✅ Used a `for` loop to repeat code
- ✅ Worked with the `range()` function
- ✅ Combined user input with loop iterations
- ✅ Formatted output in a clear, readable way

Ready for the next exercise? Great work! 🚀