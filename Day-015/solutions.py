"""
Day 15 – Exception Handling
100 Days of Python for AI/ML

Solutions for Exercises 1–40
+ Complete Input Validator Challenge
+ Bonus Challenge

Topics:
- try
- except
- else
- finally
- Multiple exceptions
- raise
- Custom exceptions
- Input validation
"""

# ============================================================
# SECTION 1 – BASIC EXCEPTION HANDLING
# ============================================================

# Exercise 1
# Divide 10 by a number entered by the user.
# Handle ZeroDivisionError.

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Exercise 2
# Ask the user to enter an integer.
# Handle ValueError.

try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)
except ValueError:
    print("Please enter a valid integer.")


# Exercise 3
# Convert user input into an integer.

try:
    number = int(input("Enter a number: "))
    print("Integer:", number)
except ValueError:
    print("Invalid input. Please enter an integer.")


# Exercise 4
# Handle IndexError.

numbers = [10, 20, 30]

try:
    index = int(input("Enter an index: "))
    print("Value:", numbers[index])
except ValueError:
    print("Index must be an integer.")
except IndexError:
    print("Index does not exist.")


# Exercise 5
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


# Exercise 6
# Handle TypeError.

try:
    result = "10" + 5
    print(result)
except TypeError:
    print("Cannot add a string and an integer.")


# Exercise 7
# Open data.txt and handle FileNotFoundError.

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("data.txt was not found.")


# Exercise 8
# Divide two numbers.
# Handle ValueError and ZeroDivisionError.

try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    result = first / second

    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ============================================================
# SECTION 2 – try, except, else
# ============================================================

# Exercise 9
# Use try-except-else for integer validation.

try:
    number = int(input("Enter an integer: "))

except ValueError:
    print("Invalid input")

else:
    print("Valid input")


# Exercise 10
# Age validation using try-except-else.

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Invalid age.")

else:
    print("Your age is:", age)


# Exercise 11
# Calculate sum using try-except-else.

try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

except ValueError:
    print("Please enter valid numbers.")

else:
    total = first + second
    print("Sum:", total)


# Exercise 12
# Calculate square using try-except-else.

try:
    number = float(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    square = number ** 2
    print("Square:", square)


# Exercise 13
# Marks validation using try-except-else.

try:
    marks = float(input("Enter your marks: "))

except ValueError:
    print("Invalid marks.")

else:
    print("Marks:", marks)


# ============================================================
# SECTION 3 – finally
# ============================================================

# Exercise 14
# Use finally to display completion message.

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program execution completed.")


# Exercise 15
# Divide two numbers and use finally.

try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    result = first / second
    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Calculation finished.")


# Exercise 16
# Open example.txt and use finally.

try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("example.txt was not found.")

finally:
    print("File operation completed.")


# Exercise 17
# Use try, except, else and finally.

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Age must be an integer.")

else:
    print("Your age is:", age)

finally:
    print("Age validation completed.")


# ============================================================
# SECTION 4 – MULTIPLE EXCEPTIONS
# ============================================================

# Exercise 18
# Handle ValueError and ZeroDivisionError separately.

try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    result = first / second

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)


# Exercise 19
# Handle ValueError and IndexError.

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index: "))
    print("Value:", numbers[index])

except ValueError:
    print("Index must be an integer.")

except IndexError:
    print("Index does not exist.")


# Exercise 20
# Handle KeyError and ValueError.

student = {
    "name": "Amit",
    "marks": 85,
    "course": "Python"
}

try:
    key = input("Enter a key: ")
    value = student[key]

    number = int(input("Enter an integer: "))

    print("Dictionary value:", value)
    print("Integer:", number)

except KeyError:
    print("Key does not exist.")

except ValueError:
    print("Invalid integer.")


# Exercise 21
# Handle multiple exceptions together.

try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    result = first / second
    print("Result:", result)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")


# ============================================================
# SECTION 5 – raise
# ============================================================

# Exercise 22
# Raise ValueError if age is negative.

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age:", age)

except ValueError as error:
    print("Error:", error)


# Exercise 23
# Raise ValueError if marks are outside 0–100.

try:
    marks = float(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    print("Valid marks")

except ValueError as error:
    print("Error:", error)


# Exercise 24
# Raise ValueError if number is not positive.

try:
    number = float(input("Enter a positive number: "))

    if number <= 0:
        raise ValueError("Number must be positive.")

    print("Valid number:", number)

except ValueError as error:
    print("Error:", error)


# Exercise 25
# Validate age between 0 and 120.

try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

    print("Valid age:", age)

except ValueError as error:
    print("Error:", error)


# Exercise 26
# Validate password length.

try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise ValueError(
            "Password must contain at least 8 characters."
        )

    print("Valid password")

except ValueError as error:
    print("Error:", error)


# ============================================================
# SECTION 6 – CUSTOM EXCEPTIONS
# ============================================================

# Exercise 27
# Create and use AgeError.

class AgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise AgeError("Age cannot be negative.")

    print("Valid age:", age)

except ValueError:
    print("Age must be an integer.")

except AgeError as error:
    print("Age Error:", error)


# Exercise 28
# Create and use MarksError.

class MarksError(Exception):
    pass


try:
    marks = float(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        raise MarksError("Marks must be between 0 and 100.")

    print("Valid marks:", marks)

except ValueError:
    print("Marks must be a number.")

except MarksError as error:
    print("Marks Error:", error)


# Exercise 29
# Create and use PasswordError.

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


# Exercise 30
# Create and use InsufficientBalanceError.

class InsufficientBalanceError(Exception):
    pass


balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient balance."
        )

    balance -= amount

    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except ValueError as error:
    print("Error:", error)

except InsufficientBalanceError as error:
    print("Balance Error:", error)


# ============================================================
# SECTION 7 – INPUT VALIDATION
# ============================================================

# Exercise 31
# Number validator.

try:
    number = int(input("Enter a number: "))

    if number <= 0:
        raise ValueError("Number must be positive.")

except ValueError as error:
    print("Invalid input:", error)

else:
    print("Valid number:", number)


# Exercise 32
# Age validator.

try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

except ValueError:
    print("Invalid age")

else:
    print("Valid age")


# Exercise 33
# Marks validator.

try:
    marks = float(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

except ValueError as error:
    print("Invalid marks:", error)

else:
    print("Valid marks:", marks)


# Exercise 34
# Username validator.

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


# Exercise 35
# Password validator.

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
# SECTION 8 – PRACTICAL PROBLEMS
# ============================================================

# Exercise 36
# Simple calculator.

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


# Exercise 37
# Student marks validator.

try:
    mathematics = float(input("Mathematics marks: "))
    python = float(input("Python marks: "))
    aiml = float(input("AI/ML marks: "))

    marks = [mathematics, python, aiml]

    for mark in marks:
        if mark < 0 or mark > 100:
            raise ValueError(
                "Each mark must be between 0 and 100."
            )

    average = sum(marks) / len(marks)

except ValueError as error:
    print("Invalid marks:", error)

else:
    print("Mathematics:", mathematics)
    print("Python:", python)
    print("AI/ML:", aiml)
    print("Average:", average)


# Exercise 38
# Simple login validator.

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


# Exercise 39
# Division calculator with retry.

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


# Exercise 40
# File reader.

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
# SECTION 9 – CHALLENGE
# ============================================================

# Complete Input Validator
#
# Validate:
# - Name
# - Age
# - Email
# - Marks

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")
    marks = float(input("Enter your marks: "))

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

    if "@" not in email:
        raise ValueError("Email must contain '@'.")

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

except ValueError as error:
    print("Validation Error:", error)

else:
    print("\nAll inputs are valid!")

finally:
    print("\nValidation completed.")


# ============================================================
# BONUS CHALLENGE
# ============================================================

# Custom ValidationError

class ValidationError(Exception):
    pass


try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if not name.strip():
        raise ValidationError("Name cannot be empty.")

    if age < 0 or age > 120:
        raise ValidationError(
            "Age must be between 0 and 120."
        )

    if "@" not in email:
        raise ValidationError(
            "Email must contain '@'."
        )

    if len(password) < 8:
        raise ValidationError(
            "Password must contain at least 8 characters."
        )

except ValueError:
    print("Age must be a valid integer.")

except ValidationError as error:
    print("Validation Error:", error)

else:
    print("\nRegistration successful!")
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print("Password: Valid")

finally:
    print("\nRegistration validation completed.")


# ===========================================================
# END OF DAY 15 SOLUTIONS
# ===========================================================
