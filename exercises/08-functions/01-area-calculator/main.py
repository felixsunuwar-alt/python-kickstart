# Exercise 1: Area Calculator Functions
# Practice defining and using functions for mathematical calculations

# TODO: Define your area calculation functions here

import math

def calculate_rectangle_area(length, width):

  
    # TODO: Calculate and return length * width
    return length * width

def calculate_circle_area(radius):
    """Calculate the area of a circle"""
    # TODO: Calculate and return π * radius²
    # Use 3.14159 for π
    return 3.14159 * radius**2

def calculate_triangle_area(base, height):
    """Calculate the area of a triangle"""
    # TODO: Calculate and return (base * height) / 2
    return (base * height) / 2

# TODO: Use your functions to calculate areas
def meny():
    print("=== Area Calculator ===")
    print("1. räkna ut area av en rektangel")
    print("2. räkna ut arean av en circel")
    print("3. räkna ut area av en triangle")
    print("4. avsluta")
    val = input("Välj ett alternativ (1-4): ")
    if val == "1":
        length = float(input("Ange bredden på rektangeln: "))
        width = float(input("Ange höjden på rektangeln: "))
        area = calculate_rectangle_area(length, width)
        print(f"Arean av rektangeln är: {area} kvadratenheter")
    elif val =="2":
        radie = float(input("ange arean"))
        area = calculate_circle_area(radie)
        print(f"arean av cirkeln är: {area}")
    elif val == "3":
        base = float(input("ange basen: "))
        höjd = float(input("ange höjden: "))
        area = calculate_triangle_area(base, höjd)
        print(f"arean av trianglen är: {area}")
    elif val == "4":
        print("tack för att du kom! ")
    else: 
        print("välj mellan 1-4 din idiot ")
meny()
    
    

# Test your functions with these values:
# Rectangle: length=5, width=3
# Circle: radius=4
# Triangle: base=6, height=8

# Example of how to call a function (uncomment and complete):
# rectangle_area = calculate_rectangle_area(5, 3)
# print(f"Rectangle (5 × 3): {rectangle_area} square units")

# TODO: Add calls for circle and triangle calculations