# Day 011 Notes
# Topic: Tuples

---

# What is a Tuple?

A **tuple** is an ordered collection of items in Python. It can store multiple values of different data types in a single variable.

Unlike lists, **tuples are immutable**, which means their elements **cannot be changed, added, or removed** after creation.

---

# Why Use Tuples?

Tuples are useful when you want to store data that should remain constant throughout the program.

Examples:
- Coordinates (x, y)
- RGB Colors
- Student Records
- Employee Details
- Days of the Week
- Months of the Year

---

# Characteristics of Tuples

- Ordered
- Immutable
- Allows Duplicate Values
- Can Store Different Data Types
- Faster than Lists
- Supports Indexing and Slicing

---

# Creating Tuples

### Empty Tuple

```python
empty_tuple = ()
```

---

### Tuple with Integers

```python
numbers = (10, 20, 30, 40)
```

---

### Tuple with Strings

```python
fruits = ("Apple", "Banana", "Mango")
```

---

### Mixed Data Types

```python
data = (101, "Amit", 95.5, True)
```

---

### Nested Tuple

```python
student = (
    ("Amit", 101),
    ("Rahul", 102)
)
```

---

# Creating a Single Element Tuple

A single element tuple **must** have a comma.

Correct:

```python
number = (5,)
```

Wrong:

```python
number = (5)
```

The second one is treated as an integer.

---

# Accessing Tuple Elements

Indexing starts from **0**.

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits[0])
print(fruits[1])
print(fruits[2])
```

Output

```
Apple
Banana
Mango
```

---

# Negative Indexing

Negative indexing starts from **-1**.

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits[-1])
print(fruits[-2])
```

Output

```
Mango
Banana
```

---

# Tuple Slicing

Syntax

```python
tuple[start:stop:step]
```

Example

```python
numbers = (10,20,30,40,50,60)

print(numbers[:3])
print(numbers[2:])
print(numbers[1:5])
print(numbers[::-1])
```

Output

```
(10,20,30)
(30,40,50,60)
(20,30,40,50)
(60,50,40,30,20,10)
```

---

# Tuple Packing

Packing means storing multiple values into one tuple.

```python
student = ("Amit", 23, "Delhi")
```

---

# Tuple Unpacking

Unpacking means assigning tuple elements to variables.

```python
student = ("Amit", 23, "Delhi")

name, age, city = student

print(name)
print(age)
print(city)
```

Output

```
Amit
23
Delhi
```

---

# Tuple Methods

Python tuples have only **two built-in methods**.

---

## count()

Counts how many times a value appears.

```python
numbers = (10,20,30,20,40)

print(numbers.count(20))
```

Output

```
2
```

---

## index()

Returns the position of an element.

```python
numbers = (10,20,30,40)

print(numbers.index(30))
```

Output

```
2
```

---

# Tuple Operations

## Concatenation

```python
tuple1 = (1,2,3)

tuple2 = (4,5,6)

print(tuple1 + tuple2)
```

Output

```
(1,2,3,4,5,6)
```

---

## Repetition

```python
numbers = (1,2)

print(numbers * 3)
```

Output

```
(1,2,1,2,1,2)
```

---

# Membership Operators

## in

```python
fruits = ("Apple","Banana","Mango")

print("Apple" in fruits)
```

Output

```
True
```

---

## not in

```python
print("Orange" not in fruits)
```

Output

```
True
```

---

# Iterating Through Tuples

## Using for Loop

```python
fruits = ("Apple","Banana","Mango")

for fruit in fruits:
    print(fruit)
```

---

## Using while Loop

```python
numbers = (10,20,30)

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1
```

---

# Nested Tuples

A tuple can contain another tuple.

```python
students = (
    ("Amit",90),
    ("Rahul",85),
    ("Riya",95)
)

print(students[0])
print(students[1][0])
print(students[2][1])
```

---

# Tuple vs List

| Feature | Tuple | List |
|----------|-------|------|
| Syntax | () | [] |
| Mutable | No | Yes |
| Ordered | Yes | Yes |
| Faster | Yes | Slightly Slower |
| Duplicate Values | Yes | Yes |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |

---

# Advantages of Tuples

- Faster than Lists
- Less Memory Usage
- Safe for Read-Only Data
- Can Be Used as Dictionary Keys
- Suitable for Fixed Collections

---

# Limitations of Tuples

- Cannot Add Elements
- Cannot Remove Elements
- Cannot Modify Existing Elements

---

# Real-World Applications

Tuples are commonly used for:

- Employee Records
- Student Information
- GPS Coordinates
- RGB Color Values
- Database Records
- Product Details
- Date and Time
- Configuration Settings

---

# Best Practices

- Use tuples when data should not change.
- Use meaningful variable names.
- Prefer tuples for fixed collections.
- Use lists when frequent modification is required.

---

# Summary

Today you learned:

- What Tuples are
- Creating Tuples
- Single Element Tuples
- Packing and Unpacking
- Indexing
- Negative Indexing
- Slicing
- Tuple Methods
- Tuple Operations
- Membership Operators
- Iterating Through Tuples
- Nested Tuples
- Tuple vs List
- Advantages and Limitations
- Real-World Applications

---

# Key Takeaways

- Tuples are ordered and immutable.
- They support indexing and slicing.
- Only two built-in methods are available: `count()` and `index()`.
- Packing and unpacking make tuples easy to use.
- Tuples are ideal for storing fixed data.
- They are faster and more memory-efficient than lists.

---

# Congratulations!

You have successfully completed the theory for **Day 011 – Tuples**.

Next, you'll strengthen your understanding by solving practice programs, exercises, quizzes, and building a real-world mini project using tuples.