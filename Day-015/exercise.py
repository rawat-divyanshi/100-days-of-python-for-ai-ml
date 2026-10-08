"""
Day 15 – Exception Handling
100 Days of Python for AI/ML

Topics:
- try
- except
- else
- finally
- Handling multiple exceptions
- raise
- Custom exceptions
- Input validation

Complete the exercises below.
"""

# ============================================================
# SECTION 1 – BASIC EXCEPTION HANDLING
# ============================================================

# Exercise 1
# Write a program that divides 10 by a number entered by the user.
# Handle ZeroDivisionError.


# Exercise 2
# Ask the user to enter an integer.
# Handle ValueError if the user enters something that is not an integer.


# Exercise 3
# Write a program that converts user input into an integer.
# Use try-except to handle invalid input.


# Exercise 4
# Create a list:
# numbers = [10, 20, 30]
#
# Ask the user for an index and print the corresponding element.
# Handle IndexError.


# Exercise 5
# Create the dictionary:
#
# student = {
#     "name": "Amit",
#     "age": 22,
#     "course": "Python"
# }
#
# Ask the user for a key and print its value.
# Handle KeyError if the key does not exist.


# Exercise 6
# Write a program that tries to add a number and a string.
# Handle TypeError.


# Exercise 7
# Write a program that opens "data.txt" for reading.
# Handle FileNotFoundError if the file does not exist.


# Exercise 8
# Create a program that asks the user for two numbers
# and divides the first number by the second number.
#
# Handle:
# - ValueError
# - ZeroDivisionError


# ============================================================
# SECTION 2 – try, except, else
# ============================================================

# Exercise 9
# Ask the user to enter an integer.
#
# If the input is valid:
#     Print "Valid input"
#
# If the input is invalid:
#     Print "Invalid input"
#
# Use try-except-else.


# Exercise 10
# Ask the user to enter their age.
#
# Use:
# - try for converting input to integer
# - except for invalid input
# - else to print the valid age


# Exercise 11
# Ask the user for two numbers.
# Calculate their sum.
#
# Use try-except-else.
#
# Example:
# Enter first number: 10
# Enter second number: 20
# Sum: 30


# Exercise 12
# Ask the user to enter a number.
# Calculate its square.
#
# Use try-except-else.


# Exercise 13
# Ask the user for their marks.
#
# If the input is valid:
#     Print the marks.
#
# Otherwise:
#     Print "Invalid marks."
#
# Use try-except-else.


# ============================================================
# SECTION 3 – finally
# ============================================================

# Exercise 14
# Write a program that asks the user for a number.
# Handle ValueError.
# Use finally to print:
#
# "Program execution completed."


# Exercise 15
# Ask the user for two numbers and divide them.
#
# Handle:
# - ValueError
# - ZeroDivisionError
#
# Use finally to print:
#
# "Calculation finished."


# Exercise 16
# Write a program that opens "example.txt".
#
# Handle FileNotFoundError.
# Use finally to print:
#
# "File operation completed."


# Exercise 17
# Create a program that asks the user for their age.
#
# Use try, except, else, and finally.
#
# Expected structure:
#
# try:
#     convert input
#
# except:
#     handle error
#
# else:
#     display age
#
# finally:
#     display completion message


# ============================================================
# SECTION 4 – MULTIPLE EXCEPTIONS
# ============================================================

# Exercise 18
# Ask the user for two numbers.
# Divide the first number by the second number.
#
# Handle ValueError and ZeroDivisionError separately.


# Exercise 19
# Ask the user to enter an index for:
#
# numbers = [10, 20, 30, 40, 50]
#
# Handle:
# - ValueError
# - IndexError


# Exercise 20
# Create a dictionary:
#
# student = {
#     "name": "Amit",
#     "marks": 85,
#     "course": "Python"
# }
#
# Ask the user for a key.
#
# Handle:
# - KeyError
# - ValueError
#
# Use appropriate exception handling.


# Exercise 21
# Handle multiple exceptions together.
#
# Ask the user for two numbers and divide them.
#
# Handle ValueError and ZeroDivisionError using:
#
# except (ValueError, ZeroDivisionError):
#
# Display:
# "Invalid input or division by zero."


# ============================================================
# SECTION 5 – raise
# ============================================================

# Exercise 22
# Ask the user for their age.
#
# If age is less than 0:
#     raise ValueError("Age cannot be negative.")
#
# Otherwise print the age.


# Exercise 23
# Ask the user for marks.
#
# If marks are less than 0 or greater than 100:
#     raise ValueError("Marks must be between 0 and 100.")
#
# Otherwise print:
# "Valid marks"


# Exercise 24
# Ask the user for a positive number.
#
# If the number is less than or equal to 0:
#     raise ValueError("Number must be positive.")
#
# Handle the exception using except.


# Exercise 25
# Ask the user for their age.
#
# Valid age range:
# 0 to 120
#
# If the age is outside this range:
#     raise ValueError("Age must be between 0 and 120.")
#
# Handle the exception and display a useful message.


# Exercise 26
# Ask the user for a password.
#
# If the password contains fewer than 8 characters:
#     raise ValueError("Password must contain at least 8 characters.")
#
# Otherwise print:
# "Valid password"


# ============================================================
# SECTION 6 – CUSTOM EXCEPTIONS
# ============================================================

# Exercise 27
# Create a custom exception called AgeError.
#
# Example:
#
# class AgeError(Exception):
#     pass
#
# Ask the user for their age.
# If age is negative, raise AgeError.


# Exercise 28
# Create a custom exception called MarksError.
#
# If marks are less than 0 or greater than 100,
# raise MarksError.
#
# Handle the exception using except.


# Exercise 29
# Create a custom exception called PasswordError.
#
# If the password has fewer than 8 characters,
# raise PasswordError.
#
# Handle the exception and display an appropriate message.


# Exercise 30
# Create a custom exception called InsufficientBalanceError.
#
# Start with:
#
# balance = 5000
#
# Ask the user for a withdrawal amount.
#
# If withdrawal amount is greater than balance:
#     raise InsufficientBalanceError
#
# Otherwise:
#     Deduct the amount and display the remaining balance.


# ============================================================
# SECTION 7 – INPUT VALIDATION
# ============================================================

# Exercise 31
# Create a number validator.
#
# Ask the user for a number.
#
# Requirements:
# - Input must be an integer.
# - Number must be positive.
#
# Handle invalid input using ValueError.


# Exercise 32
# Create an age validator.
#
# Requirements:
# - Age must be an integer.
# - Age must be between 0 and 120.
#
# Display:
# "Valid age"
# or
# "Invalid age"


# Exercise 33
# Create a marks validator.
#
# Requirements:
# - Marks must be numeric.
# - Marks must be between 0 and 100.
#
# Handle invalid input using exception handling.


# Exercise 34
# Create a username validator.
#
# Requirements:
# - Username must contain at least 5 characters.
# - Username must not be empty.
#
# Raise ValueError if the input is invalid.


# Exercise 35
# Create a password validator.
#
# Requirements:
# - At least 8 characters
# - Must not be empty
#
# Raise ValueError if the password is invalid.


# ============================================================
# SECTION 8 – PRACTICAL PROBLEMS
# ============================================================

# Exercise 36
# Create a simple calculator.
#
# Ask the user for:
# - First number
# - Operator (+, -, *, /)
# - Second number
#
# Handle:
# - ValueError
# - ZeroDivisionError
#
# Also handle an invalid operator.


# Exercise 37
# Create a student marks validator.
#
# Ask the user for marks in:
# - Mathematics
# - Python
# - AI/ML
#
# Requirements:
# - Each mark must be between 0 and 100.
# - Invalid marks should raise ValueError.
# - Calculate the average if all inputs are valid.


# Exercise 38
# Create a simple login validator.
#
# Store:
#
# username = "admin"
# password = "python123"
#
# Ask the user to enter username and password.
#
# Raise ValueError if either is incorrect.
# Handle the exception with a useful message.


# Exercise 39
# Create a division calculator that keeps asking the user
# for numbers until valid input is entered.
#
# Handle:
# - ValueError
# - ZeroDivisionError
#
# Once valid input is entered, display the result.


# Exercise 40
# Create a file reader.
#
# Ask the user for a filename.
#
# Try to open and read the file.
#
# Handle:
# - FileNotFoundError
# - PermissionError
#
# Use finally to print:
# "File operation completed."


# ============================================================
# SECTION 9 – CHALLENGE
# ============================================================

# Challenge: Complete Input Validator
#
# Build a program that asks the user for:
#
# 1. Name
# 2. Age
# 3. Email
# 4. Marks
#
# Validation rules:
#
# Name:
# - Cannot be empty
#
# Age:
# - Must be an integer
# - Must be between 0 and 120
#
# Email:
# - Must contain "@"
#
# Marks:
# - Must be a number
# - Must be between 0 and 100
#
# Requirements:
#
# - Use try-except.
# - Use raise for invalid values.
# - Handle different exceptions appropriately.
# - Use else for successful validation.
# - Use finally to display:
#   "Validation completed."
#
# Example:
#
# ==============================
#       INPUT VALIDATOR
# ==============================
#
# Enter your name: Amit
# Enter your age: 22
# Enter your email: amit@example.com
# Enter your marks: 85
#
# All inputs are valid!
#
# Validation completed.


# ============================================================
# BONUS CHALLENGE
# ============================================================

# Create a custom exception:
#
# class ValidationError(Exception):
#     pass
#
# Use this single custom exception to handle different
# validation errors in a user registration system.
#
# Validate:
# - Name
# - Age
# - Email
# - Password
#
# Requirements:
# - Use try
# - Use except
# - Use else
# - Use finally
# - Use raise
# - Use a custom exception
#
# Display clear and meaningful error messages.
