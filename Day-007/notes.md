# Day 007 – Loops (Part 2) & Logic Building

# Introduction

Congratulations! 🎉

You have already learned:

- `for` loop
- `while` loop
- `range()`
- `break`
- `continue`
- `pass`

Today, we'll move one step ahead and learn how to solve real programming problems using loops.

Today's focus is not on writing more code—it's on **thinking logically**.

---

# Nested Loops

A Nested Loop simply means:

> **A loop inside another loop.**

Syntax:

```python
for i in range(3):

    for j in range(3):
        print("*", end=" ")

    print()
```

Output

```
* * *
* * *
* * *
```

Think of it like this:

```
Outer Loop
     ↓
Runs 3 Times

Every time it runs

↓

Inner Loop

Runs Completely
```

Memory Trick

```
Outer Loop → Rows

Inner Loop → Columns
```

Whenever you see rows and columns, think of Nested Loops.

---

# Loop with else Clause

Many beginners don't know that loops can also have an `else`.

Syntax

```python
for variable in range():

    statements

else:
    statements
```

The `else` block executes only if the loop finishes normally.

Example

```python
for i in range(5):
    print(i)

else:
    print("Loop Completed")
```

Output

```
0
1
2
3
4
Loop Completed
```

---

# When does else NOT execute?

If the loop is terminated using `break`.

Example

```python
for i in range(5):

    if i == 3:
        break

    print(i)

else:
    print("Completed")
```

Output

```
0
1
2
```

Notice:

The `else` block is skipped because the loop ended using `break`.

---

# Prime Number

A Prime Number has only two factors:

- 1
- Itself

Examples

Prime Numbers

```
2
3
5
7
11
13
17
19
```

Not Prime

```
4
6
8
9
10
12
```

Logic

```
Take a Number

↓

Count Factors

↓

Exactly Two?

↓

Prime
```

---

# Factorial

Factorial means multiplying every number from 1 to the given number.

Example

```
5!

↓

5 × 4 × 3 × 2 × 1

↓

120
```

Examples

```
4!

↓

24

6!

↓

720
```

Memory Trick

```
Factorial

=

Repeated Multiplication
```

---

# Fibonacci Series

A Fibonacci Series is a sequence where:

Every new number is the sum of the previous two numbers.

Example

```
0 1 1 2 3 5 8 13 21 ...
```

How?

```
0 + 1 = 1

1 + 1 = 2

1 + 2 = 3

2 + 3 = 5

3 + 5 = 8
```

Memory Trick

```
Next Number

=

Previous Two Numbers Added Together
```

---

# Logic Building

Programming is not about remembering syntax.

Programming is about solving problems.

Today's goal is to improve your logical thinking.

We'll solve beginner problems like:

- Reverse Counting
- Prime Number
- Factorial
- Fibonacci Series
- Number Patterns
- Star Patterns
- Multiplication Tables
- Sum of Numbers
- Count Digits
- Reverse a Number

These problems are commonly asked in coding interviews and help build strong programming fundamentals.

---

# Real-World Applications

Loops are used in:

- AI and Machine Learning
- Data Processing
- Automation
- Banking Software
- Games
- Chatbots
- Pattern Recognition
- Report Generation
- Searching Algorithms
- Data Analysis

---

# Key Points to Remember

✔ Nested Loop = Loop inside another loop.

✔ Outer Loop controls Rows.

✔ Inner Loop controls Columns.

✔ `else` executes only when the loop finishes normally.

✔ `break` skips the `else` block.

✔ Prime Numbers have exactly two factors.

✔ Factorial uses repeated multiplication.

✔ Fibonacci is formed by adding the previous two numbers.

✔ Logic improves only by solving problems.

---

# Summary

Today, we explored Nested Loops, the `else` clause with loops, Prime Numbers, Factorials, and the Fibonacci Series. More importantly, we started focusing on logical thinking and problem-solving. These concepts form the foundation for coding interviews, DSA, competitive programming, and real-world software development.