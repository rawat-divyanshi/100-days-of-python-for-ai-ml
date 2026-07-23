"""
====================================================
Day 012 - Mini Project
Project: Student Management System
====================================================

Features:
1. Add Student
2. View All Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Show Class Statistics
7. Exit

Concepts Used:
✔ Dictionaries
✔ Dictionary Methods
✔ Loops
✔ Functions
✔ Conditional Statements
✔ get()
✔ keys()
✔ values()
✔ items()

"""

students = {}


# ==========================================
# Add Student
# ==========================================
def add_student():

    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists.")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    students[roll_no] = {
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    print("Student added successfully!")


# ==========================================
# View Students
# ==========================================
def view_students():

    if not students:
        print("No student records found.")
        return

    print("\n========== Student Records ==========")

    for roll_no, details in students.items():

        print(f"\nRoll No : {roll_no}")

        for key, value in details.items():
            print(f"{key}: {value}")


# ==========================================
# Search Student
# ==========================================
def search_student():

    roll_no = input("Enter Roll Number: ")

    student = students.get(roll_no)

    if student:

        print("\nStudent Found")

        for key, value in student.items():
            print(f"{key}: {value}")

    else:
        print("Student not found.")


# ==========================================
# Update Marks
# ==========================================
def update_marks():

    roll_no = input("Enter Roll Number: ")

    if roll_no in students:

        new_marks = float(input("Enter New Marks: "))

        students[roll_no]["Marks"] = new_marks

        print("Marks updated successfully!")

    else:
        print("Student not found.")


# ==========================================
# Delete Student
# ==========================================
def delete_student():

    roll_no = input("Enter Roll Number: ")

    if roll_no in students:

        del students[roll_no]

        print("Student deleted successfully!")

    else:
        print("Student not found.")


# ==========================================
# Class Statistics
# ==========================================
def class_statistics():

    if not students:
        print("No records available.")
        return

    marks = [student["Marks"] for student in students.values()]

    print("\n========== Class Statistics ==========")

    print("Total Students :", len(students))
    print("Highest Marks  :", max(marks))
    print("Lowest Marks   :", min(marks))
    print("Average Marks  :", round(sum(marks) / len(marks), 2))


# ==========================================
# Menu
# ==========================================
while True:

    print("\n=================================")
    print(" STUDENT MANAGEMENT SYSTEM")
    print("=================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Class Statistics")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

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
        class_statistics()

    elif choice == "7":

        print("\nThank you for using Student Management System.")
        break

    else:
        print("Invalid choice! Please try again.")