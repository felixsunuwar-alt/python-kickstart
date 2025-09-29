# Mini-Project: Personal Finance Tracker
# Build upon function exercises by creating a comprehensive financial management tool!

# 📖 IMPORTANT: Read the README.md file first for detailed instructions,
#    examples, and ideas on how to approach this project!

# This project builds on what you learned in function exercises:
# - Defining functions with parameters and return values
# - Organizing code into logical, reusable functions
# - Separating calculation logic from user interface
# - Creating modular, maintainable code

# TODO: Create your Personal Finance Tracker here!

# Here's a simple example to get you started:
def calculate_budget(income, expenses):
    """Calculate budget surplus/deficit and savings rate"""
    remaining = income - expenses
    savings_rate = (remaining / income) * 100 if income > 0 else 0
    return remaining, savings_rate

def show_main_menu():
    """Display the main menu options"""
    print("\n=== Personal Finance Tracker ===")
    print("1. Budget Calculator")
    print("2. Savings Goal Tracker")
    print("3. Exit")

def budget_calculator():
    """Handle the budget calculator feature"""
    print("\n=== Budget Calculator ===")
    income = float(input("Enter your monthly income: "))
    expenses = float(input("Enter your monthly expenses: "))
    
    remaining, savings_rate = calculate_budget(income, expenses)
    
    print(f"\nBudget Analysis:")
    print(f"- Monthly Income: ${income:,.2f}")
    print(f"- Monthly Expenses: ${expenses:,.2f}")
    print(f"- Remaining Budget: ${remaining:,.2f}")
    print(f"- Savings Rate: {savings_rate:.1f}%")
    
    if savings_rate >= 20:
        print("Recommendation: Excellent! You're saving well.")
    elif savings_rate > 0:
        print("Recommendation: Good start! Try to increase savings if possible.")
    else:
        print("Recommendation: Review your expenses to create a positive budget.")

# Main program
print("=== Personal Finance Tracker ===")
print("Manage your money with smart calculations!")

show_main_menu()
choice = input("Enter your choice (1-3): ")

if choice == "1":
    budget_calculator()
elif choice == "2":
    print("Savings Goal Tracker - Coming soon!")
else:
    print("Thank you for using Personal Finance Tracker!")

# YOUR TURN: 
# 1. Add more financial calculation functions (savings goals, investments, etc.)
# 2. Create a main program loop to allow multiple calculations
# 3. Add input validation functions for user data
# 4. Create functions for different financial recommendations
# 5. Add more sophisticated financial formulas
# 6. Organize functions into logical groups

# HINTS:
# - Use functions for each major calculation (budget, savings, investment)
# - Create helper functions for user input and validation
# - Separate calculation logic from display logic
# - Use meaningful function names and docstrings
# - Test each function individually before combining

# Remember: This is YOUR project - make it useful and well-organized!