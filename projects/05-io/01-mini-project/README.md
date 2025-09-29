# Mini-Project: Personal Recipe Calculator

## 🎯 Goal

Create an interactive recipe calculator that asks users for ingredient information and calculates serving adjustments, nutritional estimates, and shopping costs. This project builds upon the input/output skills from Chapter 5 and the [`profile-builder`](../../exercises/05-io/01-profile-builder/) exercise.

## 📖 Project Description

Build a program that:
- Prompts the user for recipe details (servings, ingredients, quantities)
- Asks for additional information like desired serving size and ingredient prices
- Calculates adjusted quantities for different serving sizes
- Estimates total cost and basic nutritional information
- Displays a formatted recipe card with all calculations

This is a practical application that demonstrates real-world use of input/output and mathematical calculations!

## 🎮 Example Interaction

```
=== Personal Recipe Calculator ===
Let's calculate your recipe details!

Enter recipe name: Chocolate Chip Cookies
Enter original number of servings: 12
Enter your name: Alice

=== Ingredient Information ===
Enter ingredient 1 name: flour
Enter quantity for flour (in cups): 2.5
Enter price per cup for flour: 0.50

Enter ingredient 2 name: sugar
Enter quantity for sugar (in cups): 1.0
Enter price per cup for sugar: 0.75

Enter ingredient 3 name: chocolate chips
Enter quantity for chocolate chips (in cups): 1.5
Enter price per cup for chocolate chips: 2.00

How many servings do you want to make? 18

=== Alice's Recipe Card ===
Recipe: Chocolate Chip Cookies
Original Servings: 12 → Adjusted for: 18 servings
Scaling Factor: 1.5x

=== Adjusted Ingredients ===
• flour: 3.75 cups ($1.88)
• sugar: 1.50 cups ($1.13)
• chocolate chips: 2.25 cups ($4.50)

=== Recipe Summary ===
Total Estimated Cost: $7.51
Cost per Serving: $0.42
Estimated Prep Time: 45 minutes
Estimated Calories per Serving: ~180

Happy cooking, Alice! 🍪
```

## 🧠 What You'll Practice

This project reinforces concepts from **Chapter 5: Input & Output**:
- Using [`input()`](../../../book/05-io.md#input-with-input) to get multiple user inputs
- Using [`print()`](../../../book/05-io.md#output-with-print) for formatted output
- [Type conversion](../../../book/05-io.md#working-with-numbers-from-input) with `int()` and `float()`
- [F-string formatting](../../../book/05-io.md#pythons-f-string-formatting-recommended) for professional output
- Creating an [interactive program flow](../../../book/05-io.md#practical-applications)

**Building on the [`profile-builder`](../../exercises/05-io/01-profile-builder/) exercise:**
- Instead of just collecting personal information, you'll work with recipe data
- Instead of simple display, you'll perform calculations and adjustments
- You'll practice working with multiple related inputs and mathematical operations
- You'll create a more complex, formatted output with calculations

## 🚀 Getting Started

1. **Open `main.py` in this folder**

2. **Follow the step-by-step approach:**
   - Start by asking for basic recipe information
   - Add ingredient collection (start with 2-3 ingredients)
   - Implement serving size adjustment calculations
   - Add cost calculations
   - Build your formatted output piece by piece
   - Test frequently with `python main.py`

3. **Test your project:** `python main.py`

## 💡 Implementation Ideas

### Approach 1: Basic Recipe Scaling
```python
print("=== Personal Recipe Calculator ===")

recipe_name = input("Enter recipe name: ")
original_servings = int(input("Enter original number of servings: "))
desired_servings = int(input("How many servings do you want to make? "))

scaling_factor = desired_servings / original_servings

print(f"\nScaling factor: {scaling_factor:.1f}x")
print(f"Recipe: {recipe_name}")
print(f"Original: {original_servings} → Adjusted: {desired_servings} servings")
```

### Approach 2: Ingredient Collection and Calculation
```python
# Collect ingredient information
ingredient1 = input("Enter ingredient 1 name: ")
quantity1 = float(input(f"Enter quantity for {ingredient1}: "))
price1 = float(input(f"Enter price per unit for {ingredient1}: "))

# Calculate adjusted quantities
adjusted_quantity1 = quantity1 * scaling_factor
adjusted_cost1 = adjusted_quantity1 * price1

print(f"• {ingredient1}: {adjusted_quantity1:.2f} units (${adjusted_cost1:.2f})")
```

### Approach 3: Professional Formatting
```python
print("\n" + "=" * 30)
print(f"    {recipe_name.upper()}")
print("=" * 30)
print(f"Servings: {original_servings} → {desired_servings}")
print(f"Scale Factor: {scaling_factor:.1f}x")
print("-" * 30)
# Your ingredient list here
print("=" * 30)
```

## ✅ Success Criteria

Your project is successful when:
- [ ] You ask the user for recipe name, original servings, and desired servings
- [ ] You collect information for at least 3 ingredients (name, quantity, price)
- [ ] You correctly calculate the scaling factor and adjust all quantities
- [ ] You calculate and display the total cost and cost per serving
- [ ] Your output is well-formatted and professional-looking
- [ ] You can run the program multiple times with different inputs

## 🎨 Creative Extensions (Optional)

Want to make your recipe calculator even better? Try these ideas:
- Add multiple recipe templates to choose from
- Include estimated cooking/prep time calculations
- Add basic nutritional estimates (calories, protein, etc.)
- Create different measurement unit conversions (cups to grams, etc.)
- Add input validation to ensure positive numbers
- Save favorite recipes to a simple text format
- Add ingredient substitution suggestions

## 🔗 Concepts Applied

This project demonstrates mastery of:
- **Variables** (Chapter 3) → Storing recipe data and calculations
- **Operators** (Chapter 4) → Mathematical calculations for scaling and costs
- **Input/Output** (Chapter 5) → Multiple prompts, type conversion, and formatted output

## 🎉 What You've Accomplished

By completing this project, you've shown you can:
- Handle multiple related user inputs in sequence
- Perform mathematical calculations with user data
- Work with different data types (strings, integers, floats)
- Create a practical, real-world application
- Structure a program with clear input, processing, and output phases

This is a significant step up from the simple profile builder exercise. You're now ready for the decision-making concepts in Chapter 6!

## 🚀 Next Steps

Ready for more? The next chapter will introduce decision-making with `if` statements, allowing your programs to make choices based on user input and calculated values!