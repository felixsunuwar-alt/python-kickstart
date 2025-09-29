"""
Sample pytest test file

This demonstrates the basic structure of a pytest test.
Replace with your actual tests.
"""

def test_example():
    """
    A simple example test.
    """
    # Arrange
    expected = 4

    # Act
    result = 2 + 2

    # Assert
    assert result == expected

def test_string_concatenation():
    """
    Test string concatenation.
    """
    # Arrange
    first_name = "Hello"
    last_name = "World"

    # Act
    full_name = first_name + " " + last_name

    # Assert
    assert full_name == "Hello World"