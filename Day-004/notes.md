# Day 004 – Input, Type Conversion & Strings

## Introduction

Today, we learned how to make Python programs interactive by taking input from the user. We also explored strings, one of the most commonly used data types in Python, and learned how to access, manipulate, and format them.

---

# 1. The `input()` Function

## What is `input()`?

The `input()` function is used to take input from the user while the program is running.

Syntax:

```python
variable = input("Enter something: ")
```

Example:

```python
name = input("Enter your name: ")
print(name)
```

### Output

```
Enter your name: Amit
Amit
```

### Important Note

No matter what the user enters, `input()` always returns a **string (`str`)**.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

Output:

```
<class 'str'>
```

Even if the user enters:

```
20
```

Python stores it as:

```python
"20"
```

and **not** as the number `20`.

---

# 2. Type Conversion

## What is Type Conversion?

Type conversion means changing one data type into another.

Python provides built-in functions for this purpose.

### `int()`

Converts a value into an integer.

```python
age = int(input("Enter your age: "))
```

---

### `float()`

Converts a value into a decimal number.

```python
price = float("99.99")
```

---

### `str()`

Converts a value into a string.

```python
age = 22

text = str(age)
```

---

### `bool()`

Converts a value into `True` or `False`.

Examples:

```python
bool(1)
```

Output:

```
True
```

```python
bool(0)
```

Output:

```
False
```

---

## Why is Type Conversion Needed?

Consider this example:

```python
age = input("Enter your age: ")

print(age + 5)
```

This produces an error because `age` is a string and `5` is an integer.

Correct version:

```python
age = int(input("Enter your age: "))

print(age + 5)
```

Output:

```
Enter your age: 20
25
```

---

# 3. Strings

## What is a String?

A string is a sequence of characters enclosed inside quotes.

A string may contain:

* Letters
* Numbers
* Spaces
* Symbols
* Emojis
* Special characters

Examples:

```python
name = "Amit"

city = "Delhi"

course = "Python for AI/ML"
```

---

## Ways to Create Strings

### Double Quotes

```python
language = "Python"
```

### Single Quotes

```python
language = 'Python'
```

### Triple Quotes

Used for multi-line strings.

```python
message = """
Hello
Welcome to Python
"""
```

---

# 4. String Indexing

Every character inside a string has a position called an **index**.

Example:

```python
word = "Python"
```

| Character | P | y | t | h | o | n |
| --------- | - | - | - | - | - | - |
| Index     | 0 | 1 | 2 | 3 | 4 | 5 |

Python starts counting from **0**.

Examples:

```python
print(word[0])
```

Output:

```
P
```

```python
print(word[3])
```

Output:

```
h
```

---

## Negative Indexing

Python can also count from the end.

| Character      | P  | y  | t  | h  | o  | n  |
| -------------- | -- | -- | -- | -- | -- | -- |
| Negative Index | -6 | -5 | -4 | -3 | -2 | -1 |

Example:

```python
print(word[-1])
```

Output:

```
n
```

---

# 5. String Slicing

Slicing allows us to extract a part of a string.

Syntax:

```python
string[start:stop:step]
```

### Important Rule

* **Start index is included.**
* **Stop index is excluded.**

Example:

```python
word = "Python"

print(word[0:4])
```

Output:

```
Pyth
```

Python includes indexes:

```
0
1
2
3
```

but excludes index `4`.

---

## Common Examples

### From the beginning

```python
word[:4]
```

Output:

```
Pyth
```

---

### Till the end

```python
word[2:]
```

Output:

```
thon
```

---

### Every second character

```python
word[::2]
```

Output:

```
Pto
```

---

### Reverse a String

```python
word[::-1]
```

Output:

```
nohtyP
```

---

# 6. String Immutability

## What does Immutable mean?

Immutable means **cannot be changed after creation**.

Example:

```python
word = "Python"

word[0] = "J"
```

Output:

```
TypeError
```

This happens because strings cannot be modified character by character.

---

## How Can We Change a String?

Instead of changing the existing string, Python creates a **new string**.

Example:

```python
word = "Python"

word = "Jython"
```

This is valid because the variable now points to a completely new string.

---

# 7. String Methods

String methods are built-in functions that help us work with strings more easily.

---

## `upper()`

Converts all letters to uppercase.

```python
text = "python"

print(text.upper())
```

Output:

```
PYTHON
```

---

## `lower()`

Converts all letters to lowercase.

```python
text = "PYTHON"

print(text.lower())
```

Output:

```
python
```

---

## `strip()`

Removes extra spaces from the beginning and end.

```python
text = "   Python   "

print(text.strip())
```

Output:

```
Python
```

---

## `replace()`

Replaces one word or character with another.

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output:

```
I like Python
```

---

## `split()`

Splits a string into a list.

```python
text = "Python AI ML"

print(text.split())
```

Output:

```python
['Python', 'AI', 'ML']
```

---

## `join()`

Joins multiple strings into one.

```python
words = ["Python", "AI", "ML"]

print(" ".join(words))
```

Output:

```
Python AI ML
```

---

## `format()`

An older method for formatting strings.

```python
name = "Amit"

print("Hello {}".format(name))
```

Output:

```
Hello Amit
```

---

# 8. f-Strings (Recommended)

f-Strings are the modern and recommended way to format strings.

Syntax:

```python
f"text {variable}"
```

Example:

```python
name = "Amit"

print(f"Hello {name}")
```

Output:

```
Hello Amit
```

Example with multiple variables:

```python
name = "Amit"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

Output:

```
My name is Amit and I am 22 years old.
```

---

# Key Points to Remember

* `input()` always returns a string.
* Use `int()`, `float()`, `str()`, or `bool()` for type conversion.
* A string is a sequence of characters enclosed in quotes.
* Python uses **zero-based indexing**.
* In slicing, the **start index is included** and the **stop index is excluded**.
* Strings are **immutable**, meaning individual characters cannot be changed.
* String methods make text processing easier.
* f-Strings are the preferred way to format output in modern Python.

---

# Summary

In this lesson, you learned how to take user input, convert data types, work with strings, access characters using indexing, extract parts of strings using slicing, understand why strings are immutable, use common string methods, and format output using f-strings. These concepts are fundamental and will be used throughout Python programming, data analysis, automation, and AI/ML projects.
