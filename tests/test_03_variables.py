#!/usr/bin/env python3
"""
Tests for Chapter 3: Variables and Data Types exercises
"""

import subprocess
import sys
import re
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


class TestExercise03_01:
    """Tests for Exercise 3.1: Personal Information"""
    
    def test_personal_info_output(self):
        """Test that the personal info exercise uses variables correctly"""
        exercise_path = PROJECT_ROOT / "exercises" / "03-variables" / "01-personal-info" / "main.py"
        
        # Run the student's code and capture output
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # Check that the program ran successfully
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        # Check that output has multiple lines for different data types
        output_lines = result.stdout.strip().split('\n')
        assert len(output_lines) >= 4, "Expected at least 4 lines of output (name, age, height, is_student)"
        
        # Check that the file contains variable assignments
        with open(exercise_path, 'r') as f:
            content = f.read()
        
        # Look for variable assignments (basic pattern matching)
        variable_patterns = [
            r'name\s*=\s*["\']',  # String assignment
            r'age\s*=\s*\d+',     # Integer assignment
            r'height\s*=\s*\d+\.\d+',  # Float assignment
            r'is_student\s*=\s*(True|False)'  # Boolean assignment
        ]
        
        found_patterns = 0
        for pattern in variable_patterns:
            if re.search(pattern, content):
                found_patterns += 1
        
        assert found_patterns >= 3, f"Expected at least 3 different variable types, found {found_patterns}"


class TestExercise03_02:
    """Tests for Exercise 3.2: Rectangle Calculator"""
    
    def test_rectangle_calculator_output(self):
        """Test that the rectangle calculator performs correct calculations"""
        exercise_path = PROJECT_ROOT / "exercises" / "03-variables" / "02-rectangle-calculator" / "main.py"
        
        # Run the student's code and capture output
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # Check that the program ran successfully
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        # Check that output contains width, height, area, and perimeter
        output_text = result.stdout.lower()
        required_terms = ["width", "height", "area", "perimeter"]
        
        for term in required_terms:
            assert term in output_text, f"Expected '{term}' in output"
        
        # Check that the file contains mathematical operations
        with open(exercise_path, 'r') as f:
            content = f.read()
        
        # Look for multiplication and addition operations
        assert '*' in content, "Expected multiplication operation for area calculation"
        assert '+' in content, "Expected addition operation for perimeter calculation"
        
        # Extract numbers from output to verify calculations
        numbers = re.findall(r'\d+', result.stdout)
        assert len(numbers) >= 4, "Expected at least 4 numbers in output (width, height, area, perimeter)"


class TestExercise03_03:
    """Tests for Exercise 3.3: Variable Updates"""
    
    def test_variable_updates_output(self):
        """Test that the variable updates exercise shows progression"""
        exercise_path = PROJECT_ROOT / "exercises" / "03-variables" / "03-variable-updates" / "main.py"
        
        # Run the student's code and capture output
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # Check that the program ran successfully
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        # Check that output shows progression of values
        output_lines = result.stdout.strip().split('\n')
        assert len(output_lines) >= 3, "Expected at least 3 lines showing score progression"
        
        # Extract numbers from each line to verify they're increasing
        numbers_in_lines = []
        for line in output_lines:
            numbers = re.findall(r'\d+', line)
            if numbers:
                numbers_in_lines.append(int(numbers[-1]))  # Take the last number in each line
        
        assert len(numbers_in_lines) >= 3, "Expected at least 3 numeric values in output"
        
        # Check that values are increasing (showing updates)
        for i in range(1, len(numbers_in_lines)):
            assert numbers_in_lines[i] > numbers_in_lines[i-1], f"Expected increasing values, but {numbers_in_lines[i]} <= {numbers_in_lines[i-1]}"
        
        # Check that the file contains variable updates
        with open(exercise_path, 'r') as f:
            content = f.read()
        
        # Look for variable reassignment patterns
        update_patterns = [
            r'score\s*=\s*score\s*\+',  # score = score + ...
            r'score\s*\+=',             # score += ...
        ]
        
        found_update = False
        for pattern in update_patterns:
            if re.search(pattern, content):
                found_update = True
                break
        
        assert found_update, "Expected variable update operations (score = score + ... or score += ...)"