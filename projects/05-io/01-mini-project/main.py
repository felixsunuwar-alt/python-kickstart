# Mini-Project: Personal Recipe Calculator
# Build upon the profile-builder exercise by creating an interactive recipe calculator!

# 📖 IMPORTANT: Read the README.md file first for detailed instructions,
#    examples, and ideas on how to approach this project!

# This project builds on what you learned in the profile-builder exercise:
# - Getting user input with input()
# - Using print() for formatted output
# - Type conversion with int() and float()
# - F-string formatting for professional output

# TODO: Create your Personal Recipe Calculator here!

# Here's a simple example to get you started:
print("=== Personal Recipe Calculator ===")
print("Let's calculate your recipe details!\n")

# Get basic recipe information
recipe_name = input("Enter recipe name: ")
original_servings = int(input("Enter original number of servings: "))
cook_name = input("Enter your name: ")

# Get desired serving size
desired_servings = int(input("How many servings do you want to make? "))

# Calculate scaling factor
scaling_factor = desired_servings / original_servings

# Display basic information
print(f"\n=== {cook_name}'s Recipe Card ===")
print(f"Recipe: {recipe_name}")
print(f"Original Servings: {original_servings} → Adjusted for: {desired_servings} servings")
print(f"Scaling Factor: {scaling_factor:.1f}x")

print("\nThanks for using the Recipe Calculator!")

# YOUR TURN: 
# 1. Add ingredient collection (name, quantity, price for 3+ ingredients)
# 2. Calculate adjusted quantities using the scaling factor
# 3. Calculate total cost and cost per serving
# 4. Make your output formatting look professional
# 5. Test with different inputs to make sure it works!

# HINTS:
# - Use float() for quantities and prices
# - Multiply original quantities by scaling_factor for adjusted amounts
# - Use f-strings with :.2f for currency formatting
# - Add sections with === headers for organization

# Remember: This is YOUR project - make it useful and creative!