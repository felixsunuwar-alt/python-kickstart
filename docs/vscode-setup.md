# 🛠️ VS Code Setup Guide – Python Kickstart

This guide will help you set up Visual Studio Code for Python development in the Python Kickstart course.

## Prerequisites

- **Python 3.x** installed on your system
- **Visual Studio Code** downloaded and installed

## Installing the Python Extension

1. Open Visual Studio Code
2. Click on the Extensions icon in the left sidebar (or press `Ctrl+Shift+X`)
3. Search for "Python" in the marketplace
4. Find the official **Python** extension by Microsoft
5. Click **Install**

## Verifying Python Installation

1. Open a new terminal in VS Code (`Ctrl+Shift+`` or View → Terminal)
2. Type `python --version` and press Enter
3. You should see output like: `Python 3.x.x`
4. If you see an error, Python may not be installed or not in your PATH

## Running Python Code

### Method 1: Using the Terminal
1. Create a new file called `hello.py`
2. Add this code:
   ```python
   print("Hello, World!")
   ```
3. Save the file
4. In the terminal, run: `python hello.py`

### Method 2: Using VS Code's Run Button
1. Open your `hello.py` file
2. Look for the "Run" button (▶️) in the top-right corner
3. Click it to run your code
4. Output will appear in the terminal panel

## Running Tests with pytest

The Python Kickstart course uses automated tests to give you instant feedback on your exercises.

1. Install dependencies (including pytest):
   ```
   pip install -r requirements.txt
   ```

2. Test your exercise solutions:
   ```bash
   # Test a specific exercise (replace with your chapter/exercise)
   pytest tests/test_01_intro.py::TestExercise01_01::test_hello_world_output -v
   
   # Test all exercises in a chapter
   pytest tests/test_01_intro.py -v
   
   # Test all exercises
   pytest tests/ -v
   ```

3. Understanding test results:
   - ✅ **PASSED**: Your solution works correctly!
   - ❌ **FAILED**: Check the error message to see what needs fixing
   - The `-v` flag gives you detailed output

For complete testing instructions, see the main [README.md](../README.md#-testing-your-code) and [`tests/README.md`](../tests/README.md).

## Useful VS Code Features

### IntelliSense
- Auto-completion for Python code
- Hover over variables/functions for information
- Error highlighting and suggestions

### Debugging
1. Click to the left of a line number to set a breakpoint (red dot)
2. Press `F5` or click the Debug icon
3. Use the debug panel to step through code

### Integrated Terminal
- Run Python commands directly in VS Code
- Access to pip for installing packages
- Git commands for version control

## Troubleshooting

### Python not found
- Ensure Python is installed and added to your system PATH
- Try `python3` instead of `python`
- Restart VS Code after installation

### Extension not working
- Reload VS Code (`Ctrl+Shift+P` → "Developer: Reload Window")
- Check that the Python extension is enabled
- Verify Python interpreter selection (bottom status bar)

### Import errors
- Install required packages: `pip install <package-name>`
- Check that you're in the correct directory
- Use virtual environments for project isolation

## Next Steps

Once VS Code is set up:
1. Clone or download the Python Kickstart repository
2. Open the folder in VS Code
3. Install dependencies: `pip install -r requirements.txt`
4. Start with the exercises in the `exercises/` directory
5. Run tests to check your progress

## 💾 Want to Save Your Progress?

Consider using GitHub to save and sync your work across devices:
- **[🐙 Using GitHub](using-github.md)** - Complete guide to forking and syncing your work
- **[🚨 Troubleshooting](TROUBLESHOOTING.md)** - Solutions to common Python and setup issues

Happy coding! 🐍