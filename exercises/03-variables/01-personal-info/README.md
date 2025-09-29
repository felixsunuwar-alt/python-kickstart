# Exercise 1: Personal Information

Store and display personal information using variables of different data types.

## 📖 Before You Start

**⚠️ IMPORTANT: Read Chapter 3 first!**

Before attempting this exercise, make sure you have:
- ✅ Read **Chapter 3: Variables and Data Types** in the `book/03-variables.md` file
- ✅ Completed the Chapter 1 and 2 exercises

## 🎯 Goal

Create a program that stores your personal information in variables and prints them with descriptive labels.

## 📚 What You'll Learn

- How to create variables with different data types
- How to use appropriate data types (str, int, float, bool)
- How to print variable values with labels

## 📝 Instructions

1. **Open the file**: Look at the `main.py` file in this folder
2. **Write your code**: Create variables for name, age, height, and student status
3. **Test your code**: Run your script to see if it works:
   ```bash
   python exercises/03-variables/01-personal-info/main.py
   ```
4. **Check with tests**: Run the automated test to verify your solution:
   ```bash
   pytest tests/test_03_variables.py::TestExercise03_01::test_variables_exist_and_correct_types
   ```

## 💡 Hints

- Use `str` for text, `int` for whole numbers, `float` for decimals, `bool` for True/False
- Print with labels like "Name:", "Age:", etc.
- Use meaningful variable names

## ✅ Expected Output

When you run your program, you should see:
```
Name: Anna
Age: 25
Height: 1.75
Is student: True
```

## 🎉 Success!

Once your program works, you've successfully:
- ✅ Created variables with different data types
- ✅ Used appropriate types for different kinds of data
- ✅ Printed formatted output with labels

Great work with variables! 🚀