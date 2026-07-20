"""
=========================================
Day 009 - Practice
Topic: Functions (Part 2)
=========================================

Practice every example one by one.
Understand the output before running it.
"""

# =========================================
# Example 1
# Local Variable
# =========================================

def greet():
    name = "Amit"
    print("Hello", name)

greet()

print("-" * 40)

# =========================================
# Example 2
# Local Variable cannot be accessed outside
# =========================================

def student():
    course = "Python"
    print(course)

student()

# print(course)  # NameError

print("-" * 40)

# =========================================
# Example 3
# Global Variable
# =========================================

country = "India"

def display():
    print(country)

display()

print(country)

print("-" * 40)

# =========================================
# Example 4
# Using global Keyword
# =========================================

count = 0

def increment():
    global count
    count += 1

increment()
increment()

print(count)

print("-" * 40)

# =========================================
# Example 5
# *args
# =========================================

def numbers(*args):
    print(args)

numbers(10, 20, 30)

print("-" * 40)

# =========================================
# Example 6
# Looping through *args
# =========================================

def display_numbers(*args):

    for number in args:
        print(number)

display_numbers(5, 10, 15, 20)

print("-" * 40)

# =========================================
# Example 7
# Sum using *args
# =========================================

def add(*numbers):
    print(sum(numbers))

add(10, 20, 30, 40)

print("-" * 40)

# =========================================
# Example 8
# Largest Number using *args
# =========================================

def maximum(*numbers):
    print(max(numbers))

maximum(12, 55, 7, 91, 44)

print("-" * 40)

# =========================================
# Example 9
# **kwargs
# =========================================

def student(**details):
    print(details)

student(name="Amit", age=22)

print("-" * 40)

# =========================================
# Example 10
# Looping through **kwargs
# =========================================

def profile(**details):

    for key, value in details.items():
        print(key, ":", value)

profile(name="Amit", city="Delhi", course="Python")

print("-" * 40)

# =========================================
# Example 11
# Lambda Function
# =========================================

square = lambda x: x * x

print(square(6))

print("-" * 40)

# =========================================
# Example 12
# Lambda with Two Values
# =========================================

add = lambda a, b: a + b

print(add(15, 25))

print("-" * 40)

# =========================================
# Example 13
# Lambda for Even/Odd
# =========================================

even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(even(10))
print(even(15))

print("-" * 40)

# =========================================
# Example 14
# Lambda for Maximum
# =========================================

largest = lambda a, b: a if a > b else b

print(largest(90, 55))

print("-" * 40)

# =========================================
# Example 15
# Recursive Factorial
# =========================================

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

print("-" * 40)

# =========================================
# Example 16
# Recursive Fibonacci
# =========================================

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

print("-" * 40)

# =========================================
# Example 17
# Recursive Sum
# =========================================

def total(n):

    if n == 1:
        return 1

    return n + total(n - 1)

print(total(10))

print("-" * 40)

# =========================================
# Example 18
# Recursive Countdown
# =========================================

def countdown(n):

    if n == 0:
        print("Done!")
        return

    print(n)

    countdown(n - 1)

countdown(5)

print("-" * 40)

# =========================================
# Example 19
# Recursive Palindrome Check
# =========================================

def palindrome(text):

    text = text.lower()

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])

print(palindrome("madam"))
print(palindrome("python"))

print("-" * 40)

# =========================================
# Example 20
# Combining *args and **kwargs
# =========================================

def information(*subjects, **student):

    print("Subjects:")

    for subject in subjects:
        print("-", subject)

    print()

    print("Student Details:")

    for key, value in student.items():
        print(key.title(), ":", value)

information(
    "Python",
    "AI",
    "Machine Learning",
    name="Amit",
    age=22,
    city="Haridwar"
)

print("-" * 40)

# =========================================
# Example 21
# Mini Utility Function
# =========================================

def calculate(*numbers):

    print("Numbers :", numbers)
    print("Total   :", sum(numbers))
    print("Maximum :", max(numbers))
    print("Minimum :", min(numbers))
    print("Average :", sum(numbers) / len(numbers))

calculate(10, 20, 30, 40, 50)

print("-" * 40)

# =========================================
# END
# =========================================

print("🎉 Practice Completed!")
print("You have successfully practiced Day 009.")