"""
=========================================
Day 009 - Mini Project
Project: Student Utility System
=========================================

Features:
1. Add Student
2. Display Student
3. Calculate Percentage
4. Find Grade
5. Sum Marks using *args
6. Student Profile using **kwargs
7. Exit
"""

# ==========================================
# Global Variable
# ==========================================

students = []

# ==========================================
# Add Student
# ==========================================

def add_student():

    name = input("Enter Student Name: ")

    marks = []

    print("Enter Marks of 5 Subjects")

    for i in range(5):
        mark = float(input(f"Subject {i+1}: "))
        marks.append(mark)

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)

    print("\nStudent Added Successfully!\n")


# ==========================================
# Display Students
# ==========================================

def display_students():

    if not students:
        print("\nNo Student Found.\n")
        return

    print("\nStudent Records")
    print("-" * 40)

    for student in students:

        print("Name :", student["name"])
        print("Marks:", student["marks"])
        print()


# ==========================================
# Percentage
# ==========================================

def calculate_percentage(marks):

    total = sum(marks)

    return total / len(marks)


# ==========================================
# Grade
# ==========================================

grade = lambda p: (
    "A+" if p >= 90 else
    "A" if p >= 80 else
    "B" if p >= 70 else
    "C" if p >= 60 else
    "D" if p >= 50 else
    "Fail"
)


# ==========================================
# *args Example
# ==========================================

def total_marks(*marks):

    return sum(marks)


# ==========================================
# **kwargs Example
# ==========================================

def student_profile(**details):

    print("\nStudent Profile")
    print("-" * 30)

    for key, value in details.items():
        print(f"{key.title()} : {value}")

    print()


# ==========================================
# Recursive Countdown
# ==========================================

def countdown(n):

    if n == 0:
        print("Starting...\n")
        return

    print(n)

    countdown(n - 1)


# ==========================================
# Menu
# ==========================================

while True:

    print("=" * 45)
    print("      STUDENT UTILITY SYSTEM")
    print("=" * 45)

    print("1. Add Student")
    print("2. Display Students")
    print("3. Show Percentage & Grade")
    print("4. Sum Marks (*args)")
    print("5. Student Profile (**kwargs)")
    print("6. Countdown (Recursion)")
    print("7. Exit")

    choice = input("\nEnter Choice: ")

    # ======================================

    if choice == "1":

        add_student()

    # ======================================

    elif choice == "2":

        display_students()

    # ======================================

    elif choice == "3":

        if not students:

            print("\nNo Student Available.\n")
            continue

        for student in students:

            percentage = calculate_percentage(student["marks"])

            print("\nName :", student["name"])
            print("Percentage :", round(percentage, 2))
            print("Grade :", grade(percentage))

    # ======================================

    elif choice == "4":

        print()

        print("Total =", total_marks(78, 65, 90, 88, 95))

        print()

    # ======================================

    elif choice == "5":

        student_profile(
            name="Amit",
            age=22,
            course="Python",
            city="Haridwar"
        )

    # ======================================

    elif choice == "6":

        countdown(5)

    # ======================================

    elif choice == "7":

        print("\nThank You!")

        break

    # ======================================

    else:

        print("\nInvalid Choice\n")