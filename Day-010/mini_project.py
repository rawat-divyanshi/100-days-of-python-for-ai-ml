"""
=========================================
Day 010 - Mini Project
Project: Student Record Management System
=========================================

Features:
1. Add Student
2. View Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Sort Students
7. Highest Marks
8. Average Marks
9. Exit
"""

students = []


# ==========================================
# Add Student
# ==========================================

def add_student():

    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    student = [name, marks]

    students.append(student)

    print("\nStudent Added Successfully!\n")


# ==========================================
# View Students
# ==========================================

def view_students():

    if len(students) == 0:
        print("\nNo Student Records Found.\n")
        return

    print("\nStudent Records")
    print("-" * 35)

    for student in students:
        print("Name :", student[0])
        print("Marks:", student[1])
        print()


# ==========================================
# Search Student
# ==========================================

def search_student():

    name = input("Enter Student Name: ")

    found = False

    for student in students:

        if student[0].lower() == name.lower():

            print("\nStudent Found")
            print("Name :", student[0])
            print("Marks:", student[1])

            found = True
            break

    if not found:
        print("\nStudent Not Found.")


# ==========================================
# Update Marks
# ==========================================

def update_marks():

    name = input("Enter Student Name: ")

    for student in students:

        if student[0].lower() == name.lower():

            marks = int(input("Enter New Marks: "))

            student[1] = marks

            print("\nMarks Updated Successfully!")

            return

    print("\nStudent Not Found.")


# ==========================================
# Delete Student
# ==========================================

def delete_student():

    name = input("Enter Student Name: ")

    for student in students:

        if student[0].lower() == name.lower():

            students.remove(student)

            print("\nStudent Deleted Successfully!")

            return

    print("\nStudent Not Found.")


# ==========================================
# Sort Students
# ==========================================

def sort_students():

    if len(students) == 0:
        print("\nNo Records Found.")
        return

    students.sort()

    print("\nStudents Sorted Successfully!")


# ==========================================
# Highest Marks
# ==========================================

def highest_marks():

    if len(students) == 0:
        print("\nNo Student Records.")
        return

    highest = students[0]

    for student in students:

        if student[1] > highest[1]:
            highest = student

    print("\nTop Performer")
    print("Name :", highest[0])
    print("Marks:", highest[1])


# ==========================================
# Average Marks
# ==========================================

def average_marks():

    if len(students) == 0:
        print("\nNo Student Records.")
        return

    total = 0

    for student in students:
        total += student[1]

    average = total / len(students)

    print("\nAverage Marks:", round(average, 2))


# ==========================================
# Main Menu
# ==========================================

while True:

    print("=" * 45)
    print("     STUDENT RECORD MANAGEMENT")
    print("=" * 45)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Sort Students")
    print("7. Highest Marks")
    print("8. Average Marks")
    print("9. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        view_students()

    elif choice == "3":

        search_student()

    elif choice == "4":

        update_marks()

    elif choice == "5":

        delete_student()

    elif choice == "6":

        sort_students()

    elif choice == "7":

        highest_marks()

    elif choice == "8":

        average_marks()

    elif choice == "9":

        print("\nThank You!")
        break

    else:

        print("\nInvalid Choice! Try Again.\n")