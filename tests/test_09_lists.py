#!/usr/bin/env python3
"""
Tests for Chapter 9: Lists exercises
"""

import subprocess
import sys
import re
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


class TestExercise09_01:
    """Tests for Exercise 9.1: Shopping List Manager"""
    
    def test_shopping_list_operations(self):
        """Test that the shopping list manager works correctly"""
        exercise_path = PROJECT_ROOT / "solutions" / "09-lists" / "09-01-shopping-list.py"
        
        # Run the solution code
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        output = result.stdout.strip()
        
        # Check that the output contains expected list operations
        assert "Starting with an empty list: []" in output, "Empty list initialization missing"
        assert "Adding items to the list" in output, "Adding items section missing"
        assert "milk" in output, "milk item missing from output"
        assert "bread" in output, "bread item missing from output"
        assert "eggs" in output, "eggs item missing from output"
        assert "apples" in output, "apples item missing from output"
        assert "cheese" in output, "cheese item missing from output"
        
        # Check numbered list display
        assert "1. milk" in output, "Numbered list display missing"
        assert "2. bread" in output, "Numbered list display missing"
        
        # Check removal operation
        assert "Removing 'bread' from the list" in output, "Removal operation missing"
        assert "Final shopping list has 4 items" in output, "Final count incorrect"
        
        # Check that the header is present
        assert "Shopping List Manager" in output, "Missing program header"
    
    def test_list_operations_exist(self):
        """Test that the required list operations are used"""
        exercise_path = PROJECT_ROOT / "solutions" / "09-lists" / "09-01-shopping-list.py"
        
        # Read the solution file
        with open(exercise_path, 'r') as f:
            content = f.read()
        
        # Check that list operations are used
        assert "shopping_list = []" in content, "Empty list creation missing"
        assert ".append(" in content, "append() method not used"
        assert ".remove(" in content, "remove() method not used"
        assert "len(" in content, "len() function not used"
        assert "range(len(" in content, "Loop with range(len()) not used"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])