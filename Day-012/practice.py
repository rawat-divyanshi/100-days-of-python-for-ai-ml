"""
===========================================
Day 012 - Practice
Topic: Dictionaries
Programs 1 - 10
===========================================
"""

# ==========================================
# Program 1
# Create an Empty Dictionary
# ==========================================

student = {}

print(student)


# ==========================================
# Program 2
# Create a Dictionary
# ==========================================

student = {
    "name": "Amit",
    "age": 23,
    "course": "Python"
}

print(student)


# ==========================================
# Program 3
# Access Dictionary Values
# ==========================================

print("Name :", student["name"])
print("Age :", student["age"])


# ==========================================
# Program 4
# Access Values using get()
# ==========================================

print(student.get("course"))
print(student.get("city"))      # Returns None


# ==========================================
# Program 5
# Add New Key-Value Pair
# ==========================================

student["city"] = "Haridwar"

print(student)


# ==========================================
# Program 6
# Update Existing Value
# ==========================================

student["age"] = 24

print(student)


# ==========================================
# Program 7
# Print All Keys
# ==========================================

print(student.keys())


# ==========================================
# Program 8
# Print All Values
# ==========================================

print(student.values())


# ==========================================
# Program 9
# Print All Key-Value Pairs
# ==========================================

print(student.items())


# ==========================================
# Program 10
# Check if a Key Exists
# ==========================================

if "name" in student:
    print("Key Found")
else:
    print("Key Not Found")

    """
===========================================
Day 012 - Practice
Topic: Dictionaries
Programs 11 - 20
===========================================
"""

# ==========================================
# Program 11
# Remove an Item using pop()
# ==========================================

student = {
    "name": "Amit",
    "age": 24,
    "course": "Python",
    "city": "Haridwar"
}

removed = student.pop("city")

print("Removed:", removed)
print(student)


# ==========================================
# Program 12
# Remove the Last Item using popitem()
# ==========================================

student = {
    "name": "Amit",
    "age": 24,
    "course": "Python"
}

item = student.popitem()

print("Removed Item:", item)
print(student)


# ==========================================
# Program 13
# Delete a Key using del
# ==========================================

student = {
    "name": "Amit",
    "age": 24,
    "course": "Python"
}

del student["course"]

print(student)


# ==========================================
# Program 14
# Clear a Dictionary
# ==========================================

student = {
    "name": "Amit",
    "age": 24,
    "course": "Python"
}

student.clear()

print(student)


# ==========================================
# Program 15
# Traverse Dictionary Keys
# ==========================================

student = {
    "name": "Amit",
    "age": 24,
    "city": "Haridwar"
}

print("Keys:")

for key in student:
    print(key)


# ==========================================
# Program 16
# Traverse Dictionary Values
# ==========================================

student = {
    "name": "Amit",
    "age": 24,
    "city": "Haridwar"
}

print("Values:")

for value in student.values():
    print(value)


# ==========================================
# Program 17
# Traverse Keys and Values
# ==========================================

student = {
    "name": "Amit",
    "age": 24,
    "city": "Haridwar"
}

print("Student Information:")

for key, value in student.items():
    print(key, ":", value)


# ==========================================
# Program 18
# Nested Dictionary
# ==========================================

students = {
    "S101": {
        "name": "Amit",
        "marks": 90
    },
    "S102": {
        "name": "Rahul",
        "marks": 85
    }
}

print(students)


# ==========================================
# Program 19
# Access Nested Dictionary
# ==========================================

print("Student Name:", students["S101"]["name"])
print("Marks:", students["S101"]["marks"])


# ==========================================
# Program 20
# Dictionary Comprehension
# Squares of Numbers
# ==========================================

squares = {x: x ** 2 for x in range(1, 11)}

print(squares)

"""
===========================================
Day 012 - Practice
Topic: Dictionaries
Programs 21 - 30
===========================================
"""

# ==========================================
# Program 21
# Conditional Dictionary Comprehension
# Store Squares of Even Numbers
# ==========================================

even_squares = {
    x: x ** 2
    for x in range(1, 11)
    if x % 2 == 0
}

print(even_squares)


# ==========================================
# Program 22
# Merge Two Dictionaries
# ==========================================

student1 = {
    "name": "Amit",
    "age": 23
}

student2 = {
    "city": "Haridwar",
    "course": "Python"
}

student1.update(student2)

print(student1)


# ==========================================
# Program 23
# Character Frequency Counter
# ==========================================

text = "dictionary"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character Frequency:")

for char, count in frequency.items():
    print(char, ":", count)


# ==========================================
# Program 24
# Word Frequency Counter
# ==========================================

sentence = "python is easy and python is powerful"

words = sentence.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency:")

for word, count in word_count.items():
    print(word, ":", count)


# ==========================================
# Program 25
# Sort Dictionary Keys
# ==========================================

student = {
    "city": "Haridwar",
    "name": "Amit",
    "course": "Python",
    "age": 23
}

print("Sorted Keys:")

for key in sorted(student.keys()):
    print(key, ":", student[key])


# ==========================================
# Program 26
# Student Marks Analysis
# ==========================================

marks = {
    "Amit": 90,
    "Rahul": 85,
    "Priya": 92,
    "Neha": 88,
    "Rohan": 95
}

print("Highest Marks :", max(marks.values()))
print("Lowest Marks  :", min(marks.values()))
print("Average Marks :", sum(marks.values()) / len(marks))


# ==========================================
# Program 27
# Product Inventory
# ==========================================

products = {
    "Laptop": 10,
    "Mouse": 50,
    "Keyboard": 30
}

print("Available Products:")

for product, quantity in products.items():
    print(product, ":", quantity)


# ==========================================
# Program 28
# Employee Information
# ==========================================

employee = {
    "ID": 101,
    "Name": "Amit",
    "Department": "IT",
    "Salary": 50000
}

print("Employee Details:")

for key, value in employee.items():
    print(key, ":", value)


# ==========================================
# Program 29
# Count Vowels Using a Dictionary
# ==========================================

text = "Artificial Intelligence"

vowels = "aeiouAEIOU"

vowel_count = {}

for char in text:
    if char in vowels:
        vowel_count[char] = vowel_count.get(char, 0) + 1

print("Vowel Count:")

for vowel, count in vowel_count.items():
    print(vowel, ":", count)


# ==========================================
# Program 30
# Simple Phone Book
# ==========================================

phone_book = {
    "Amit": "9876543210",
    "Rahul": "9123456789",
    "Priya": "9988776655"
}

print("Phone Book:")

for name, number in phone_book.items():
    print(name, ":", number)

search = input("\nEnter Name to Search: ")

if search in phone_book:
    print("Phone Number:", phone_book[search])
else:
    print("Contact Not Found.")