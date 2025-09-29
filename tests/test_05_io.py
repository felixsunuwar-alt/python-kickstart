#!/usr/bin/env python3
"""
Tests for Chapter 5: Input/Output exercises
"""

import subprocess
import sys
import re
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


class TestExercise05_01:
    """Tests for Exercise 5.1: Profile Builder"""
    
    def test_profile_builder_output(self):
        """Test that the profile builder produces correct output"""
        exercise_path = PROJECT_ROOT / "exercises" / "05-io" / "01-profile-builder" / "main.py"
        
        # Create a test input string
        test_input = "Alice Johnson\n25\n1.68\nPhotography\n"
        
        # Run the student's code with test input
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            input=test_input,
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # Check that the program ran successfully
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        # Check that output contains the input values
        output_text = result.stdout
        
        # Should contain the name, age, height, and hobby from input
        assert "Alice Johnson" in output_text, "Expected name to appear in output"
        assert "25" in output_text, "Expected age to appear in output"
        assert "1.68" in output_text, "Expected height to appear in output"
        assert "Photography" in output_text, "Expected hobby to appear in output"
        
        # Should contain birth year calculation (2024 - 25 = 1999)
        assert "1999" in output_text, "Expected calculated birth year to appear in output"
        
        # Check that the file contains input() calls
        with open(exercise_path, 'r') as f:
            content = f.read()
        
        # Count input() calls
        input_calls = len(re.findall(r'input\s*\(', content))
        assert input_calls >= 4, f"Expected at least 4 input() calls, found {input_calls}"
        
        # Check for type conversion
        conversion_patterns = [
            r'int\s*\(\s*input',  # int(input(...))
            r'float\s*\(\s*input'  # float(input(...))
        ]
        
        found_conversion = False
        for pattern in conversion_patterns:
            if re.search(pattern, content):
                found_conversion = True
                break
        
        assert found_conversion, "Expected type conversion (int or float) for numeric input"
        
        # Check for f-string usage (modern Python formatting)
        f_string_pattern = r'f["\'].*\{.*\}.*["\']'
        has_f_strings = re.search(f_string_pattern, content)
        
        # Allow either f-strings or other formatting methods
        formatting_patterns = [
            r'f["\'].*\{.*\}.*["\']',  # f-strings
            r'\.format\s*\(',          # .format() method
            r'%.*%',                   # % formatting
            r'\+.*\+',                 # string concatenation
        ]
        
        found_formatting = any(re.search(pattern, content) for pattern in formatting_patterns)
        assert found_formatting, "Expected some form of string formatting for output"