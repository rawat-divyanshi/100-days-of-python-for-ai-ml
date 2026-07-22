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