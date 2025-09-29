# Exercise 1: Shopping List Manager

Create a program that uses lists to manage a shopping list with add, remove, and display functionality.

## 📖 Before You Start

**⚠️ IMPORTANT: Read Chapter 9 first!**

Before attempting this exercise, make sure you have:
- ✅ Read **Chapter 9: Lists** in the `book/09-lists.md` file
- ✅ Understood how to create and manipulate lists
- ✅ Learned about list methods like `append()`, `remove()`, and `pop()`
- ✅ Practiced iterating through lists with loops

This exercise will help you practice working with lists to store and manage collections of data.

## 🎯 Goal

Create a program that manages a shopping list using list operations to add items, remove items, and display the current list.

## 📚 What You'll Learn

- How to create and modify lists
- How to use list methods for adding and removing items
- How to iterate through lists to display contents
- How to work with list indices and length

## 📝 Instructions

1. **Open the file**: Look at the `main.py` file in this folder
2. **Write your code**: Create a shopping list manager that:
   - Creates an empty shopping list
   - Adds several items to the list using `append()`
   - Displays all items in the list with their positions
   - Removes an item from the list using `remove()`
   - Shows the final list and its length
3. **Test your code**: Run your script to see if it works:
   ```bash
   python exercises/09-lists/01-shopping-list/main.py
   ```
4. **Check with tests**: Run the automated test to verify your solution:
   ```bash
   pytest tests/test_09_lists.py::TestExercise09_01::test_shopping_list_operations -v
   ```

## 💡 Hints

- Create an empty list: `shopping_list = []`
- Add items: `shopping_list.append("item")`
- Remove items: `shopping_list.remove("item")`
- Get list length: `len(shopping_list)`
- Loop through with index: `for i in range(len(shopping_list)):`
- Loop through items: `for item in shopping_list:`

## ✅ Expected Output

When you run your program, you should see something like:
```
=== Shopping List Manager ===
Starting with an empty list: []

Adding items to the list...
Current list: ['milk', 'bread', 'eggs', 'apples', 'cheese']

Shopping List:
1. milk
2. bread
3. eggs
4. apples
5. cheese

Removing 'bread' from the list...
Updated list: ['milk', 'eggs', 'apples', 'cheese']

Final shopping list has 4 items.
```

## 🎉 Success!

Once your program works, you've successfully:
- ✅ Created and manipulated lists
- ✅ Used list methods to add and remove items
- ✅ Iterated through lists to display contents
- ✅ Worked with list length and indexing

Ready for the next exercise? Great work! 🚀