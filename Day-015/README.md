````markdown
# Day 015 – Exception Handling

Welcome to **Day 15 of 100 Days of Python for AI/ML**.

Today, the focus is on **Exception Handling** — learning how to detect errors, handle them properly, validate user input, and prevent programs from terminating unexpectedly.

---

## Topics Covered

### 1. Basic Exception Handling

Learn how to handle errors using:

- `try`
- `except`

Common exceptions covered:

- `ValueError`
- `TypeError`
- `ZeroDivisionError`
- `IndexError`
- `KeyError`
- `FileNotFoundError`

Example:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
````

---

### 2. `try`, `except`, `else`, and `finally`

Learn how the different blocks work together.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("Valid input.")
finally:
    print("Program execution completed.")
```

#### `try`

Contains code that may produce an exception.

#### `except`

Handles the exception.

#### `else`

Runs when no exception occurs.

#### `finally`

Runs whether an exception occurs or not.

---

### 3. Handling Multiple Exceptions

Learn how to handle different types of exceptions.

```python
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Multiple exceptions can also be handled together:

```python
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")
```

---

### 4. Raising Exceptions

Python allows us to manually raise an exception using the `raise` keyword.

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Other validation examples include:

* Marks must be between 0 and 100
* Age must be between 0 and 120
* Number must be positive
* Password must contain at least 8 characters

---

### 5. Custom Exceptions

Python allows us to create our own exception classes.

Example:

```python
class AgeError(Exception):
    pass
```

Then the custom exception can be raised:

```python
if age < 0:
    raise AgeError("Age cannot be negative.")
```

Custom exceptions make error handling more meaningful and specific to an application.

---

### 6. Input Validation

Exception handling is especially useful when accepting input from users.

Examples of validation practiced:

* Positive integer validation
* Age validation
* Marks validation
* Username validation
* Password validation
* Email validation

Example:

```python
try:
    marks = float(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

except ValueError as error:
    print(error)
```

---

## Practice: Input Validator

The main practical task for Day 15 is to build an **Input Validator**.

The program validates:

1. Name
2. Age
3. Email
4. Marks

### Validation Rules

* Name cannot be empty.
* Age must be an integer between 0 and 120.
* Email must contain `@`.
* Marks must be a number between 0 and 100.

The program uses:

* `try`
* `except`
* `else`
* `finally`
* `raise`
* Input validation

---

## Mini Project – Input Validator

### Project Name

**Input Validator with Exception Handling**

### Features

* Validate name
* Validate age
* Validate email
* Validate marks
* Handle invalid input
* Raise meaningful errors
* Display successful validation results
* Use `try`, `except`, `else`, and `finally`

### Example Output

```text
=======================================================
             DAY 15 - INPUT VALIDATOR
=======================================================
Enter your name: Amit
Enter your age: 22
Enter your email: amit@example.com
Enter your marks: 85

=======================================================
             VALIDATION SUCCESSFUL
=======================================================
Name           : Amit
Age            : 22
Email          : amit@example.com
Marks          : 85.0
=======================================================
All inputs are valid!

Validation completed.
```

---

# Learning Objectives

By the end of Day 15, you should be able to:

* Understand what exceptions are.
* Use `try` and `except`.
* Handle common Python exceptions.
* Use `else` with exception handling.
* Use `finally` for code that must execute.
* Handle multiple exceptions.
* Manually raise exceptions using `raise`.
* Create custom exceptions.
* Validate user input.
* Build programs that handle invalid input safely.
* Build a complete input validation program.

---

# Repository Structure

```text
Day-015/
│
├── README.md
├── notes.md
├── exercise.py
├── solutions.py
├── practice.py
├── mini_project.py
└── quiz.md
```

---

# Files Description

| File              | Description                                     |
| ----------------- | ----------------------------------------------- |
| `README.md`       | Day 15 overview and learning summary            |
| `notes.md`        | Detailed notes on exception handling            |
| `exercise.py`     | Exception handling and validation exercises     |
| `solutions.py`    | Complete solutions to the exercises             |
| `practice.py`     | Additional exception handling practice programs |
| `mini_project.py` | Input Validator mini project                    |
| `quiz.md`         | 40-question Day 15 quiz                         |

---

# Key Concepts

## Basic Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## `else`

```python
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid input.")
else:
    print("Valid input.")
```

---

## `finally`

```python
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid input.")
finally:
    print("Program completed.")
```

---

## `raise`

```python
if age < 0:
    raise ValueError("Age cannot be negative.")
```

---

## Custom Exception

```python
class MarksError(Exception):
    pass
```

---

# Exception Handling Flow

```text
             try
              |
              v
       Does exception occur?
          /          \
        Yes           No
         |             |
         v             v
      except         else
         \             /
          \           /
             finally
                |
                v
          Program continues
```

---

# Practice Completed

Day 15 includes:

* 40 exception handling exercises
* Basic exception handling
* `try-except-else`
* `finally`
* Multiple exceptions
* `raise`
* Custom exceptions
* Input validation
* Practical exception handling programs
* Complete Input Validator Challenge
* Bonus Custom `ValidationError`
* 50 additional practice programs
* Complete solutions
* 40-question quiz
* Input Validator mini project

---

# Skills Developed

After completing Day 15, you have practiced:

* Error handling
* Exception handling
* Input validation
* Defensive programming
* Custom exceptions
* Error messages
* User input processing
* Writing more reliable Python programs

---

# Why Exception Handling Matters for AI/ML

Exception handling is important in AI/ML applications because real-world programs frequently deal with:

* User input
* Missing or invalid data
* Incorrect data types
* File operations
* Data preprocessing
* API responses
* Model inputs
* Configuration errors

For example, an ML application should not completely crash just because a user enters invalid input.

Exception handling allows the program to handle such situations gracefully.

---

# Day 15 Progress

* [x] Learned `try`
* [x] Learned `except`
* [x] Learned `else`
* [x] Learned `finally`
* [x] Learned common exceptions
* [x] Learned multiple exception handling
* [x] Learned `raise`
* [x] Learned custom exceptions
* [x] Practiced input validation
* [x] Completed exercises
* [x] Completed practice programs
* [x] Built Input Validator mini project
* [x] Completed quiz

---

# Key Takeaways

1. Exceptions are runtime problems that can interrupt program execution.
2. `try` contains code that may cause an exception.
3. `except` handles exceptions.
4. `else` runs when no exception occurs.
5. `finally` runs whether an exception occurs or not.
6. Multiple exceptions can be handled separately or together.
7. `raise` allows us to manually generate exceptions.
8. Custom exceptions make error handling more specific.
9. Exception handling is important for reliable programs.
10. Input validation is a practical application of exception handling.

---

# Day 15 Summary

| Topic               | Learned         |
| ------------------- | --------------- |
| `try`               | Yes             |
| `except`            | Yes             |
| `else`              | Yes             |
| `finally`           | Yes             |
| Common Exceptions   | Yes             |
| Multiple Exceptions | Yes             |
| `raise`             | Yes             |
| Custom Exceptions   | Yes             |
| Input Validation    | Yes             |
| Mini Project        | Input Validator |
| Quiz                | 40 Questions    |

---

**Day 15 completed.**


```
```
