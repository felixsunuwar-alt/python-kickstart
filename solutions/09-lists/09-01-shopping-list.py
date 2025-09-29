# Exercise 9.1: Shopping List Manager - Solution
# Complete implementation of shopping list management using lists

print("=== Shopping List Manager ===")

# Create an empty shopping list
shopping_list = []
print(f"Starting with an empty list: {shopping_list}")

print("\nAdding items to the list...")
# Add items to the shopping list
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")
shopping_list.append("apples")
shopping_list.append("cheese")

# Display the current list
print(f"Current list: {shopping_list}")

print("\nShopping List:")
# Display each item with its position number
for i in range(len(shopping_list)):
    print(f"{i + 1}. {shopping_list[i]}")

# Remove "bread" from the list
print("\nRemoving 'bread' from the list...")
shopping_list.remove("bread")

# Display the updated list
print(f"Updated list: {shopping_list}")

# Display the final count of items
print(f"\nFinal shopping list has {len(shopping_list)} items.")