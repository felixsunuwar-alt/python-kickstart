#!/usr/bin/env python3
"""
Tests for Chapter 1: Introduction to Python exercises
"""

import subprocess
import sys
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


class TestExercise01_01:
    """Tests for Exercise 1.1: Hello World"""
    
    def test_hello_world_output(self):
        """Test that the hello world exercise produces correct output"""
        exercise_path = PROJECT_ROOT / "exercises" / "01-intro" / "01-hello-world" / "main.py"
        
        # Run the student's code and capture output
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # Check that the program ran successfully
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        # Check the output
        expected_output = "Hello, World!\n"
        assert result.stdout == expected_output, f"Expected '{expected_output.strip()}', got '{result.stdout.strip()}'"


class TestExercise01_02:
    """Tests for Exercise 1.2: Personal Greeting"""
    
    def test_personal_greeting_output(self):
        """Test that the personal greeting exercise produces correct output"""
        exercise_path = PROJECT_ROOT / "exercises" / "01-intro" / "02-personal-greeting" / "main.py"
        
        # Run the student's code and capture output
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # Check that the program ran successfully
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        # Check that output contains a name and welcome message
        output_lines = result.stdout.strip().split('\n')
        assert len(output_lines) >= 2, "Expected at least 2 lines of output (name and welcome message)"
        
        # Check that the second line contains "Welcome" and "Python"
        welcome_line = output_lines[1].lower()
        assert "welcome" in welcome_line, "Second line should contain 'Welcome'"
        assert "python" in welcome_line, "Second line should contain 'Python'"


class TestExercise01_03:
    """Tests for Exercise 1.3: Comments and Code"""
    
    def test_comments_and_code_output(self):
        """Test that the comments and code exercise produces correct output"""
        exercise_path = PROJECT_ROOT / "exercises" / "01-intro" / "03-comments-and-code" / "main.py"
        
        # Run the student's code and capture output
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # Check that the program ran successfully
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        # Check that there is some output (the exercise should print something)
        assert result.stdout.strip(), "Expected some output from the program"
        
        # Check that the file contains comments (read the file to verify)
        with open(exercise_path, 'r') as f:
            content = f.read()
        
        # Count comment lines (lines starting with #, excluding shebang)
        comment_lines = [line for line in content.split('\n') if line.strip().startswith('#') and not line.startswith('#!/')]
        assert len(comment_lines) >= 2, "Expected at least 2 comment lines in the code"