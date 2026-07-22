"""
=========================================
Day 011 - Mini Project
Project: Employee Directory System
=========================================

Features:
1. View All Employees
2. Search Employee by ID
3. Count Employees
4. Display Highest Salary
5. Display Average Salary
6. Exit

Concepts Used:
- Tuples
- Nested Tuples
- Indexing
- Slicing
- Loops
- Functions
- Packing & Unpacking
"""

# ==========================================
# Employee Records (Read-Only)
# ==========================================

employees = (
    ("E101", "Amit", "Developer", 60000),
    ("E102", "Rahul", "Designer", 55000),
    ("E103", "Riya", "Data Analyst", 65000),
    ("E104", "Priya", "HR", 50000),
    ("E105", "Arjun", "Manager", 80000)
)


# ==========================================
# View All Employees
# ==========================================

def view_employees():

    print("\n========== Employee Records ==========\n")

    for employee in employees:

        emp_id, name, department, salary = employee

        print(f"ID         : {emp_id}")
        print(f"Name       : {name}")
        print(f"Department : {department}")
        print(f"Salary     : ₹{salary}")
        print("-" * 35)


# ==========================================
# Search Employee
# ==========================================

def search_employee():

    emp_id = input("\nEnter Employee ID: ").upper()

    found = False

    for employee in employees:

        if employee[0] == emp_id:

            print("\nEmployee Found\n")

            print("ID         :", employee[0])
            print("Name       :", employee[1])
            print("Department :", employee[2])
            print("Salary     : ₹", employee[3])

            found = True
            break

    if not found:
        print("\nEmployee Not Found.")


# ==========================================
# Count Employees
# ==========================================

def count_employees():

    print("\nTotal Employees:", len(employees))


# ==========================================
# Highest Salary
# ==========================================

def highest_salary():

    highest = employees[0]

    for employee in employees:

        if employee[3] > highest[3]:
            highest = employee

    print("\nHighest Salary Employee")

    print("ID         :", highest[0])
    print("Name       :", highest[1])
    print("Department :", highest[2])
    print("Salary     : ₹", highest[3])


# ==========================================
# Average Salary
# ==========================================

def average_salary():

    total = 0

    for employee in employees:
        total += employee[3]

    average = total / len(employees)

    print("\nAverage Salary: ₹", round(average, 2))


# ==========================================
# Main Menu
# ==========================================

while True:

    print("\n" + "=" * 45)
    print("      EMPLOYEE DIRECTORY SYSTEM")
    print("=" * 45)

    print("1. View All Employees")
    print("2. Search Employee by ID")
    print("3. Count Employees")
    print("4. Display Highest Salary")
    print("5. Display Average Salary")
    print("6. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        view_employees()

    elif choice == "2":
        search_employee()

    elif choice == "3":
        count_employees()

    elif choice == "4":
        highest_salary()

    elif choice == "5":
        average_salary()

    elif choice == "6":
        print("\nThank You for using Employee Directory System!")
        break

    else:
        print("\nInvalid Choice! Please try again.")