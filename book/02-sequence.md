# Chapter 02: Program Sequence

## Learning Objectives

By the end of this chapter, you will be able to:
- Understand how Python executes code line by line
- Write programs with multiple statements
- Use blank lines and indentation for readability
- Debug simple sequencing issues

## Introduction

Computer programs execute instructions in a specific order, one after another. This is called **sequence**. Python reads your code from top to bottom, executing each line in order.

Understanding sequence is fundamental to programming. It's like following a recipe: you must do step 1 before step 2, or your cake won't turn out right!

## Core Concepts

### Multiple Statements

A program can have many lines of code. Python executes them in order:

```python
print("First message")
print("Second message")
print("Third message")
```

Output:
```
First message
Second message
Third message
```

### Execution Flow

Imagine your program as a list of instructions that Python follows:

1. Start at the first line
2. Execute that line
3. Move to the next line
4. Repeat until the end

```python
# Line 1: This runs first
print("Step 1: Start")

# Line 2: This runs second
print("Step 2: Continue")

# Line 3: This runs third
print("Step 3: Finish")
```

### Readability with Blank Lines

Blank lines don't affect execution but make code easier to read:

```python
print("Welcome!")

print("This is a program.")

print("Goodbye!")
```

### Comments and Sequence

Comments are ignored by Python but help humans understand the flow:

```python
# Step 1: Greet the user
print("Hello!")

# Step 2: Ask for their name
print("What's your name?")

# Step 3: Say goodbye
print("Nice to meet you!")
```

## Common Mistakes

### Expecting Wrong Order

```python
print("Second")
print("First")  # ❌ This prints first, then second
```

### Missing Statements

```python
print("Hello")
# Forgot to add more code!
```

### Confusing Comments with Code

```python
print("This runs")
# print("This doesn't run")  # Comments are ignored
print("This runs too")
```

## Practice

Create programs that demonstrate sequence:

1. Write a program that prints a morning routine (wake up, brush teeth, eat breakfast)
2. Create a program that tells a short story with 5-6 events in order
3. Write a program that asks three questions in sequence

## Summary

In this chapter, you learned:
- Programs execute statements in order, from top to bottom
- Multiple `print()` statements create multiple lines of output
- Blank lines and comments improve code readability
- Sequence is the foundation of all programming

Now that you understand sequence, you're ready to learn about storing and reusing data with variables in the next chapter.