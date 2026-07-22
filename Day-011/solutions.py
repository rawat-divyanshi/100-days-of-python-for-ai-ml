"""
=========================================
Day 011 - Solutions
Topic: Tuples
Part 1 (Exercises 1-10)
=========================================
"""

# ==========================================
# Solution 1
# Create a tuple containing five integers.
# ==========================================

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)


# ==========================================
# Solution 2
# Create a tuple containing your name,
# age, and city.
# ==========================================

person = ("Amit", 23, "Haridwar")

print(person)


# ==========================================
# Solution 3
# Print the first element of a tuple.
# ==========================================

fruits = ("Apple", "Banana", "Mango")

print("First Element:", fruits[0])


# ==========================================
# Solution 4
# Print the last element using
# negative indexing.
# ==========================================

fruits = ("Apple", "Banana", "Mango")

print("Last Element:", fruits[-1])


# ==========================================
# Solution 5
# Print the third element of a tuple.
# ==========================================

numbers = (100, 200, 300, 400, 500)

print("Third Element:", numbers[2])


# ==========================================
# Solution 6
# Slice the first four elements
# from a tuple.
# ==========================================

numbers = (10, 20, 30, 40, 50, 60)

print("First Four Elements:", numbers[:4])


# ==========================================
# Solution 7
# Slice the last three elements
# from a tuple.
# ==========================================

numbers = (10, 20, 30, 40, 50, 60)

print("Last Three Elements:", numbers[-3:])


# ==========================================
# Solution 8
# Reverse a tuple using slicing.
# ==========================================

numbers = (10, 20, 30, 40, 50)

print("Reversed Tuple:", numbers[::-1])


# ==========================================
# Solution 9
# Create a single-element tuple.
# ==========================================

single = (100,)

print(single)

print(type(single))


# ==========================================
# Solution 10
# Concatenate two tuples.
# ==========================================

tuple1 = (1, 2, 3)

tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("Concatenated Tuple:", result)


print("\nExercises 1-10 Completed Successfully!")

# ==========================================
# Solution 11
# Repeat a tuple three times.
# ==========================================

numbers = (1, 2, 3)

result = numbers * 3

print("Repeated Tuple:", result)


# ==========================================
# Solution 12
# Find the length of a tuple.
# ==========================================

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Length of Tuple:", len(fruits))


# ==========================================
# Solution 13
# Count how many times the value
# 20 appears in a tuple.
# ==========================================

numbers = (10, 20, 30, 20, 40, 20, 50)

print("Count of 20:", numbers.count(20))


# ==========================================
# Solution 14
# Find the index of an element
# in a tuple.
# ==========================================

numbers = (10, 20, 30, 40, 50)

print("Index of 30:", numbers.index(30))


# ==========================================
# Solution 15
# Check whether "Python"
# exists in a tuple.
# ==========================================

languages = ("Python", "Java", "C++", "JavaScript")

print("Python" in languages)


# ==========================================
# Solution 16
# Check whether "Java"
# is NOT present in a tuple.
# ==========================================

languages = ("Python", "C++", "JavaScript")

print("Java" not in languages)


# ==========================================
# Solution 17
# Traverse a tuple using
# a for loop.
# ==========================================

colors = ("Red", "Green", "Blue", "Yellow")

print("Colors:")

for color in colors:
    print(color)


# ==========================================
# Solution 18
# Traverse a tuple using
# a while loop.
# ==========================================

numbers = (10, 20, 30, 40, 50)

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1


# ==========================================
# Solution 19
# Perform tuple packing.
# ==========================================

student = "Amit", 23, "Haridwar"

print("Packed Tuple:", student)


# ==========================================
# Solution 20
# Perform tuple unpacking.
# ==========================================

student = ("Amit", 23, "Haridwar")

name, age, city = student

print("Name :", name)
print("Age  :", age)
print("City :", city)


print("\nExercises 11-20 Completed Successfully!")

# ==========================================
# Solution 21
# Create a nested tuple
# containing student details.
# ==========================================

students = (
    ("Amit", 90),
    ("Rahul", 85),
    ("Riya", 95)
)

print("Nested Tuple:")
print(students)


# ==========================================
# Solution 22
# Access an element from
# a nested tuple.
# ==========================================

students = (
    ("Amit", 90),
    ("Rahul", 85),
    ("Riya", 95)
)

print("First Student:", students[0])
print("Second Student Name:", students[1][0])
print("Third Student Marks:", students[2][1])


# ==========================================
# Solution 23
# Print every student name
# from a nested tuple.
# ==========================================

students = (
    ("Amit", 90),
    ("Rahul", 85),
    ("Riya", 95)
)

print("Student Names:")

for student in students:
    print(student[0])


# ==========================================
# Solution 24
# Create a tuple of marks and
# display maximum, minimum,
# total, and average marks.
# ==========================================

marks = (85, 92, 76, 64, 98)

print("Marks:", marks)
print("Maximum Marks:", max(marks))
print("Minimum Marks:", min(marks))
print("Total Marks:", sum(marks))
print("Average Marks:", sum(marks) / len(marks))


# ==========================================
# Solution 25
# Create a tuple of five numbers.
# Display:
# - Largest number
# - Smallest number
# - Sum
# - Average
# - Reverse the tuple
# ==========================================

numbers = (15, 30, 45, 60, 75)

print("Tuple:", numbers)
print("Largest Number:", max(numbers))
print("Smallest Number:", min(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Reversed Tuple:", numbers[::-1])


print("\nCongratulations!")
print("You have successfully completed all Day 011 Exercises.")
print("Keep practicing and Happy Coding!")