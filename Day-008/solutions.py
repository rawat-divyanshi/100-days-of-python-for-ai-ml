# ==========================================================
# Day 008 - Solutions
# Topic: Functions (Part 1)
# ==========================================================

# ----------------------------------------------------------
# Q1
# greet()
# ----------------------------------------------------------

def greet():
    print("Welcome to Python Programming!")

greet()

print()


# ----------------------------------------------------------
# Q2
# show_name()
# ----------------------------------------------------------

def show_name(name):
    print("Hello,", name)

show_name("Amit")

print()


# ----------------------------------------------------------
# Q3
# add()
# ----------------------------------------------------------

def add(a, b):
    print("Sum =", a + b)

add(10, 20)

print()


# ----------------------------------------------------------
# Q4
# square()
# ----------------------------------------------------------

def square(number):
    print("Square =", number * number)

square(5)

print()


# ----------------------------------------------------------
# Q5
# even_odd()
# ----------------------------------------------------------

def even_odd(number):

    if number % 2 == 0:
        print("Even Number")

    else:
        print("Odd Number")

even_odd(12)

print()


# ==========================================================
# 🟡 Level 2
# ==========================================================

# ----------------------------------------------------------
# Q6
# maximum()
# ----------------------------------------------------------

def maximum(a, b):

    if a > b:
        print("Maximum =", a)

    else:
        print("Maximum =", b)

maximum(45, 30)

print()


# ----------------------------------------------------------
# Q7
# area_rectangle()
# ----------------------------------------------------------

def area_rectangle(length, width):
    return length * width

area = area_rectangle(10, 5)

print("Area =", area)

print()


# ----------------------------------------------------------
# Q8
# factorial()
# ----------------------------------------------------------

def factorial(number):

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact

print("Factorial =", factorial(5))

print()


# ----------------------------------------------------------
# Q9
# is_prime()
# ----------------------------------------------------------

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True

print(is_prime(13))

print()


# ----------------------------------------------------------
# Q10
# table()
# ----------------------------------------------------------

def table(number):

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

table(7)

print()


# ==========================================================
# 🔴 Level 3
# ==========================================================

# ----------------------------------------------------------
# Q11
# calculator()
# ----------------------------------------------------------

def calculator(num1, operator, num2):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        return num1 / num2

    else:
        return "Invalid Operator"

print(calculator(10, "+", 20))

print()


# ----------------------------------------------------------
# Q12
# fibonacci()
# ----------------------------------------------------------

def fibonacci(terms):

    first = 0
    second = 1

    for i in range(terms):

        print(first, end=" ")

        next_number = first + second
        first = second
        second = next_number

fibonacci(10)

print("\n")


# ----------------------------------------------------------
# Q13
# count_vowels()
# ----------------------------------------------------------

def count_vowels(text):

    vowels = "aeiouAEIOU"
    count = 0

    for letter in text:

        if letter in vowels:
            count += 1

    return count

print("Total Vowels =", count_vowels("Python Programming"))

print()


# ----------------------------------------------------------
# Q14
# reverse_string()
# ----------------------------------------------------------

def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))

print()


# ----------------------------------------------------------
# Q15
# student_result()
# ----------------------------------------------------------

def student_result(name, marks):

    if marks >= 90:
        grade = "Grade A"

    elif marks >= 75:
        grade = "Grade B"

    elif marks >= 50:
        grade = "Grade C"

    else:
        grade = "Fail"

    return f"{name} : {grade}"

print(student_result("Amit", 88))

print()


# ==========================================================
# ⭐ Bonus Challenge
# Utility Functions Program
# ==========================================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def even_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"


def maximum(a, b):

    if a > b:
        return a

    return b


print("===== Utility Functions =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Even/Odd Checker")
print("6. Maximum Number")

choice = int(input("Enter your choice: "))

print()

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

else:
    print("Invalid Choice")

print()

# ==========================================================
# End of Solutions
# ==========================================================