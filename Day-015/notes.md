Yes, Captain. You mean **all of Day 15 notes in one single copy-paste box**, without breaking it into multiple boxes.

````markdown
# Day 015 – Exception Handling

Welcome to Day 15 of the **100 Days of Python for AI/ML** challenge.

Today we learn how to handle errors and unexpected situations in Python using **Exception Handling**.

---

## Topics Covered

- Errors and Exceptions
- `try`
- `except`
- `else`
- `finally`
- Handling multiple exceptions
- `raise`
- Custom exceptions
- Input validation with error handling

---

# 1. Errors and Exceptions

An **error** is a problem in a program that prevents it from working correctly.

Example:

```python
print(10 / 0)
````

Output:

```text
ZeroDivisionError
```

Python calls this a **runtime exception**.

Some common Python exceptions are:

```text
ValueError
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
```

---

# 2. What is Exception Handling?

Exception handling allows us to detect and handle errors so that our program does not crash unexpectedly.

Basic structure:

```python
try:
    # Code that may cause an error
except:
    # Code that handles the error
```

Example:

```python
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Please enter a valid number.")
```

If the user enters:

```text
25
```

Output:

```text
25
```

If the user enters:

```text
hello
```

Output:

```text
Please enter a valid number.
```

---

# 3. try Block

The `try` block contains code that might generate an exception.

Example:

```python
try:
    result = 10 / 2
    print(result)
except:
    print("Something went wrong.")
```

The code inside the `try` block is executed first.

If an exception occurs, Python moves to the appropriate `except` block.

---

# 4. except Block

The `except` block is used to handle an exception.

Example:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
```

If the input cannot be converted into an integer, a `ValueError` occurs and the `except` block handles it.

---

# 5. Handling Specific Exceptions

It is better to specify the type of exception we want to handle.

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")
```

Here:

* `ValueError` handles invalid integer input.
* `ZeroDivisionError` handles division by zero.

---

# 6. Common Python Exceptions

## ValueError

Occurs when a value has an inappropriate value.

Example:

```python
number = int("hello")
```

Result:

```text
ValueError
```

---

## TypeError

Occurs when an operation is performed on incompatible data types.

Example:

```python
result = "10" + 5
```

Result:

```text
TypeError
```

---

## ZeroDivisionError

Occurs when we try to divide by zero.

Example:

```python
result = 10 / 0
```

Result:

```text
ZeroDivisionError
```

---

## IndexError

Occurs when we try to access an index that does not exist.

Example:

```python
numbers = [10, 20, 30]

print(numbers[5])
```

Result:

```text
IndexError
```

---

## KeyError

Occurs when we try to access a dictionary key that does not exist.

Example:

```python
student = {
    "name": "Amit"
}

print(student["age"])
```

Result:

```text
KeyError
```

---

## FileNotFoundError

Occurs when we try to open a file that does not exist.

Example:

```python
file = open("missing.txt", "r")
```

Result:

```text
FileNotFoundError
```

---

# 7. else Block

The `else` block runs **only when no exception occurs** in the `try` block.

Syntax:

```python
try:
    # Risky code

except:
    # Error handling

else:
    # Runs when no error occurs
```

Example:

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print(f"You entered {number}")
```

If the input is valid, the `else` block runs.

If an exception occurs, the `except` block runs.

---

# 8. finally Block

The `finally` block **always executes**, whether an exception occurs or not.

Syntax:

```python
try:
    # Code

except:
    # Error handling

finally:
    # Always executes
```

Example:

```python
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program finished.")
```

The `finally` block is commonly used for cleanup operations.

---

# 9. Complete try-except-else-finally

We can use all four blocks together.

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")

else:
    print(f"Result: {result}")

finally:
    print("Execution completed.")
```

### Flow

```text
        try
         |
         ↓
   Error occurs?
      /      \
    Yes       No
     |         |
     ↓         ↓
  except     else
     \         /
      \       /
       ↓     ↓
       finally
          |
          ↓
       Continue
```

---

# 10. Handling Multiple Exceptions

A program can produce different types of exceptions.

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Each exception has its own handling logic.

---

# 11. Handling Multiple Exceptions Together

If the same action should be performed for multiple exceptions, they can be grouped inside a tuple.

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")
```

This handles both `ValueError` and `ZeroDivisionError` with the same message.

---

# 12. Raising Exceptions using raise

Python allows us to manually generate an exception using the `raise` statement.

Syntax:

```python
raise ExceptionType("message")
```

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Output:

```text
ValueError: Age cannot be negative.
```

---

# 13. Why Use raise?

`raise` is useful when we want to enforce our own rules.

Example:

```python
marks = 150

if marks > 100:
    raise ValueError("Marks cannot be greater than 100.")
```

Here, we manually raise a `ValueError` because the value does not satisfy our condition.

---

# 14. Custom Exceptions

Python allows us to create our own exception classes.

A custom exception normally inherits from the built-in `Exception` class.

Example:

```python
class AgeError(Exception):
    pass
```

Now we can use it:

```python
age = -10

if age < 0:
    raise AgeError("Age cannot be negative.")
```

---

# 15. Handling a Custom Exception

Custom exceptions can also be handled using `except`.

Example:

```python
class AgeError(Exception):
    pass


try:
    age = -5

    if age < 0:
        raise AgeError("Age cannot be negative.")

except AgeError as error:
    print(error)
```

Output:

```text
Age cannot be negative.
```

---

# 16. Input Validation

**Input validation** means checking whether the data entered by the user is valid.

Example:

```python
try:
    number = int(input("Enter a positive number: "))

    if number <= 0:
        raise ValueError("Number must be positive.")

    print(f"Valid number: {number}")

except ValueError as error:
    print(f"Invalid input: {error}")
```

Valid input:

```text
Enter a positive number: 10
Valid number: 10
```

Invalid input:

```text
Enter a positive number: -5
Invalid input: Number must be positive.
```

---

# 17. Input Validator Example

A simple age validator:

```python
try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

    print(f"Valid age: {age}")

except ValueError as error:
    print(f"Invalid input: {error}")
```

This combines:

* `try`
* `except`
* `raise`
* Input validation

---

# 18. Difference Between try, except, else and finally

| Block     | Purpose                                   |
| --------- | ----------------------------------------- |
| `try`     | Contains code that may cause an exception |
| `except`  | Handles an exception                      |
| `else`    | Runs when no exception occurs             |
| `finally` | Always executes                           |

### Easy Way to Remember

```text
try      → Try this code
except   → If something goes wrong
else     → If nothing goes wrong
finally  → Do this anyway
```

---

# 19. Exception Handling Flow

```text
             try
              |
              ↓
       Does an error occur?
          /           \
        Yes            No
         |              |
         ↓              ↓
      except           else
         \              /
          \            /
           ↓          ↓
             finally
                |
                ↓
             Continue
```

---

# 20. Important Rules

### Rule 1

A `try` block must be followed by at least one `except` or `finally`.

### Rule 2

The `else` block runs only when no exception occurs in the `try` block.

### Rule 3

The `finally` block runs whether an exception occurs or not.

### Rule 4

Use specific exceptions whenever possible.

Prefer:

```python
except ValueError:
```

instead of:

```python
except:
```

### Rule 5

Use `raise` when you want to manually trigger an exception.

---

# 21. Practical Example

```python
try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as error:
    print(f"Invalid input: {error}")

else:
    print(f"Your age is {age}")

finally:
    print("Age validation completed.")
```

This example demonstrates:

* `try`
* `except`
* `else`
* `finally`
* `raise`
* Input validation

---

# 22. Why Exception Handling Matters

Exception handling is important because real-world programs often receive unexpected input or encounter unexpected situations.

### Without Exception Handling

```text
Invalid Input
     ↓
Program crashes
```

### With Exception Handling

```text
Invalid Input
     ↓
Exception detected
     ↓
Error handled
     ↓
Useful message
     ↓
Program continues safely
```

---

# 23. Exception Handling in AI/ML

Exception handling is useful in AI/ML applications for:

* Validating user input
* Handling missing files
* Handling invalid datasets
* Handling incorrect data types
* Handling model input errors
* Handling API failures
* Handling invalid configuration values
* Building reliable data-processing pipelines

Example:

```python
try:
    data = int(input("Enter dataset size: "))

except ValueError:
    print("Dataset size must be a number.")
```

Reliable AI/ML programs need to handle unexpected situations instead of crashing.

---

# 24. Quick Revision

```text
Exception Handling
        |
        ├── try
        |     └── Code that may cause an error
        |
        ├── except
        |     └── Handles the error
        |
        ├── else
        |     └── Runs when no error occurs
        |
        ├── finally
        |     └── Always runs
        |
        ├── raise
        |     └── Manually raises an exception
        |
        └── Custom Exception
              └── User-defined exception class
```

---

# 25. Key Takeaways

* Exceptions are runtime problems that can interrupt program execution.
* `try` contains code that may cause an exception.
* `except` handles exceptions.
* Specific exceptions should be handled whenever possible.
* Multiple exceptions can be handled separately or together.
* `else` runs when the `try` block succeeds.
* `finally` runs regardless of whether an exception occurs.
* `raise` allows us to manually generate an exception.
* Custom exceptions can be created by inheriting from `Exception`.
* Input validation and exception handling can be combined to build safer programs.

---

# Day 15 Summary

| Concept          | Purpose                            |
| ---------------- | ---------------------------------- |
| `try`            | Test risky code                    |
| `except`         | Handle errors                      |
| `else`           | Run when no error occurs           |
| `finally`        | Always execute                     |
| `raise`          | Manually raise an exception        |
| Custom Exception | Create application-specific errors |
| Input Validation | Check whether user input is valid  |

---

## Day 15 Goal

Build Python programs that do not simply crash when something unexpected happens, but instead **handle errors properly and provide meaningful feedback**.

```
```
