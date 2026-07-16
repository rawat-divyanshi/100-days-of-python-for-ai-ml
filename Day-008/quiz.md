# Day 008 Quiz

## Multiple Choice Questions (MCQs)

### Q1. Which keyword is used to define a function in Python?

A. function

B. def

C. define

D. fun

**Answer:** ________

---

### Q2. What is the correct way to call a function named `greet`?

A. greet

B. greet[]

C. greet()

D. call greet()

**Answer:** ________

---

### Q3. Which statement sends a value back from a function?

A. print

B. return

C. input

D. pass

**Answer:** ________

---

### Q4. What are parameters?

A. Values passed while calling a function

B. Variables defined inside the function

C. Output of a function

D. None of these

**Answer:** ________

---

### Q5. What will happen if no value is passed to a default parameter?

A. Error

B. Python uses the default value

C. Function stops

D. Program crashes

**Answer:** ________

---

# True or False

### Q6.

A function can be called multiple times.

**Answer:** ________

---

### Q7.

A function executes automatically after it is defined.

**Answer:** ________

---

### Q8.

Parameters and Arguments are exactly the same thing.

**Answer:** ________

---

### Q9.

The `return` statement ends the execution of a function.

**Answer:** ________

---

### Q10.

A function can return only one value.

**Answer:** ________

---

# Short Answer Questions

### Q11.

What is a Function?

---

### Q12.

Why do we use Functions?

---

### Q13.

What is the difference between Parameters and Arguments?

---

### Q14.

What is a Default Parameter?

---

### Q15.

What is the difference between `print()` and `return`?

---

# Predict the Output

### Q16.

```python
def greet():
    print("Hello")

greet()
```

**Output:**

____________________

---

### Q17.

```python
def add(a, b):
    print(a + b)

add(5, 10)
```

**Output:**

____________________

---

### Q18.

```python
def square(n):
    return n * n

print(square(4))
```

**Output:**

____________________

---

### Q19.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
```

**Output:**

____________________

---

### Q20.

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)

print(result + 10)
```

**Output:**

____________________

---

# Interview Questions

1. What is a Function in Python?

2. Why are Functions important in programming?

3. What is the difference between defining and calling a function?

4. Explain Parameters and Arguments with an example.

5. What are Default Parameters?

6. What is the difference between `print()` and `return`?

7. Can a function return multiple values? Explain.

8. Why is `return` preferred over `print()` in real-world programming?

9. What are reusable functions?

10. Give three real-world examples where functions are used.

---

# Debug the Code

Find and correct the mistake.

```python
def add(a, b)
    return a + b

print(add(5, 10))
```

**What's wrong?**

____________________

---

# Challenge Question

Without running the code, predict the output.

```python
def greet(name="Python"):
    return "Hello " + name

print(greet())
print(greet("Amit"))
```

**Output:**

____________________

---

# Coding Challenge

Write a function named `largest()` that:

- Accepts three numbers as parameters.
- Returns the largest number.
- Print the returned value.

Try solving it without looking at `solutions.py`.

---

# Quick Revision

## Function

```
Input
   ↓
Function
   ↓
Output
```

---

## Function Syntax

```python
def function_name():
    statements
```

---

## Parameter vs Argument

```
Function Definition

↓

Parameter

Function Call

↓

Argument
```

---

## Default Parameter

```python
def greet(name="Guest"):
```

---

## print() vs return

```
print()

↓

Displays Output

----------------------

return

↓

Returns Value
```

---

# Key Points

✔ Functions help avoid code duplication.

✔ Functions make programs modular and reusable.

✔ Parameters receive values.

✔ Arguments provide values.

✔ `print()` displays output.

✔ `return` sends a value back.

✔ Functions improve code readability and maintenance.

---

## Day 008 Complete

If you can create your own functions, use parameters, understand the difference between `print()` and `return`, and solve today's exercises without help, you've learned one of the most important concepts in Python programming.