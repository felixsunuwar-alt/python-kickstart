# Mini-Project: Smart Home Control System
# Build upon the grade-calculator exercise by creating an intelligent home automation system!

# 📖 IMPORTANT: Read the README.md file first for detailed instructions,
#    examples, and ideas on how to approach this project!

# This project builds on what you learned in the grade-calculator exercise:
# - Using if/elif/else statements for multiple conditions
# - Handling different types of user input
# - Creating logical decision trees
# - Providing appropriate feedback based on conditions

# TODO: Create your Smart Home Control System here!

# Here's a simple example to get you started:
print("=== Smart Home Control System ===")
print("Welcome to your Smart Home Assistant!\n")

# Get current conditions
print("Current Status:")
time_of_day = input("What time is it? (morning/afternoon/evening/night): ")
outside_temp = float(input("Outside temperature (°C): "))

print(f"- Time: {time_of_day.title()}")
print(f"- Outside Temperature: {outside_temp}°C")

# Simple device menu
print("\nWhat would you like to control?")
print("1. Lighting")
print("2. Temperature")
print("3. Security")

choice = input("Enter your choice (1-3): ")

# Basic device control
if choice == "1":
    print("\n=== Lighting Control ===")
    setting = input("Lighting setting (bright/dim/auto/off): ")
    
    if setting == "auto":
        if time_of_day == "evening" or time_of_day == "night":
            print("Setting lights to dim for evening comfort")
        else:
            print("Setting lights to bright for daytime activities")
    elif setting == "bright":
        print("Lights set to 100% brightness")
    elif setting == "dim":
        print("Lights set to 30% brightness")
    else:
        print("Lights turned off")
        
elif choice == "2":
    print("\n=== Temperature Control ===")
    temp = float(input("Set temperature (18-26°C): "))
    
    if temp >= 18 and temp <= 26:
        print(f"Temperature set to {temp}°C")
        if temp > outside_temp + 5:
            print("Note: This setting may use more energy due to outside temperature")
    else:
        print("Temperature must be between 18-26°C")
        
else:
    print("\n=== Security Control ===")
    print("Security system activated")

print("\nThank you for using Smart Home Control System!")

# YOUR TURN: 
# 1. Add more device categories and options
# 2. Create intelligent recommendations based on time and weather
# 3. Add nested conditions for more sophisticated logic
# 4. Include energy usage estimates and helpful tips
# 5. Allow controlling multiple devices in one session
# 6. Handle invalid input gracefully

# HINTS:
# - Use nested if statements for complex logic
# - Combine conditions with 'and' and 'or' operators
# - Use string methods like .lower() for input validation
# - Add loops to allow multiple device controls (Chapter 7 preview!)

# Remember: This is YOUR project - make it smart and useful!