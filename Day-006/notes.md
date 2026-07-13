# Day 006 – Loops (Part 1)

# Introduction

Imagine you are asked to print:

```
Hello
Hello
Hello
Hello
Hello
```

One way is:

```python
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
```

But what if you have to print **Hello** 1,000 times?

Writing `print()` 1,000 times would be a terrible idea.

This is where **Loops** come into the picture.

A loop allows us to execute the same block of code multiple times without writing it again and again.

---

# What is a Loop?

A **loop** is used to repeat a block of code until a condition is satisfied.

Think of it like this:

```
Repeat
      ↓
Repeat
      ↓
Repeat
      ↓
Stop
```

Instead of writing the same code multiple times, we tell Python:

> "Repeat this code."

---

# Types of Loops in Python

Python has two types of loops.

1. `for` Loop
2. `while` Loop

---

# The for Loop

A **for loop** is used when we already know how many times we want to repeat something.

Example:

```python
for i in range(5):
    print("Hello")
```

Output

```
Hello
Hello
Hello
Hello
Hello
```

The loop runs **5 times**.

---

# Understanding range()

The `range()` function generates a sequence of numbers.

It is commonly used with `for` loops.

There are three ways to use it.

---

## 1. range(stop)

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

Notice:

The loop starts from **0**.

The stop value is **not included**.

Memory Trick:

```
range(5)

Start = 0
Stop = 5

Output

0 1 2 3 4
```

---

## 2. range(start, stop)

```python
for i in range(2,6):
    print(i)
```

Output

```
2
3
4
5
```

Starts from **2**.

Stops before **6**.

---

## 3. range(start, stop, step)

```python
for i in range(2,11,2):
    print(i)
```

Output

```
2
4
6
8
10
```

The third value is called the **step**.

It tells Python how much to increase each time.

---

# The while Loop

A **while loop** repeats code as long as the condition is True.

Syntax

```python
while condition:
    statement
```

Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```
1
2
3
4
5
```

Unlike a `for` loop, a `while` loop depends on a condition instead of a fixed number of repetitions.

---

# Infinite Loop

An infinite loop never stops.

Example

```python
while True:
    print("Hello")
```

Since the condition is always **True**, the loop keeps running forever.

To stop it manually:

**Ctrl + C**

---

# break Statement

The `break` statement immediately exits the loop.

Example

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

Output

```
0
1
2
3
4
```

The loop stops when `i` becomes 5.

---

# continue Statement

The `continue` statement skips the current iteration and moves to the next one.

Example

```python
for i in range(6):

    if i == 3:
        continue

    print(i)
```

Output

```
0
1
2
4
5
```

Notice that **3 is skipped**.

---

# pass Statement

The `pass` statement does nothing.

It is used as a placeholder when code will be added later.

Example

```python
for i in range(5):

    if i == 3:
        pass

    print(i)
```

The program runs normally because `pass` simply tells Python to do nothing.

---

# Pattern Printing

Loops are commonly used to print patterns.

Example

```
*
**
***
****
*****
```

Example

```
1
12
123
1234
12345
```

Pattern printing improves logical thinking and prepares you for coding interviews.

---

# Number Series

Loops are also used to generate number sequences.

Examples:

- Numbers from 1 to 10
- Even numbers
- Odd numbers
- Multiplication tables
- Sum of first N numbers

---

# Real-World Applications

Loops are used in almost every software application.

Examples:

- Reading files
- Processing large datasets
- AI and Machine Learning
- Web scraping
- Automation scripts
- Games
- Banking software
- Chatbots

---

# Key Points to Remember

✔ A loop repeats a block of code.

✔ `for` loop is used when the number of iterations is known.

✔ `while` loop is used when repetition depends on a condition.

✔ `range(stop)` starts from 0.

✔ The stop value is never included.

✔ `break` exits the loop.

✔ `continue` skips the current iteration.

✔ `pass` is a placeholder.

---

# Summary

Today, we learned how to repeat tasks using loops. We explored `for` loops, the `range()` function, `while` loops, and loop control statements such as `break`, `continue`, and `pass`. These concepts are fundamental to writing efficient Python programs and are used extensively in automation, data analysis, AI/ML, and software development.