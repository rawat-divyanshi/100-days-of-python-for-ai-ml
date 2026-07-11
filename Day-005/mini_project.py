# ==========================================================
# Day 005 - Mini Project
# Project: Student Result Management System
# ==========================================================

print("=" * 50)
print("      STUDENT RESULT MANAGEMENT SYSTEM")
print("=" * 50)

# ----------------------------------------------------------
# Take Input
# ----------------------------------------------------------

name = input("Enter Student Name: ").title()
marks = int(input("Enter Marks (0-100): "))
attendance = int(input("Enter Attendance Percentage: "))

print()

# ----------------------------------------------------------
# Check Attendance
# ----------------------------------------------------------

if attendance < 75:
    print("Status : Detained due to low attendance.")
else:

    # ------------------------------------------------------
    # Calculate Grade
    # ------------------------------------------------------

    if marks >= 90:
        grade = "A+"

    elif marks >= 80:
        grade = "A"

    elif marks >= 70:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    elif marks >= 40:
        grade = "D"

    else:
        grade = "F"

    # ------------------------------------------------------
    # Result using Ternary Operator
    # ------------------------------------------------------

    result = "PASS" if marks >= 40 else "FAIL"

    # ------------------------------------------------------
    # Display Report Card
    # ------------------------------------------------------

    print("=" * 50)
    print("             STUDENT REPORT CARD")
    print("=" * 50)

    print(f"Student Name : {name}")
    print(f"Marks        : {marks}")
    print(f"Attendance   : {attendance}%")
    print(f"Grade        : {grade}")
    print(f"Result       : {result}")

    print("-" * 50)

    if result == "PASS":
        print("Congratulations! Keep working hard.")

    else:
        print("Better luck next time. Keep practicing.")

print("=" * 50)
print("        Thank You for Using the Program")
print("=" * 50)