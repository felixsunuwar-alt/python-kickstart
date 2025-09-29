#!/usr/bin/env python3
"""
Tests for Chapter 6: Selections exercises
"""

import subprocess
import sys
import re
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


class TestExercise06_01:
    """Tests for Exercise 6.1: Grade Calculator"""
    
    def test_grade_calculator_output(self):
        """Test that the grade calculator produces correct output"""
        exercise_path = PROJECT_ROOT / "exercises" / "06-selections" / "01-grade-calculator" / "main.py"
        
        # Test different score ranges
        test_cases = [
            ("95\n", "A"),    # Excellent grade
            ("85\n", "B"),    # Good grade
            ("75\n", "C"),    # Average grade
            ("65\n", "D"),    # Below average
            ("55\n", "F"),    # Failing grade
        ]
        
        for test_input, expected_grade in test_cases:
            # Run the student's code with test input
            result = subprocess.run(
                [sys.executable, str(exercise_path)],
                input=test_input,
                capture_output=True,
                text=True,
                cwd=PROJECT_ROOT
            )
            
            # Check that the program ran successfully
            assert result.returncode == 0, f"Program failed to run with input {test_input.strip()}: {result.stderr}"
            
            # Check that the expected grade appears in output
            output_text = result.stdout
            assert expected_grade in output_text, f"Expected grade '{expected_grade}' for score {test_input.strip()}, got output: {output_text}"
        
        # Check that the file contains conditional statements
        with open(exercise_path, 'r') as f:
            content = f.read()
        
        # Check for if/elif/else structure
        assert "if" in content, "Expected 'if' statement for grade calculation"
        assert "elif" in content, "Expected 'elif' statements for multiple grade ranges"
        
        # Check for comparison operators
        comparison_operators = ['>=', '>', '<', '<=']
        found_comparison = any(op in content for op in comparison_operators)
        assert found_comparison, "Expected comparison operators for grade ranges"
        
        # Check for input conversion
        input_conversion_patterns = [
            r'float\s*\(\s*input',  # float(input(...))
            r'int\s*\(\s*input'     # int(input(...))
        ]
        
        found_conversion = False
        for pattern in input_conversion_patterns:
            if re.search(pattern, content):
                found_conversion = True
                break
        
        assert found_conversion, "Expected numeric conversion of input (int or float)"
        
        # Check that all grade letters are present in the code
        grade_letters = ['A', 'B', 'C', 'D', 'F']
        for grade in grade_letters:
            assert f'"{grade}"' in content or f"'{grade}'" in content, f"Expected grade '{grade}' to be assigned in code"