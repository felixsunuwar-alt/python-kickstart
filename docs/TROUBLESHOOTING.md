# Troubleshooting Guide

> A comprehensive guide to solving common issues you might encounter while learning Python with this course.

## 🚨 Quick Help

**Having trouble?** Follow this checklist first:

1. **Check your syntax** - Missing colons, indentation, or quotes?
2. **Read error messages carefully** - They often tell you exactly what's wrong
3. **Test with simple examples** - Start small and build up
4. **Check the console** - Look for error messages in your terminal
5. **Compare with solutions** - Each exercise has a `solution.py` file

---

## 📋 Common Issues by Category

### 🔧 Setup and Installation Issues

#### Python Not Found
**Problem:** `'python' is not recognized as an internal or external command`

**Solution:**
1. Install Python from [python.org](https://python.org/)
2. Choose Python 3.8 or higher
3. **Important**: Check "Add Python to PATH" during installation
4. Restart your terminal after installation
5. Test with: `python --version` or `python3 --version`

#### pip Commands Not Working
**Problem:** `'pip' is not recognized` or pip commands fail

**Solution:**
1. Python installation includes pip automatically
2. Try `python -m pip` instead of just `pip`
3. On some systems, use `pip3` instead of `pip`
4. For permission issues on Mac/Linux: `sudo pip install`

#### pytest Installation Issues
**Problem:** `ModuleNotFoundError: No module named 'pytest'`

**Solution:**
```bash
pip install pytest
```

If that fails:
```bash
python -m pip install pytest
```

Or on some systems:
```bash
pip3 install pytest
```

### 💻 Running Code Issues

#### Script Won't Run
**Problem:** `python main.py` does nothing or shows errors

**Common Causes & Solutions:**

1. **Wrong directory:**
   ```bash
   # Make sure you're in the right folder
   cd exercises/01-intro/01-hello-world
   python main.py
   ```

2. **File doesn't exist:**
   ```bash
   # Check if file exists
   ls main.py
   # or on Windows
   dir main.py
   ```

3. **Syntax errors in code:**
   - Check for missing colons after `if`, `for`, `while`, `def`
   - Check indentation (Python uses spaces, not brackets)
   - Look at the error message for line numbers

#### Tests Won't Run
**Problem:** `pytest` command fails or tests don't run

**Solutions:**

1. **Run from project root:**
   ```bash
   # Make sure you're in the main project directory
   cd /path/to/python-kickstart
   pytest tests/test_01_intro.py -v
   ```

2. **Install pytest:**
   ```bash
   pip install pytest
   ```

3. **Check test command syntax:**
   ```bash
   # Correct format for testing your work
   pytest tests/test_06_selections.py -v
   pytest tests/test_08_functions.py -v
   ```

#### Understanding Test Results
**Problem:** Tests fail but you're not sure why

**What the tests check:**
- **Student tests** (`pytest`) check your `main.py` files
- Tests will fail until you complete the exercises (this is normal!)
- Error messages show what's expected vs. what your code produces

**For instructors only:**
- **Solution tests** (`python test_solutions.py`) check the reference `solution.py` files
- These should always pass and are used for validation

### 🧪 Understanding the Testing System

#### How Tests Work
**Important:** The automated tests check your `main.py` files, not the solution files.

**Normal Testing Flow:**
1. **Red Phase**: Tests fail when you start (expected!)
2. **Green Phase**: Tests pass when you complete the exercise
3. **Refactor Phase**: Improve your code while keeping tests green

#### Test Commands for Students
```bash
# Test all your exercises
pytest tests/ -v

# Test a specific chapter
pytest tests/test_08_functions.py -v
pytest tests/test_09_lists.py -v

# Test a specific exercise
pytest tests/test_01_intro.py::TestExercise01_01::test_hello_world_output -v
```

#### What Test Results Mean
- **❌ FAILED**: Your code doesn't match the expected output yet
- **✅ PASSED**: Your code works correctly!
- **⏭️ MANUAL TESTING REQUIRED**: Exercise uses user input (test manually)

#### Common Test Confusion
**"Why do tests fail even though I copied the solution?"**
- Tests check your `main.py` file, not `solution.py`
- Make sure you're editing the right file
- Solution files are for reference only

**"Tests pass but I didn't write any code"**
- You might be looking at a completed exercise
- Check that `main.py` contains placeholder text like "# Replace this with your solution!"

### 🐛 Python Syntax Errors

#### Indentation Errors
**Problem:** `IndentationError: expected an indented block`

**Example:**
```python
# Wrong: Missing indentation
if age >= 18:
print("Adult")

# Correct: Proper indentation
if age >= 18:
    print("Adult")
```

**Solutions:**
- Use 4 spaces for each indentation level
- Be consistent with spaces vs tabs (prefer spaces)
- Use a code editor that shows whitespace

#### Missing Colons
**Problem:** `SyntaxError: invalid syntax`

**Common Issues:**
```python
# Missing colon after if
if age >= 18
    print("Adult")

# Missing colon after function definition
def greet(name)
    print(f"Hello, {name}")

# Missing colon after for loop
for i in range(5)
    print(i)
```

**Solutions:**
- Always add `:` after `if`, `elif`, `else`, `for`, `while`, `def`, `class`

#### Unclosed Quotes/Brackets
**Problem:** `SyntaxError: EOL while scanning string literal`

**Common Issues:**
```python
# Missing closing quote
message = "Hello world

# Missing closing bracket
numbers = [1, 2, 3

# Missing closing parenthesis
print("Hello"
```

#### Variable Name Issues
**Problem:** `NameError: name 'variable' is not defined`

**Common Issues:**
```python
# Using variable before defining
print(name)
name = "Alice"

# Typo in variable name
user_name = "Bob"
print(username)  # Wrong case!

# Using reserved keywords
def = 5  # 'def' is a reserved word
```

### 🔄 Logic Errors

#### Infinite Loops
**Problem:** Program hangs and never finishes

**Common Causes:**
```python
# Forgot to increment counter
i = 1
while i <= 5:
    print(i)
    # Missing: i += 1

# Wrong condition
i = 1
while i >= 1:  # Will never be false!
    print(i)
    i += 1
```

**Solutions:**
- Always update loop variables
- Double-check loop conditions
- Use `Ctrl+C` to stop infinite loops

#### Off-by-One Errors
**Problem:** Loop runs too many or too few times

**Examples:**
```python
# Wrong: Misses last element
for i in range(len(my_list) - 1):
    print(my_list[i])

# Correct: Includes all elements
for i in range(len(my_list)):
    print(my_list[i])

# Even better: Use direct iteration
for item in my_list:
    print(item)
```

#### Comparison vs Assignment
**Problem:** `if` statements don't work as expected

**Common Mistake:**
```python
# Wrong: Assignment instead of comparison
if age = 18:
    print("Exactly 18")

# Correct: Use == for comparison
if age == 18:
    print("Exactly 18")
```

### 📥 Input/Output Issues

#### Input Always Returns Strings
**Problem:** Math operations don't work with user input

**Issue:**
```python
age = input("Enter age: ")  # This is a string!
next_year = age + 1  # TypeError: can't add int to string
```

**Solution:**
```python
age = int(input("Enter age: "))  # Convert to integer
next_year = age + 1  # Now works correctly
```

#### Print Statement Issues
**Problem:** Output doesn't appear or looks wrong

**Common Issues:**
```python
# Forgetting to call print
result = 5 + 3  # Nothing appears

# Should be:
result = 5 + 3
print(result)

# String concatenation vs addition
print("Age: " + 20 + 5)  # TypeError
print("Age: " + str(20 + 5))  # Correct
print(f"Age: {20 + 5}")  # Even better with f-strings
```

### 🔧 Function Issues

#### Function Not Defined
**Problem:** `NameError: name 'function_name' is not defined`

**Common Causes:**
```python
# Calling function before defining it
say_hello()  # Error!

def say_hello():
    print("Hello!")
```

**Solution:** Define functions before calling them

#### Missing Return Statement
**Problem:** Function returns `None`

**Issue:**
```python
def add(a, b):
    a + b  # Missing return!

result = add(5, 3)
print(result)  # None
```

**Solution:**
```python
def add(a, b):
    return a + b  # Don't forget return!
```

#### Indentation in Functions
**Problem:** `IndentationError` in function body

**Issue:**
```python
def greet(name):
print(f"Hello, {name}")  # Not indented!
```

**Solution:**
```python
def greet(name):
    print(f"Hello, {name}")  # Properly indented
```

### 📚 List Issues

#### Index Out of Range
**Problem:** `IndexError: list index out of range`

**Issue:**
```python
colors = ["red", "green", "blue"]
print(colors[5])  # Error - no element at index 5
```

**Solution:** Check list length and use valid indexes (0 to len-1)

#### Forgetting Zero-Based Indexing
**Problem:** Getting wrong elements

**Common Mistake:**
```python
fruits = ["apple", "banana", "orange"]
print(fruits[1])  # "banana", not "apple"!
```

**Remember:** Lists start at index 0, not 1

#### Modifying Lists During Iteration
**Problem:** Unexpected behavior when removing elements

**Risky:**
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Can skip elements!
```

**Better:** Create a new list or iterate backwards

---

## 🔍 Debugging Strategies

### 1. Read Error Messages Carefully
Error messages tell you:
- **What** went wrong
- **Where** it happened (file and line number)
- **Why** it might have occurred

### 2. Use Print Statements for Debugging
```python
def calculate_grade(score):
    print(f"Input score: {score}")  # Debug input
    
    percentage = score / 100
    print(f"Percentage: {percentage}")  # Debug calculation
    
    if percentage >= 0.9:
        print("Returning A")  # Debug logic
        return "A"
    # ... rest of function
```

### 3. Test with Simple Cases
```python
# Test with known values first
print(add(2, 3))  # Should be 5
print(add(0, 0))  # Should be 0
print(add(-1, 1))  # Should be 0
```

### 4. Break Down Complex Problems
```python
# Instead of one complex line
result = ((a + b) * c) / (d - e)

# Break it into steps
sum_ab = a + b
product = sum_ab * c
difference = d - e
result = product / difference
```

### 5. Use a Code Editor with Syntax Highlighting
Recommended editors:
- **Visual Studio Code** (free, excellent for Python)
- **PyCharm** (Community Edition is free)
- **Sublime Text**

---

## 🆘 Getting Help

### 1. Check the Solution Files
Every exercise has a `solution.py` file you can reference for the correct implementation.

**Note:** The automated tests check your `main.py` files, not the solution files. This means:
- Tests will fail until you complete the exercise (this is expected!)
- You can compare your code with the solution file if you get stuck
- The solution files are for reference and learning

### 2. Review the Chapter
Go back to the relevant chapter in the `book/` folder.

### 3. Test Incrementally
- Start with the simplest version
- Add one feature at a time
- Test after each change

### 4. Common Error Patterns

| Error Message | Common Cause | Solution |
|---------------|--------------|----------|
| `SyntaxError: invalid syntax` | Missing colon, wrong indentation | Check syntax carefully |
| `NameError: name 'X' is not defined` | Typo in variable name or not defined | Check spelling and definition |
| `TypeError: unsupported operand type(s)` | Wrong data types in operation | Check data types and conversions |
| `IndentationError` | Inconsistent spacing | Use 4 spaces consistently |
| `IndexError: list index out of range` | Accessing invalid list index | Check list length and valid indexes |

---

## 🎯 Best Practices to Avoid Issues

### 1. Consistent Naming
```python
# Good: Consistent snake_case
first_name = "Alice"
last_name = "Smith"

# Avoid: Mixed styles
firstName = "Alice"
LastName = "Smith"
```

### 2. Proper Indentation
```python
# Good: Consistent 4-space indentation
if age >= 18:
    print("Adult")
    if age >= 65:
        print("Senior")

# Avoid: Mixed indentation
if age >= 18:
  print("Adult")  # 2 spaces
    if age >= 65:  # 4 spaces
        print("Senior")  # 8 spaces
```

### 3. Use Meaningful Names
```python
# Good
student_score = 85
max_score = 100

# Avoid
x = 85
y = 100
```

### 4. Comment Your Code
```python
# Calculate the percentage score
percentage = (student_score / max_score) * 100

# Determine letter grade based on percentage
if percentage >= 90:
    return "A"
```

### 5. Test Early and Often
- Test each function as you write it
- Use simple test cases first
- Don't wait until everything is complete

---

## 📞 Still Stuck?

If you're still having trouble:

1. **Re-read the exercise instructions** carefully
2. **Check the solution file** for that exercise
3. **Review the relevant chapter** in the book
4. **Start over with a simpler version** and build up
5. **Take a break** and come back with fresh eyes

Remember: Debugging is a normal part of programming! Even experienced developers spend time troubleshooting. Each error you fix makes you a better programmer.

---