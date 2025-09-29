#!/usr/bin/env python3
"""
Tests for Chapter 4: Operators exercises
"""

import subprocess
import sys
import re
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


class TestExercise04_01:
    """Tests for Exercise 4.1: BMI Calculator"""
    
    def test_bmi_calculator_output(self):
        """Test that the BMI calculator produces correct output"""
        exercise_path = PROJECT_ROOT / "exercises" / "04-operators" / "01-bmi-calculator" / "main.py"
        
        # Run the student's code and capture output
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # Check that the program ran successfully
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        # Check that output contains expected elements
        output_text = result.stdout.lower()
        
        # Should contain weight, height, BMI, and category
        required_terms = ["weight", "height", "bmi", "category"]
        for term in required_terms:
            assert term in output_text, f"Expected '{term}' in output"
        
        # Check that the file contains BMI calculation
        with open(exercise_path, 'r') as f:
            content = f.read()
        
        # Look for BMI calculation pattern
        bmi_calculation_patterns = [
            r'weight\s*/\s*\(\s*height\s*\*\*\s*2\s*\)',  # weight / (height ** 2)
            r'weight\s*/\s*height\s*\*\*\s*2',             # weight / height ** 2
        ]
        
        found_calculation = False
        for pattern in bmi_calculation_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                found_calculation = True
                break
        
        assert found_calculation, "Expected BMI calculation using weight / (height ** 2)"
        
        # Check for comparison operations (categorization)
        comparison_operators = ['<', '>', '>=', '<=', '==']
        found_comparison = any(op in content for op in comparison_operators)
        assert found_comparison, "Expected comparison operators for BMI categorization"