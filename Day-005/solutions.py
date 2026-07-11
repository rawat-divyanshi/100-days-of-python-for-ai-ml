# ==========================================================
# Day 005 - Solutions
# Topic: Conditional Statements
# ==========================================================

# ----------------------------------------------------------
# Q1
# Check if the user is eligible to vote.
# ----------------------------------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")

print()


# ----------------------------------------------------------
# Q2
# Check whether the number is positive.
# ----------------------------------------------------------

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")

print()


# ----------------------------------------------------------
# Q3
# Check whether the student has passed.
# ----------------------------------------------------------

marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Pass")

print()


# ----------------------------------------------------------
# Q4
# Password Verification
# ----------------------------------------------------------

password = input("Enter password: ")

if password == "python123":
    print("Login Successful")

print()


# ----------------------------------------------------------
# Q5
# Check whether a number is even.
# ----------------------------------------------------------

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")

print()


# ==========================================================
# 🟡 Level 2
# ==========================================================

# ----------------------------------------------------------
# Q6
# Voting Eligibility
# ----------------------------------------------------------

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

print()


# ----------------------------------------------------------
# Q7
# Find the greater number.
# ----------------------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greater Number:", num1)
else:
    print("Greater Number:", num2)

print()


# ----------------------------------------------------------
# Q8
# Even or Odd
# ----------------------------------------------------------

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

print()


# ----------------------------------------------------------
# Q9
# Positive, Negative or Zero
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
# Q10
# Grade Calculator
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


# ==========================================================
# 🔴 Level 3
# ==========================================================

# ----------------------------------------------------------
# Q11
# Login System
# ----------------------------------------------------------

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "python123":
    print("Login Successful")

else:
    print("Invalid Credentials")

print()


# ----------------------------------------------------------
# Q12
# Leap Year Checker
# ----------------------------------------------------------

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")

else:
    print("Not a Leap Year")

print()


# ----------------------------------------------------------
# Q13
# Largest of Three Numbers
# ----------------------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest Number:", num1)

elif num2 >= num1 and num2 >= num3:
    print("Largest Number:", num2)

else:
    print("Largest Number:", num3)

print()


# ----------------------------------------------------------
# Q14
# Age Category
# ----------------------------------------------------------

age = int(input("Enter your age: "))

if age <= 12:
    print("Child")

elif age <= 19:
    print("Teenager")

elif age <= 59:
    print("Adult")

else:
    print("Senior Citizen")

print()


# ----------------------------------------------------------
# Q15
# Ternary Operator
# ----------------------------------------------------------

number = int(input("Enter a number: "))

result = "Positive" if number >= 0 else "Negative"

print(result)

print()


# ==========================================================
# ⭐ Bonus Challenge
# Grade Calculator
# ==========================================================

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
    print("Congratulations!")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

else:
    print("Fail")

print()

# ==========================================================
# End of Solutions
# ==========================================================