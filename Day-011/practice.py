"""
=========================================
Day 011 - Practice
Topic: Tuples
Part 1 (Programs 1-10)
=========================================

Practice each program and understand
the output before moving ahead.
"""

# ==========================================
# Practice 1
# Creating a Tuple
# ==========================================

fruits = ("Apple", "Banana", "Mango")

print(fruits)


# ==========================================
# Practice 2
# Tuple with Different Data Types
# ==========================================

data = (101, "Python", 99.5, True)

print(data)


# ==========================================
# Practice 3
# Single Element Tuple
# ==========================================

number = (100,)

print(number)
print(type(number))


# ==========================================
# Practice 4
# Positive Indexing
# ==========================================

colors = ("Red", "Green", "Blue", "Yellow")

print("First Color :", colors[0])
print("Second Color:", colors[1])
print("Last Color  :", colors[3])


# ==========================================
# Practice 5
# Negative Indexing
# ==========================================

numbers = (10, 20, 30, 40, 50)

print(numbers[-1])
print(numbers[-2])
print(numbers[-3])


# ==========================================
# Practice 6
# Tuple Slicing
# ==========================================

numbers = (10, 20, 30, 40, 50, 60)

print("Original Tuple :", numbers)
print("First 3        :", numbers[:3])
print("Last 3         :", numbers[-3:])
print("Middle         :", numbers[2:5])


# ==========================================
# Practice 7
# Reverse Tuple using Slicing
# ==========================================

numbers = (1, 2, 3, 4, 5)

print(numbers[::-1])


# ==========================================
# Practice 8
# Tuple Packing
# ==========================================

student = "Amit", 23, "Haridwar"

print(student)


# ==========================================
# Practice 9
# Tuple Unpacking
# ==========================================

student = ("Amit", 23, "Haridwar")

name, age, city = student

print("Name :", name)
print("Age  :", age)
print("City :", city)


# ==========================================
# Practice 10
# Tuple Concatenation
# ==========================================

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)


print("\nPractice Programs 1-10 Completed Successfully!")

# ==========================================
# Practice 11
# Tuple Repetition
# ==========================================

numbers = (1, 2, 3)

print(numbers * 3)


# ==========================================
# Practice 12
# Finding Length of a Tuple
# ==========================================

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Length:", len(fruits))


# ==========================================
# Practice 13
# count() Method
# ==========================================

numbers = (10, 20, 30, 20, 40, 20)

print("Count of 20:", numbers.count(20))


# ==========================================
# Practice 14
# index() Method
# ==========================================

numbers = (10, 20, 30, 40, 50)

print("Index of 30:", numbers.index(30))


# ==========================================
# Practice 15
# Membership Operator (in)
# ==========================================

languages = ("Python", "Java", "C++", "JavaScript")

print("Python" in languages)
print("HTML" in languages)


# ==========================================
# Practice 16
# Membership Operator (not in)
# ==========================================

languages = ("Python", "Java", "C++", "JavaScript")

print("HTML" not in languages)
print("Java" not in languages)


# ==========================================
# Practice 17
# Traversing Tuple using for Loop
# ==========================================

colors = ("Red", "Green", "Blue", "Yellow")

for color in colors:
    print(color)


# ==========================================
# Practice 18
# Traversing Tuple using while Loop
# ==========================================

numbers = (10, 20, 30, 40, 50)

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1


# ==========================================
# Practice 19
# Using enumerate()
# ==========================================

fruits = ("Apple", "Banana", "Mango", "Orange")

for index, fruit in enumerate(fruits):
    print(index, fruit)


# ==========================================
# Practice 20
# Built-in Functions
# ==========================================

marks = (85, 92, 76, 64, 98)

print("Maximum :", max(marks))
print("Minimum :", min(marks))
print("Sum     :", sum(marks))
print("Average :", sum(marks) / len(marks))


print("\nPractice Programs 11-20 Completed Successfully!")

# ==========================================
# Practice 21
# Nested Tuple
# ==========================================

students = (
    ("Amit", 90),
    ("Rahul", 85),
    ("Riya", 95)
)

print(students)


# ==========================================
# Practice 22
# Accessing Nested Tuple Elements
# ==========================================

students = (
    ("Amit", 90),
    ("Rahul", 85),
    ("Riya", 95)
)

print("First Student :", students[0])
print("Second Name   :", students[1][0])
print("Third Marks   :", students[2][1])


# ==========================================
# Practice 23
# Printing Nested Tuple Data
# ==========================================

students = (
    ("Amit", 90),
    ("Rahul", 85),
    ("Riya", 95)
)

print("Student Records")

for student in students:
    print("Name :", student[0])
    print("Marks:", student[1])
    print()


# ==========================================
# Practice 24
# Tuple Comparison
# ==========================================

tuple1 = (10, 20, 30)
tuple2 = (10, 20, 30)
tuple3 = (5, 10, 15)

print(tuple1 == tuple2)
print(tuple1 == tuple3)
print(tuple1 != tuple3)


# ==========================================
# Practice 25
# Convert Tuple to List
# ==========================================

numbers = (10, 20, 30, 40)

numbers_list = list(numbers)

print(numbers_list)
print(type(numbers_list))


# ==========================================
# Practice 26
# Convert List to Tuple
# ==========================================

fruits = ["Apple", "Banana", "Mango"]

fruits_tuple = tuple(fruits)

print(fruits_tuple)
print(type(fruits_tuple))


# ==========================================
# Practice 27
# Sort a Tuple
# (Convert to List → Sort → Tuple)
# ==========================================

numbers = (50, 20, 10, 40, 30)

numbers_list = list(numbers)

numbers_list.sort()

sorted_tuple = tuple(numbers_list)

print(sorted_tuple)


# ==========================================
# Practice 28
# Employee Records using Tuples
# ==========================================

employees = (
    ("E101", "Amit", "Developer"),
    ("E102", "Rahul", "Designer"),
    ("E103", "Riya", "Tester")
)

for employee in employees:
    print(employee)


# ==========================================
# Practice 29
# Student Marks Analysis
# ==========================================

marks = (85, 92, 76, 64, 98)

print("Highest :", max(marks))
print("Lowest  :", min(marks))
print("Total   :", sum(marks))
print("Average :", sum(marks) / len(marks))


# ==========================================
# Practice 30
# Product Information using Tuples
# ==========================================

product = (
    "Laptop",
    "Dell",
    65000,
    4.6
)

name, brand, price, rating = product

print("Product Name :", name)
print("Brand        :", brand)
print("Price        :", price)
print("Rating       :", rating)


print("\nCongratulations!")
print("You have successfully completed all Day 011 Practice Programs.")
print("Keep practicing and Happy Coding!")