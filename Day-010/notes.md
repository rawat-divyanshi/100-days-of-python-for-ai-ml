# 📘 Day 010 - Lists in Python

> *"Lists are one of the most powerful and versatile data structures in Python. They allow us to store multiple values in a single variable and are widely used in real-world applications such as AI, Machine Learning, Data Science, Web Development, and Automation."*

---

# 📚 What is a List?

A **list** is an ordered collection of items.

A list can store:

- Integers
- Floating-point numbers
- Strings
- Boolean values
- Objects
- Other Lists

Unlike strings, **lists are mutable**, which means we can modify their elements after creation.

---

# ✨ Characteristics of Lists

- Ordered
- Mutable (Can be modified)
- Allows duplicate values
- Can store different data types
- Indexed
- Dynamic size

Example:

```python
numbers = [10, 20, 30, 40]
```

---

# 🏗 Creating Lists

## Empty List

```python
my_list = []
```

or

```python
my_list = list()
```

---

## List of Integers

```python
numbers = [10, 20, 30, 40]
```

---

## List of Strings

```python
fruits = ["Apple", "Banana", "Mango"]
```

---

## Mixed Data Types

```python
data = [10, "Python", 3.14, True]
```

---

## Nested List

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

---

# 📍 Indexing

Every element has an index.

Positive Indexing starts from **0**.

```python
fruits = ["Apple", "Banana", "Mango"]

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

# 📍 Negative Indexing

Negative indexing starts from the end.

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
```

Output

```
Mango
Banana
Apple
```

---

# ✂ List Slicing

Syntax

```python
list[start:stop:step]
```

Example

```python
numbers = [10,20,30,40,50,60]

print(numbers[1:4])
```

Output

```
[20,30,40]
```

---

## Skip Elements

```python
numbers = [10,20,30,40,50,60]

print(numbers[::2])
```

Output

```
[10,30,50]
```

---

## Reverse a List

```python
numbers = [10,20,30,40]

print(numbers[::-1])
```

Output

```
[40,30,20,10]
```

---

# 🔧 List Methods

---

## 1. append()

Adds an element to the end.

```python
fruits = ["Apple","Banana"]

fruits.append("Mango")

print(fruits)
```

Output

```
['Apple', 'Banana', 'Mango']
```

---

## 2. insert()

Inserts an element at a specific position.

```python
fruits = ["Apple","Banana"]

fruits.insert(1,"Orange")

print(fruits)
```

Output

```
['Apple', 'Orange', 'Banana']
```

---

## 3. remove()

Removes the first matching value.

```python
numbers = [10,20,30]

numbers.remove(20)

print(numbers)
```

Output

```
[10,30]
```

---

## 4. pop()

Removes an element using its index.

```python
numbers = [10,20,30]

numbers.pop()

print(numbers)
```

Output

```
[10,20]
```

---

## 5. sort()

Sorts the list in ascending order.

```python
numbers = [40,10,30,20]

numbers.sort()

print(numbers)
```

Output

```
[10,20,30,40]
```

---

### Descending Order

```python
numbers.sort(reverse=True)

print(numbers)
```

Output

```
[40,30,20,10]
```

---

## 6. reverse()

Reverses the list.

```python
numbers = [10,20,30]

numbers.reverse()

print(numbers)
```

Output

```
[30,20,10]
```

---

# 📋 Useful Built-in Functions

## Length

```python
numbers = [10,20,30]

print(len(numbers))
```

---

## Maximum

```python
print(max(numbers))
```

---

## Minimum

```python
print(min(numbers))
```

---

## Sum

```python
print(sum(numbers))
```

---

# 🔁 Traversing a List

## Using for Loop

```python
fruits = ["Apple","Banana","Mango"]

for fruit in fruits:
    print(fruit)
```

---

## Using while Loop

```python
numbers = [10,20,30]

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1
```

---

## Using enumerate()

```python
fruits = ["Apple","Banana","Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output

```
0 Apple
1 Banana
2 Mango
```

---

# ⚡ List Comprehension

List Comprehension is a shorter way to create lists.

Syntax

```python
[expression for item in iterable]
```

---

## Example 1

```python
numbers = [x for x in range(5)]

print(numbers)
```

Output

```
[0,1,2,3,4]
```

---

## Example 2

Squares

```python
squares = [x*x for x in range(1,6)]

print(squares)
```

Output

```
[1,4,9,16,25]
```

---

## Example 3

Even Numbers

```python
even = [x for x in range(20) if x % 2 == 0]

print(even)
```

Output

```
[0,2,4,6,8,10,12,14,16,18]
```

---

# 🌍 Real-World Applications

Lists are used in:

- Student Records
- Shopping Cart
- Employee Management
- Machine Learning Datasets
- Image Processing
- Banking Systems
- Social Media Applications
- Task Management Systems
- Game Development

---

# ⚖ List vs Tuple

| List | Tuple |
|------|------|
| Mutable | Immutable |
| Uses [] | Uses () |
| Can Modify | Cannot Modify |
| Slower | Faster |
| More Flexible | More Secure |

---

# 💡 Tips

- Use lists when data may change.
- Use slicing to access multiple elements.
- Prefer list comprehensions for cleaner code.
- Use `append()` to add items.
- Use `remove()` to remove by value.
- Use `pop()` to remove by index.
- Use `sort()` to arrange data.
- Use `reverse()` to reverse the order.

---

# 📝 Summary

Today, we learned:

✅ Creating Lists

✅ Indexing

✅ Negative Indexing

✅ List Slicing

✅ List Methods

- append()
- insert()
- remove()
- pop()
- sort()
- reverse()

✅ Built-in Functions

- len()
- max()
- min()
- sum()

✅ Traversing Lists

- for loop
- while loop
- enumerate()

✅ List Comprehension

---

# 🎯 Key Takeaways

- Lists are ordered and mutable collections.
- They can store multiple values of different data types.
- Indexing and slicing help access elements efficiently.
- List methods simplify insertion, deletion, sorting, and modification.
- List comprehensions provide a concise and Pythonic way to create lists.
- Lists are one of the most frequently used data structures in Python and form the foundation for working with data in AI/ML.

---

# 🚀 Congratulations!

You have successfully completed the theory for **Day 010 – Lists**.

The next step is to practice these concepts by solving coding exercises and building small projects.