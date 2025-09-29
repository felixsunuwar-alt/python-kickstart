# Python Kickstart

A beginner-friendly Python curriculum for Programming 1 (PRRPRR01), designed to teach programming fundamentals through hands-on exercises and projects.

## Overview

Python Kickstart provides a structured learning path for students new to programming, featuring:

- **Interactive Chapters**: Step-by-step lessons covering Python basics
- **Auto-tested Exercises**: Immediate feedback on coding tasks
- **Open-ended Projects**: Creative opportunities for exploration
- **Teacher Resources**: Solutions, rubrics, and classroom guides

## Getting Started

### Prerequisites

- Python 3.8 or higher
- VS Code with Python extension
- Git for version control

### Setup

1. Clone this repository
2. Follow the [VS Code Setup Guide](docs/vscode-setup.md)
3. Install dependencies: `pip install -r requirements.txt`
4. Start with Chapter 1 in the `book/` directory

## 🧪 Testing Your Code

This course uses automated tests to give you instant feedback on your exercises. Here's how to test your solutions:

### Test a Single Exercise
```bash
# Example: Test your Chapter 1, Exercise 1 solution
pytest tests/test_01_intro.py::TestExercise01_01::test_hello_world_output -v
```

### Test All Exercises in a Chapter
```bash
# Example: Test all Chapter 1 exercises
pytest tests/test_01_intro.py -v
```

### Test Everything
```bash
# Test all exercises across all chapters
pytest tests/ -v
```

### Understanding Test Results
- ✅ **PASSED**: Your solution works correctly!
- ❌ **FAILED**: Check the error message to see what needs to be fixed
- 📝 **Tip**: Tests check both your program's output and code structure

For more detailed testing information, see [`tests/README.md`](tests/README.md).

## 💾 Saving Your Progress with GitHub

Want to save your work and access it from different computers? GitHub makes it easy to sync your progress across all your devices.

### 📚 GitHub Guides

- **[🐙 Using GitHub](docs/using-github.md)** - Complete guide to forking, cloning, and syncing your work
- **[🔄 Updating Your Fork](docs/UPDATING-FORK.md)** - How to get the latest course updates
- **[🚨 Troubleshooting](docs/TROUBLESHOOTING.md)** - Solutions to common Python and setup issues

### 🚀 Quick Start with GitHub

1. **Fork** the repository on GitHub to create your own copy
2. **Clone** your fork: `git clone https://github.com/YOUR-USERNAME/python-kickstart.git`
3. **Work** on exercises and save progress: `git add . && git commit -m "Complete Chapter X"`
4. **Sync** your work: `git push origin main`

See the [complete GitHub guide](docs/using-github.md) for detailed instructions.

## Project Structure

```
python-kickstart/
├── book/           # Course chapters and lessons
├── exercises/      # Auto-tested coding exercises
├── tests/          # Test files for exercises
├── projects/       # Open-ended project briefs
├── solutions/      # Teacher solutions and rubrics
├── templates/      # Starter project templates
└── docs/           # Documentation and guides
```

## Contributing

This project follows the structure of JS Kickstart and C# Kickstart for consistency. See [PLAN.md](docs/devdocs/PLAN.md) for development roadmap and [BACKLOG.md](docs/devdocs/BACKLOG.md) for current tasks.

## License

MIT License - see [LICENSE](LICENSE) file for details.