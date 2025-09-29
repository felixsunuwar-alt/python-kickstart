# Mini-Project: Smart Home Control System

## 🎯 Goal

Create an interactive smart home control system that uses decision-making to manage different home devices and settings. This project builds upon the selection concepts from Chapter 6 and combines them with the input/output skills from previous chapters.

## 📖 Project Description

Build a smart home controller that:
- Presents the user with different home automation scenarios
- Based on user input and conditions, controls various smart devices
- Uses multiple `if/elif/else` statements to create intelligent responses
- Considers multiple factors like time, weather, and user preferences
- Provides helpful feedback and recommendations

This is like having a smart assistant that helps you control your home environment!

## 🎮 Example Interaction

```
=== Smart Home Control System ===
Welcome to your Smart Home Assistant!

Current Status:
- Time: Evening (7 PM)
- Outside Temperature: 15°C
- Weather: Cloudy

What would you like to control?
1. Lighting
2. Temperature
3. Security
4. Entertainment
5. Exit

Enter your choice (1-5): 1

=== Lighting Control ===
Current room: Living Room
Time of day: Evening

Lighting options:
- bright: Full brightness
- dim: Soft lighting
- auto: Automatic based on time
- off: Turn off lights

What lighting setting do you want? (bright/dim/auto/off): auto

Since it's evening, I'm setting the lights to 40% brightness with warm color.
This creates a cozy atmosphere perfect for relaxing!

Energy saved: 60% compared to full brightness
Estimated cost: $0.15/hour

Would you like to control another system? (yes/no): yes

What would you like to control?
1. Lighting
2. Temperature
3. Security
4. Entertainment
5. Exit

Enter your choice (1-5): 2

=== Temperature Control ===
Current temperature: 20°C
Outside temperature: 15°C
Time: Evening

Recommended settings:
- Since it's cooler outside and evening time
- Suggested temperature: 22°C (comfortable for relaxing)

Set temperature to (18-26°C): 22

Perfect! Setting temperature to 22°C.
The heating system will gradually adjust over the next 15 minutes.
Estimated energy cost: $1.20/hour

Smart tip: This temperature is optimal for evening comfort and energy efficiency!

Would you like to control another system? (yes/no): no

Thank you for using Smart Home Control System!
Have a comfortable evening! 🏠
```

## 🧠 What You'll Practice

This project reinforces concepts from **Chapter 6: Selections**:
- Using [`if/elif/else`](../../../book/06-selections.md#if-elif-else-statement) statements for multiple device options
- [Logical operators](../../../book/06-selections.md#logical-operators-in-selections) to combine conditions (time AND weather)
- [Comparison operators](../../../book/06-selections.md#comparison-operators-in-selections) for temperature and time ranges
- [String comparisons](../../../book/06-selections.md#basic-if-statement) with user input
- Creating [menu systems](../../../book/06-selections.md#practical-applications) for device control

**Building on previous exercises:**
- Unlike [`grade-calculator`](../../exercises/06-selections/01-grade-calculator/) which uses number ranges, this uses multiple types of conditions
- Combines I/O from Chapter 5 with complex decision-making from Chapter 6
- Uses nested conditions and multiple decision points
- Provides practical, real-world application of conditional logic

## 🚀 Getting Started

1. **Open `main.py` in this folder**

2. **Follow the step-by-step approach:**
   - Start with a simple menu system (choose device type)
   - Add basic device control logic
   - Gradually add more sophisticated conditions (time, weather, etc.)
   - Add intelligent recommendations based on multiple factors
   - Test each feature to make sure it works

3. **Test your project:** `python main.py`

## 💡 Implementation Ideas

### Approach 1: Simple Device Control
```python
print("=== Smart Home Control ===")
print("What would you like to control?")
print("1. Lights")
print("2. Temperature")
print("3. Security")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    print("Controlling lights...")
    setting = input("Brightness (low/medium/high): ")
    if setting == "high":
        print("Lights set to 100% brightness")
    elif setting == "medium":
        print("Lights set to 60% brightness")
    else:
        print("Lights set to 30% brightness")
elif choice == "2":
    print("Controlling temperature...")
    # Add temperature logic
elif choice == "3":
    print("Controlling security...")
    # Add security logic
else:
    print("Invalid choice")
```

### Approach 2: Intelligent Recommendations
```python
# Get current conditions
time_of_day = input("Time of day (morning/afternoon/evening/night): ")
outside_temp = float(input("Outside temperature (°C): "))

# Make intelligent recommendations
if time_of_day == "evening" and outside_temp < 18:
    print("Recommendation: Warm lighting and increase heating")
    print("Perfect time for cozy indoor activities!")
elif time_of_day == "morning" and outside_temp > 20:
    print("Recommendation: Bright lights and fresh air circulation")
    print("Great day to open windows!")
```

### Approach 3: Multiple Condition Logic
```python
# Complex decision making
if device == "lights":
    if time_of_day == "night":
        if room == "bedroom":
            print("Setting very dim night light")
        else:
            print("Turning off lights for energy saving")
    elif time_of_day == "morning":
        if weather == "sunny":
            print("Reducing artificial light, opening blinds")
        else:
            print("Increasing brightness to compensate for clouds")
```

## ✅ Success Criteria

Your project is successful when:
- [ ] You present the user with at least 3 different device categories to control
- [ ] Each device has multiple setting options that use conditional logic
- [ ] You use `if/elif/else` statements to handle different choices
- [ ] You incorporate at least 2 environmental factors (time, temperature, weather)
- [ ] Your system provides intelligent recommendations based on conditions
- [ ] You handle invalid input gracefully
- [ ] The program can control multiple devices in one session

## 🎨 Creative Extensions (Optional)

Want to make your smart home even smarter? Try these ideas:
- Add more devices (music system, blinds, garden sprinklers)
- Create user profiles with different preferences
- Add energy usage calculations and cost estimates
- Include seasonal adjustments (summer vs winter settings)
- Add voice-like responses that feel more natural
- Create preset scenes (movie night, party mode, sleep mode)
- Add security features with different access levels

## 🔗 Concepts Applied

This project demonstrates mastery of:
- **Variables** (Chapter 3) → Storing device states and user preferences
- **Operators** (Chapter 4) → Comparison and logical operations
- **Input/Output** (Chapter 5) → Interactive menus and device feedback
- **Selections** (Chapter 6) → Complex decision trees and intelligent automation

## 🎉 What You've Accomplished

By completing this project, you've shown you can:
- Create complex decision trees with multiple factors
- Handle different types of user input and validation
- Build practical, real-world applications
- Use nested conditions and logical operators effectively
- Structure a program with clear menu systems and user flow

This is a significant step up from the simple grade categorization and demonstrates real-world application of conditional logic. You're now ready for the repetition concepts in Chapter 7!

## 🚀 Next Steps

Ready for more? The next chapter will introduce loops, allowing your programs to repeat actions and handle ongoing user interaction without restarting!