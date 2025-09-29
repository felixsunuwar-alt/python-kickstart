# Chapter 01: Introduction to Python

## Learning Objectives

By the end of this chapter, you will be able to:
- Understand what Python is and why it's useful for beginners
- Run your first Python program
- Use the `print()` function to display output
- Write basic comments in your code

## Introduction

Welcome to Python programming! Python is a high-level programming language known for its simplicity and readability. It's an excellent choice for beginners because:

- **Easy to read**: Python code looks almost like English
- **Quick to learn**: You can start writing useful programs quickly
- **Widely used**: Python powers websites, games, data analysis, and more
- **Large community**: Lots of help and resources available

In this chapter, we'll write our first Python program and learn the basics of running code.

## Installing Python

Before you can run Python programs, you need to have Python installed on your computer. Many operating systems come with Python pre-installed, but you may need to install it or update to a newer version.

### Checking if Python is Already Installed

Open a terminal/command prompt and type:

python --version


If you see output like `Python 3.x.x`, Python is already installed. If not, follow the installation instructions below.

### Windows

1. Visit the official Python website: https://python.org/downloads
2. Download the latest Python 3.x installer for Windows
3. Run the installer
4. **Important**: Check the box "Add Python to PATH" during installation
5. Click "Install Now"
6. Verify installation: `python --version`

### macOS

macOS may come with Python 2 pre-installed, but you need Python 3.

1. Visit https://python.org/downloads
2. Download the latest Python 3.x installer for macOS
3. Open the downloaded `.pkg` file
4. Follow the installation wizard
5. Verify installation: `python3 --version` (or `python --version`)

### Linux (Ubuntu/Debian)

1. Open a terminal
2. Update package list: `sudo apt update`
3. Install Python 3: `sudo apt install python3`
4. Verify installation: `python3 --version`

### Linux (Fedora/CentOS/RHEL)

1. Open a terminal
2. Install Python 3: `sudo dnf install python3` (Fedora) or `sudo yum install python3` (CentOS/RHEL)
3. Verify installation: `python3 --version`

### Verifying Your Installation

After installation, you should be able to:
- Run `python --version` (or `python3 --version` on some systems)
- See output showing Python 3.x.x
- Create and run `.py` files

If you encounter any issues, check the official Python documentation or ask your teacher for help.

## Core Concepts

### Your First Program: Hello World

The traditional first program in any language is "Hello World". Here's how to do it in Python:

```python
print("Hello, World!")
```

This single line of code displays the text "Hello, World!" on the screen.

### The print() Function

`print()` is a built-in Python function that displays information. You can print text (strings) by placing them in quotation marks:

```python
print("Welcome to Python!")
print("Let's start coding!")
```

### Comments

Comments are notes in your code that Python ignores. They're useful for explaining what your code does. Use the `#` symbol to create a comment:

```python
# This is a comment
print("Hello!")  # This prints Hello!
```

### Running Python Programs

To run a Python program:
1. Save your code in a file with a `.py` extension (like `hello.py`)
2. Open a terminal/command prompt
3. Navigate to the folder containing your file
4. Type `python hello.py` and press Enter

## Common Mistakes

### Forgetting Quotation Marks
```python
print(Hello, World!)  # ❌ Error: Hello and World are not defined
print("Hello, World!")  # ✅ Correct
```

### Wrong File Extension
Make sure your file ends with `.py`, not `.txt` or other extensions.

### Not Running from Correct Directory
If you get a "file not found" error, make sure you're in the same folder as your Python file.

## Practice

Try these exercises to practice what you've learned:

1. Create a program that prints your name
2. Write a program that prints three different messages
3. Add comments to explain what each line does

## Summary

In this chapter, you learned:
- Python is a beginner-friendly programming language
- How to use `print()` to display text
- How to write comments with `#`
- How to run Python programs from the terminal

You're now ready to move on to more complex concepts. In the next chapter, we'll learn about program sequence and multiple statements.