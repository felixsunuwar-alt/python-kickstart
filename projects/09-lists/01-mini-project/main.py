# Mini-Project: Student Grade Tracker
# Build upon list exercises by creating a comprehensive academic data management system!

# 📖 IMPORTANT: Read the README.md file first for detailed instructions,
#    examples, and ideas on how to approach this project!

# This project builds on what you learned in list exercises:
# - Creating and managing lists of related data
# - Using parallel lists for complex data relationships
# - Combining lists with loops for data processing
# - Using list methods for adding and accessing data

# TODO: Create your Student Grade Tracker here!

# Here's a simple example to get you started:

# Parallel lists to store related data
students = []
subjects = []
grades = []

def add_grade(student_name, subject_name, grade_value):
    """Add a new grade to the tracking system"""
    students.append(student_name)
    subjects.append(subject_name)
    grades.append(grade_value)
    print("Grade added successfully!")

def display_all_grades():
    """Display all grades in a simple format"""
    print("\n=== All Grades ===")
    for i in range(len(students)):
        print(f"{students[i]} - {subjects[i]}: {grades[i]}")

def calculate_class_average():
    """Calculate the overall class average"""
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def show_menu():
    """Display the main menu"""
    print("\n=== Student Grade Tracker ===")
    print("1. Add Student Grade")
    print("2. View All Grades")
    print("3. Calculate Class Average")
    print("4. Exit")

# Simple demonstration
print("=== Student Grade Tracker ===")
print("Track and analyze academic performance!")

# Add some sample data
add_grade("Alice Johnson", "Mathematics", 87)
add_grade("Bob Smith", "Science", 92)

# Display the data
display_all_grades()

# Show statistics
average = calculate_class_average()
print(f"\nClass Average: {average:.1f}")

print("\nThank you for using Student Grade Tracker!")

# YOUR TURN: 
# 1. Create a main program loop with menu system
# 2. Add functions to find highest and lowest grades
# 3. Calculate averages by student and by subject
# 4. Add performance analysis and recommendations
# 5. Implement better data organization and display
# 6. Add input validation for grades (0-100)

# HINTS:
# - Use parallel lists: students[], subjects[], grades[]
# - Use list methods: append(), index(), max(), min()
# - Use loops to process all data in lists
# - Create helper functions for calculations
# - Use dictionaries for grouping data by student/subject
# - Provide meaningful analysis and recommendations

# Remember: This is YOUR project - make it useful for educators!