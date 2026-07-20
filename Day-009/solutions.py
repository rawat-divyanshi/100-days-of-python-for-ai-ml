"""
=========================================
Day 009 - Solutions
Topic: Functions (Part 2)
=========================================
"""

# =========================================
# Exercise 1
# =========================================

country = "India"

def show_country():
    print(country)

show_country()

print("-" * 40)

# =========================================
# Exercise 2
# =========================================

count = 0

def increment():
    global count
    count += 1

increment()
print("Count:", count)

print("-" * 40)

# =========================================
# Exercise 3
# =========================================

def display(*numbers):
    for num in numbers:
        print(num)

display(10, 20, 30)

print("-" * 40)

# =========================================
# Exercise 4
# =========================================

def add(*numbers):
    return sum(numbers)

print("Sum:", add(10, 20, 30))

print("-" * 40)

# =========================================
# Exercise 5
# =========================================

def student(**details):
    for key, value in details.items():
        print(key, ":", value)

student(name="Amit", age=22)

print("-" * 40)

# =========================================
# Exercise 6
# =========================================

square = lambda x: x * x

print(square(5))

print("-" * 40)

# =========================================
# Exercise 7
# =========================================

maximum = lambda a, b: a if a > b else b

print(maximum(10, 20))

print("-" * 40)

# =========================================
# Exercise 8
# =========================================

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

print("-" * 40)

# =========================================
# Exercise 9
# =========================================

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))

print("-" * 40)

# =========================================
# Exercise 10
# =========================================

def maximum_number(*numbers):
    return max(numbers)

print(maximum_number(12, 45, 2, 99, 18))

print("-" * 40)

# =========================================
# Exercise 11
# =========================================

def profile(**details):

    print("Student Profile")
    print("-" * 20)

    for key, value in details.items():
        print(key.title(), ":", value)

profile(
    name="Amit",
    age=22,
    course="Python"
)

print("-" * 40)

# =========================================
# Exercise 12
# =========================================

def calculator(a, b, operator):

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

    return operations[operator](a, b)

print(calculator(10, 20, "+"))
print(calculator(20, 5, "-"))
print(calculator(5, 4, "*"))
print(calculator(20, 4, "/"))

print("-" * 40)

# =========================================
# Exercise 13
# =========================================

def sum_numbers(n):

    if n == 1:
        return 1

    return n + sum_numbers(n - 1)

print(sum_numbers(5))

print("-" * 40)

# =========================================
# Exercise 14
# =========================================

def analyze(*numbers):

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print("Total   :", total)
    print("Average :", average)
    print("Maximum :", maximum)
    print("Minimum :", minimum)

analyze(10, 20, 30)

print("-" * 40)

# =========================================
# Exercise 15
# =========================================

def employee(**details):

    print("Employee Details")
    print("-" * 25)

    for key, value in details.items():
        print(key.title(), ":", value)

employee(
    name="Rahul",
    age=25,
    salary=50000,
    city="Delhi",
    department="IT"
)

print("-" * 40)

# =========================================
# Bonus Challenge
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
# END
# =========================================

print("🎉 Congratulations!")
print("You have completed Day 009 - Functions (Part 2).")