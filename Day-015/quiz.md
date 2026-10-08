````
# Day 15 – Exception Handling Quiz

## Instructions

- Answer all questions.
- Choose the correct option: A, B, C, or D.
- Try to solve the questions without looking at your notes.
- Check your answers using the answer key at the end.

---

# Section 1 – Basic Exception Handling

### Q1. What is the purpose of `try` in Python?

A. To define a function  
B. To test code that may cause an exception  
C. To stop the program permanently  
D. To create a loop  

---

### Q2. Which block is used to handle an exception?

A. `try`  
B. `error`  
C. `except`  
D. `handle`  

---

### Q3. What exception occurs when we divide a number by zero?

A. `ValueError`  
B. `TypeError`  
C. `ZeroDivisionError`  
D. `ArithmeticError`  

---

### Q4. What exception occurs when `int("hello")` is executed?

A. `TypeError`  
B. `ValueError`  
C. `KeyError`  
D. `IndexError`  

---

### Q5. What exception occurs when we access an invalid list index?

A. `IndexError`  
B. `KeyError`  
C. `ValueError`  
D. `TypeError`  

---

### Q6. What exception occurs when a dictionary key does not exist?

A. `IndexError`  
B. `KeyError`  
C. `ValueError`  
D. `NameError`  

---

### Q7. What exception can occur when trying to open a file that does not exist?

A. `FileError`  
B. `OpenError`  
C. `FileNotFoundError`  
D. `ValueError`  

---

### Q8. What exception occurs in this code?

```python
print(10 + "5")
````

A. `ValueError`
B. `TypeError`
C. `KeyError`
D. `ZeroDivisionError`

---

# Section 2 – try, except, else and finally

### Q9. When does the `else` block execute?

A. When an exception occurs
B. Always
C. When no exception occurs
D. Before the `try` block

---

### Q10. When does the `finally` block normally execute?

A. Only when an exception occurs
B. Only when there is no exception
C. Whether an exception occurs or not
D. Never

---

### Q11. What is the correct structure?

A.

```python
except
try
else
finally
```

B.

```python
try
except
else
finally
```

C.

```python
try
else
except
finally
```

D.

```python
try
finally
except
else
```

---

### Q12. What will this program print?

```python
try:
    number = int("10")
except ValueError:
    print("Invalid")
else:
    print("Valid")
finally:
    print("Done")
```

A.

```text
Invalid
Done
```

B.

```text
Valid
```

C.

```text
Valid
Done
```

D.

```text
Done
```

---

### Q13. What will this code print?

```python
try:
    number = int("abc")
except ValueError:
    print("Invalid")
else:
    print("Valid")
finally:
    print("Done")
```

A.

```text
Valid
Done
```

B.

```text
Invalid
Done
```

C.

```text
Invalid
Valid
```

D.

```text
Done
```

---

# Section 3 – Multiple Exceptions

### Q14. Which syntax correctly handles different exceptions separately?

A.

```python
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...
```

B.

```python
try:
    ...
error ValueError:
    ...
```

C.

```python
try:
    ...
except:
    ValueError
    ZeroDivisionError
```

D.

```python
try:
    ...
handle ValueError:
    ...
```

---

### Q15. Which syntax can handle multiple exceptions in one `except` block?

A.

```python
except ValueError, ZeroDivisionError:
```

B.

```python
except [ValueError, ZeroDivisionError]:
```

C.

```python
except (ValueError, ZeroDivisionError):
```

D.

```python
except ValueError + ZeroDivisionError:
```

---

### Q16. What happens if an exception is not handled?

A. Python automatically fixes it
B. The program may terminate and display an error message
C. The exception is ignored
D. The program starts again

---

# Section 4 – Raising Exceptions

### Q17. Which keyword is used to manually raise an exception?

A. `throw`
B. `error`
C. `raise`
D. `exception`

---

### Q18. What will happen here?

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

A. Nothing happens
B. A `ValueError` is raised
C. A `TypeError` is raised
D. Age becomes 0

---

### Q19. Which statement is best for validating marks between 0 and 100?

A.

```python
if marks < 0 or marks > 100:
    raise ValueError("Invalid marks.")
```

B.

```python
if marks == 100:
    raise ValueError("Invalid marks.")
```

C.

```python
if marks > 0:
    raise ValueError("Invalid marks.")
```

D.

```python
raise marks
```

---

### Q20. What is the purpose of `raise`?

A. To create a loop
B. To manually generate an exception
C. To catch an exception
D. To close a file

---

# Section 5 – Custom Exceptions

### Q21. Which code correctly creates a custom exception?

A.

```python
class AgeError:
    pass
```

B.

```python
class AgeError(Exception):
    pass
```

C.

```python
exception AgeError:
    pass
```

D.

```python
class Exception(AgeError):
    pass
```

---

### Q22. Why do we create custom exceptions?

A. To make Python faster
B. To provide meaningful and specific errors for our application
C. To avoid using functions
D. To replace all built-in data types

---

### Q23. What does this code define?

```python
class MarksError(Exception):
    pass
```

A. A function
B. A loop
C. A custom exception
D. A dictionary

---

### Q24. Which statement correctly raises a custom exception?

A.

```python
raise MarksError("Invalid marks.")
```

B.

```python
throw MarksError("Invalid marks.")
```

C.

```python
error MarksError("Invalid marks.")
```

D.

```python
except MarksError("Invalid marks.")
```

---

# Section 6 – Input Validation

### Q25. What should happen if a user enters an age of `150` when the valid range is 0–120?

A. Accept the age
B. Raise a validation error
C. Convert it to 120 automatically
D. Ignore the input

---

### Q26. Which condition correctly checks that marks are outside the valid range?

A.

```python
marks > 0 and marks < 100
```

B.

```python
marks < 0 or marks > 100
```

C.

```python
marks == 50
```

D.

```python
marks >= 0
```

---

### Q27. Which validation is appropriate for a password requiring at least 8 characters?

A.

```python
if len(password) < 8:
    raise ValueError("Password must contain at least 8 characters.")
```

B.

```python
if len(password) > 8:
    raise ValueError("Password is invalid.")
```

C.

```python
if password == 8:
    raise ValueError("Password is invalid.")
```

D.

```python
raise password
```

---

### Q28. What should happen if an email does not contain `@` in the Day 15 input validator?

A. It should be accepted
B. It should raise a validation error
C. It should be converted to lowercase automatically
D. The program should ignore the email

---

# Section 7 – Code-Based Questions

### Q29. What will this program print?

```python
try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

A. `10`
B. `0`
C. `Cannot divide by zero.`
D. Nothing

---

### Q30. What will this program print?

```python
try:
    number = int("25")
except ValueError:
    print("Invalid")
else:
    print("Valid")
finally:
    print("Completed")
```

A.

```text
Invalid
Completed
```

B.

```text
Valid
Completed
```

C.

```text
Completed
```

D.

```text
Valid
```

---

### Q31. What will this code print?

```python
try:
    numbers = [10, 20, 30]
    print(numbers[5])
except IndexError:
    print("Invalid index.")
finally:
    print("Finished.")
```

A.

```text
Invalid index.
Finished.
```

B.

```text
Finished.
```

C.

```text
Invalid index.
```

D. Nothing

---

### Q32. What will this code print?

```python
try:
    age = -10

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as error:
    print(error)
```

A. `-10`
B. `Age cannot be negative.`
C. `ValueError`
D. Nothing

---

### Q33. What does `as error` allow us to do?

```python
except ValueError as error:
    print(error)
```

A. Create a new exception
B. Store the exception object in the variable `error`
C. Ignore the exception
D. Stop the `except` block

---

# Section 8 – Day 15 Mini Project

### Q34. What is the main purpose of the Day 15 Input Validator project?

A. File management
B. Image processing
C. Validate user inputs using exception handling
D. Sorting numbers

---

### Q35. Which function is used to validate the name in the mini project?

A.

```python
validate_name()
```

B.

```python
check_string()
```

C.

```python
name_check()
```

D.

```python
name_validator()
```

---

### Q36. Which function validates age?

A.

```python
check_age()
```

B.

```python
validate_age()
```

C.

```python
age_check()
```

D.

```python
verify_age()
```

---

### Q37. Which exception is used when the entered marks are not a valid number?

A. `KeyError`
B. `ValueError`
C. `IndexError`
D. `FileNotFoundError`

---

### Q38. Why is `finally` useful in the input validator?

A. It runs only when the input is correct
B. It ensures the completion message is displayed
C. It replaces `except`
D. It prevents all exceptions

---

### Q39. What message is displayed by the mini project after validation finishes?

A. `Program stopped.`
B. `Validation failed.`
C. `Validation completed.`
D. `Input accepted.`

---

### Q40. Which combination of concepts is demonstrated by the Day 15 mini project?

A. Lists, tuples and sets
B. File handling and CSV
C. `try`, `except`, `else`, `finally`, `raise` and input validation
D. Loops and list comprehensions only

---

# Answer Key

| Question | Answer | Question | Answer |
| -------- | ------ | -------- | ------ |
| 1        | B      | 21       | B      |
| 2        | C      | 22       | B      |
| 3        | C      | 23       | C      |
| 4        | B      | 24       | A      |
| 5        | A      | 25       | B      |
| 6        | B      | 26       | B      |
| 7        | C      | 27       | A      |
| 8        | B      | 28       | B      |
| 9        | C      | 29       | C      |
| 10       | C      | 30       | B      |
| 11       | B      | 31       | A      |
| 12       | C      | 32       | B      |
| 13       | B      | 33       | B      |
| 14       | A      | 34       | C      |
| 15       | C      | 35       | A      |
| 16       | B      | 36       | B      |
| 17       | C      | 37       | B      |
| 18       | B      | 38       | B      |
| 19       | A      | 39       | C      |
| 20       | B      | 40       | C      |

---

# Score Guide

| Score | Level               |
| ----- | ------------------- |
| 36–40 | Excellent           |
| 32–35 | Very Good           |
| 27–31 | Good                |
| 20–26 | Needs Revision      |
| 0–19  | Revise Day 15 Again |

---

# Day 15 Revision Checklist

Before moving to Day 16, make sure you can explain and use:

* [ ] `try`
* [ ] `except`
* [ ] `else`
* [ ] `finally`
* [ ] `ValueError`
* [ ] `TypeError`
* [ ] `ZeroDivisionError`
* [ ] `IndexError`
* [ ] `KeyError`
* [ ] `FileNotFoundError`
* [ ] Handling multiple exceptions
* [ ] `raise`
* [ ] Custom exceptions
* [ ] Input validation
* [ ] Positive number validation
* [ ] Age validation
* [ ] Marks validation
* [ ] Password validation
* [ ] Complete input validator
* [ ] Day 15 Mini Project

---

# Key Takeaway

Exception handling makes Python programs more reliable by allowing us to detect errors, handle them properly, validate user input, and prevent unexpected program termination.

**Day 15 Complete — Exception Handling**

```
```
