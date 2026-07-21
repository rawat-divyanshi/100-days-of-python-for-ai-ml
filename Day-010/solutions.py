"""
=========================================
Day 010 - Solutions
Topic: Lists
Exercises 1 - 10
=========================================

Solutions for the first 10 exercises.
"""

# ==========================================
# Exercise 1
# ==========================================
# Create a list containing five fruits and
# print the entire list.

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print(fruits)


# ==========================================
# Exercise 2
# ==========================================
# Create a list of five numbers and print:
# First element
# Last element
# Third element

numbers = [10, 20, 30, 40, 50]

print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Third Element:", numbers[2])


# ==========================================
# Exercise 3
# ==========================================
# Create a list of colors and print the list
# in reverse using slicing.

colors = ["Red", "Blue", "Green", "Yellow", "Pink"]

print(colors[::-1])


# ==========================================
# Exercise 4
# ==========================================
# Create an empty list and add five numbers
# using append().

numbers = []

numbers.append(10)
numbers.append(20)
numbers.append(30)
numbers.append(40)
numbers.append(50)

print(numbers)


# ==========================================
# Exercise 5
# ==========================================
# Insert "Python" at index 2 in the list.

languages = ["C", "Java", "C++"]

languages.insert(2, "Python")

print(languages)


# ==========================================
# Exercise 6
# ==========================================
# Remove "Banana" from the list.

fruits = ["Apple", "Banana", "Orange", "Mango"]

fruits.remove("Banana")

print(fruits)


# ==========================================
# Exercise 7
# ==========================================
# Remove the last element using pop().

numbers = [10, 20, 30, 40, 50]

numbers.pop()

print(numbers)


# ==========================================
# Exercise 8
# ==========================================
# Sort the following list in ascending order.

numbers = [45, 12, 89, 2, 67]

numbers.sort()

print(numbers)


# ==========================================
# Exercise 9
# ==========================================
# Sort the following list in descending order.

numbers = [10, 90, 45, 76, 22]

numbers.sort(reverse=True)

print(numbers)


# ==========================================
# Exercise 10
# ==========================================
# Reverse the list using reverse().

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)


print("\nExercises 1–10 Completed Successfully!")

# ==========================================
# Exercise 11
# ==========================================
# Print every element using a for loop.

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# ==========================================
# Exercise 12
# ==========================================
# Print every element using a while loop.

numbers = [100, 200, 300, 400]

i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1


# ==========================================
# Exercise 13
# ==========================================
# Print both index and value using enumerate().

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# ==========================================
# Exercise 14
# ==========================================
# Find the length of the list.

numbers = [5, 10, 15, 20, 25]

print("Length:", len(numbers))


# ==========================================
# Exercise 15
# ==========================================
# Find the maximum, minimum and sum of
# the following list.

numbers = [8, 15, 42, 3, 27]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


# ==========================================
# Exercise 16
# ==========================================
# Create a list of squares from 1 to 10
# using list comprehension.

squares = [x ** 2 for x in range(1, 11)]

print(squares)


# ==========================================
# Exercise 17
# ==========================================
# Create a list containing all even numbers
# between 1 and 30 using list comprehension.

even_numbers = [x for x in range(1, 31) if x % 2 == 0]

print(even_numbers)


# ==========================================
# Exercise 18
# ==========================================
# Create a list containing all odd numbers
# between 1 and 30 using list comprehension.

odd_numbers = [x for x in range(1, 31) if x % 2 != 0]

print(odd_numbers)


# ==========================================
# Exercise 19
# ==========================================
# Given the following list:
# Print:
# First three elements
# Last three elements
# Every second element

numbers = [10, 20, 30, 40, 50]

print("First Three:", numbers[:3])
print("Last Three:", numbers[-3:])
print("Every Second:", numbers[::2])


# ==========================================
# Exercise 20
# ==========================================
# Find the largest number in the list
# without using max().

numbers = [12, 56, 89, 23, 67]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest Number:", largest)


print("\nExercises 11–20 Completed Successfully!")

# ==========================================
# Exercise 21
# ==========================================
# Find the smallest number in the list
# without using min().

numbers = [45, 9, 34, 76, 2]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest Number:", smallest)


# ==========================================
# Exercise 22
# ==========================================
# Calculate the average of all numbers.

numbers = [15, 20, 35, 40, 50]

average = sum(numbers) / len(numbers)

print("Average:", average)


# ==========================================
# Exercise 23
# ==========================================
# Count how many even numbers are present
# in the list.

numbers = [2, 5, 8, 11, 14, 19, 20]

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print("Even Numbers:", count)


# ==========================================
# Exercise 24
# ==========================================
# Remove duplicate elements from the list.

numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)


# ==========================================
# Exercise 25
# ==========================================
# Create a new list containing only numbers
# greater than 50.

numbers = [10, 65, 23, 89, 41, 72, 5]

greater_than_50 = []

for number in numbers:
    if number > 50:
        greater_than_50.append(number)

print(greater_than_50)


# ==========================================
# Bonus Challenge
# ==========================================
# Create a program that accepts 10 numbers
# from the user and then displays:
#
# • Largest Number
# • Smallest Number
# • Sum
# • Average
# • Sorted List
# • Reversed List

numbers = []

print("Enter 10 Numbers")

for i in range(10):
    number = int(input(f"Enter Number {i + 1}: "))
    numbers.append(number)

print("\nResults")
print("-" * 30)

print("Numbers:", numbers)
print("Largest Number:", max(numbers))
print("Smallest Number:", min(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

sorted_numbers = numbers.copy()
sorted_numbers.sort()
print("Sorted List:", sorted_numbers)

reversed_numbers = numbers.copy()
reversed_numbers.reverse()
print("Reversed List:", reversed_numbers)


print("\nCongratulations! You have completed all Day 010 exercises.")