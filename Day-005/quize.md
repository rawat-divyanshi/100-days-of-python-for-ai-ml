# Day 005 Quiz

## Multiple Choice Questions (MCQs)

### Q1. Which statement is used to execute code only when a condition is True?

A. `for`

B. `while`

C. `if`

D. `print`

**Answer:** ________

---

### Q2. Which keyword is used when the first `if` condition is False but another condition needs to be checked?

A. `otherwise`

B. `elif`

C. `then`

D. `switch`

**Answer:** ________

---

### Q3. Which keyword is used to execute code when all previous conditions are False?

A. `default`

B. `elif`

C. `else`

D. `case`

**Answer:** ________

---

### Q4. What will `10 > 5` return?

A. `"True"`

B. `1`

C. `True`

D. `False`

**Answer:** ________

---

### Q5. Which operator checks if two values are equal?

A. `=`

B. `==`

C. `!=`

D. `>=`

**Answer:** ________

---

# True or False

### Q6.

Python uses indentation to define blocks of code.

**Answer:** ________

---

### Q7.

The `else` block is always executed.

**Answer:** ________

---

### Q8.

Nested `if` means an `if` statement inside another `if`.

**Answer:** ________

---

### Q9.

The ternary operator is a one-line version of `if-else`.

**Answer:** ________

---

### Q10.

Comparison operators always return either `True` or `False`.

**Answer:** ________

---

# Short Answer Questions

### Q11.

What is a conditional statement?

---

### Q12.

Why is indentation important in Python?

---

### Q13.

What is the difference between `if` and `if-else`?

---

### Q14.

When should we use `elif`?

---

### Q15.

What is a ternary operator?

---

# Predict the Output

### Q16.

```python
age = 20

if age >= 18:
    print("Adult")
```

**Output:**

____________________

---

### Q17.

```python
marks = 35

if marks >= 40:
    print("Pass")
else:
    print("Fail")
```

**Output:**

____________________

---

### Q18.

```python
number = 5

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Output:**

____________________

---

### Q19.

```python
marks = 82

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
```

**Output:**

____________________

---

### Q20.

```python
age = 16

message = "Adult" if age >= 18 else "Minor"

print(message)
```

**Output:**

____________________

---

# Interview Questions

1. What is the purpose of conditional statements?

2. Explain the difference between `if`, `elif`, and `else`.

3. What is indentation in Python, and why is it important?

4. What is a nested `if` statement?

5. What is the difference between `=` and `==`?

6. What are comparison operators?

7. What is the ternary operator? Write its syntax.

8. Can an `if` statement exist without an `else` statement? Explain.

---

# Challenge Question

Without running the code, predict the output:

```python
age = 25
salary = 40000

if age >= 18:
    if salary >= 30000:
        print("Loan Approved")
    else:
        print("Income Too Low")
else:
    print("Not Eligible")
```

**Output:**

____________________

---

# Coding Challenge

Write a Python program to:

- Take a student's marks as input.
- Print:
  - Grade A (90 and above)
  - Grade B (75–89)
  - Grade C (50–74)
  - Fail (Below 50)

Try solving it without looking at `solutions.py`.