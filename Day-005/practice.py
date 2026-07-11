# ==========================================================
# Day 005 - Practice
# Topic: Conditional Statements
# ==========================================================

# ----------------------------------------------------------
# Example 1: Comparison Operators
# ----------------------------------------------------------

# Comparison operators compare two values.
# They always return either True or False.

print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 5)
print(10 >= 18)
print(15 <= 20)

print()


# ----------------------------------------------------------
# Example 2: if Statement
# ----------------------------------------------------------

# Execute the code only if the condition is True.

age = 20

if age >= 18:
    print("You are eligible to vote.")

print()


# ----------------------------------------------------------
# Example 3: if Statement (False Condition)
# ----------------------------------------------------------

age = 15

if age >= 18:
    print("You are eligible to vote.")

# Nothing will be printed because the condition is False.

print()


# ----------------------------------------------------------
# Example 4: if...else Statement
# ----------------------------------------------------------

# If the condition is True, execute the if block.
# Otherwise, execute the else block.

age = 16

if age >= 18:
    print("Eligible to Vote")

else:
    print("Not Eligible")

print()


# ----------------------------------------------------------
# Example 5: Even or Odd
# ----------------------------------------------------------

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")

print()


# ----------------------------------------------------------
# Example 6: if...elif...else
# ----------------------------------------------------------

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

print()


# ----------------------------------------------------------
# Example 7: Nested if
# ----------------------------------------------------------

# A nested if means one if statement inside another.

age = 20
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to Vote")

    else:
        print("Not a Citizen")

else:
    print("Under Age")

print()


# ----------------------------------------------------------
# Example 8: Ternary Operator
# ----------------------------------------------------------

# Short way to write if...else.

age = 22

result = "Adult" if age >= 18 else "Minor"

print(result)

print()


# ----------------------------------------------------------
# Example 9: Positive, Negative or Zero
# ----------------------------------------------------------

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")

print()


# ----------------------------------------------------------
# Example 10: Largest of Two Numbers
# ----------------------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greater Number:", num1)

else:
    print("Greater Number:", num2)

print()


# ----------------------------------------------------------
# Example 11: Password Checker
# ----------------------------------------------------------

password = input("Enter Password: ")

if password == "python123":
    print("Login Successful")

else:
    print("Wrong Password")

print()


# ----------------------------------------------------------
# Example 12: Combined Example
# ----------------------------------------------------------

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 50:
    grade = "C"

else:
    grade = "Fail"

print()

print("========== REPORT ==========")
print(f"Student : {name}")
print(f"Marks   : {marks}")
print(f"Result  : {grade}")
print("============================")

print()

print("===== End of Day 005 Practice =====")