# Exercise 8.1: Area Calculator Functions - Solution
# Complete implementation of area calculation functions

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

def calculate_circle_area(radius):
    """Calculate the area of a circle"""
    pi = 3.14159
    return pi * radius ** 2

def calculate_triangle_area(base, height):
    """Calculate the area of a triangle"""
    return (base * height) / 2

# Use the functions to calculate areas
print("=== Area Calculator ===")

# Calculate areas with given values
rectangle_area = calculate_rectangle_area(5, 3)
circle_area = calculate_circle_area(4)
triangle_area = calculate_triangle_area(6, 8)

# Display results
print(f"Rectangle (5 × 3): {rectangle_area} square units")
print(f"Circle (radius 4): {circle_area} square units")
print(f"Triangle (base 6, height 8): {triangle_area} square units")