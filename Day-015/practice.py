"""
Day 15 – Exception Handling
100 Days of Python for AI/ML

Practice Programs:
- try
- except
- else
- finally
- Multiple exceptions
- raise
- Custom exceptions
- Input validation

Try to solve each program yourself before checking the solution.
"""


# ============================================================
# PART 1 – BASIC EXCEPTION HANDLING
# ============================================================

# Program 1
# Handle division by zero.

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Program 2
# Handle invalid integer input.

try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)
except ValueError:
    print("Please enter a valid integer.")


# Program 3
# Convert user input to float and handle ValueError.

try:
    number = float(input("Enter a decimal number: "))
    print("Number:", number)
except ValueError:
    print("Invalid decimal number.")


# Program 4
# Handle TypeError.

try:
    result = "10" + 5
    print(result)
except TypeError:
    print("Cannot add a string and an integer.")


# Program 5
# Handle IndexError.

numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter an index: "))
    print("Value:", numbers[index])
except ValueError:
    print("Index must be an integer.")
except IndexError:
    print("Index is outside the list range.")


# Program 6
# Handle KeyError.

student = {
    "name": "Amit",
    "age": 22,
    "course": "Python"
}

try:
    key = input("Enter a key: ")
    print("Value:", student[key])
except KeyError:
    print("Key does not exist.")


# Program 7
# Handle FileNotFoundError.

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")


# Program 8
# Handle ValueError and ZeroDivisionError.

try:
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))

    result = first / second

    print("Result:", result)

except ValueError:
    print("Please enter valid integers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# Program 9
# Handle multiple exceptions together.

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")


# Program 10
# Create a safe calculator for two numbers.

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    print("Division:", a / b)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")


# ============================================================
# PART 2 – try, except, else
# ============================================================

# Program 11
# Use try-except-else for integer validation.

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input.")
else:
    print("Valid integer:", number)


# Program 12
# Calculate the square of a number using try-except-else.

try:
    number = float(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
else:
    print("Square:", number ** 2)


# Program 13
# Calculate the average of two numbers.

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    print("Please enter valid numbers.")
else:
    average = (a + b) / 2
    print("Average:", average)


# Program 14
# Check whether a number is even or odd.

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid integer.")
else:
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


# Program 15
# Calculate the area of a rectangle.

try:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
except ValueError:
    print("Invalid input.")
else:
    area = length * width
    print("Area:", area)


# Program 16
# Use else to display a successful login message.

try:
    username = input("Username: ")
    password = input("Password: ")

    if username == "" or password == "":
        raise ValueError("Username and password cannot be empty.")

except ValueError as error:
    print("Login error:", error)

else:
    print("Input received successfully.")


# ============================================================
# PART 3 – finally
# ============================================================

# Program 17
# Demonstrate finally.

try:
    number = int(input("Enter a number: "))
    print("Number:", number)
except ValueError:
    print("Invalid input.")
finally:
    print("Program execution completed.")


# Program 18
# Use finally with division.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Calculation finished.")


# Program 19
# Use finally with file handling.

try:
    with open("example.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("example.txt was not found.")

finally:
    print("File operation completed.")


# Program 20
# Use try, except, else and finally together.

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Age must be an integer.")

else:
    print("Your age is:", age)

finally:
    print("Age validation completed.")


# ============================================================
# PART 4 – MULTIPLE EXCEPTIONS
# ============================================================

# Program 21
# Handle ValueError and ZeroDivisionError separately.

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator

except ValueError:
    print("Please enter integers.")

except ZeroDivisionError:
    print("Denominator cannot be zero.")

else:
    print("Result:", result)


# Program 22
# Handle ValueError and IndexError.

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print(numbers[index])

except ValueError:
    print("Index must be an integer.")

except IndexError:
    print("Index does not exist.")


# Program 23
# Handle KeyError and ValueError.

student = {
    "name": "Amit",
    "age": 22,
    "marks": 85
}

try:
    key = input("Enter key: ")
    value = student[key]

    number = int(input("Enter another integer: "))

    print("Dictionary value:", value)
    print("Integer:", number)

except KeyError:
    print("Key does not exist.")

except ValueError:
    print("Invalid integer.")


# Program 24
# Handle multiple exceptions using one except block.

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except (ValueError, ZeroDivisionError):
    print("Something went wrong with your input.")


# Program 25
# Create a safe list access program.

numbers = [5, 10, 15, 20, 25]

try:
    index = int(input("Enter an index: "))
    value = numbers[index]

except ValueError:
    print("Please enter an integer index.")

except IndexError:
    print("That index does not exist.")

else:
    print("Selected value:", value)

finally:
    print("List operation completed.")


# ============================================================
# PART 5 – raise
# ============================================================

# Program 26
# Raise ValueError if age is negative.

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Valid age:", age)

except ValueError as error:
    print("Error:", error)


# Program 27
# Raise ValueError if marks are outside 0–100.

try:
    marks = float(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    print("Valid marks:", marks)

except ValueError as error:
    print("Error:", error)


# Program 28
# Raise ValueError if a number is not positive.

try:
    number = int(input("Enter a positive number: "))

    if number <= 0:
        raise ValueError("Number must be positive.")

    print("Valid number:", number)

except ValueError as error:
    print("Error:", error)


# Program 29
# Raise ValueError if password is too short.

try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")

    print("Valid password.")

except ValueError as error:
    print("Error:", error)


# Program 30
# Validate age between 0 and 120.

try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

    print("Valid age.")

except ValueError as error:
    print("Error:", error)


# ============================================================
# PART 6 – CUSTOM EXCEPTIONS
# ============================================================

# Program 31
# Create and use a custom AgeError.

class AgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise AgeError("Age cannot be negative.")

    print("Valid age.")

except AgeError as error:
    print("Age Error:", error)


# Program 32
# Create a custom MarksError.

class MarksError(Exception):
    pass


try:
    marks = float(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise MarksError("Marks must be between 0 and 100.")

    print("Valid marks.")

except MarksError as error:
    print("Marks Error:", error)

except ValueError:
    print("Marks must be a number.")


# Program 33
# Create a custom PasswordError.

class PasswordError(Exception):
    pass


try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise PasswordError(
            "Password must contain at least 8 characters."
        )

    print("Valid password.")

except PasswordError as error:
    print("Password Error:", error)


# Program 34
# Create a custom BalanceError.

class BalanceError(Exception):
    pass


balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise BalanceError("Withdrawal amount must be positive.")

    if amount > balance:
        raise BalanceError("Insufficient balance.")

    balance -= amount

    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except BalanceError as error:
    print("Balance Error:", error)

except ValueError:
    print("Please enter a valid amount.")


# Program 35
# Create a custom ValidationError.

class ValidationError(Exception):
    pass


try:
    name = input("Enter your name: ")

    if not name.strip():
        raise ValidationError("Name cannot be empty.")

    print("Valid name:", name)

except ValidationError as error:
    print("Validation Error:", error)


# ============================================================
# PART 7 – INPUT VALIDATION
# ============================================================

# Program 36
# Number Validator
#
# Requirements:
# - Must be an integer
# - Must be positive

try:
    number = int(input("Enter a positive integer: "))

    if number <= 0:
        raise ValueError("Number must be positive.")

except ValueError as error:
    print("Invalid input:", error)

else:
    print("Valid number:", number)


# Program 37
# Age Validator
#
# Requirements:
# - Integer
# - Between 0 and 120

try:
    age = int(input("Enter age: "))

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

except ValueError as error:
    print("Invalid age:", error)

else:
    print("Valid age:", age)


# Program 38
# Marks Validator
#
# Requirements:
# - Number
# - Between 0 and 100

try:
    marks = float(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

except ValueError as error:
    print("Invalid marks:", error)

else:
    print("Valid marks:", marks)


# Program 39
# Username Validator
#
# Requirements:
# - Cannot be empty
# - At least 5 characters

try:
    username = input("Enter username: ")

    if not username.strip():
        raise ValueError("Username cannot be empty.")

    if len(username) < 5:
        raise ValueError(
            "Username must contain at least 5 characters."
        )

except ValueError as error:
    print("Invalid username:", error)

else:
    print("Valid username:", username)


# Program 40
# Password Validator
#
# Requirements:
# - At least 8 characters
# - Cannot be empty

try:
    password = input("Enter password: ")

    if not password:
        raise ValueError("Password cannot be empty.")

    if len(password) < 8:
        raise ValueError(
            "Password must contain at least 8 characters."
        )

except ValueError as error:
    print("Invalid password:", error)

else:
    print("Valid password.")


# ============================================================
# PART 8 – PRACTICAL PROGRAMS
# ============================================================

# Program 41
# Simple Calculator
#
# Ask for:
# - First number
# - Operator
# - Second number
#
# Handle invalid input and division by zero.

try:
    first = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    second = float(input("Enter second number: "))

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        result = first / second
    else:
        raise ValueError("Invalid operator.")

except ValueError as error:
    print("Error:", error)

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)


# Program 42
# Student Marks Validator

try:
    math_marks = float(input("Mathematics marks: "))
    python_marks = float(input("Python marks: "))
    aiml_marks = float(input("AI/ML marks: "))

    marks = [math_marks, python_marks, aiml_marks]

    for mark in marks:
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100.")

    average = sum(marks) / len(marks)

except ValueError as error:
    print("Invalid marks:", error)

else:
    print("Average Marks:", average)


# Program 43
# Login Validator

username = "admin"
password = "python123"

try:
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")

    if entered_username != username:
        raise ValueError("Incorrect username.")

    if entered_password != password:
        raise ValueError("Incorrect password.")

except ValueError as error:
    print("Login Error:", error)

else:
    print("Login successful.")


# Program 44
# Division Calculator with Retry

while True:
    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        result = first / second

    except ValueError:
        print("Please enter valid numbers.")
        continue

    except ZeroDivisionError:
        print("Cannot divide by zero.")
        continue

    else:
        print("Result:", result)
        break


# Program 45
# File Reader

filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile Content:")
        print(content)

except FileNotFoundError:
    print("File was not found.")

except PermissionError:
    print("Permission denied.")

finally:
    print("File operation completed.")


# ============================================================
# PART 9 – MORE PRACTICE
# ============================================================

# Program 46
# Validate a person's name and age.

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

except ValueError as error:
    print("Validation Error:", error)

else:
    print("Name:", name)
    print("Age:", age)

finally:
    print("Validation completed.")


# Program 47
# Validate an email address.
#
# Basic rule:
# Email must contain "@".

try:
    email = input("Enter email: ")

    if not email.strip():
        raise ValueError("Email cannot be empty.")

    if "@" not in email:
        raise ValueError("Email must contain '@'.")

except ValueError as error:
    print("Invalid email:", error)

else:
    print("Valid email:", email)


# Program 48
# Validate three inputs:
# - Name
# - Age
# - Marks

try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    if age < 0 or age > 120:
        raise ValueError("Invalid age.")

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

except ValueError as error:
    print("Validation Error:", error)

else:
    print("\nAll inputs are valid!")
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)

finally:
    print("Validation completed.")


# Program 49
# Create a reusable age validation function.

def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

    return True


try:
    age = int(input("Enter age: "))
    validate_age(age)

except ValueError as error:
    print("Invalid age:", error)

else:
    print("Age is valid.")


# Program 50
# Complete Input Validator
#
# Validate:
# - Name
# - Age
# - Email
# - Marks
# - Password
#
# Use:
# - try
# - except
# - else
# - finally
# - raise
#
# Challenge: Improve this program by creating separate
# validation functions for each input.

try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    marks = float(input("Enter marks: "))
    password = input("Enter password: ")

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

    if "@" not in email:
        raise ValueError("Invalid email.")

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    if len(password) < 8:
        raise ValueError(
            "Password must contain at least 8 characters."
        )

except ValueError as error:
    print("\nValidation Error:", error)

else:
    print("\nAll inputs are valid!")

    print("\nUser Details")
    print("-" * 30)
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print("Marks:", marks)
    print("Password: Valid")

finally:
    print("\nValidation completed.")


# ============================================================
# END OF DAY 15 PRACTICE
# ============================================================
