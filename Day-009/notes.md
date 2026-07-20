# Day 009 - Functions (Part 2)

> **"Functions become truly powerful when they can handle flexible inputs, access variables correctly, and even call themselves."**

---

# Introduction

In Day 8, we learned how to create and use functions.

Today, we'll explore advanced function concepts that make Python more powerful and flexible. These concepts are widely used in AI/ML libraries, web development, automation, and software engineering.

Topics covered:

- Variable Scope
- Global Keyword
- *args
- **kwargs
- Lambda Functions
- Recursion

---

# 1. Variable Scope

## What is Scope?

**Scope** refers to the region of a program where a variable can be accessed.

Python has two common scopes:

- Local Scope
- Global Scope

---

# Local Variable

A variable created inside a function is called a **local variable**.

It can only be used inside that function.

Example:

```python
def greet():
    name = "Amit"
    print(name)

greet()
```

Output

```
Amit
```

Trying to access `name` outside the function will produce an error.

```python
print(name)
```

Output

```
NameError
```

---

# Global Variable

A variable created outside every function is called a **global variable**.

It can be accessed from anywhere in the program.

Example

```python
name = "Amit"

def greet():
    print(name)

greet()
print(name)
```

Output

```
Amit
Amit
```

---

# Global Keyword

Normally, a function cannot change a global variable.

To modify it, use the **global** keyword.

Example

```python
count = 0

def increment():
    global count
    count += 1

increment()

print(count)
```

Output

```
1
```

---

# Local vs Global

| Local Variable | Global Variable |
|---------------|----------------|
| Created inside a function | Created outside all functions |
| Exists only inside that function | Accessible throughout the program |
| Temporary | Exists until the program ends |

---

# 2. *args

Sometimes we don't know how many values a function will receive.

Python provides **\*args**.

It collects multiple positional arguments into a tuple.

Syntax

```python
def function_name(*args):
    pass
```

Example

```python
def add(*numbers):
    print(numbers)

add(10,20,30)
```

Output

```
(10, 20, 30)
```

---

## Loop through *args

```python
def add(*numbers):

    total = 0

    for num in numbers:
        total += num

    return total

print(add(10,20,30,40))
```

Output

```
100
```

---

## Why use *args?

- Accept unlimited arguments
- Cleaner code
- Flexible functions
- Useful in libraries

---

# 3. **kwargs

Sometimes we want unlimited **keyword arguments**.

Python provides **\*\*kwargs**.

It stores values as a dictionary.

Syntax

```python
def function_name(**kwargs):
    pass
```

Example

```python
def student(**details):
    print(details)

student(name="Amit", age=22)
```

Output

```
{'name': 'Amit', 'age': 22}
```

---

## Accessing kwargs

```python
def student(**details):

    for key, value in details.items():
        print(key, value)

student(name="Amit", city="Delhi", age=22)
```

Output

```
name Amit
city Delhi
age 22
```

---

## Why use **kwargs?

- Unlimited keyword arguments
- Flexible functions
- Configuration settings
- APIs
- Web development

---

# Difference Between *args and **kwargs

| *args | **kwargs |
|--------|-----------|
| Positional Arguments | Keyword Arguments |
| Stored as Tuple | Stored as Dictionary |
| Uses * | Uses ** |

---

# 4. Lambda Functions

A **Lambda Function** is a small anonymous function.

It is written in a single line.

Syntax

```python
lambda arguments : expression
```

---

## Example 1

```python
square = lambda x: x*x

print(square(5))
```

Output

```
25
```

---

## Example 2

```python
add = lambda a,b : a+b

print(add(10,20))
```

Output

```
30
```

---

## Normal Function vs Lambda

Normal Function

```python
def square(x):
    return x*x
```

Lambda Function

```python
square = lambda x : x*x
```

---

## Advantages

- Short code
- Easy to write
- Useful with map()
- Useful with filter()
- Useful with sorted()

---

# 5. Recursion

A function calling itself is called **Recursion**.

Example

```python
def hello():

    print("Hello")

    hello()
```

This creates an infinite loop.

---

# Base Case

Every recursive function must have a stopping condition.

This is called the **Base Case**.

Without it, Python throws

```
RecursionError
```

---

# Factorial using Recursion

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(5))
```

Output

```
120
```

Working

```
factorial(5)

↓

5 × factorial(4)

↓

5 × 4 × factorial(3)

↓

5 × 4 × 3 × factorial(2)

↓

5 × 4 × 3 × 2 × factorial(1)

↓

120
```

---

# Fibonacci using Recursion

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
```

Output

```
8
```

Sequence

```
0 1 1 2 3 5 8 13 ...
```

---

# Advantages of Recursion

- Elegant code
- Solves complex problems
- Used in Trees
- Used in Graphs
- Used in Divide and Conquer Algorithms
- Used in Dynamic Programming

---

# Disadvantages

- Slower than loops
- More memory usage
- Can cause RecursionError
- Difficult to debug

---

# Real-Life Applications

## Variable Scope

- Banking Applications
- User Login Systems
- Game Development

---

## *args

- Calculator
- Shopping Cart
- AI Libraries
- NumPy

---

## **kwargs

- API Development
- Flask
- Django
- FastAPI
- Configuration Files

---

## Lambda

- Data Sorting
- Data Cleaning
- Machine Learning
- Pandas
- NumPy

---

## Recursion

- Folder Traversal
- Binary Trees
- Graph Algorithms
- File Systems
- Maze Solving
- AI Search Algorithms

---

# Summary

Today you learned:

✅ Local Variables

✅ Global Variables

✅ Global Keyword

✅ *args

✅ **kwargs

✅ Lambda Functions

✅ Recursion

✅ Factorial using Recursion

✅ Fibonacci using Recursion

---

# Key Takeaways

✔ Local variables exist only inside functions.

✔ Global variables can be accessed throughout the program.

✔ Use the `global` keyword to modify global variables inside a function.

✔ `*args` allows a function to accept any number of positional arguments.

✔ `**kwargs` allows a function to accept any number of keyword arguments.

✔ Lambda functions are short, anonymous functions written in one line.

✔ Recursion is when a function calls itself.

✔ Every recursive function must have a **base case** to stop infinite recursion.

---

## Congratulations!

You have now completed **Functions (Part 2)**.

You can now write more flexible, reusable, and professional Python functions—skills that are widely used in AI/ML, data science, automation, and software development.