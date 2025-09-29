# Exercise 1: Area Calculator Functions

Create a program that uses functions to calculate areas of different shapes.

## 📖 Before You Start

**⚠️ IMPORTANT: Read Chapter 8 first!**

Before attempting this exercise, make sure you have:
- ✅ Read **Chapter 8: Functions** in the `book/08-functions.md` file
- ✅ Understood how to define functions with `def`
- ✅ Learned about parameters and return values
- ✅ Practiced calling functions and using their results

This exercise will help you practice creating reusable functions for mathematical calculations.

## 🎯 Goal

Create a program that defines functions to calculate the area of rectangles, circles, and triangles, then uses these functions to solve area problems.

## 📚 What You'll Learn

- How to define functions with parameters
- How to return values from functions
- How to call functions and use their results
- How to organize code using functions

## 📝 Instructions

1. **Open the file**: Look at the `main.py` file in this folder
2. **Write your code**: Create area calculator functions that:
   - Define a function `calculate_rectangle_area(length, width)` that returns the area
   - Define a function `calculate_circle_area(radius)` that returns the area (use π ≈ 3.14159)
   - Define a function `calculate_triangle_area(base, height)` that returns the area
   - Use these functions to calculate and display areas for given measurements
3. **Test your code**: Run your script to see if it works:
   ```bash
   python exercises/08-functions/01-area-calculator/main.py
   ```
4. **Check with tests**: Run the automated test to verify your solution:
   ```bash
   pytest tests/test_08_functions.py::TestExercise08_01::test_area_functions -v
   ```

## 💡 Hints

- Rectangle area: `length * width`
- Circle area: `π * radius²` (use `radius ** 2` for squaring)
- Triangle area: `(base * height) / 2`
- Use `return` to send the calculated value back from the function
- Call functions like: `area = calculate_rectangle_area(5, 3)`

## ✅ Expected Output

When you run your program, you should see something like:
```
=== Area Calculator ===
Rectangle (5 × 3): 15.0 square units
Circle (radius 4): 50.26544 square units
Triangle (base 6, height 8): 24.0 square units
```

## 🎉 Success!

Once your program works, you've successfully:
- ✅ Defined functions with parameters
- ✅ Used return values to get results from functions
- ✅ Called functions and used their results
- ✅ Organized mathematical calculations into reusable functions

Ready for the next exercise? Great work! 🚀