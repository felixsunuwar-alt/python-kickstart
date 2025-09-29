# Final Project: Personal Expense Manager
# Combine everything you've learned to create a comprehensive financial tracking system!

# 📖 IMPORTANT: Read the README.md file first for detailed instructions,
#    examples, and ideas on how to approach this project!

# This project combines ALL concepts you've learned:
# - Input/Output (Chapter 5): Interactive expense entry and reporting
# - Selections (Chapter 6): Menu systems and expense categorization
# - Iterations (Chapter 7): Looping through financial data
# - Functions (Chapter 8): Organized, reusable financial calculations
# - Lists (Chapter 9): Managing collections of expense data

# TODO: Create your Personal Expense Manager here!

# Here's a simple example to get you started:

# Parallel lists to store expense data
expenses = []
amounts = []
categories = []

def add_expense():
    """Add a new expense to the tracking system"""
    print("\n=== Add Expense ===")
    description = input("Enter expense description: ")
    amount = float(input("Enter amount: $"))
    category = input("Enter category (Food/Transport/Entertainment/Other): ")
    
    expenses.append(description)
    amounts.append(amount)
    categories.append(category)
    print("Expense added successfully!")

def view_expenses():
    """Display all recorded expenses"""
    print("\n=== All Expenses ===")
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    
    for i in range(len(expenses)):
        print(f"{expenses[i]}: ${amounts[i]:.2f} ({categories[i]})")

def calculate_total():
    """Calculate total spending"""
    total = sum(amounts)
    print(f"\nTotal Spending: ${total:.2f}")
    return total

def show_menu():
    """Display the main menu"""
    print("\n=== Personal Expense Manager ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total")
    print("4. Exit")

# Simple demonstration
print("=== Personal Expense Manager ===")
print("Track your spending and manage your budget!")

# Add some sample data
expenses.append("Coffee")
amounts.append(4.50)
categories.append("Food")

expenses.append("Bus fare")
amounts.append(2.75)
categories.append("Transportation")

# Show current data
view_expenses()
calculate_total()

print("\nThank you for using Personal Expense Manager!")

# YOUR TURN: 
# 1. Create a main program loop with full menu system
# 2. Add budget tracking and remaining budget calculations
# 3. Calculate spending by category
# 4. Add financial analysis and recommendations
# 5. Include income tracking alongside expenses
# 6. Add data validation and error handling
# 7. Create detailed financial reports

# HINTS:
# - Use parallel lists: expenses[], amounts[], categories[]
# - Create functions for each major feature
# - Use loops for menu systems and data processing
# - Add budget vs. spending comparisons
# - Provide meaningful financial insights
# - Consider adding dates, income, and savings goals

# Remember: This is YOUR capstone project - make it comprehensive and useful!
# Think about what would help you manage your real finances effectively.