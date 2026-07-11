# Day 005 – Conditional Statements

# Introduction

Until now, every Python program we wrote executed **line by line**.

But real-world programs are smarter.

They make decisions.

Think about these situations:

- If it is raining, take an umbrella.
- If you are 18 or older, you can vote.
- If your password is correct, you can log in.
- If your exam marks are above 40, you pass.

This ability to make decisions is called **Conditional Statements**.

Today, we'll learn how to make our programs think.

---

# What is a Conditional Statement?

A conditional statement allows a program to execute different blocks of code depending on whether a condition is **True** or **False**.

Think of it like asking a question.

Example:

Is age greater than or equal to 18?

If YES → Allow voting.

If NO → Do not allow voting.

Python does the same thing.

---

# Comparison Operators

Before learning `if`, we need to know how Python compares values.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `10 == 10` → True |
| `!=` | Not Equal to | `10 != 5` → True |
| `>` | Greater Than | `20 > 15` → True |
| `<` | Less Than | `5 < 10` → True |
| `>=` | Greater Than or Equal To | `18 >= 18` → True |
| `<=` | Less Than or Equal To | `15 <= 20` → True |

These operators always return either:

- `True`
- `False`

---

# The if Statement

The `if` statement is the simplest conditional statement.

It asks:

**"Is this condition True?"**

If the answer is **Yes**, Python executes the code.

If the answer is **No**, Python skips it.

Syntax:

```python
if condition:
    statement
```

Example:

```python
age = 20

if age >= 18:
    print("You can vote.")
```

Output

```
You can vote.
```

---

Example

```python
age = 15

if age >= 18:
    print("You can vote.")
```

Output

```
Nothing
```

Why?

Because the condition is False.

---

# Indentation

One of Python's special features is **Indentation**.

Most programming languages use `{ }`.

Python uses spaces.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Notice the spaces before `print()`.

These spaces tell Python that the line belongs to the `if` statement.

Without indentation:

```python
if age >= 18:
print("Adult")
```

Python gives an error.

Always use **4 spaces** or press the **Tab** key.

---

# if...else Statement

Sometimes we want Python to do something when the condition is False.

That's where `else` comes in.

Syntax:

```python
if condition:
    statement

else:
    statement
```

Example:

```python
age = 16

if age >= 18:
    print("Eligible to Vote")

else:
    print("Not Eligible")
```

Output

```
Not Eligible
```

---

# if...elif...else

What if there are more than two choices?

Example:

Marks

90–100 → Grade A

75–89 → Grade B

50–74 → Grade C

Below 50 → Fail

Instead of writing many `if` statements, Python provides `elif`.

Example:

```python
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")
```

Output

```
Grade B
```

---

# Nested if

A Nested if means an `if` statement inside another `if`.

Example

Imagine entering an exam hall.

Question 1

Do you have an Admit Card?

If YES

↓

Question 2

Do you have an ID Card?

If YES

↓

Enter Exam Hall

Python does exactly the same thing.

Example

```python
age = 20
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to Vote")
```

---

# Ternary Operator

Sometimes an entire if-else can be written in one line.

Syntax

```python
value_if_true if condition else value_if_false
```

Example

```python
age = 20

message = "Adult" if age >= 18 else "Minor"

print(message)
```

Output

```
Adult
```

---

# Real-Life Applications

Conditional statements are used everywhere.

- ATM Machines
- Login Systems
- Face Unlock
- OTP Verification
- Shopping Websites
- Food Delivery Apps
- AI Chatbots
- Games

Every smart application makes decisions using conditional statements.

---

# Key Points to Remember

✔ Every condition returns either True or False.

✔ Python uses indentation instead of braces.

✔ `if` checks one condition.

✔ `if-else` gives two choices.

✔ `elif` handles multiple conditions.

✔ Nested `if` means an `if` inside another `if`.

✔ Ternary Operator writes simple if-else in one line.

---

# Summary

Today, we learned how Python makes decisions using conditional statements. We explored `if`, `if-else`, `if-elif-else`, nested `if`, and the ternary operator. These concepts are the foundation of decision-making in programming and are used in almost every real-world application.