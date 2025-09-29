# Exercise 3: Variable Updates

Demonstrate how variables can be updated with new values throughout a program.

## 📖 Before You Start

**⚠️ IMPORTANT: Complete Exercise 2 first!**

Make sure you have successfully completed the "Rectangle Calculator" exercise.

## 🎯 Goal

Create a program that shows a score being updated multiple times, like in a game.

## 📚 What You'll Learn

- How to update variable values using assignment
- How to use the current value of a variable in calculations
- How variables can change throughout program execution

## 📝 Instructions

1. **Open the file**: Look at the `main.py` file in this folder
2. **Write your code**: Create a score variable and update it multiple times
3. **Test your code**: Run your script to see if it works:
   ```bash
   python exercises/03-variables/03-variable-updates/main.py
   ```
4. **Check with tests**: Run the automated test to verify your solution:
   ```bash
   pytest tests/test_03_variables.py::TestExercise03_03::test_variable_updates
   ```

## 💡 Hints

- Start with `score = 0`
- Use `score = score + points` to add to the current value
- Print the score after each update with descriptive messages

## ✅ Expected Output

When you run your program, you should see:
```
Initial score: 0
After first level: 10
After second level: 25
Final score: 40
```

## 🎉 Success!

Once your program works, you've successfully:
- ✅ Updated variables with new values
- ✅ Used variables in arithmetic expressions
- ✅ Demonstrated how data changes throughout a program

Perfect work with variable updates! 🚀