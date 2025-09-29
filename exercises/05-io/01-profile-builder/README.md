# Exercise 1: Personal Profile Builder

Create an interactive program that collects user information and displays a formatted profile.

## 📖 Before You Start

**⚠️ IMPORTANT: Read Chapter 5 first!**

Before attempting this exercise, make sure you have:
- ✅ Read **Chapter 5: Input and Output** in the `book/05-io.md` file
- ✅ Understood how to use `input()` to get user input
- ✅ Learned about type conversion with `int()` and `float()`
- ✅ Practiced with f-string formatting for output

This exercise will help you practice creating interactive programs with clean, formatted output.

## 🎯 Goal

Create a program that asks the user for personal information and displays it in a nicely formatted profile card.

## 📚 What You'll Learn

- How to use `input()` to collect different types of information
- How to convert string input to numbers when needed
- How to use f-strings for professional-looking output
- How to organize output with formatting and spacing

## 📝 Instructions

1. **Open the file**: Look at the `main.py` file in this folder
2. **Write your code**: Create a profile builder that:
   - Asks for the user's name, age, height (in meters), and favorite hobby
   - Converts numeric inputs to appropriate types
   - Calculates additional information (like birth year)
   - Displays all information in a formatted profile card
3. **Test your code**: Run your script to see if it works:
   ```bash
   python exercises/05-io/01-profile-builder/main.py
   ```
4. **Check with tests**: Run the automated test to verify your solution:
   ```bash
   pytest tests/test_05_io.py::TestExercise05_01::test_profile_builder_output -v
   ```

## 💡 Hints

- Use clear, friendly prompts like "Enter your full name: "
- Convert age to integer: `int(input("..."))`
- Convert height to float: `float(input("..."))`
- Calculate birth year: `2024 - age` (or use current year)
- Use f-strings for clean output: `f"Name: {name}"`
- Add spacing and formatting to make output look professional

## ✅ Expected Output

When you run your program, it should look something like:
```
=== Personal Profile Builder ===
Enter your full name: Alice Johnson
Enter your age: 25
Enter your height in meters: 1.68
Enter your favorite hobby: Photography

=== Your Profile ===
Name: Alice Johnson
Age: 25 years old
Height: 1.68m
Birth Year: 1999
Hobby: Photography
===================
```

## 🎉 Success!

Once your program works, you've successfully:
- ✅ Used `input()` to collect user information
- ✅ Converted strings to numbers when needed
- ✅ Used f-strings for formatted output
- ✅ Created an interactive, user-friendly program

Ready for the next exercise? Great work! 🚀