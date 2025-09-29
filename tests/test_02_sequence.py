#!/usr/bin/env python3
"""
Tests for Chapter 2: Program Sequence exercises
"""

import subprocess
import sys
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


class TestExercise02_01:
    """Tests for Exercise 2.1: Morning Routine"""
    
    def test_morning_routine_output(self):
        """Test that the morning routine exercise produces correct sequence"""
        exercise_path = PROJECT_ROOT / "exercises" / "02-sequence" / "01-morning-routine" / "main.py"
        
        # Run the student's code and capture output
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # Check that the program ran successfully
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        # Check that output has multiple lines (sequence of steps)
        output_lines = result.stdout.strip().split('\n')
        assert len(output_lines) >= 3, "Expected at least 3 steps in the morning routine"
        
        # Check that the output contains typical morning routine activities
        output_text = result.stdout.lower()
        morning_keywords = ["wake", "brush", "eat", "breakfast", "school", "shower", "dress"]
        found_keywords = [keyword for keyword in morning_keywords if keyword in output_text]
        assert len(found_keywords) >= 2, f"Expected morning routine keywords, found: {found_keywords}"


class TestExercise02_02:
    """Tests for Exercise 2.2: Recipe Steps"""
    
    def test_recipe_steps_output(self):
        """Test that the recipe steps exercise produces correct sequence"""
        exercise_path = PROJECT_ROOT / "exercises" / "02-sequence" / "02-recipe-steps" / "main.py"
        
        # Run the student's code and capture output
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # Check that the program ran successfully
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        # Check that output has multiple lines (sequence of steps)
        output_lines = result.stdout.strip().split('\n')
        assert len(output_lines) >= 4, "Expected at least 4 steps in the recipe"
        
        # Check that the file contains comments (read the file to verify)
        with open(exercise_path, 'r') as f:
            content = f.read()
        
        # Count comment lines (lines starting with #, excluding shebang)
        comment_lines = [line for line in content.split('\n') if line.strip().startswith('#') and not line.startswith('#!/')]
        assert len(comment_lines) >= 3, "Expected at least 3 comment lines explaining the steps"


class TestExercise02_03:
    """Tests for Exercise 2.3: Story Sequence"""
    
    def test_story_sequence_output(self):
        """Test that the story sequence exercise produces correct narrative"""
        exercise_path = PROJECT_ROOT / "exercises" / "02-sequence" / "03-story-sequence" / "main.py"
        
        # Run the student's code and capture output
        result = subprocess.run(
            [sys.executable, str(exercise_path)],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        # Check that the program ran successfully
        assert result.returncode == 0, f"Program failed to run: {result.stderr}"
        
        # Check that output has multiple lines (story sequence)
        output_lines = result.stdout.strip().split('\n')
        assert len(output_lines) >= 5, "Expected at least 5 lines for a complete story"
        
        # Check that the story has a beginning, middle, and end structure
        output_text = result.stdout.lower()
        story_indicators = ["once", "upon", "time", "then", "finally", "end", "after"]
        found_indicators = [indicator for indicator in story_indicators if indicator in output_text]
        assert len(found_indicators) >= 1, f"Expected story structure indicators, found: {found_indicators}"
        
        # Check that each line is a reasonable length for a story sentence
        for i, line in enumerate(output_lines):
            assert len(line.strip()) >= 10, f"Line {i+1} seems too short for a story sentence: '{line.strip()}'"