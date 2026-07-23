# Day 012 Notes
# Topic: Dictionaries

---

# What is a Dictionary?

A **dictionary** is a built-in Python data structure that stores data in the form of **key-value pairs**.

Each key in a dictionary is unique and is used to access its corresponding value.

Unlike lists and tuples, dictionaries are optimized for fast lookup using keys.

---

# Why Use Dictionaries?

Dictionaries are useful when data has a meaningful relationship between a key and its value.

Examples:

- Student Records
- Employee Information
- Phone Contacts
- Product Details
- Country Capitals
- Word Meaning
- Configuration Settings

---

# Characteristics of Dictionaries

- Stores data as **Key : Value** pairs
- Mutable (can be modified)
- Keys must be unique
- Values can be duplicated
- Ordered (Python 3.7+)
- Fast data lookup

---

# Creating Dictionaries

## Empty Dictionary

```python
student = {}

print(student)
```

Output

```
{}
```

---

## Dictionary with Data

```python
student = {
    "name": "Amit",
    "age": 23,
    "course": "Python"
}

print(student)
```

Output

```
{'name': 'Amit', 'age': 23, 'course': 'Python'}
```

---

## Dictionary using dict()

```python
student = dict(
    name="Amit",
    age=23,
    city="Haridwar"
)

print(student)
```

---

## Nested Dictionary

```python
students = {
    "student1": {
        "name": "Amit",
        "marks": 90
    },
    "student2": {
        "name": "Rahul",
        "marks": 85
    }
}
```

---

# Accessing Values

## Using Keys

```python
student = {
    "name": "Amit",
    "age": 23
}

print(student["name"])
print(student["age"])
```

Output

```
Amit
23
```

---

## Using get()

```python
student = {
    "name": "Amit",
    "age": 23
}

print(student.get("name"))
print(student.get("city"))
```

Output

```
Amit
None
```

`get()` is safer than using square brackets because it does not raise an error if the key is missing.

---

# Adding New Items

```python
student = {
    "name": "Amit"
}

student["age"] = 23

print(student)
```

Output

```
{'name': 'Amit', 'age': 23}
```

---

# Updating Values

```python
student = {
    "name": "Amit",
    "age": 23
}

student["age"] = 24

print(student)
```

---

# Dictionary Methods

## keys()

Returns all keys.

```python
student = {
    "name": "Amit",
    "age": 23
}

print(student.keys())
```

---

## values()

Returns all values.

```python
print(student.values())
```

---

## items()

Returns key-value pairs.

```python
print(student.items())
```

---

## get()

Returns the value of a key.

```python
print(student.get("name"))
```

---

## update()

Updates one or more key-value pairs.

```python
student = {
    "name": "Amit",
    "age": 23
}

student.update({"city": "Haridwar"})

print(student)
```

Output

```
{
'name':'Amit',
'age':23,
'city':'Haridwar'
}
```

---

# Removing Items

## pop()

Removes a specific key.

```python
student.pop("age")
```

---

## popitem()

Removes the last inserted item.

```python
student.popitem()
```

---

## del

Deletes a key.

```python
del student["name"]
```

---

## clear()

Removes all items.

```python
student.clear()
```

---

# Traversing Dictionaries

## Loop Through Keys

```python
student = {
    "name":"Amit",
    "age":23,
    "city":"Haridwar"
}

for key in student:
    print(key)
```

---

## Loop Through Values

```python
for value in student.values():
    print(value)
```

---

## Loop Through Keys and Values

```python
for key, value in student.items():
    print(key, value)
```

---

# Dictionary Comprehension

Dictionary comprehension provides a concise way to create dictionaries.

## Basic Example

```python
numbers = {
    x: x*x
    for x in range(1,6)
}

print(numbers)
```

Output

```
{
1:1,
2:4,
3:9,
4:16,
5:25
}
```

---

## Conditional Dictionary Comprehension

```python
even = {
    x: x*x
    for x in range(1,11)
    if x % 2 == 0
}

print(even)
```

Output

```
{
2:4,
4:16,
6:36,
8:64,
10:100
}
```

---

# Membership Operators

## in

```python
student = {
    "name":"Amit",
    "age":23
}

print("name" in student)
```

Output

```
True
```

---

## not in

```python
print("city" not in student)
```

Output

```
True
```

---

# Nested Dictionaries

```python
students = {

    "S101": {
        "name":"Amit",
        "marks":90
    },

    "S102": {
        "name":"Rahul",
        "marks":85
    }

}

print(students["S101"]["name"])
```

Output

```
Amit
```

---

# Dictionary vs List

| Feature | Dictionary | List |
|----------|------------|------|
| Stores | Key-Value Pairs | Values |
| Ordered | Yes | Yes |
| Mutable | Yes | Yes |
| Duplicate Keys | No | Yes |
| Fast Lookup | Yes | No |

---

# Advantages of Dictionaries

- Fast searching
- Easy to update
- Easy to organize data
- Stores related information together
- Efficient for large datasets

---

# Limitations of Dictionaries

- Keys must be unique
- Keys must be immutable
- Slightly higher memory usage than lists

---

# Real-World Applications

Dictionaries are widely used in:

- Student Management Systems
- Banking Applications
- E-commerce Websites
- Contact Lists
- JSON Data
- APIs
- Employee Records
- Configuration Files
- Machine Learning Data
- Web Development

---

# Best Practices

- Use meaningful key names.
- Prefer `get()` when a key might not exist.
- Keep dictionary structures simple and readable.
- Use nested dictionaries for hierarchical data.
- Use dictionary comprehensions when appropriate.

---

# Summary

Today you learned:

- What Dictionaries are
- Creating Dictionaries
- Key-Value Pairs
- Accessing Values
- Adding Items
- Updating Items
- Removing Items
- Dictionary Methods
- Dictionary Comprehensions
- Membership Operators
- Nested Dictionaries
- Traversing Dictionaries
- Dictionary vs List
- Real-World Applications

---

# Key Takeaways

- Dictionaries store data as **key-value pairs**.
- Keys are unique and immutable.
- Values can be of any data type.
- `get()` safely retrieves values.
- `keys()`, `values()`, and `items()` are essential methods.
- Dictionary comprehensions make dictionary creation concise.
- Dictionaries are ideal for fast lookups and structured data.

---

# Congratulations!

You have successfully completed the theory for **Day 012 – Dictionaries**.

Next, you'll strengthen your understanding by solving practice programs, exercises, quizzes, and building a **Word Frequency Counter** mini project using dictionaries.