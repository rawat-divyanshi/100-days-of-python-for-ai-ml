# ==========================================================
# Day 008 - Mini Project
# Project: Utility Toolkit
# ==========================================================

print("=" * 55)
print("             PYTHON UTILITY TOOLKIT")
print("=" * 55)


# ----------------------------------------------------------
# Functions
# ----------------------------------------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


def even_odd(number):
    if number % 2 == 0:
        return "Even Number"
    return "Odd Number"


def maximum(a, b):
    if a > b:
        return a
    return b


def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact


# ----------------------------------------------------------
# Menu
# ----------------------------------------------------------

print("""
Choose an Option

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Even / Odd Checker
6. Maximum of Two Numbers
7. Factorial
""")

choice = int(input("Enter your choice (1-7): "))

print()

# ----------------------------------------------------------
# Operations
# ----------------------------------------------------------

if choice == 1:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Answer =", add(a, b))


elif choice == 2:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Answer =", subtract(a, b))


elif choice == 3:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Answer =", multiply(a, b))


elif choice == 4:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Answer =", divide(a, b))


elif choice == 5:

    number = int(input("Enter a number: "))

    print(even_odd(number))


elif choice == 6:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Maximum =", maximum(a, b))


elif choice == 7:

    number = int(input("Enter a number: "))

    print("Factorial =", factorial(number))


else:

    print("Invalid Choice!")

print()
print("=" * 55)
print("      Thank You for Using Utility Toolkit")
print("=" * 55)