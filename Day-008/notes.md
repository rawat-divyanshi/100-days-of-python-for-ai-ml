# Day 008 – Functions (Part 1)

# Introduction

Imagine you need to print the same welcome message 20 times in different parts of your program.

One way is to write the same code again and again.

```python
print("Welcome to Python")
print("Welcome to Python")
print("Welcome to Python")
```

But repeating code is not a good practice.

Instead, we can write the code **once** and use it whenever we need it.

This is exactly why **Functions** exist.

---

# What is a Function?

A **Function** is a reusable block of code that performs a specific task.

Think of it as a machine.

```
Input
   ↓
Function
   ↓
Output
```

Instead of writing the same code multiple times, we write it once inside a function and call it whenever needed.

---

# Why Do We Use Functions?

Functions make our programs:

- Shorter
- Cleaner
- Easier to Read
- Easier to Debug
- Reusable

Without Functions

```python
print("Hello Amit")
print("Hello Amit")
print("Hello Amit")
```

With Functions

```python
def greet():
    print("Hello Amit")

greet()
greet()
greet()
```

Same output, but much cleaner.

---

# Defining a Function

We create a function using the `def` keyword.

Syntax

```python
def function_name():
    statements
```

Example

```python
def greet():
    print("Hello, Welcome to Python!")
```

Here,

- `def` tells Python that we are creating a function.
- `greet` is the function name.
- `()` can hold parameters.
- `:` starts the function body.

---

# Calling a Function

Defining a function does **not** execute it.

We must **call** it.

Example

```python
def greet():
    print("Hello!")

greet()
```

Output

```
Hello!
```

Memory Trick

```
Define

↓

Store the Function

↓

Call

↓

Execute the Function
```

---

# Parameters

Parameters are variables written inside the function definition.

Example

```python
def greet(name):
    print("Hello", name)
```

Here,

`name` is a **Parameter**.

Think of a parameter as an **empty box** waiting for a value.

---

# Arguments

Arguments are the actual values we pass while calling a function.

Example

```python
greet("Amit")
```

Here,

`"Amit"` is an **Argument**.

Memory Trick

```
Function Definition

↓

Parameter

Function Call

↓

Argument
```

Example

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Parameters → `a`, `b`

Arguments → `10`, `20`

---

# Default Parameters

A default parameter already has a value.

If no argument is given, Python uses the default value.

Example

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Amit")
```

Output

```
Hello Guest
Hello Amit
```

---

# Return Statement

The `return` statement sends a value back to the place where the function was called.

Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output

```
30
```

---

# print() vs return

Many beginners confuse these two.

## print()

- Displays output on the screen.
- Does not send the value back.

Example

```python
def add(a, b):
    print(a + b)
```

---

## return

- Sends the value back.
- Can be stored in a variable.
- Can be used in further calculations.

Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Memory Trick

```
print()

↓

Show Output

----------------------

return

↓

Give Output Back
```

---

# Real-Life Example

Imagine a restaurant.

You order food.

The chef prepares it.

Then the waiter **returns** the food to your table.

```
Input

↓

Kitchen (Function)

↓

Return Food

↓

Customer
```

That's exactly how `return` works.

---

# Why is return Better?

Suppose we want to multiply the result by 2.

Using `print()`

```python
def add(a, b):
    print(a + b)
```

We cannot use the answer later.

Using `return`

```python
def add(a, b):
    return a + b

answer = add(10, 20)

print(answer * 2)
```

Output

```
60
```

---

# Real-World Applications

Functions are used everywhere.

- ATM Machines
- Banking Software
- AI Models
- Games
- Websites
- Mobile Apps
- Chatbots
- Data Analysis
- Machine Learning
- Automation Scripts

Large software projects may contain thousands of functions.

---

# Key Points to Remember

✔ A function is a reusable block of code.

✔ `def` is used to create a function.

✔ A function executes only when it is called.

✔ Parameters receive values.

✔ Arguments provide values.

✔ Default parameters make functions flexible.

✔ `print()` displays output.

✔ `return` sends the value back.

✔ Functions reduce code duplication.

---

# Summary

Today, we learned one of the most important concepts in programming: **Functions**. We explored how to define and call functions, understood the difference between parameters and arguments, learned about default parameters, and compared `print()` with `return`. Functions help us write cleaner, reusable, and more professional code, making them a fundamental building block of software development.