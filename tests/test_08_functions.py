#!/usr/bin/env python3
"""
Tests for Chapter 8: Functions exercises
"""

import subprocess
import sys
import re
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


class TestExercise08_01:
    """Tests for Exercise 8.1: Area Calculator Functions"""
    
    def test_area_functions(self):
        """Test that the area calculator functions work correctly"""
        exercise_path = PROJECT_ROOT / "solutions" / "08-functions" / "08-01-area-calculator.py"
        
        # Run the solution code
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        output = result.stdout.strip()
        
        # Check that the output contains expected calculations
        assert "Rectangle (5 × 3): 15" in output, "Rectangle area calculation missing or incorrect"
        assert "Circle (radius 4): 50.26544" in output, "Circle area calculation missing or incorrect"
        assert "Triangle (base 6, height 8): 24" in output, "Triangle area calculation missing or incorrect"
        
        # Check that the header is present
        assert "Area Calculator" in output, "Missing program header"
    
    def test_functions_exist(self):
        """Test that the required functions are defined"""
        exercise_path = PROJECT_ROOT / "solutions" / "08-functions" / "08-01-area-calculator.py"
        
        # Read the solution file
        with open(exercise_path, 'r') as f:
            content = f.read()
        
        # Check that functions are defined
        assert "def calculate_rectangle_area(" in content, "calculate_rectangle_area function not defined"
        assert "def calculate_circle_area(" in content, "calculate_circle_area function not defined"
        assert "def calculate_triangle_area(" in content, "calculate_triangle_area function not defined"
        
        # Check that functions have return statements
        assert "return" in content, "Functions should return values"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])