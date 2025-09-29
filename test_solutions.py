#!/usr/bin/env python3
"""
Test script to validate our pytest tests against the solution files.
This ensures our tests work correctly before students use them.
"""

import subprocess
import sys
import tempfile
import shutil
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent

def test_solution_against_test(solution_path, test_command, exercise_dir):
    """
    Test a solution file by temporarily copying it to main.py and running the test.
    """
    exercise_path = PROJECT_ROOT / exercise_dir
    main_py_path = exercise_path / "main.py"
    
    # Backup original main.py if it exists
    backup_content = None
    if main_py_path.exists():
        with open(main_py_path, 'r') as f:
            backup_content = f.read()
    
    try:
        # Copy solution to main.py
        shutil.copy2(solution_path, main_py_path)
        
        # Run the test
        result = subprocess.run(
            test_command,
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        return result.returncode == 0, result.stdout, result.stderr
        
    finally:
        # Restore original main.py
        if backup_content is not None:
            with open(main_py_path, 'w') as f:
                f.write(backup_content)
        elif main_py_path.exists():
            main_py_path.unlink()

def main():
    """Test all solutions against their corresponding tests."""
    
    test_cases = [
        # Chapter 1
        ("solutions/01-intro/01-01-hello-world.py",
         [sys.executable, "-m", "pytest", "tests/test_01_intro.py::TestExercise01_01::test_hello_world_output", "-v"],
         "exercises/01-intro/01-hello-world"),
        ("solutions/01-intro/01-02-personal-greeting.py",
         [sys.executable, "-m", "pytest", "tests/test_01_intro.py::TestExercise01_02::test_personal_greeting_output", "-v"],
         "exercises/01-intro/02-personal-greeting"),
        ("solutions/01-intro/01-03-comments-and-code.py",
         [sys.executable, "-m", "pytest", "tests/test_01_intro.py::TestExercise01_03::test_comments_and_code_output", "-v"],
         "exercises/01-intro/03-comments-and-code"),
        
        # Chapter 2
        ("solutions/02-sequence/02-01-morning-routine.py",
         [sys.executable, "-m", "pytest", "tests/test_02_sequence.py::TestExercise02_01::test_morning_routine_output", "-v"],
         "exercises/02-sequence/01-morning-routine"),
        ("solutions/02-sequence/02-02-recipe-steps.py",
         [sys.executable, "-m", "pytest", "tests/test_02_sequence.py::TestExercise02_02::test_recipe_steps_output", "-v"],
         "exercises/02-sequence/02-recipe-steps"),
        ("solutions/02-sequence/02-03-story-sequence.py",
         [sys.executable, "-m", "pytest", "tests/test_02_sequence.py::TestExercise02_03::test_story_sequence_output", "-v"],
         "exercises/02-sequence/03-story-sequence"),
        
        # Chapter 3
        ("solutions/03-variables/03-01-personal-information.py",
         [sys.executable, "-m", "pytest", "tests/test_03_variables.py::TestExercise03_01::test_personal_info_output", "-v"],
         "exercises/03-variables/01-personal-info"),
        ("solutions/03-variables/03-02-rectangle-calculator.py",
         [sys.executable, "-m", "pytest", "tests/test_03_variables.py::TestExercise03_02::test_rectangle_calculator_output", "-v"],
         "exercises/03-variables/02-rectangle-calculator"),
        ("solutions/03-variables/03-03-variable-updates.py",
         [sys.executable, "-m", "pytest", "tests/test_03_variables.py::TestExercise03_03::test_variable_updates_output", "-v"],
         "exercises/03-variables/03-variable-updates"),
        
        # Chapter 4
        ("solutions/04-operators/04-01-bmi-calculator.py",
         [sys.executable, "-m", "pytest", "tests/test_04_operators.py::TestExercise04_01::test_bmi_calculator_output", "-v"],
         "exercises/04-operators/01-bmi-calculator"),
        
        # Chapter 5
        ("solutions/05-io/05-01-profile-builder.py",
         [sys.executable, "-m", "pytest", "tests/test_05_io.py::TestExercise05_01::test_profile_builder_output", "-v"],
         "exercises/05-io/01-profile-builder"),
        
        # Chapter 6
        ("solutions/06-selections/06-01-grade-calculator.py",
         [sys.executable, "-m", "pytest", "tests/test_06_selections.py::TestExercise06_01::test_grade_calculator_output", "-v"],
         "exercises/06-selections/01-grade-calculator"),
        
        # Chapter 7
        ("solutions/07-iterations/07-01-times-table.py",
         [sys.executable, "-m", "pytest", "tests/test_07_iterations.py::TestExercise07_01::test_times_table_output", "-v"],
         "exercises/07-iterations/01-times-table"),
        
        # Chapter 8
        ("solutions/08-functions/08-01-area-calculator.py",
         [sys.executable, "-m", "pytest", "tests/test_08_functions.py::TestExercise08_01::test_area_functions", "-v"],
         "exercises/08-functions/01-area-calculator"),
        
        # Chapter 9
        ("solutions/09-lists/09-01-shopping-list.py",
         [sys.executable, "-m", "pytest", "tests/test_09_lists.py::TestExercise09_01::test_shopping_list_operations", "-v"],
         "exercises/09-lists/01-shopping-list"),
    ]
    
    print("Testing all solutions against their pytest tests...\n")
    
    passed = 0
    failed = 0
    
    for solution_file, test_command, exercise_dir in test_cases:
        solution_path = PROJECT_ROOT / solution_file
        
        if not solution_path.exists():
            print(f"[FAIL] Solution file not found: {solution_file}")
            failed += 1
            continue
        
        print(f"Testing: {solution_file}")
        success, stdout, stderr = test_solution_against_test(solution_path, test_command, exercise_dir)
        
        if success:
            print(f"[PASS] PASSED")
            passed += 1
        else:
            print(f"[FAIL] FAILED")
            print(f"   stdout: {stdout}")
            print(f"   stderr: {stderr}")
            failed += 1
        print()
    
    print(f"Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("All tests passed! The pytest system is working correctly.")
        return 0
    else:
        print("Some tests failed. Check the test logic.")
        return 1

if __name__ == "__main__":
    sys.exit(main())