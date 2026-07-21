"""
=========================================
Day 010 - Practice
Topic: Lists
Part 1 (Programs 1-10)
=========================================

Practice each program and understand
the output before moving ahead.
"""

# ==========================================
# Practice 1
# Creating a List
# ==========================================

fruits = ["Apple", "Banana", "Mango"]

print(fruits)


# ==========================================
# Practice 2
# List with Different Data Types
# ==========================================

data = [10, 3.14, "Python", True]

print(data)


# ==========================================
# Practice 3
# Positive Indexing
# ==========================================

colors = ["Red", "Blue", "Green", "Yellow"]

print("First Color :", colors[0])
print("Second Color:", colors[1])
print("Last Color  :", colors[3])


# ==========================================
# Practice 4
# Negative Indexing
# ==========================================

numbers = [10, 20, 30, 40, 50]

print(numbers[-1])
print(numbers[-2])
print(numbers[-3])


# ==========================================
# Practice 5
# List Slicing
# ==========================================

numbers = [10, 20, 30, 40, 50, 60]

print("Original :", numbers)
print("First 3  :", numbers[:3])
print("Last 3   :", numbers[-3:])
print("Middle   :", numbers[2:5])


# ==========================================
# Practice 6
# Reverse using Slicing
# ==========================================

numbers = [1, 2, 3, 4, 5]

print(numbers[::-1])


# ==========================================
# Practice 7
# append()
# ==========================================

fruits = ["Apple", "Banana"]

fruits.append("Orange")
fruits.append("Mango")

print(fruits)


# ==========================================
# Practice 8
# insert()
# ==========================================

languages = ["Python", "Java", "C++"]

languages.insert(1, "C")

print(languages)


# ==========================================
# Practice 9
# remove()
# ==========================================

animals = ["Dog", "Cat", "Lion", "Tiger"]

animals.remove("Lion")

print(animals)


# ==========================================
# Practice 10
# pop()
# ==========================================

numbers = [10, 20, 30, 40, 50]

removed = numbers.pop()

print("Removed:", removed)
print("Updated List:", numbers)


print("\nPractice Programs 1-10 Completed Successfully!")

# ==========================================
# Practice 11
# sort()
# ==========================================

numbers = [45, 12, 89, 23, 5]

numbers.sort()

print("Ascending Order:", numbers)


# ==========================================
# Practice 12
# sort(reverse=True)
# ==========================================

numbers = [45, 12, 89, 23, 5]

numbers.sort(reverse=True)

print("Descending Order:", numbers)


# ==========================================
# Practice 13
# reverse()
# ==========================================

numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print(numbers)


# ==========================================
# Practice 14
# len()
# ==========================================

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Length:", len(fruits))


# ==========================================
# Practice 15
# max(), min(), sum()
# ==========================================

numbers = [10, 25, 5, 90, 40]

print("Maximum :", max(numbers))
print("Minimum :", min(numbers))
print("Sum     :", sum(numbers))


# ==========================================
# Practice 16
# Traversing using for Loop
# ==========================================

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)


# ==========================================
# Practice 17
# Traversing using while Loop
# ==========================================

numbers = [10, 20, 30, 40]

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1


# ==========================================
# Practice 18
# enumerate()
# ==========================================

languages = ["Python", "Java", "C++", "JavaScript"]

for index, language in enumerate(languages):
    print(index, language)


# ==========================================
# Practice 19
# Membership Operator (in)
# ==========================================

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)


# ==========================================
# Practice 20
# Membership Operator (not in)
# ==========================================

colors = ["Red", "Blue", "Green"]

print("Yellow" not in colors)
print("Blue" not in colors)


print("\nPractice Programs 11-20 Completed Successfully!")

# ==========================================
# Practice 21
# List Comprehension
# ==========================================

numbers = [x for x in range(1, 11)]

print(numbers)


# ==========================================
# Practice 22
# Squares using List Comprehension
# ==========================================

squares = [x ** 2 for x in range(1, 11)]

print(squares)


# ==========================================
# Practice 23
# Even Numbers using List Comprehension
# ==========================================

even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print(even_numbers)


# ==========================================
# Practice 24
# Odd Numbers using List Comprehension
# ==========================================

odd_numbers = [x for x in range(1, 21) if x % 2 != 0]

print(odd_numbers)


# ==========================================
# Practice 25
# Copying a List
# ==========================================

fruits = ["Apple", "Banana", "Mango"]

new_fruits = fruits.copy()

print("Original List:", fruits)
print("Copied List  :", new_fruits)


# ==========================================
# Practice 26
# Concatenating Two Lists
# ==========================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)


# ==========================================
# Practice 27
# Repeating a List
# ==========================================

numbers = [1, 2, 3]

print(numbers * 3)


# ==========================================
# Practice 28
# Removing Duplicate Elements
# ==========================================

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)


# ==========================================
# Practice 29
# Filtering Numbers Greater than 50
# ==========================================

numbers = [10, 65, 34, 89, 41, 72, 15]

greater_than_50 = [number for number in numbers if number > 50]

print(greater_than_50)


# ==========================================
# Practice 30
# Student Marks Analysis
# ==========================================

marks = [85, 92, 76, 64, 98]

print("Marks        :", marks)
print("Highest      :", max(marks))
print("Lowest       :", min(marks))
print("Total        :", sum(marks))
print("Average      :", sum(marks) / len(marks))

marks.sort()

print("Sorted Marks :", marks)

marks.reverse()

print("Reversed List:", marks)


print("\nCongratulations!")
print("You have completed all Day 010 Practice Programs.")