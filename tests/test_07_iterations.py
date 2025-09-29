#!/usr/bin/env python3
"""
Tests for Chapter 7: Iterations exercises
"""

import subprocess
import sys
import re
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


class TestExercise07_01:
    """Tests for Exercise 7.1: Times Table Generator"""
    
    def test_times_table_output(self):
        """Test that the times table generator produces correct output"""
        exercise_path = PROJECT_ROOT / "exercises" / "07-iterations" / "01-times-table" / "main.py"
        
        # Test with number 5
        test_input = "5\n"
        
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
        
        # Check that output contains the multiplication table
        output_text = result.stdout
        
        # Should contain all multiplications from 5×1 to 5×10
        expected_results = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        for result_value in expected_results:
            assert str(result_value) in output_text, f"Expected result {result_value} to appear in output"
        
        # Should contain multiplication symbols and equals signs
        assert "×" in output_text or "*" in output_text, "Expected multiplication symbol in output"
        assert "=" in output_text, "Expected equals sign in output"
        
        # Should contain the number 5 multiple times (in each line)
        five_count = output_text.count("5")
        assert five_count >= 10, f"Expected number 5 to appear at least 10 times, found {five_count}"
        
        # Check that the file contains a for loop
        with open(exercise_path, 'r') as f:
            content = f.read()
        
        # Check for for loop
        assert "for" in content, "Expected 'for' loop for generating times table"
        
        # Check for range() function
        assert "range" in content, "Expected 'range()' function in for loop"
        
        # Check for input conversion
        input_conversion_patterns = [
            r'int\s*\(\s*input',    # int(input(...))
            r'float\s*\(\s*input'   # float(input(...))
        ]
        
        found_conversion = False
        for pattern in input_conversion_patterns:
            if re.search(pattern, content):
                found_conversion = True
                break
        
        assert found_conversion, "Expected numeric conversion of input (int or float)"
        
        # Check for multiplication operation
        multiplication_patterns = [
            r'\*',           # * operator
            r'×',            # × symbol
        ]
        
        found_multiplication = any(re.search(pattern, content) for pattern in multiplication_patterns)
        assert found_multiplication, "Expected multiplication operation in the code"
        
        # Check that range goes from 1 to 10 (or 11)
        range_patterns = [
            r'range\s*\(\s*1\s*,\s*11\s*\)',  # range(1, 11)
            r'range\s*\(\s*1\s*,\s*10\s*\+\s*1\s*\)',  # range(1, 10+1)
        ]
        
        found_correct_range = any(re.search(pattern, content) for pattern in range_patterns)
        assert found_correct_range, "Expected range(1, 11) or equivalent for 1 to 10 multiplication"