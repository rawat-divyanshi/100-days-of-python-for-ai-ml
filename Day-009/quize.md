# Day 009 Quiz

## Multiple Choice Questions (MCQs)

### Q1. What is the scope of a local variable?

A. Entire Program

B. Inside the Function Only

C. Outside the Function

D. Everywhere

**Answer:** ________

---

### Q2. Which keyword is used to modify a global variable inside a function?

A. local

B. global

C. public

D. static

**Answer:** ________

---

### Q3. What does `*args` store?

A. List

B. Tuple

C. Dictionary

D. String

**Answer:** ________

---

### Q4. What does `**kwargs` store?

A. List

B. Tuple

C. Dictionary

D. Integer

**Answer:** ________

---

### Q5. Which keyword creates an anonymous function?

A. function

B. lambda

C. def

D. return

**Answer:** ________

---

### Q6. Which of the following is true about recursion?

A. A function calling another function

B. A function calling itself

C. A loop inside a function

D. None of these

**Answer:** ________

---

### Q7. Which statement stops a recursive function?

A. continue

B. break

C. Base Case

D. pass

**Answer:** ________

---

### Q8. Which function can accept unlimited positional arguments?

A. **kwargs

B. *args

C. lambda

D. return

**Answer:** ________

---

### Q9. Which function can accept unlimited keyword arguments?

A. **kwargs

B. *args

C. lambda

D. global

**Answer:** ________

---

### Q10. What error occurs when recursion has no stopping condition?

A. SyntaxError

B. NameError

C. RecursionError

D. IndexError

**Answer:** ________

---

# True or False

### Q11.

A global variable can be accessed inside a function.

**Answer:** ________

---

### Q12.

Local variables can be used outside the function.

**Answer:** ________

---

### Q13.

`*args` stores values in a tuple.

**Answer:** ________

---

### Q14.

`**kwargs` stores values in a dictionary.

**Answer:** ________

---

### Q15.

Lambda functions always require the `def` keyword.

**Answer:** ________

---

### Q16.

Every recursive function must have a base case.

**Answer:** ________

---

### Q17.

A lambda function can have only one expression.

**Answer:** ________

---

### Q18.

`global` allows a function to modify a global variable.

**Answer:** ________

---

### Q19.

Recursion can solve factorial problems.

**Answer:** ________

---

### Q20.

`*args` and `**kwargs` can be used in the same function.

**Answer:** ________

---

# Short Answer Questions

### Q21.

What is Variable Scope?

---

### Q22.

What is the difference between Local and Global Variables?

---

### Q23.

Why do we use the `global` keyword?

---

### Q24.

What is `*args`?

---

### Q25.

What is `**kwargs`?

---

### Q26.

What is a Lambda Function?

---

### Q27.

What is Recursion?

---

### Q28.

What is a Base Case?

---

### Q29.

Give one real-world use of Lambda Functions.

---

### Q30.

Why is recursion useful?

---

# Predict the Output

### Q31.

```python
x = 10

def show():
    print(x)

show()
```

**Output:**

____________________

---

### Q32.

```python
def add(*numbers):
    print(sum(numbers))

add(5, 10, 15)
```

**Output:**

____________________

---

### Q33.

```python
def student(**data):
    print(data["name"])

student(name="Amit", age=22)
```

**Output:**

____________________

---

### Q34.

```python
square = lambda x: x*x

print(square(8))
```

**Output:**

____________________

---

### Q35.

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(4))
```

**Output:**

____________________

---

# Debug the Code

### Q36.

```python
count = 0

def increase():
    count += 1

increase()

print(count)
```

**What's wrong?**

____________________

---

### Q37.

```python
square = lambda x
print(square(5))
```

**Find the mistake.**

____________________

---

### Q38.

```python
def student(**kwargs):
    print(kwargs(name))
```

**Find the mistake.**

____________________

---

### Q39.

```python
def factorial(n):
    return n * factorial(n-1)
```

**Why is this function dangerous?**

____________________

---

### Q40.

```python
def add(*args, **kwargs):
    print(args)
    print(kwargs)
```

Is this function valid?

____________________

---

# Interview Questions

1. What is Variable Scope in Python?

2. Explain Local vs Global Variables.

3. What is the `global` keyword?

4. Explain `*args` with an example.

5. Explain `**kwargs` with an example.

6. What is the difference between `*args` and `**kwargs`?

7. What is a Lambda Function?

8. Why are Lambda Functions useful?

9. What is Recursion?

10. What is the importance of a Base Case in recursion?

11. What are the advantages of recursion?

12. What are the disadvantages of recursion?

13. Where is recursion used in real-world programming?

14. Can `*args` and `**kwargs` be used together? Explain.

15. When should you use recursion instead of loops?

---

# Coding Challenge

### Challenge 1

Write a function using `*args` that returns the average of all numbers.

---

### Challenge 2

Create a function using `**kwargs` that prints a student's complete profile.

---

### Challenge 3

Create a lambda function that returns the cube of a number.

---

### Challenge 4

Write a recursive function to calculate the sum of the first `n` natural numbers.

---

### Challenge 5

Write a recursive function to check whether a string is a palindrome.

---

# Quick Revision

## Variable Scope

```
Global Variable
       │
       ▼
Accessible Everywhere

------------------------

Local Variable
       │
       ▼
Accessible Only Inside Function
```

---

## *args

```
Multiple Positional Arguments

↓

Stored as Tuple
```

---

## **kwargs

```
Multiple Keyword Arguments

↓

Stored as Dictionary
```

---

## Lambda Function

```python
lambda arguments : expression
```

---

## Recursion

```
Function

↓

Calls Itself

↓

Base Case

↓

Stops
```

---

# Key Takeaways

✔ Local variables exist only inside functions.

✔ Global variables are accessible throughout the program.

✔ Use `global` to modify a global variable inside a function.

✔ `*args` accepts unlimited positional arguments.

✔ `**kwargs` accepts unlimited keyword arguments.

✔ Lambda functions are short, anonymous functions.

✔ Recursion is a function calling itself.

✔ Every recursive function must have a base case.

✔ `*args` stores data as a tuple.

✔ `**kwargs` stores data as a dictionary.

---

# Day 009 Complete

If you can confidently explain **Variable Scope**, **`*args`**, **`**kwargs`**, **Lambda Functions**, and **Recursion**, and solve today's exercises without looking at the solutions, you've built a strong understanding of advanced Python functions that will help you in AI/ML, software development, and coding interviews.