# ==========================================================
# Day 004 - Mini Project
# Project: Student Profile Generator
# ==========================================================

print("=" * 50)
print("        STUDENT PROFILE GENERATOR")
print("=" * 50)

# ----------------------------------------------------------
# Take user input
# ----------------------------------------------------------

name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: "))
city = input("Enter your city: ").strip().title()
course = input("Enter your course: ").strip()

print()

# ----------------------------------------------------------
# Display Student Profile
# ----------------------------------------------------------

print("=" * 50)
print("              STUDENT PROFILE")
print("=" * 50)

print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"City   : {city}")
print(f"Course : {course}")

print("-" * 50)

# ----------------------------------------------------------
# Some Useful Information
# ----------------------------------------------------------

print(f"After 5 years, you will be {age + 5} years old.")
print(f"Your name in UPPERCASE : {name.upper()}")
print(f"Your name in lowercase : {name.lower()}")

print("=" * 50)
print("      Thank you for using the program!")
print("=" * 50)